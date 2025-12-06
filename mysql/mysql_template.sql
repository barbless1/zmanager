-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 06, 2025 at 08:53 AM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `data_zoo`
--

-- --------------------------------------------------------

--
-- Table structure for table `animal`
--

DROP TABLE IF EXISTS `animal`;
CREATE TABLE IF NOT EXISTS `animal` (
  `IdAnimal` int(11) NOT NULL AUTO_INCREMENT,
  `NomAnimal` varchar(32) DEFAULT NULL,
  `DateNaissance` date DEFAULT NULL,
  `DateArriveeZoo` date DEFAULT NULL,
  `DateDepartZoo` date DEFAULT NULL,
  PRIMARY KEY (`IdAnimal`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `animal`
--

INSERT INTO `animal` (`IdAnimal`, `NomAnimal`, `DateNaissance`, `DateArriveeZoo`, `DateDepartZoo`) VALUES
(1, 'BLACK', '2010-10-01', '2014-01-18', NULL),
(2, 'LADY', '2006-01-28', '2014-05-26', NULL),
(3, 'REMUS', '2006-01-28', '2014-05-26', NULL),
(4, 'HUAN HUAN', '2012-04-13', '2016-10-09', NULL),
(5, 'YUAN MENG', '2017-12-04', '2017-12-04', NULL),
(6, 'KRUGER', '2009-03-24', '2011-08-12', '2018-07-24'),
(7, 'SWAHILI', '2016-02-16', '2016-02-16', NULL),
(8, 'DIABLO', '2006-05-03', '2012-12-01', '2019-10-15'),
(9, 'TANA', '2013-07-23', '2013-07-23', NULL),
(10, 'NORA', '2008-09-10', '2015-11-09', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `utilisateurs`
--

DROP TABLE IF EXISTS `utilisateurs`;
CREATE TABLE IF NOT EXISTS `utilisateurs` (
  `IdSoigneur` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(11) DEFAULT NULL,
  `Prenom` varchar(32) DEFAULT NULL,
  `Roles` int(11) NOT NULL DEFAULT '1' COMMENT 'Correspond au rôle de l''utilisateur sur la plateforme (0 à 3)\r\n0 - Invité\r\n1 - Soigneur\r\n2 - Soigneur chef\r\n3 - Admin Système',
  `encrypted_motdepasse` text NOT NULL COMMENT 'Mot de passe encrypté en local par MD5',
  PRIMARY KEY (`IdSoigneur`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `utilisateurs`
--

INSERT INTO `utilisateurs` (`IdSoigneur`, `Nom`, `Prenom`, `Roles`, `encrypted_motdepasse`) VALUES
(1, 'GENET', 'Jean-Pierre', 1, ''),
(2, 'LETELLIER', 'Pierre', 1, ''),
(3, 'JOLY', 'Frédéric', 1, ''),
(4, 'MARTIN', 'Lisa', 1, ''),
(5, 'JOLY', 'Frédéric', 1, ''),
(6, 'MARTIN', 'Lisa', 1, ''),
(7, 'MICHEL', 'Anne', 1, ''),
(8, 'LEFEBVRE', 'Joëlle', 1, ''),
(9, 'ANTOINE', 'Eric', 1, ''),
(10, 'DUMONT', 'Sophie', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `vaccin`
--

DROP TABLE IF EXISTS `vaccin`;
CREATE TABLE IF NOT EXISTS `vaccin` (
  `IdVaccin` int(11) NOT NULL AUTO_INCREMENT,
  `TypeVaccin` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`IdVaccin`)
) ENGINE=InnoDB AUTO_INCREMENT=761535490 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `vaccin`
--

INSERT INTO `vaccin` (`IdVaccin`, `TypeVaccin`) VALUES
(1564984, 'meningocoque'),
(1654823, 'Leptospirose'),
(5148236, 'Leucose'),
(6557984, 'antirabique'),
(6848945, 'antirabique'),
(7564982, 'poliomyélite'),
(16543278, 'meningocoques'),
(35843162, 'grippe'),
(44597815, 'parvovirose'),
(69386541, 'antirabique'),
(95623484, 'hépatite'),
(135465132, 'encéphalomyocardite'),
(761535489, 'maladie de carré');

-- --------------------------------------------------------

--
-- Table structure for table `visite`
--

DROP TABLE IF EXISTS `visite`;
CREATE TABLE IF NOT EXISTS `visite` (
  `IdVisite` int(11) NOT NULL AUTO_INCREMENT,
  `DateDerniereVisite` date DEFAULT NULL,
  `DateDernierVaccin` date DEFAULT NULL,
  `DateDerniereEchographie` date DEFAULT NULL,
  `Pathologie` varchar(32) DEFAULT NULL,
  `DescriptionVisite` varchar(255) DEFAULT NULL,
  `IdAnimal` int(11) NOT NULL,
  `IdSoigneur` int(11) NOT NULL,
  `IdVaccin` int(11) DEFAULT NULL,
  PRIMARY KEY (`IdVisite`),
  KEY `IdAnimal` (`IdAnimal`),
  KEY `IdSoigneur` (`IdSoigneur`),
  KEY `IdVaccin` (`IdVaccin`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `visite`
--

INSERT INTO `visite` (`IdVisite`, `DateDerniereVisite`, `DateDernierVaccin`, `DateDerniereEchographie`, `Pathologie`, `DescriptionVisite`, `IdAnimal`, `IdSoigneur`, `IdVaccin`) VALUES
(1, '2018-12-23', '2018-12-23', NULL, NULL, 'Visite annuelle conforme. Vaccin leptospirose', 1, 1, 1654823),
(2, '2019-09-01', '2018-12-07', '2019-09-01', 'GESTATION', 'Suivi grossesse', 2, 7, NULL),
(3, '2019-10-16', '2018-12-07', '2019-10-16', 'GESTATION', 'Suivi grossesse', 2, 7, NULL),
(4, '2019-08-06', '2019-08-06', '2017-11-28', NULL, 'Visite annuelle vaccin', 4, 5, 761535489),
(5, '2019-06-19', '2019-04-04', NULL, 'Plaie pate avant droite', NULL, 5, 5, NULL),
(6, '2019-10-02', '2019-10-02', NULL, NULL, 'Visite annuelle conforme.Vaccin', 10, 2, 44597815),
(7, '2019-10-02', '2019-04-03', '2019-10-02', 'Perte de poids', 'Examens approfondis Echographie abdominale prise de sang', 7, 8, NULL),
(8, '2018-07-24', NULL, NULL, NULL, 'Visite départ conforme', 6, 1, NULL),
(9, '2019-10-15', NULL, NULL, NULL, 'Visite départ conforme', 8, 9, NULL),
(10, '2019-07-27', '2018-12-07', '2019-07-27', 'GESTATION', 'Suivi grossesse', 2, 10, NULL);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `visite`
--
ALTER TABLE `visite`
  ADD CONSTRAINT `visite_ibfk_1` FOREIGN KEY (`IdAnimal`) REFERENCES `animal` (`IdAnimal`),
  ADD CONSTRAINT `visite_ibfk_2` FOREIGN KEY (`IdSoigneur`) REFERENCES `utilisateurs` (`IdSoigneur`),
  ADD CONSTRAINT `visite_ibfk_3` FOREIGN KEY (`IdVaccin`) REFERENCES `vaccin` (`IdVaccin`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
