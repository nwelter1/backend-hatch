# Flask HW Blog Posts

### Description
Take-home assessment code for the HW blog posts API project using Flask.
NOTE: Extra credit portion (caching API calls) is not fully implemented here... but can be using the [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) package. Go check it out!

## GET STARTED HERE:
- If you want this application to run locally, clone this repo, and do the following:
  - `cd` into the cloned repo `backend-hatch`
  - Create a Python virtual env:
    - `python -m venv <name_of_your_env>`
  - Activate Python virtual env AND set Flask ENV variables in terminal/CMD:
    - Mac
        - `source <name of env>/bin/activate`
        - `export FLASK_APP=hatch_api`
        - `export FLASK_ENV=development`
    - Windows
        - `<name_of_your_env>\Scripts\activate.bat`
        - `set FLASK_APP=hatch_api`
        - `set FLASK_ENV=development`
  - Install dependencies:
    - `pip install -r requirements.txt`
  - Start dev server:
    - `flask run`
