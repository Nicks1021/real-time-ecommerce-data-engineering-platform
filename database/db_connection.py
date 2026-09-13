import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce_realtime",
    user="postgres",
    password="Nikhil@1234",
    port="5432"
)

print("PostgreSQL Connection Successful!")

conn.close()