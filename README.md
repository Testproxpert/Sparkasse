# Sparkasse Web Testing Automation

## Project Overview
Automated test suite for the Sparkasse web application focusing on:
- Login
- Account balance view
- Money transfer

## Project Structure
```
sparkasse-web-testing/
│
├── pages/          # Page Objects
├── tests/          # Test cases
├── utils/          # Utilities (config, driver manager)
├── .env            # Environment variables (credentials, URL)
├── requirements.txt
├── README.md
└── bug_report_template.md
```

## Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/sparkasse-web-testing.git
cd sparkasse-web-testing
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # MacOS
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

3. Set your credentials and base URL in `.env` file.

4. Run tests using pytest:
```bash
pytest tests/
```

## Test Reports
Test results will be displayed in the console. You can extend with pytest-html or other reporting plugins.

## Bug Reporting
Use the `bug_report_template.md` file as a base for reporting any issues found.
