import os

SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")


def connect_to_snowflake():
    import snowflake.connector

    # Gets the version
    print("Connecting...")
    ctx = snowflake.connector.connect(
        user=SNOWFLAKE_USER, password=SNOWFLAKE_PASSWORD, account=SNOWFLAKE_ACCOUNT
    )
    print("Cursor", end=" ")
    cs = ctx.cursor()
    print(cs, end=" ")
    try:
        cs.execute("SELECT current_version()")
        one_row = cs.fetchone()
        print("current_version:", one_row[0])
    finally:
        cs.close()
    ctx.close()


def main():
    connect_to_snowflake()


if __name__ == "__main__":
    main()
