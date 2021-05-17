-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: school
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrator`
--

DROP TABLE IF EXISTS `administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator` (
  `Admin_id` smallint NOT NULL,
  PRIMARY KEY (`Admin_id`),
  KEY `Admin_id` (`Admin_id`),
  CONSTRAINT `Admin_id_fk` FOREIGN KEY (`Admin_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator`
--

LOCK TABLES `administrator` WRITE;
/*!40000 ALTER TABLE `administrator` DISABLE KEYS */;
INSERT INTO `administrator` VALUES (1);
/*!40000 ALTER TABLE `administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `Course_name` char(30) NOT NULL,
  `Course_Description` varchar(50) DEFAULT NULL,
  `Study` char(30) NOT NULL,
  `Teacher_id` smallint NOT NULL,
  `Credits` varchar(2) NOT NULL,
  `Study_id` varchar(10) NOT NULL,
  `course_id` varchar(5) NOT NULL,
  PRIMARY KEY (`course_id`),
  KEY `Study_id` (`Study_id`),
  KEY `Teacher_id` (`Teacher_id`),
  CONSTRAINT `Study_id2_fk` FOREIGN KEY (`Study_id`) REFERENCES `study` (`Study_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Teacher_id_fk` FOREIGN KEY (`Teacher_id`) REFERENCES `teachers` (`Teacher_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES ('Precalculus','introduction to math','Mathematical Engineering',1111,'3','33CC','0011A'),('Datamodelleren','inleiding tot datamodels','Business ICT',1112,'2','11AA','0012B'),('Optics','lenzen en prisma\'s','Precision engineering',1114,'3','55EE','0013C'),('Differential equations','For smart students','Mathematical engineering',1113,'4','33CC','0014D'),('Mechanics','F=ma and all that','Plane design',1111,'3','44DD','0015E'),('Control systems','how to control things','Precision Engineering',1114,'2','55EE','0016F'),('ICT','Introduction to ICT','Part-time Business ICT',1113,'2','11AA','0017G'),('Drawing','Drawing with software','architecture',1116,'2','66FF','0018H');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exams`
--

DROP TABLE IF EXISTS `exams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exams` (
  `Exam_id` varchar(10) NOT NULL,
  `Course_id` varchar(20) NOT NULL,
  `Room` varchar(4) NOT NULL,
  `Resit` tinyint NOT NULL,
  `Date_start_time` datetime NOT NULL,
  `exam_length` int NOT NULL,
  PRIMARY KEY (`Exam_id`),
  KEY `Course_id` (`Course_id`),
  CONSTRAINT `Course_id_fk` FOREIGN KEY (`Course_id`) REFERENCES `course` (`course_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exams`
--

LOCK TABLES `exams` WRITE;
/*!40000 ALTER TABLE `exams` DISABLE KEYS */;
INSERT INTO `exams` VALUES ('1919DE2','0014D','A45',0,'2017-08-02 14:00:00',2),('3111CS1','0016F','B88',0,'2016-06-06 16:00:00',2),('3719OP1','0013C','A34',0,'2017-12-17 10:00:00',2),('3719OP2','0013C','B12',1,'2018-03-03 13:00:00',2),('3788ME1','0015E','B13',0,'2017-01-04 09:00:00',2),('3788ME2','0015E','A21',1,'2018-09-20 19:00:00',2),('5555PC1','0011A','A8',0,'2018-05-12 14:00:00',2),('6666DM1','0012B','A34',0,'2016-12-13 14:00:00',2);
/*!40000 ALTER TABLE `exams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `results` (
  `Exam_id` varchar(10) NOT NULL,
  `Student_id` smallint NOT NULL,
  `Grade` varchar(2) NOT NULL,
  `Passed` tinyint NOT NULL,
  PRIMARY KEY (`Exam_id`,`Student_id`),
  KEY `Exam_id` (`Exam_id`),
  KEY `Student_id_fk_idx` (`Student_id`),
  CONSTRAINT `Exam_id_fk` FOREIGN KEY (`Exam_id`) REFERENCES `exams` (`Exam_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Student_id_fk` FOREIGN KEY (`Student_id`) REFERENCES `students` (`Student_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` VALUES ('1919DE2',6665,'8',1),('3111CS1',6662,'4',0),('3719OP1',6661,'3',0),('3719OP2',6661,'9',1),('3788ME1',6660,'6',1),('5555PC1',6663,'7',1),('5555PC1',6666,'4',0);
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `Student_id` smallint NOT NULL,
  `Study_id` varchar(5) NOT NULL,
  `Start_year` int NOT NULL,
  `Counselor_id` smallint NOT NULL,
  PRIMARY KEY (`Student_id`),
  KEY `Study_id` (`Study_id`),
  KEY `Study_Counselor` (`Counselor_id`),
  KEY `student_id` (`Student_id`) /*!80000 INVISIBLE */,
  CONSTRAINT `Counselor_id_fk` FOREIGN KEY (`Counselor_id`) REFERENCES `teachers` (`Teacher_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Studentn_id_fk` FOREIGN KEY (`Student_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Study_id_fk` FOREIGN KEY (`Study_id`) REFERENCES `study` (`Study_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (6660,'22BB',2017,1115),(6661,'33CC',2017,1111),(6662,'33CC',2018,1115),(6663,'55EE',2016,1111),(6664,'22BB',2016,1114),(6665,'44DD',2017,1111),(6666,'55EE',2016,1114),(6667,'66FF',2018,1116),(6668,'22BB',2019,1115),(6669,'11AA',2019,1116),(6670,'66FF',2018,1116);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `study`
--

DROP TABLE IF EXISTS `study`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `study` (
  `study_name` char(30) NOT NULL,
  `Description` varchar(255) NOT NULL,
  `language` char(30) NOT NULL,
  `Number_of_years` int NOT NULL,
  `Study_id` varchar(5) NOT NULL,
  PRIMARY KEY (`Study_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `study`
--

LOCK TABLES `study` WRITE;
/*!40000 ALTER TABLE `study` DISABLE KEYS */;
INSERT INTO `study` VALUES ('Business ICT','for management studies','Dutch',3,'11AA'),('BIM parttime','Part time students of BIM','Dutch',4,'22BB'),('Mathematical Engineering',' ','English',4,'33CC'),('Plane design','For aeronautical engineers','English',4,'44DD'),('Precision Engineering','Study of very small things','Dutch',4,'55EE'),('Architecture','designing buildings','Dutch',4,'66FF');
/*!40000 ALTER TABLE `study` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `Teacher_id` smallint NOT NULL,
  `Salary` int DEFAULT NULL,
  `Studycounselor` tinyint NOT NULL,
  PRIMARY KEY (`Teacher_id`),
  KEY `Teacher_id` (`Teacher_id`),
  CONSTRAINT `Teachers_id_fk` FOREIGN KEY (`Teacher_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (1111,34667,1),(1112,56323,0),(1113,4566,0),(1114,6711,1),(1115,4567,1),(1116,8412,1),(1117,7500,0),(1118,5500,0);
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` smallint NOT NULL,
  `Password` varchar(15) NOT NULL,
  `First_name` varchar(20) NOT NULL,
  `Last_name` varchar(20) NOT NULL,
  `Date_of_birth` date NOT NULL,
  `Nationality` char(20) NOT NULL,
  `Street` char(30) NOT NULL,
  `House_number` int NOT NULL,
  `Postal_code` varchar(6) NOT NULL,
  `City` char(20) NOT NULL,
  `Phone_number` varchar(15) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `Gender` enum('M','F') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ID` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Admin0','Ray','Zwiep','1995-02-20','Dutch','Venlo',52,'4455','The Hague','064747449','Ray@inholland.nl','M'),(1111,'M123456','Max','Planck','1905-12-12','German','Stationsweg',55,'45897','Amsterdam','0611222252','Max@inholland.nl','M'),(1112,'Ee1234','Emmy','Noether','1945-04-04','German','trhtgr',63,'2196','Utrecht','0622553252','Emmy@inhollan.nl','F'),(1113,'Aa1234','Arthur','Eddington','1933-12-23','English','uydkrjgn',6,'967','Edam','0688889989','Arthur@inhollan.nl','M'),(1114,'Bb123456','Bert','de Wit','1955-01-09','Dutch','tryujhgf',33,'87432','Rotterdam','0611355525','Bert@inholland.nl','M'),(1115,'L123456','Louis','de Broglie','1908-12-12','French','gokore',44,'5434','Haarlem','0611885525','Louis@inholland.nl','M'),(1116,'Aa1234','Piet','Mondriaan','1907-01-31','Dutch','yuko',1,'1234','Goes','0625889989','Piet@inhollan.nl','M'),(1117,'S12345','Sanne','van Hoeve','1994-06-06','Dutch','Valentijnstraat',35,'9896','Amsterdam','0688558589','Sanne@inholland.nl','F'),(1118,'D1234','Daniel','De Graaf','1990-01-15','English','Hoefkade',77,'1412','Arnhem','0614151236','Daniel@inholland.nl','M'),(6660,'J123456','Johann','Bach','1934-01-23','Dutch','dfgjij',89,'76543','Zwolle','0611332257','jhjkhj@inholland.nl','M'),(6661,'P2456','Pjotr','Tjaikovsky','1922-10-10','Russian','oigf',45,'97','Groningen','0610101154','Pjotr@inholland.nl','M'),(6662,'H2456','Hetty','Udang','1999-09-09','Indonesian','drgr',33,'567','Almere','0622111212','Hetty@inholland.nl','F'),(6663,'F2456','Frank','Brandse','1999-01-01','Dutch','uyjghfg',88,'45678','Amsterdam','0611111111','Frank@inholland.nl','M'),(6664,'M2456','Margje','Penning','2001-02-02','Dutch','dfhffy',3,'8765','Diemen','0649911999','Margje@inholland.nl','F'),(6665,'K2456','Kate','Bush','1967-03-31','English','kolk',34,'732','Sittard','0688998898','Kate@inholland.nl','F'),(6666,'W123','Willibrord','Snel','1980-02-22','Dutch','ven',66,'345','Diemen','0631311199','Willibrord@inholland.nl','M'),(6667,'AA1234','Amir','Green','2000-02-08','German','Molstraat',101,'3636','Assen','0615154442','Amir@inholland.nl','M'),(6668,'Ss1234','Shanel','Li','2001-03-10','Japanese','Voorstraat',99,'4585','Emmen','0785544585','Shanel@inholland.nl','F'),(6669,'M12345','Mark','Dong','1999-05-16','French','Botermarkt',100,'7001','Den Haag','0758669985','Mark@inholland.nl','M'),(6670,'Mm1234','Miriam','Meer','2000-08-08','French','Laan',2,'9999','Rotterdam','0666554658','Miriam@inholland.nl','F');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-16 22:47:05
