import psycopg2

def get_db_connection():
    # We will tell AWS to use these exact passwords later
    return psycopg2.connect(
        dbname="unidb",
        user="admin",
        password="securepassword123",
        host="db" # 'db' is the name of our database container
    )
