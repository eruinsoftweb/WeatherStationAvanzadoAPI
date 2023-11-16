-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-11-2023 a las 07:04:17
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `weatherstationesp32`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `indoorweatherdataesp32`
--

CREATE TABLE `indoorweatherdataesp32` (
  `Date` datetime NOT NULL,
  `Temperature` float NOT NULL,
  `Altitude` float NOT NULL,
  `Pressure` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `indoorweatherdataesp32`
--

INSERT INTO `indoorweatherdataesp32` (`Date`, `Temperature`, `Altitude`, `Pressure`) VALUES
('2023-06-05 12:38:00', 26, 23, 3455),
('2023-06-05 12:39:00', 26.3, 23.7, 3455.8),
('2023-06-08 12:39:00', 26.3, 23.7, 3455.8),
('2023-06-05 13:11:00', 26.3, 23.7, 3455.8),
('2023-06-08 13:11:00', 26.3, 23.7, 3455.8),
('2023-06-08 13:11:00', 26.3, 23.7, 3455.8),
('2023-06-08 13:20:00', 26.3, 23.7, 3455.8),
('2023-06-08 13:20:00', 26.3, 23.7, 3455.8),
('2023-06-08 13:20:00', 26.3, 23.7, 3455.8),
('2023-06-08 13:22:00', 26.3, 23.7, 3455.8),
('2023-06-05 13:11:00', 26.3, 23.7, 3455.8),
('2023-11-16 00:21:23', 32, 63.34, 952.22),
('2023-11-16 00:22:23', 16.61, 21.79, 1053.27),
('2023-11-16 00:23:23', 31.06, 13.77, 1041.95),
('2023-11-16 00:24:23', 30.37, 51.79, 949.61),
('2023-11-16 00:25:23', 28.5, 21.37, 1097.18),
('2023-11-16 00:26:23', 6.19, 12.2, 1045.36),
('2023-11-16 00:27:23', 30.16, 54.46, 964.56),
('2023-11-16 00:28:23', 17.38, 6.78, 913.13),
('2023-11-16 00:29:23', -6.79, 61.69, 909.62),
('2023-11-16 00:30:23', 6.29, 44.85, 1057.87),
('2023-11-16 00:31:23', -10.12, 63.01, 1092.65),
('2023-11-16 00:32:23', 15.07, 68.01, 964.38),
('2023-11-16 00:33:24', 3.47, 62.53, 1051.18),
('2023-11-16 00:34:24', 23.83, 14.94, 985.34),
('2023-11-16 00:35:24', 14.02, 54.36, 1093.5),
('2023-11-16 00:36:24', 26.24, 55.82, 913.68),
('2023-11-16 00:37:24', 22.69, 17.2, 944.67),
('2023-11-16 00:38:24', 25.11, 14.1, 1074.72),
('2023-11-16 00:39:24', -9.41, 70.68, 1049.55),
('2023-11-16 00:40:24', 17.69, 52.86, 1025.09),
('2023-11-16 00:41:24', 35.08, 32.69, 999.74),
('2023-11-16 00:42:24', -13.9, 15.54, 1096.69),
('2023-11-16 00:43:24', -1.27, 69.08, 969.15),
('2023-11-16 00:44:24', 11.79, 16.87, 930.97);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
