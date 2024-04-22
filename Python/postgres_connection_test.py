"""
Test Postgres Connection
"""

import psycopg2

user = input("Enter Username: ")
passw = input("Enter Password: ")
dbname = input("Enter Dabase: ")
host = input("Enter Postgres Hostname or IP Address: ")
port = input("Enter Postgres Port (Default 5432)")
if port is None or port == "":
    port = '5432'


def postgres_test():

    try:
        conn = psycopg2.connect(f"dbname={dbname} user={user} host={host} password={passw} connect_timeout=1 port={5432}")
        conn.close()
        return True
    except:
        return False

print(postgres_test())