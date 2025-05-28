# Rockwell PLC Data Logger & Web Viewer



A Python-based application to read data from Rockwell Allen-Bradley PLCs (ControlLogix/CompactLogix) via EtherNet/IP, store it in a MySQL database, and display live and historical values on a web interface.

## Table of Contents

- [Features](#features)
- [Project Status](#project-status)
- [Architecture Overview](#architecture-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)

## Features

*   **PLC Data Acquisition:** Connects to Rockwell PLCs (ControlLogix, CompactLogix, Micro800 series with EtherNet/IP support) using [mention library, e.g., `pylogix`, `libplctag` wrapper].
*   **Tag Monitoring:** Reads specified PLC tags at configurable intervals.
*   **Data Storage:** Persists tag values and timestamps into a [Database Type] database.
*   **Web Visualization:** Displays current and historical PLC tag values on a user-friendly web page.
[//](*   **Real-time Updates (Optional):** Web interface updates dynamically using [e.g., WebSockets, Server-Sent Events, or polling].)

## Project Status

This project is used for educational purposes.

## Architecture Overview

This project typically consists of three main components:

1.  **Data Acquisition Service:** A script/service responsible for:
    *   Connecting to the Rockwell PLC.
    *   Reading the configured PLC tags periodically.
    *   Writing the retrieved data to the database.
2.  **Database:** Stores the historical and current tag data.
    *   MySQL
3.  **Web Application (Backend & Frontend):**
    *   **Backend API:** Serves data from the database to the frontend.
    *   **Frontend:** A web page that queries the backend API and displays the data in a user-friendly format (tables, charts, gauges).

## Prerequisites

Before you begin, ensure you have met the following requirements:

*   Access to a Rockwell PLC (ControlLogix, CompactLogix, or compatible) on the network.
    *   Know its IP Address.
    *   Know the Slot number for the EtherNet/IP module (usually 0 for CompactLogix or chassis-based ENBT/EN2T).
*   PLC tags you want to monitor are defined and accessible.
*   Python 3.8+ and Pip
*   MySQL server
*   Git

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ads106-senai/2501_ProjInt01.git
    cd 2501_ProjInt01
    ```

2.  **Set up Python Environment (if applicable):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
