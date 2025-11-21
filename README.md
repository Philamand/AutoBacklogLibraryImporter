# AutoBacklog Library Importer
A simple script that allows you to save your private PlayStation library into a json file, allowing you to import it to your AutoBacklog account without sharing your NPSSO.

## Run with Astral UV
Add your NPSSO on line 11, then run `uv run main.py`

## Run with a python env
_Requires python 3.10 or higher_
- Add your NPSSO on line 11
- Create a virtual env: `python3 -m venv env`
- Activate your virtual env: `source env/bin/activate`
- Install dependency: `pip install PSNAWP httpx`
- Run the script `python main.py`