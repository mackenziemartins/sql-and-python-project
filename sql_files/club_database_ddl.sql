-- COMP 3005 B Project V2
-- Kareem Kaddoura (101140255)
-- Mackenzie Martins (101228049)
-- Club Database DDL

CREATE TABLE Members (
    member_id		SERIAL PRIMARY KEY,
	first_name		VARCHAR(255) NOT NULL,
	last_name		VARCHAR(255) NOT NULL,
	username		VARCHAR(255) UNIQUE NOT NULL,
    password        VARCHAR(255) NOT NULL
);

CREATE TABLE Trainers (
    trainer_id		SERIAL PRIMARY KEY,
	first_name		VARCHAR(255) NOT NULL,
	last_name		VARCHAR(255) NOT NULL,
	username		VARCHAR(255) UNIQUE NOT NULL,
    password        VARCHAR(255) NOT NULL
);

CREATE TABLE Admins (
    admin_id		SERIAL PRIMARY KEY,
	first_name		VARCHAR(255) NOT NULL,
	last_name		VARCHAR(255) NOT NULL,
	username		VARCHAR(255) UNIQUE NOT NULL,
    password        VARCHAR(255) NOT NULL
);

CREATE TABLE Health_metrics (
	metric_id		SERIAL PRIMARY KEY,
    member_id	    INT,
	date			DATE,
	height			INT,
	weight			INT,
	mile_time		TIME,
	resting_hr		INT,
	blood_pressure	VARCHAR(255),
	FOREIGN KEY (member_id)
		references Members
);

CREATE TABLE Goals (
	goal_id				SERIAL PRIMARY KEY,
    member_id	    	INT,
	date				DATE,
	goal_weight			INT,
	goal_mile_time		TIME,
	goal_bench			INT,
	goal_squat			INT,
	goal_deadlift		INT,
	goal_plank			TIME,
	FOREIGN KEY (member_id)
		references Members
);

CREATE TABLE Achievements (
	achievement_id	SERIAL PRIMARY KEY,
	member_id		INT,
	a_weight		INT,
	a_mile_time		TIME,
	a_bench_pr		INT,
	a_squat_pr		INT,
	a_deadlift_pr	INT,
	a_plank_pr		TIME,
	FOREIGN KEY (member_id)
		references Members
);

CREATE TABLE Rooms (
	room_id         SERIAL PRIMARY KEY,
    room_name       VARCHAR(255),
	max_members		INT
);

CREATE TABLE Routines (
	routine_id		SERIAL PRIMARY KEY,
	routine_type	VARCHAR(255),
	routine_desc	VARCHAR(255)
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
		references Members,
	FOREIGN KEY (room_id)
		references Rooms
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
	day					VARCHAR(255),
	start_time			TIME,
	end_time			TIME,
	FOREIGN KEY (trainer_id)
		references Trainers
);

CREATE TABLE Billing (
	bill_id			SERIAL PRIMARY KEY,
	member_id		INT,
	bill_desc		VARCHAR(255),
	bill_amount		DEC(5, 2),
	due_date		DATE,
	bill_paid		BOOL
);

CREATE TABLE Equipment (
    equipment_id				SERIAL PRIMARY KEY,
	equipment_type				VARCHAR(255),
	upcoming_maintenance_date	DATE,
	last_maintenance_date		DATE
);
