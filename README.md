# 🛡 Advanced Packet Sniffer & ARP Spoofing Detector (Mini Network IDS)

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Scapy](https://img.shields.io/badge/Scapy-Network%20Security-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

---

## 📌 Project Overview

**Advanced Packet Sniffer & ARP Spoofing Detector (Mini Network IDS)** is a real-time Network Intrusion Detection System (NIDS) developed using **Python**, **Scapy**, **SQLite**, and **Streamlit**.

The application captures live network packets, analyzes multiple network protocols, detects ARP spoofing attacks, stores packet information in a database, visualizes network traffic using an interactive dashboard, and generates professional security reports.

This project demonstrates practical cybersecurity concepts including packet sniffing, protocol analysis, intrusion detection, database management, and security monitoring.

---

# 🚀 Features

### ✅ Live Packet Capture

- Capture packets in real time
- Analyze incoming and outgoing traffic
- Works with Scapy

---

### ✅ Protocol Analysis

Detects and analyzes:

- TCP
- UDP
- ICMP
- ARP
- IPv6

---

### ✅ ARP Spoofing Detection

- Monitors IP-to-MAC mappings
- Detects suspicious MAC changes
- Generates security alerts
- Stores alerts in SQLite

---

### ✅ SQLite Database

Stores

- Captured Packets
- Alerts
- Sessions
- Runtime Statistics

---

### ✅ Professional Dashboard

Interactive Streamlit Dashboard with

- Live Statistics
- Protocol Distribution
- Traffic Timeline
- Top Source IPs
- Top Destination IPs
- Packet Explorer
- Alert Monitoring
- Session Information

---

### ✅ Report Generation

Generate reports in

- PDF
- CSV
- JSON

---

### ✅ Logging

Maintains detailed logs of

- Packet Capture
- Alerts
- Errors
- Runtime Events

---

# 🏗 Project Architecture

```
                        +----------------------+
                        |   Network Interface  |
                        +----------+-----------+
                                   |
                                   |
                            Scapy Packet Sniffer
                                   |
                     +-------------+--------------+
                     |                            |
             Packet Analyzer              ARP Detector
                     |                            |
                     +-------------+--------------+
                                   |
                            SQLite Database
                                   |
                     +-------------+-------------+
                     |                           |
             Streamlit Dashboard         Report Generator
                     |
              Charts & Analytics
```

---

# 📂 Project Structure

```
Advanced-Packet-Sniffer-ARP-Detector/

│
├── dashboard/
│   └── app.py
│
├── database/
│   └── packets.db
│
├── logs/
│
├── reports/
│
├── src/
│   ├── arp_detector.py
│   ├── capture_manager.py
│   ├── charts.py
│   ├── config.py
│   ├── database.py
│   ├── detector_manager.py
│   ├── export.py
│   ├── logger.py
│   ├── packet_analyzer.py
│   ├── report_generator.py
│   ├── sniffer.py
│   ├── statistics.py
│   └── utils.py
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Advanced-Packet-Sniffer-ARP-Detector.git

cd Advanced-Packet-Sniffer-ARP-Detector
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Npcap (Windows)

Download and install:

https://npcap.com

Enable

✅ WinPcap Compatible Mode

---

# ▶ Run the Packet Sniffer

```bash
python main.py
```

---

# ▶ Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📊 Dashboard

The dashboard provides

- Live Packet Statistics
- Protocol Distribution
- Traffic Timeline
- Top Source Hosts
- Top Destination Hosts
- Packet Explorer
- Security Alerts
- Export Reports

---

# 📄 Generated Reports

Supports

- PDF Report
- CSV Report
- JSON Report

---

# 🛠 Technologies Used

### Programming Language

- Python 3.11

### Libraries

- Scapy
- Streamlit
- Plotly
- Pandas
- ReportLab
- SQLite3

### Database

- SQLite

### Visualization

- Plotly
- Streamlit

---

# 🔐 Security Concepts Demonstrated

- Packet Sniffing
- Protocol Analysis
- ARP Spoofing Detection
- Network Monitoring
- Intrusion Detection
- Security Event Logging
- Report Generation
- Network Traffic Analysis

---

# 📸 Screenshots

Add screenshots here after running the project.

```
screenshots/

dashboard.png

packet_capture.png

alerts.png

report.png
```

---

# 🎯 Future Improvements

- Port Scan Detection
- SYN Flood Detection
- ICMP Flood Detection
- DNS Monitoring
- Email Alerts
- Geo-IP Mapping
- Threat Intelligence Integration
- Machine Learning Based Detection

---

# 💼 Resume Description

Developed a real-time **Mini Network Intrusion Detection System (NIDS)** using **Python, Scapy, SQLite, Streamlit, and Plotly**. The system captures live network packets, analyzes multiple protocols, detects ARP spoofing attacks, stores packet information in SQLite, generates professional PDF/CSV/JSON reports, and provides an interactive SOC-style dashboard for network monitoring and security analysis.

---

# 🎓 Learning Outcomes

Through this project I gained practical experience with

- Packet Capture
- Network Protocols
- Cybersecurity Fundamentals
- Intrusion Detection
- SQLite Database Design
- Streamlit Dashboard Development
- Report Generation
- Logging
- Software Architecture
- Modular Python Development

---

# 👨‍💻 Author

**Aryan Choughule**

Computer Engineering Student

Cybersecurity Enthusiast

---

# 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star!
