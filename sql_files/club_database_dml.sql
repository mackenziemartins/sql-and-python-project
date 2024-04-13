-- COMP 3005 B Project V2
-- Kareem Kaddoura (101140255)
-- Mackenzie Martins (101228049)
-- Club Database DML


-- Populate Members Table
INSERT INTO Members (first_name, last_name, username, password)
VALUES
('John', 'Smith', 'jsmith', 'smith123'),
('Alice', 'Knowles', 'aknowles', 'knowles123'),
('Alex', 'George', 'ageorge', 'george123'),
('Sarah', 'Fortner', 'sfortner', 'fortner123');

-- Populate Trainers Table
INSERT INTO Trainers (first_name, last_name, username, password)
VALUES
('Amber', 'Brown', 'abrown', 'brown123'),
('Jack', 'Ryan', 'jryan', 'ryan123'),
('Lloyd', 'Jameson', 'ljameson', 'jameson123');

-- Populate Admins Table
INSERT INTO Admins (first_name, last_name, username, password)
VALUES
('James', 'Field', 'jfield', 'field123'),
('Rylan', 'Noel', 'rnoel', 'noel123');

-- Populate Health_metrics Table
INSERT INTO Health_metrics (member_id, date, height, weight, mile_time, resting_hr, blood_pressure)
VALUES
(1, '2024-04-06', 183, 67, '00:08:25', 72, '119/70'),
(2, '2024-04-10', 160, 58, '00:09:30', 72, '110/68'),
(3, '2024-04-11', 178, 61, '00:08:03', 72, '115/68');

-- Popualte Goals Table
INSERT INTO Goals (member_id, goal_weight, goal_mile_time, goal_bench, goal_squat, goal_deadlift, goal_plank)
VALUES
(1, 70, '00:08:00', 150, 200, 200, '00:02:00'),
(2, 55, '00:09:00', 135, 250, 180, '00:03:00');

-- Populate Rooms Table
INSERT INTO Rooms (room_name, max_members)
VALUES
('Main Gym', 200),
('Workout Room A', 30),
('Workout Room B', 30),
('Workout Room C', 30);

-- Populate Routines Table
INSERT INTO Routines (routine_type, routine_desc)
VALUES
('Arms', 'Bicep Curls, Bench Presses, Hammer Curls'),
('Legs', 'Deadlifts, Squats, Leg Curls'),
('Chest', 'Pushups, Cable Crossovers, Chest Presses'),
('Cardio', 'Treadmill, Rowing Machine, Jumping Jacks');

-- Populate Personal_sessions Table
INSERT INTO Personal_sessions (routine_id, trainer_id, member_id, room_id, date, start_time, end_time)
VALUES
(1, 2, 1, 1, '2024-04-12', '09:00:00', '10:00:00'),
(2, 1, 3, 1, '2024-04-11', '10:00:00', '11:00:00'),
(3, 2, 4, 1, '2024-04-12', '11:00:00', '12:00:00');

-- Populate Group_classes Table
INSERT INTO Group_classes (routine_id, trainer_id, room_id, date, start_time, end_time)
VALUES
(2, 1, 2, '2024-04-12', '12:00:00', '13:00:00'),
(4, 3, 4, '2024-04-12', '13:00:00', '14:00:00');

-- Populate Class_registration Table
INSERT INTO Class_registration (member_id, class_id)
VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(4, 2);

-- Populate Trainer_availability Table
INSERT INTO Trainer_availability (trainer_id, day, start_time, end_time)
VALUES
(1, 'Monday', '09:00:00', '17:00:00'),
(1, 'Tuesday', '09:00:00', '17:00:00'),
(1, 'Wednesday', '09:00:00', '17:00:00'),
(1, 'Thursday', '09:00:00', '17:00:00'),
(1, 'Friday', '09:00:00', '17:00:00'),
(2, 'Monday', '09:00:00', '17:00:00'),
(2, 'Tuesday', '09:00:00', '17:00:00'),
(2, 'Wednesday', '09:00:00', '17:00:00'),
(2, 'Thursday', '09:00:00', '17:00:00'),
(2, 'Friday', '09:00:00', '17:00:00'),
(3, 'Monday', '09:00:00', '17:00:00'),
(3, 'Tuesday', '09:00:00', '17:00:00'),
(3, 'Wednesday', '09:00:00', '17:00:00'),
(3, 'Thursday', '09:00:00', '17:00:00'),
(3, 'Friday', '09:00:00', '17:00:00');

-- Populate Billing Table
INSERT INTO Billing (member_id, bill_desc, bill_amount, due_date, bill_paid)
VALUES
(1, 'Monthly Membership Fee', 45.00, '2024-04-30', FALSE),
(1, 'Damaged Equipment', 150.00, '2024-04-28', TRUE),
(2, 'Monthly Membership Fee', 45.00, '2024-04-30', TRUE),
(3, 'Monthly Membership Fee', 45.00, '2024-04-24', TRUE),
(3, 'Lost Equipment', 80.00, '2024-04-26', FALSE),
(4, 'Monthly Membership Fee', 45.00, '2024-04-30', FALSE);

-- Populate Equipment Table
INSERT INTO Equipment (equipment_type, upcoming_maintenance_date, last_maintenance_date)
VALUES
('Ellipticals', '2024-05-25', '2023-11-25'),
('Treadmills', '2024-08-20', '2024-02-20'),
('Rowing Machines', '2024-06-30', '2023-12-30'),
('Cable Machines', '2024-07-24', '2024-01-24'),
('Squat Racks', '2024-08-11', '2024-02-11');
