#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration Module for Course Platform Scraper

This module contains all configuration settings and constants for the web scraper,
including URLs, request parameters, and file paths.
"""

import os
from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# URLs
BASE_URL = "https://harkirat.classx.co.in"
LOGIN_URL = f"{BASE_URL}/login"
COURSE_URL = f"{BASE_URL}/new-courses/8-live-0-100-complete"
DASHBOARD_URL = f"{BASE_URL}/dashboard"
ANALYTICS_URL = f"{BASE_URL}/dashboard/analytics"

# HTTP Headers
HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

# Selenium Settings
SELENIUM_TIMEOUT = 30  # seconds
WEBDRIVER_PATH = None  # Set this if you need a specific driver path
HEADLESS = True
SELENIUM_WINDOW_SIZE = (1920, 1080)

# Request Settings
REQUEST_TIMEOUT = 30  # seconds
REQUEST_DELAY = 3  # seconds between requests for rate limiting
MAX_RETRIES = 3

# Directory Structure
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

# Output File Paths
USER_DATA_CSV = os.path.join(PROCESSED_DATA_DIR, "user_data.csv")
FINANCIAL_DATA_JSON = os.path.join(PROCESSED_DATA_DIR, "financial_data.json")
RAW_HTML_DIR = os.path.join(RAW_DATA_DIR, "html")

# Logging Configuration
LOG_FILE = os.path.join(LOGS_DIR, "scraper.log")
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Make sure directories exist
for directory in [DATA_DIR, LOGS_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, RAW_HTML_DIR]:
    os.makedirs(directory, exist_ok=True)

# Login Form Selectors
EMAIL_FIELD_SELECTOR = "email"  # ID or name of the email input field
PASSWORD_FIELD_SELECTOR = "password"  # ID or name of the password input field
LOGIN_BUTTON_SELECTOR = "//button[contains(text(), 'Login') or contains(text(), 'Sign in')]"  # XPath for login button

# Data Selectors - Customize these based on actual HTML structure
USER_LIST_SELECTOR = ".user-list, .student-card, .user-item"
USER_NAME_SELECTOR = ".user-name"
USER_EMAIL_SELECTOR = ".user-email"
USER_PAYMENT_STATUS_SELECTOR = ".payment-status"
USER_JOIN_DATE_SELECTOR = ".join-date"

TOTAL_USERS_SELECTOR = ".total-users-value"
PAID_USERS_SELECTOR = ".paid-users-value"
TOTAL_GMV_SELECTOR = ".total-gmv-value"
TOTAL_PROFIT_SELECTOR = ".total-profit-value"

