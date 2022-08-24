# Connect to Snowflake db
https://www.snowflake.com/en/

## Usage

* Provide your Snowflake credential to `.env`:
```
cp .env.example .env
```

* Run test connection:
```
make main
```
    export PYTHONWRITEBYTECODE=1
    export PYTHONUNBUFFERED=1
    pipenv run python main.py
    Loading .env environment variables...
    Connecting...
    Cursor <snowflake.connector.cursor.SnowflakeCursor object at 0x10c7d3fd0> current_version: 6.28.1

## Prerequisite
* pipenv (https://pipenv.pypa.io/en/latest/)
* make (https://www.gnu.org/software/make/)