# Cybersecurity-Log-Database
A simulated SQL database designed for cybersecurity log analysis, focusing on user login attempts, device tracking, and suspicious activity monitoring. This project supports foundational intrusion detection use cases and demonstrates how SQL can be applied in security-focused systems.

## Overview
This SQL project simulates a cybersecurity log database used to track system access attempts, login patterns, and suspicious behavior. It supports basic log monitoring for intrusion detection, especially useful in training or testing anomaly detection models.

## Database Schema
Main tables:
- **Users**: Stores user account information.
- **Login_Attempts**: Logs successful and failed login attempts with timestamps.
- **Devices**: Tracks devices used to access the system.
- **Alerts**: Captures flagged activity based on predefined rules or thresholds.
