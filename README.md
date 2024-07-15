# Data Manipulation Project : CMS Detector 

## Overview

This project provides a tool for detecting the CMS (Content Management System) used by websites. It uses Selenium to automate interactions with a CMS detection service and processes a list of URLs from a JSON file. The results are then saved to an output JSON file with CMS information.

I also used this video to understand Selenuim :
[Python Selenium Tutorial - Automate Websites and Create Bots](https://www.youtube.com/watch?v=NB8OceGZGjA&t=1498s)


## What is CMS

A Content Management System (CMS) is a software application used to create, manage, and modify digital content. CMSs are commonly used for web content management and enterprise content management. Popular CMS platforms include WordPress, Joomla, Drupal, and many others.

## Why Selenium

Selenium is a powerful tool for controlling web browsers through programs and performing browser automation. It is functional for all browsers, works on all major OS, and its scripts can be written in various programming languages including Python, Java, C#, etc. In this project, Selenium is used to interact with the CMS detection service to automate the process of inputting URLs and scraping the resulting CMS information.

## Project Structure
```
CMS-Detector/
│
├── driver/
│   ├── chromedriver.exe
│
├── includes/
│   ├── valid.py            
│   ├── scrap.py            
│
├── data_test.json
│
├── main.py
│   
└── README.md              
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/darkiller03/CMS-Detector.git
   ```
2. **Install libraries**:
    ```bash
    pip install selenuim 
    ```
2. **Run the main function**:
    ```bash
   python main.py
   ```
   or Run the **main.py** function manually


