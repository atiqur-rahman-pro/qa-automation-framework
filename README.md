# 🎭 QA Automation Framework (Pytest + Playwright)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Pytest](https://img.shields.io/badge/Pytest-8.x-blue?logo=pytest)
![Playwright](https://img.shields.io/badge/Playwright-1.x-green?logo=playwright)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A modular, scalable End-to-End (E2E) Web Testing Framework built with **Pytest**, **Playwright (Python)**, and **Page Object Model (POM)** pattern.

---

## 🌟 Key Features

- **Page Object Model (POM)** design architecture
- **Automatic Failure Screenshots** attached to HTML reports
- **Self-Contained HTML Reports** generated automatically (`reports/report.html`)
- **Parallel Test Execution** ready with `pytest-xdist`
- **GitHub Actions CI/CD Pipeline** with automatic report artifact uploads

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9 or higher

### 2. Installation & Setup
```bash
# Clone repository
git clone https://github.com/atiqur-rahman-pro/qa-automation-framework.git
cd qa-automation-framework

# Set up virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1

# Install dependencies & Playwright browser
pip install -r requirements.txt
playwright install chromium
```

### 3. Run Tests & Generate Reports
```bash
# Run tests in headed mode
pytest --headed

# Run tests in headless mode with HTML report
pytest --headless
```

---

## 📊 CI/CD Integration

This project includes a **GitHub Actions CI/CD pipeline** (`.github/workflows/test_runner.yml`) that automatically runs the test suite on every push and pull request, attaching the execution HTML report as a downloadable artifact.

---
*Created by [Atiqur Rahman](https://github.com/atiqur-rahman-pro) – Open Source & QA Contributor to `pytest`.*
