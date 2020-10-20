-- drop the database
DROP DATABASE IF EXISTS futbolStats;

-- create the databases
CREATE DATABASE IF NOT EXISTS futbolStats;

-- create the users for each database
/*CREATE USER 'futboluser'@'%' IDENTIFIED BY 'somepassword';
GRANT CREATE, ALTER, INDEX, LOCK TABLES, REFERENCES, UPDATE, DELETE, DROP, SELECT, INSERT ON `futbolStats`.* TO 'futboluser'@'%';

FLUSH PRIVILEGES;
*/
-- create tables
CREATE TABLE `futbolStats`.`country` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC));

CREATE TABLE `futbolStats`.`team` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC));

CREATE TABLE `futbolStats`.`tournament` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));

CREATE TABLE `futbolStats`.`match` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `homeTeamId` INT NOT NULL,
  `awayTeamId` INT NOT NULL,
  `homeScore` INT NOT NULL,
  `awayScore` INT NOT NULL,
  `tournamentId` INT NOT NULL,
  `countryId` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `fk_match_1_idx` (`countryId` ASC),
  INDEX `fk_match_2_idx` (`homeTeamId` ASC),
  INDEX `fk_match_3_idx` (`awayTeamId` ASC),
  INDEX `fk_match_4_idx` (`tournamentId` ASC),
  CONSTRAINT `fk_match_1`
    FOREIGN KEY (`countryId`)
    REFERENCES `futbolStats`.`country` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_match_2`
    FOREIGN KEY (`homeTeamId`)
    REFERENCES `futbolStats`.`team` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_match_3`
    FOREIGN KEY (`awayTeamId`)
    REFERENCES `futbolStats`.`team` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_match_4`
    FOREIGN KEY (`tournamentId`)
    REFERENCES `futbolStats`.`tournament` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);




