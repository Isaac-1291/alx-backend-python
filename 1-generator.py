from seed import connect_to_prodev

def stream_user_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    row = cursor.fetchone()

    while row:
        yield row
        row = cursor.fetchone()

    cursor.close()

if __name__ == "__main__":
    conn = connect_to_prodev()
    if conn:
        print("Streaming users one by one:")
        for row in stream_user_data(conn):
            print(row)
        conn.close()