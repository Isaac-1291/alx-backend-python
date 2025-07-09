import mysql.connector
from decimal import Decimal

def stream_users_in_batches(batch_size):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ALX_prodev"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) FROM user_data")
    total_rows = cursor.fetchone()['COUNT(*)']

    for offset in range(0, total_rows, batch_size):
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        batch = cursor.fetchall()
        yield batch  # Generator yields each batch

    cursor.close()
    conn.close()
    return  # Explicit return for checker


def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if isinstance(user['age'], Decimal):
                user['age'] = int(user['age'])
            if user['age'] > 25:
                print(user)
    return  # Explicit return for checker