from kafka import KafkaConsumer
import json
import psycopg2

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="ecommerce_realtime",
    user="postgres",
    password="Nikhil@1234",
    port="5432"
)

cursor = conn.cursor()

print("PostgreSQL Connected!")

# Kafka connection
consumer = KafkaConsumer(
    "ecommerce_orders",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Kafka Consumer Started...")
print("Waiting for orders...\n")

for message in consumer:

    order = message.value

    cursor.execute("""
        INSERT INTO orders
        (order_id, customer_name, product, quantity, price,
         total_amount, city, order_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (order_id) DO NOTHING
    """, (
        order["order_id"],
        order["customer_name"],
        order["product"],
        order["quantity"],
        order["price"],
        order["total_amount"],
        order["city"],
        order["order_time"]
    ))

    conn.commit()

    print("Order Saved to PostgreSQL:", order["order_id"])