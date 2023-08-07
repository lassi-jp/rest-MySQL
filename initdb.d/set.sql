 CREATE TABLE IF NOT EXISTS `sample`.`restDB` (
   `id` INT NOT NULL AUTO_INCREMENT,
   `itemKey` VARCHAR(255) NOT NULL,
   `body` LONGTEXT NOT NULL,
   `create_date` DATETIME NULL,
   `update_date` DATETIME NULL,
   PRIMARY KEY (`id`))
 ENGINE = InnoDB;
