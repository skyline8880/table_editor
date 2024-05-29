# table_editor
Application for correcting phone number from table and comparing two tables phone or full name

### create virtual environment
* Windows
```bash
python -m venv venv
```
* Mac OS / Linux
```bash
python3 -m venv venv
```

make shure your environment is activated

* Windows
```bash
venv/Scripts/activate.bat
```
* Mac OS / Linux
```bash
source venv/bin/activate
```

### requirements

* Windows
```bash
pip install -r requirements.txt
```
* Mac OS / Linux
```bash
pip3 install -r requirements.txt
```

### packaging using pyinstaller

write command below in terminal

```bash
pyinstaller --onefile --windowed --add-data "icons:icons" --icon=sp.ico --name "Table editor" main.py
```
