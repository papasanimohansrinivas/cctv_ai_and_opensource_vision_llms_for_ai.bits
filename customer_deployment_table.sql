-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 25, 2023 at 09:00 AM
-- Server version: 8.0.32-0ubuntu0.20.04.2
-- PHP Version: 7.4.3-4ubuntu2.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cctv_ai_usecase_products`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_deployment_table`
--

CREATE TABLE `customer_deployment_table` (
  `row_no` bigint UNSIGNED NOT NULL,
  `client_name` text NOT NULL,
  `client_id_in_system` text NOT NULL,
  `subscribed_usecases` text NOT NULL,
  `dvr_static_ip` text NOT NULL,
  `dvr_port` text NOT NULL,
  `dvr_connection_protocol` text NOT NULL,
  `dvr_user_name` text NOT NULL,
  `dvr_password` text NOT NULL,
  `dvr_connection_systemd_service_name` text NOT NULL,
  `stream_decoding_systemd_service_name` text NOT NULL,
  `image_width_per_usecase` text NOT NULL,
  `image_height_per_usecase` text NOT NULL,
  `frame_aggregration_per_usecase` text NOT NULL,
  `fluentbit_systemd_service_name` text NOT NULL,
  `model_inference_systemd_service_name` text NOT NULL,
  `cam_number_list` text NOT NULL,
  `cam_number_to_udp_port_mapping_list` text NOT NULL,
  `cam_description_list` text NOT NULL,
  `allocated_udp_range_per_static_ip_plus_port_per_client` text NOT NULL,
  `rabbit_mq_queue_name` text NOT NULL,
  `cams_with_call_service_per_usecase` text NOT NULL,
  `cams_with_whatsapp_service_per_usecase` text NOT NULL,
  `subscribed_phone_numbers_for_call` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `subscribed_phone_numbers_for_whatsapp` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='customer_deployment_table';

--
-- Dumping data for table `customer_deployment_table`
--

INSERT INTO `customer_deployment_table` (`row_no`, `client_name`, `client_id_in_system`, `subscribed_usecases`, `dvr_static_ip`, `dvr_port`, `dvr_connection_protocol`, `dvr_user_name`, `dvr_password`, `dvr_connection_systemd_service_name`, `stream_decoding_systemd_service_name`, `image_width_per_usecase`, `image_height_per_usecase`, `frame_aggregration_per_usecase`, `fluentbit_systemd_service_name`, `model_inference_systemd_service_name`, `cam_number_list`, `cam_number_to_udp_port_mapping_list`, `cam_description_list`, `allocated_udp_range_per_static_ip_plus_port_per_client`, `rabbit_mq_queue_name`, `cams_with_call_service_per_usecase`, `cams_with_whatsapp_service_per_usecase`, `subscribed_phone_numbers_for_call`, `subscribed_phone_numbers_for_whatsapp`) VALUES
(1, 'something', 'client_1', 'fire_detection', '49.206.199.97', '25004', 'tcp', 'admin', 'admin#123', 'client_1_49_206_199_97_25004_dvr_connection.service', 'client_1_49_206_199_97_25004_stream_decoding.service', '312', '312', '16', 'client_1_49_206_199_97_25004_fluentbit.service', 'consumer_inference.service', '1,2,3,4,5', '11000,11001,11002,11003,11004', 'office room#second floor corridor#first floor corridor#backyard 1#backyard 2', '11000-11015', 'fire_detection', '1,2,3,4,5', '4,5,1,2,3', '7093054982', '7093054982'),
(2, 'something', 'client_1', 'fire_detection', '49.206.199.97', '25001', 'tcp', 'admin', 'admin#123', 'client_1_49_206_199_97_25001_dvr_connection.service', 'client_1_49_206_199_97_25001_stream_decoding.service', '312', '312', '16', 'client_1_49_206_199_97_25001_fluentbit.service', 'consumer_inference.service', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16', '11016,11017,11018,11019,11020,11021,11022,11023,11024,11025,11026,11027,11028,11029,11030,11031', 'Road view#Ground Floor passage#Gate View#Splash Pool View#PlayGroup GF#PlayArea1#PlayArea2#Reception#Accounts#FunRoom1#FunRoom2#FunRoom4#FunRoom3#EuroFit Area#Kitchen#Activity Room', '11016-11031', 'fire_detection', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16', '7093054982', '7093054982');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_deployment_table`
--
ALTER TABLE `customer_deployment_table`
  ADD UNIQUE KEY `row_no` (`row_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer_deployment_table`
--
ALTER TABLE `customer_deployment_table`
  MODIFY `row_no` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
