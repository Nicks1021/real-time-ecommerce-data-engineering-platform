import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce_realtime",
    user="postgres",
    password="Nikhil@1234",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
    SELECT
        product,
        COUNT(*) AS total_orders,
        SUM(total_amount) AS total_sales
    FROM orders
    GROUP BY product
    ORDER BY total_sales DESC;
""")

results = cursor.fetchall()

print("\n===== PRODUCT SALES ANALYTICS =====")

for row in results:
    print(
        "Product:", row[0],
        "| Orders:", row[1],
        "| Sales:", row[2]
    )

cursor.close()
conn.close()