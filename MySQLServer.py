import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (replace values with your credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Tokur@h10"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Safely close connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
