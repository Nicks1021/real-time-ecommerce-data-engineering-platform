import random
import time
import json
from datetime import datetime
from kafka import KafkaProducer

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse"]

cities = ["Mumbai", "Pune", "Nashik", "Nagpur", "Solapur"]

while True:

    quantity = random.randint(1, 5)
    price = random.randint(500, 80000)

    order = {
        "order_id": random.randint(10000, 99999),
        "customer_name": "Customer_" + str(random.randint(1, 1000)),
        "product": random.choice(products),
        "quantity": quantity,
        "price": price,
        "total_amount": quantity * price,
        "city": random.choice(cities),
        "order_time": datetime.now().isoformat()
    }

    # Send order to Kafka
    producer.send("ecommerce_orders", order)
    producer.flush()

    print("Sent:", order)

    time.sleep(3)