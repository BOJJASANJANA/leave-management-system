import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="leaveuser",          # change if needed
        password="leave123",  # change if needed
        database="leave_db"
    )

