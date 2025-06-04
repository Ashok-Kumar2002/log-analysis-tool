# Log Analysis Tool

# Overview

This is a simple Python script that analyzes system log files to identify:

- Failed login attempts  
- Successful logins  
- Invalid usernames used in login attempts  

The tool helps in monitoring security events by summarizing important login activities from log files.

# Features

- Counts total failed login attempts  
- Counts total successful logins  
- Lists all unique invalid usernames that attempted to log in  

# How to Use

1. Place your log file in the same folder as the script and name it sample.log.  
2. Run the script using Python:

   
   python log_analyzer.py
