-- Club Database DDL

CREATE TABLE Members (
    member_id		SERIAL PRIMARY KEY,
	first_name		VARCHAR(20) NOT NULL,
	last_name		VARCHAR(20) NOT NULL,
	username		VARCHAR(20) UNIQUE NOT NULL,
    password        VARCHAR(20) NOT NULL
);

CREATE TABLE Trainers (
    trainer_id		SERIAL PRIMARY KEY,
	first_name		VARCHAR(20) NOT NULL,
	last_name		VARCHAR(20) NOT NULL,
	username		VARCHAR(20) UNIQUE NOT NULL,
    password        VARCHAR(20) NOT NULL
);

CREATE TABLE Admins (
    admin_id		SERIAL PRIMARY KEY,
	first_name		VARCHAR(20) NOT NULL,
	last_name		VARCHAR(20) NOT NULL,
	username		VARCHAR(20) UNIQUE NOT NULL,
    password        VARCHAR(20) NOT NULL
);

CREATE TABLE Health_metrics (
	metric_id		SERIAL PRIMARY KEY,
    member_id	    INT,
	date			DATE,
	height			INT,
	weight			INT,
	mile_time		INT,
	resting_hr		INT,
	blood_pressure	INT,
	FOREIGN KEY (member_id)
		references Members
);

CREATE TABLE Goals (
	goal_id				SERIAL PRIMARY KEY,
    member_id	    	INT,
	goal_weight			INT,
	goal_mile_time		TIME,
	goal_bench_pr		INT,
	goal_squat_pr		INT,
	goal_deadlift_pr	INT,
	goal_plank_pr		INT,
	FOREIGN KEY (member_id)
		references Members
);

CREATE TABLE Rooms (
	room_id         SERIAL PRIMARY KEY,
    room_name       VARCHAR(20),
	max_members		INT
);

CREATE TABLE Routines (
	routine_id		SERIAL PRIMARY KEY,
	routine_type	VARCHAR(20),
	routine_desc	VARCHAR(20)
);

CREATE TABLE Personal_sessions (
	session_id		SERIAL PRIMARY KEY,
	routine_id		INT,
	trainer_id		INT,
	member_id		INT,
	room_id			INT DEFAULT 1,
	date			DATE,
	start_time		TIME,
	end_time		TIME,
	FOREIGN KEY (routine_id)
		references Routines,
	FOREIGN KEY (trainer_id)
		references Trainers,
	FOREIGN KEY (member_id)
		references Members
);

CREATE TABLE Group_classes (
	class_id		SERIAL PRIMARY KEY,
	routine_id		INT,
	trainer_id		INT,
	room_id			INT,
	date			DATE,
	start_time		TIME,
	end_time		TIME,
	FOREIGN KEY (routine_id)
		references Routines,
	FOREIGN KEY (trainer_id)
		references Trainers,
	FOREIGN KEY (room_id)
		references Rooms
);

CREATE TABLE Class_registration (
	registration_id		SERIAL PRIMARY KEY,
	member_id			INT,
	class_id			INT,
	FOREIGN KEY (member_id)
		references Members,
	FOREIGN KEY (class_id)
		references Group_classes
);

CREATE TABLE Trainer_availability (
	availability_id		SERIAL PRIMARY KEY,
	trainer_id			INT,
	date				DATE,
	start_time			TIME,
	end_time			TIME,
	FOREIGN KEY (trainer_id)
		references Trainers
);

CREATE TABLE Billing (
	bill_id			SERIAL PRIMARY KEY,
	member_id		INT,
	bill_desc		VARCHAR(20),
	bill_amount		DEC(5, 2),
	due_date		DATE,
	bill_paid		BOOLEAN
);

CREATE TABLE Equipment (
    equipment_id				SERIAL PRIMARY KEY,
	equipment_type				VARCHAR(20),
	upcoming_maintenance_date	DATE,
	last_maintenance_date		DATE
);