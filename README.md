# Sistemas embedidos y sensores
---
## Integrantes:
- Alberto Abarzua
- Diego Ruiz
- Nicolas Carcamo


# How to run


## 1. Install dependencies
```bash
pip install pdm 
cd python_code
pdm install
```
## 2. Build and flash the firmware
```bash
idf.py build flash
```
## 3. Run the GUI
```bash
cd python_code/src
pdm run main.py
```
