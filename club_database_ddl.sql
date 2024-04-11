-- Club Database DDL

CREATE TABLE Members (
    member_id		SERIAL PRIMARY KEY,
	first_name		VARCHAR(20) NOT NULL,
	last_name		VARCHAR(20) NOT NULL,
	username		VARCHAR(20) UNIQUE NOT NULL,
    pass        	VARCHAR(20) NOT NULL
);

CREATE TABLE Trainers (
    trainer_id		SERIAL PRIMARY KEY,
	first_name		VARCHAR(20) NOT NULL,
	last_name		VARCHAR(20) NOT NULL,
	username		VARCHAR(20) UNIQUE NOT NULL,
    pass        	VARCHAR(20) NOT NULL
);

CREATE TABLE Admins (
    admin_id		SERIAL PRIMARY KEY,
	first_name		VARCHAR(20) NOT NULL,
	last_name		VARCHAR(20) NOT NULL,
	username		VARCHAR(20) UNIQUE NOT NULL,
    pass        	VARCHAR(20) NOT NULL
);

CREATE TABLE Health_metrics (
    member_id	    INT,
	user_height		INT,
	user_weight		INT,
	mile_time		TIME,
	bench_pr		INT,
	squat_pr		INT,
	deadlift_pr		INT,
	plank_pr		INT,
	FOREIGN KEY (member_id)
		references Members
);

CREATE TABLE Goals (
    member_id		    INT,
	height_goal			INT,
	weight_goal			INT,
	mile_time_goal		TIME,
	bench_pr_goal		INT,
	squat_pr_goal		INT,
	deadlift_pr_goal	INT,
	plank_pr_goal		INT,
	notes				TEXT,
	FOREIGN KEY (member_id)
		references Members(member_id)
);

CREATE TABLE Routines (
	routine_id		SERIAL PRIMARY KEY,
	routine_type	VARCHAR(20),
	routine_desc	VARCHAR(20)
);

CREATE TABLE Schedule (
	schedule_id		SERIAL PRIMARY KEY,
	trainer_id		INT,
	date            DATE,
    start_time      TIME,
    end_time        TIME,
	FOREIGN KEY (trainer_id)
        references Trainers(trainer_id)
);

CREATE TABLE Rooms (
	room_id         SERIAL PRIMARY KEY,
    room_name       VARCHAR(20)
);

CREATE TABLE Personal_sessions (
	session_id		SERIAL PRIMARY KEY,
	session_details		INT,
	member_id		INT,
	routine_id		INT,
	room_location	INT,
	FOREIGN KEY (session_details)
		references Schedule(schedule_id),
	FOREIGN KEY (member_id)
		references Members(member_id),
	FOREIGN KEY (routine_id)
		references Routines(routine_id),
	FOREIGN KEY (room_location)
		references Rooms(room_id)
);

CREATE TABLE Group_classes (
	class_id		SERIAL PRIMARY KEY,
	class_details	INT,
	routine_id		INT,
	room_location	INT,
	FOREIGN KEY (class_details)
		references Schedule(schedule_id),
	FOREIGN KEY (routine_id)
		references Routines(routine_id),
	FOREIGN KEY (room_location)
		references Rooms(room_id)
);

CREATE TABLE Registers (
    id          SERIAL PRIMARY KEY,
    class_id    INT,
    FOREIGN KEY (id)
        references Members(member_id),
    FOREIGN KEY (class_id)
        references Group_classes(class_id)
);

CREATE TABLE Billing (
    bill_id         SERIAL PRIMARY KEY,
    bill_num        INT,
    card_num        INT NOT NULL,
    bill_paid       BOOLEAN NOT NULL,
    bill_amount     INT,
    FOREIGN KEY (bill_id)
        references Members(member_id)
);

CREATE TABLE Equipment (
    equipment_id		SERIAL PRIMARY KEY,
	equipment_type		VARCHAR(20),
	maintainence_date	DATE,
	equipment_location	INT,
	FOREIGN KEY (equipment_location)
		references Rooms(room_id)
);