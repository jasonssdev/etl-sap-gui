# MAT2.0 APP

##### Clone repo
git clone

##### Create virtual environment
python -m venv .venv

##### Virtual environment activation on Git BASH
source .venv/Scripts/activate

##### Run scripts in power shell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

##### Virtual environment activation on Git CMD
.venv\Scripts\activate.bat

##### Virtual environment activation on Power Shell
.venv\Scripts\activate.ps1

##### install dependencies
pip install -r requirements.txt

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