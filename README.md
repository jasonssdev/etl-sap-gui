# MAT2.0 APP

##### Clone repo
git clone

##### Create virtual environment
python -m venv .venv

##### Virtual environment activation on Git BASH (Window)
source .venv/Scripts/activate

##### Virtual environment activation on Terminal (MacOS)
source .venv/bin/activate  

##### Run scripts in power shell (Window)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

##### Virtual environment activation on Git CMD (Window)
.venv\Scripts\activate.bat

##### Virtual environment activation on Power Shell (Window)
.venv\Scripts\activate.ps1

##### install dependencies (Window)
pip install -r requirements.txt

##### install dependencies (MacOS)
pip3 install -r requirements.txt  

#### CDM
set PYTHONPATH=%PYTHONPATH%;C:\Users\sepujas\Dev\mat

#### BASH
export PYTHONPATH="$PYTHONPATH:/c/Users/sepujas/Dev/mat"

#### Powershell
$env:PYTHONPATH = "$env:PYTHONPATH;C:\Users\sepujas\Dev\mat\src"
echo %PYTHONPATH%

#### settings.json
notepad %APPDATA%\Code\User\settings.json

```json
{
    "symbols.hidesExplorerArrows": false,
    "workbench.iconTheme": "symbols",
    "python.pythonPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}/src"
    }
}
```


```cdm
git clone
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```