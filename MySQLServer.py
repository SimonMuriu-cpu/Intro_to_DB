import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',      # adjust if your MySQL server host is different
            user='root',           # replace with your MySQL username
            password=''            # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor.is_connected():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
