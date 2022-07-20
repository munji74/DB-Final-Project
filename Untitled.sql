CREATE TABLE `patients` (
  `patient_id` integer,
  `patient_name` varchar(255),
  `insurance_company` varchar(255)
);

CREATE TABLE `admitted_ward` (
  `admission_id` integer,
  `ward` varchar(255),
  `room` integer,
  `date_admitted` varchar(255),
  `date_released` varchar(255)
);

CREATE TABLE `test` (
  `test_id` integer,
  `test_name` varchar(255),
  `test_result` varchar(255),
  `test_time` varchar(255),
  `test_date` varchar(255)
);

CREATE TABLE `relations` (
  `patient_id` integer,
  `dmission_id` integer,
  `test_id` integer
);

ALTER TABLE `relations` ADD FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`);

ALTER TABLE `patients` ADD FOREIGN KEY (`patient_id`) REFERENCES `admitted_ward` (`admission_id`);

ALTER TABLE `test` ADD FOREIGN KEY (`test_id`) REFERENCES `admitted_ward` (`admission_id`);

ALTER TABLE `relations` ADD FOREIGN KEY (`dmission_id`) REFERENCES `admitted_ward` (`admission_id`);

ALTER TABLE `relations` ADD FOREIGN KEY (`test_id`) REFERENCES `test` (`test_id`);
