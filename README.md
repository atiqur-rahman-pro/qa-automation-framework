<div align="center">

# 🎭 Enterprise QA Automation Framework
### Scalable End-to-End Web Testing Solution with Pytest, Playwright & Page Object Model (POM)

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.x-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.x-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/python/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/atiqur-rahman-pro/qa-automation-framework/actions)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Executive Summary

This repository presents a production-ready **End-to-End (E2E) Web Test Automation Framework** engineered using **Pytest** and **Playwright (Python)**. Built around the industry-standard **Page Object Model (POM)** architectural pattern, this framework ensures high maintainability, test execution efficiency, and seamless continuous integration.

---

## 🌟 Key Architectural Features

- **Page Object Model (POM)**: Decouples page element locators and page-specific user interactions from test verification logic.
- **Automatic Failure Screenshots**: Automatically captures and attaches screenshots to the execution report whenever a test failure occurs.
- **Standalone HTML Reports**: Generates self-contained HTML test execution summaries (`reports/report.html`) complete with test duration, status, metadata, and failure evidence.
- **Parallel Test Execution**: Full compatibility with `pytest-xdist` for distributed multi-core test runs.
- **CI/CD Pipeline Integration**: Configured with GitHub Actions (`.github/workflows/test_runner.yml`) to automatically execute test suites on every `push` or `pull_request` and upload execution artifacts.

---

## 📁 Repository Structure

```text
qa-automation-framework/
├── .github/
│   └── workflows/
│       └── test_runner.yml      # GitHub Actions CI/CD Pipeline
├── pages/
│   ├── base_page.py             # Reusable Base Page Object class
│   └── login_page.py            # Page Object for Authentication
├── tests/
│   ├── conftest.py              # Pytest Fixtures & Screenshot Hooks
│   └── test_login.py            # E2E Test Suite
├── reports/                     # HTML Reports & Failure Evidence Screenshots
├── pytest.ini                   # Pytest Global Configuration
└── README.md                    # Project Documentation
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure you have **Python 3.9+** installed on your system.

### 2. Setup Virtual Environment
```bash
# Clone the repository
git clone https://github.com/atiqur-rahman-pro/qa-automation-framework.git
cd qa-automation-framework

# Create & Activate virtual environment
python -m venv .venv

# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies & Playwright Browsers
```bash
pip install pytest pytest-playwright pytest-html pytest-xdist
playwright install chromium
```

### 4. Execute Tests & View Reports
```bash
# Execute full test suite
pytest

# View generated HTML Report
# Open reports/report.html in your browser
```

---

## 🔄 CI/CD Automation

Every code commit triggers the **GitHub Actions Automated Pipeline**, executing:
1. Python environment setup & Playwright browser installation
2. Pytest execution against target web environments
3. Generation and publication of test execution artifacts downloadable directly from GitHub Actions runs.

---

## 👤 Author Identity & Connect

<div align="center">

### **Designed & Developed by Atiqur Rahman**
*Senior Software QA & Test Automation Specialist*

[![Pytest Core Contributor](https://img.shields.io/badge/PYTEST-CORE_OPEN_SOURCE_CONTRIBUTOR-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://github.com/pytest-dev/pytest/pull/14804)
[![Microsoft Playwright Contributor](https://img.shields.io/badge/MICROSOFT_PLAYWRIGHT-OPEN_SOURCE_CONTRIBUTOR-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)](https://github.com/microsoft/playwright-python/pull/3157)
[![YouTube](https://img.shields.io/badge/YOUTUBE-SUBSCRIBE_NOW-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@Digital_Digest_Live)  
[![GitHub](https://img.shields.io/badge/GITHUB-ATIQUR--RAHMAN--PRO-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/atiqur-rahman-pro)
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-CONNECT_ME-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/atiqur-rahman-pro)

</div>
