import snowflake.connector

# connect to snowflake
def connect_to_snowflake():
    try:
        config = {
            "user": 'kassambara',
            "password": 'B@mako2021',
            "account": 'kdgvgef-hs83902',
            "database": 'Systeme_Tutorat',
            "schema": 'Systeme_Tutorat_SCHEMA',
        }
        conn = snowflake.connector.connect(**config)
        cursor = conn.cursor()
        print("Connected to Snowflake")
        return cursor
    except Exception as e:
        print(f"Error connecting to Snowflake: {e}")



