Project: Network Protocol Tester
================================

Overview:
---------
This project demonstrates RFC-compliant implementations of five application-layer protocols: HTTP, DNS, SMTP, FTP, and POP3. Each protocol is developed within its own Docker container and tested using a Python-based client and a custom GUI.

Key Features:
-------------
1. HTTP: Fetches a static webpage hosted on an Nginx server.
2. DNS: Resolves domain names using a Bind9 server.
3. SMTP: Sends emails using a Namshi SMTP server.
4. FTP: Uploads and lists files using a vsftpd server.
5. POP3: Retrieves email summaries from a custom Python server.

Setup Instructions:
-------------------
1. **Copy Project Directory**:
   Place the `CompNet_Project` directory in your desired location.

2. **Create Docker Network**:
   ```bash
   docker network create --subnet=192.168.1.0/24 custom_net
