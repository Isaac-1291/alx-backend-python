import mysql.connector
from decimal import Decimal

def stream_user_ages():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ALX_prodev"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:
        if isinstance(age, Decimal):
            age = int(age)
        yield age

    cursor.close()
    conn.close()

def calculate_average_age():
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    average = total_age / count if count != 0 else 0
    print(f"Average age of users: {average}")

if __name__ == "__main__":
    calculate_average_age()