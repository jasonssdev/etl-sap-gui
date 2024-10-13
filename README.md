# ETL SAP GUI with Python

This project demonstrates an ETL (Extract, Transform, Load) process using Python, integrated with SAP GUI. The goal is to extract data from SAP, transform it according to business needs, and load it into a specified destination.

## Tech Stack 

![Python](https://img.shields.io/badge/-Python-9966ff?logo=python&logoColor=f1f1f1)&nbsp;
![Pandas](https://img.shields.io/badge/-Pandas-9966ff?logo=pandas&logoColor=f1f1f1)&nbsp;
![Jupyter](https://img.shields.io/badge/-Jupyter-9966ff?logo=jupyter&logoColor=f1f1f1)&nbsp;
![SQL_Server](https://img.shields.io/badge/-SQL_Server-9966ff?logo=microsoftsqlserver&logoColor=f1f1f1)&nbsp;
![PowerBI](https://img.shields.io/badge/-PowerBI-9966ff?logo=googleanalytics&logoColor=f1f1f1)&nbsp;
![SAP](https://img.shields.io/badge/-SAP-9966ff?logo=sap&logoColor=f1f1f1)&nbsp;
![Terminal](https://badgen.net/badge/icon/Terminal?icon=terminal&label=&color=9966ff&labelColor=9966ff&scale=1)&nbsp;
![Windows](https://badgen.net/badge/icon/Windows?icon=windows&label=&color=9966ff&labelColor=9966ff&scale=1)&nbsp;
![Git](https://img.shields.io/badge/-Git-9966ff?logo=git&logoColor=f1f1f1)&nbsp;
![Github](https://img.shields.io/badge/-Github-9966ff?logo=github&logoColor=f1f1f1)&nbsp;
![VSCode](https://badgen.net/badge/icon/VSCode?icon=visualstudio&label=&color=9966ff&labelColor=9966ff&scale=1)&nbsp;
## Getting Started

### Prerequisites

Ensure that you have the following installed:
- [Python 3.12](https://www.python.org/downloads/)
- [SAP GUI](https://support.sap.com/en/product/connectors/sap-gui.html)
- [Git](https://git-scm.com/)
- Virtual environment setup tools

### Installation

#### 1. **Clone the Repository**

To get a copy of the project locally, run:

```bash
git clone git@github.com:jasonssdev/etl-sap-gui.git
```

#### 2. **Set Up a Virtual Environment**

* On Windows (Git Bash):

```bash
python -m venv .venv
```

#### 3. **Set Up a Virtual Environment**

* On Windows (Git Bash):

```bash
source .venv/Scripts/activate
```

* On Windows (CMD):

```bash
.venv\Scripts\activate.bat
```

* On Windows (PowerShell):

```bash
.venv\Scripts\activate.ps1
```
#### 4. **Install Dependencies**
* On Windows (Git Bash):

```bash
pip install -r requirements.txt
```

## Environment Setup

To run the scripts correctly, ensure that your Python environment is set up properly:

* CMD (Windows)
```bash
set PYTHONPATH=%PYTHONPATH%;C:\Users\youruser\repository
```
* BASH (Windows)
```bash
export PYTHONPATH="$PYTHONPATH:/c/Users/youruser/repository"
```
* PowerShell (Windows)
```bash
$env:PYTHONPATH = "$env:PYTHONPATH;C:\Users\youruser\repository"
```
Check the PYTHONPATH to ensure it's set:
```bash
echo %PYTHONPATH%
```
## Configuration (VS Code)

You can configure the project in VS Code by modifying the settings.json file. This ensures that the IDE is using the correct Python interpreter and paths.

* To open the settings file:
```bash
notepad %APPDATA%\Code\User\settings.json
```
Add the following configuration:
```json
{
    "python.pythonPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}/src"
    }
}
```
## Configuration (VS Code)
Once everything is set up, you can start running your ETL scripts within the activated virtual environment. Be sure to activate the virtual environment every time before running your Python scripts.

## Project Structure

```
    ├── LICENSE
    |
    ├── README.md  <- The top-level README for developers using this project
    |
    ├── data
    │       ├── preprocessed  <- Data before to upload to remote server
    |       |
    │       └── raw  <- The original data, immutable data dump
    │
    ├── notebooks   <- Jupyter notebooks, where code was tested
    │
    ├── references  <- Scripts for reference
    │
    ├── requirements.txt <- The requirements file for reproducing the environment
    |
    ├── .gitignore  <- Directories and files to ignore in git
    │
    └── src  <- Source code directory for the project
            |
    |       ├─ sap_extract   <- Python scripts to extract Data
    |       |
    |       ├─ script_transform   <- Python scripts to transform Data
    |       |
    |       ├─ sql_server_load   <- Python scripts to load Data
    |       |
    |       ├─ main_2.py   <- main script to run every 24 hours
    |       |
    |       └─ main.py   <- main script to run every 2 hours
    |
    ├── run_mat_main_2.bat  <- script to run the app automatically every 24 hour
    │
    ├── run_mat_main.bat  <- script to run the app automatically every 2 hour
    |
    ├── .env  <- file to handle environment variables
```

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.

## Troubleshooting
If you encounter issues with virtual environment activation, check the system's execution policy on Windows:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Contributing
Feel free to submit pull requests or open issues to suggest improvements or report bugs.

## Social media contact

<p align="center">
<a href="https://www.youtube.com/@jasonssdev" target=”_blank”><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"/></a>
<a href="https://www.instagram.com/jasonssdev/" target=”_blank”><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
<a href="https://x.com/jasonssdev" target=”_blank”><img src="https://img.shields.io/badge/x-000000?style=for-the-badge&logo=x&logoColor=white"/></a>
<a href="https://www.facebook.com/jasonssdev/" target=”_blank”><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white"/></a>
<a href="https://www.tiktok.com/@jasonssdev" target=”_blank”><img src="https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white"/></a>
<a href="https://discord.com/channels/1246892189288501340/1246892189741617194/" target=”_blank”><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white"/></a>
<a href="https://www.twitch.tv/jasonssdev" target=”_blank”><img src="https://img.shields.io/badge/Twitch-9146FF?style=for-the-badge&logo=twitch&logoColor=white"/></a>
<a href="https://www.threads.net/@jasonssdev" target=”_blank”><img src="https://img.shields.io/badge/Threads-000000?style=for-the-badge&logo=Threads&logoColor=white"/></a>