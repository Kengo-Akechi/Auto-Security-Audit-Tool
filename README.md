# 🛠️ Automated Security Audit Tool & 🌐 Web Scraping and Data Extraction Tool

## Overview

Welcome to the repository containing two powerful Python-based projects designed for automated security audits and web data extraction. These tools demonstrate advanced use of various Python libraries and APIs to achieve their respective tasks efficiently.

## 📜 Table of Contents

1. [🔍 Automated Security Audit Tool](#-automated-security-audit-tool)
    - [📝 Description](#description)
    - [✨ Features](#features)
    - [💻 Technologies Used](#technologies-used)
    - [📖 Usage](#usage)
2. [🕸️ Web Scraping and Data Extraction Tool](#-web-scraping-and-data-extraction-tool)
    - [📝 Description](#description-1)
    - [✨ Features](#features-1)
    - [💻 Technologies Used](#technologies-used-1)
    - [📖 Usage](#usage-1)
3. [⚙️ Installation](#installation)


## 🔍 Automated Security Audit Tool

### 📝 Description

The Automated Security Audit Tool is designed to perform comprehensive security audits on a given domain. It identifies subdomains, conducts port scans using Nmap, gathers HTTP headers, and analyzes the results for potential vulnerabilities.

### ✨ Features

- 🌐 **Subdomain Enumeration:** Uses `crt.sh` to identify subdomains associated with a target domain.
- 🔍 **Port Scanning:** Integrates Nmap to perform comprehensive port scans and service detection.
- 📜 **HTTP Header Gathering:** Collects HTTP headers from discovered subdomains.
- 🛡️ **Vulnerability Analysis:** Implements basic checks for outdated software versions to identify potential vulnerabilities.

### 💻 Technologies Used

- 🐍 Python
- 🌐 Nmap
- 📨 Requests library
- 🍜 BeautifulSoup
- 🔍 Regex for parsing

### 📖 Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/repo-name.git
    cd repo-name
    ```

2. **Ensure Nmap is installed on your system.**

3. **Run the script:**
    ```bash
    python task2.py
    ```

4. **Enter the target domain when prompted.**

## 🕸️ Web Scraping and Data Extraction Tool

### 📝 Description

This tool performs web scraping combined with Google Custom Search. It searches for a query using Google Custom Search, scrapes the results for content, and saves the data to a JSON file.

### ✨ Features

- 🔍 **Google Custom Search:** Uses Google Custom Search API to get search results for a given query.
- 🌐 **URL Scraping:** Fetches and parses content from each URL in the search results.
- 📄 **JSON Storage:** Saves the scraped data in JSON format for further analysis.

### 💻 Technologies Used

- 🐍 Python
- 🔍 Google Custom Search API
- 📨 Requests library
- 🍜 BeautifulSoup

### 📖 Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/repo-name.git
    cd repo-name
    ```

2. **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Update the API key and CSE ID in the `web_scraping.py` script:**
    ```python
    API_KEY = 'YOUR_API_KEY'
    CSE_ID = 'YOUR_CSE_ID'
    ```

4. **Run the script:**
    ```bash
    python task1.py
    ```

## ⚙️ Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Kengo-Akechi/Auto-Security-Audit-Tool.git
    cd Auto-Security-Audit-Tool
    ```

2. **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```




