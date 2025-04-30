import os
import psycopg2
import csv

def get_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("PGHOST", "localhost"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            dbname=os.getenv("PGDATABASE")
        )
        return conn
    except Exception as e:
        print("Connection failed:", e)
        return None

def list_tables(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
        tables = cur.fetchall()
        print("Tables:")
        for table in tables:
            print("-", table[0])

def show_schema(conn, table):
    with conn.cursor() as cur:
        cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = %s;", (table,))
        columns = cur.fetchall()
        print(f"Schema of {table}:")
        for col in columns:
            print(f"- {col[0]} ({col[1]})")

def export_to_csv(conn, table):
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM {table};")
        rows = cur.fetchall()
        headers = [desc[0] for desc in cur.description]
        with open(f"{table}.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Data exported to {table}.csv")

def main():
    conn = get_connection()
    if not conn:
        return
    while True:
        print("\nOptions:")
        print("1. List tables")
        print("2. Show table schema")
        print("3. Export table to CSV")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            list_tables(conn)
        elif choice == "2":
            table = input("Enter table name: ")
            show_schema(conn, table)
        elif choice == "3":
            table = input("Enter table name: ")
            export_to_csv(conn, table)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
