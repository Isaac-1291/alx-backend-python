import mysql.connector
import csv
import uuid
from mysql.connector import Error

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
        print("Database created")
    except Error as e:
        print(f"Error: {e}")

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ALX_prodev"
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(3, 0) NOT NULL,
                INDEX idx_user_id (user_id)
            )
        """)
        cursor.close()
        print("Table created")
    except Error as e:
        print(f"Error: {e}")

def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM user_data")
        count = cursor.fetchone()[0]
        if count > 0:
            print("Data already exists")
            return

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, row["name"], row["email"], int(row["age"])))
        
        connection.commit()
        cursor.close()
        print("Data inserted")
    except Exception as e:
        print(f"Insert error: {e}")