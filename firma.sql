-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Czas generowania: 19 Gru 2022, 22:22
-- Wersja serwera: 10.4.21-MariaDB
-- Wersja PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `firma`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Godziny`
--

CREATE TABLE `Godziny` (
  `Miesiąc` int(11) NOT NULL,
  `Godziny` int(11) NOT NULL,
  `ID_PRACOWNIKA` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `Godziny`
--

INSERT INTO `Godziny` (`Miesiąc`, `Godziny`, `ID_PRACOWNIKA`) VALUES
(1, 160, 1),
(1, 180, 2),
(1, 120, 3),
(1, 200, 4),
(1, 135, 5),
(2, 200, 1),
(2, 145, 2),
(2, 155, 3),
(2, 165, 4),
(2, 180, 5),
(11, 160, 1),
(11, 123, 2),
(11, 180, 3),
(11, 160, 4),
(11, 135, 5),
(12, 134, 1),
(12, 210, 2),
(12, 155, 3),
(12, 134, 4),
(12, 160, 5);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Pracownicy`
--

CREATE TABLE `Pracownicy` (
  `ID` int(11) NOT NULL,
  `STAWKA_GODZ` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `Pracownicy`
--

INSERT INTO `Pracownicy` (`ID`, `STAWKA_GODZ`) VALUES
(1, 20),
(2, 35),
(3, 45),
(4, 40),
(5, 28);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
