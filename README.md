# 🚀 Real-Time E-Commerce Data Engineering Platform A real-time data engineering project that collects e-commerce order data, streams it through **Apache Kafka**, stores it in **PostgreSQL**, exposes analytics through a **Flask REST API**, and displays the results on a modern real-time dashboard. The project demonstrates an end-to-end data pipeline similar to what is used in real-world data engineering systems. --- ## 📌 Project Overview The platform continuously generates simulated e-commerce orders and processes them in real time. ### Data Flow
text
Python Data Generator
        ↓
   Apache Kafka
        ↓
   Kafka Consumer
        ↓
    PostgreSQL
        ↓
    Flask REST API
        ↓
 Real-Time Dashboard
The system automatically generates new orders every few seconds and updates the dashboard with the latest analytics. --- ## 🎯 Project Objectives * Generate real-time e-commerce order data * Stream data using Apache Kafka * Consume Kafka messages using Python * Store processed orders in PostgreSQL * Perform real-time sales analytics * Build REST APIs using Flask * Create an attractive dashboard * Implement login authentication * Display real-time business KPIs * Create a one-click project startup system --- ## 🛠️ Technologies Used | Technology | Purpose | | ------------ | ---------------------------------- | | Python | Data generation and processing | | Apache Kafka | Real-time data streaming | | Kafka-Python | Kafka producer and consumer | | PostgreSQL | Data storage | | Psycopg2 | PostgreSQL connectivity | | Flask | REST API and web server | | HTML | Dashboard structure | | CSS | Dashboard and login UI | | JavaScript | Dynamic dashboard | | Chart.js | Data visualization | | PySpark | Planned streaming processing layer | | Git & GitHub | Version control | --- ## 🏗️ Project Architecture
text
                    ┌─────────────────────┐
                    │  Python Data        │
                    │  Generator          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Apache Kafka      │
                    │ ecommerce_orders    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Kafka Consumer    │
                    │      Python         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    PostgreSQL       │
                    │ ecommerce_realtime  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Flask API       │
                    │   REST Endpoints    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Web Dashboard      │
                    │ HTML/CSS/JS/Chart.js│
                    └─────────────────────┘
--- ## 📂 Project Structure
text
RealTime-Data-Engineering-Platform 2/
│
├── api/
│   └── app.py
│
├── database/
│   ├── analytics.py
│   ├── analytics.sql
│   └── db_connection.py
│
├── dashboard/
│   └── index.html
│
├── kafka/
│   └── consumer.py
│
├── producer/
│   └── producer.py
│
├── spark/
│   └── streaming.py
│
├── venv/
│
├── start_project.bat
│
└── README.md
--- # ⚙️ Features ## 1. Real-Time Data Generation The Python producer automatically generates e-commerce orders. Each order contains:
text
Order ID
Customer Name
Product
Quantity
Price
Total Amount
City
Order Time
Example:
json
{
    "order_id": 12345,
    "customer_name": "Customer_101",
    "product": "Laptop",
    "quantity": 2,
    "price": 65000,
    "total_amount": 130000,
    "city": "Mumbai"
}
--- ## 2. Apache Kafka Streaming Kafka receives the generated orders through the topic:
text
ecommerce_orders
Kafka provides the real-time messaging layer between the data producer and consumer. --- ## 3. Kafka Consumer The Python consumer reads messages from Kafka and stores them in PostgreSQL. The consumer also prevents duplicate order insertion using:
sql
ON CONFLICT (order_id) DO NOTHING
--- ## 4. PostgreSQL Database Database:
text
ecommerce_realtime
Main table:
sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    product VARCHAR(100),
    quantity INT,
    price NUMERIC(10,2),
    total_amount NUMERIC(12,2),
    city VARCHAR(100),
    order_time TIMESTAMP
);
--- # 📊 Analytics The project calculates important business metrics. ### Total Orders
sql
SELECT COUNT(*)
FROM orders;
### Total Revenue
sql
SELECT SUM(total_amount)
FROM orders;
### Average Order Value
sql
SELECT AVG(total_amount)
FROM orders;
### Product Sales
sql
SELECT
    product,
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_sales
FROM orders
GROUP BY product
ORDER BY total_sales DESC;
--- # 📈 Dashboard The dashboard displays: * 🛒 Total Orders * 💰 Total Revenue * 📦 Average Order Value * 📊 Product Sales * 🛍️ Orders by Product * 📋 Product Analytics * 🔴/🟢 Live System Status The dashboard automatically refreshes every **5 seconds**. --- # 🔐 Authentication The platform includes a login page before accessing the dashboard. ### Login
text
Username: admin
Password: admin123
After successful authentication:
text
Login
  ↓
Dashboard
Unauthenticated users are redirected to the login page. --- # 🌐 Flask API Main endpoint:
text
GET /api/analytics
The API returns:
json
{
    "total_orders": 100,
    "total_sales": 500000,
    "average_order_value": 5000,
    "products": []
}
Dashboard flow:
text
PostgreSQL
     ↓
Flask API
     ↓
JavaScript Fetch
     ↓
Chart.js
     ↓
Dashboard
--- # ▶️ How to Run ## Prerequisites Install: * Python 3 * Java 17 * Apache Kafka * PostgreSQL * pgAdmin * VS Code --- ## Step 1 — Open Project Open the project folder in VS Code:
text
RealTime-Data-Engineering-Platform 2
--- ## Step 2 — Activate Virtual Environment
powershell
venv\Scripts\activate
--- ## Step 3 — Start Kafka Go to your Kafka installation directory and start the Kafka server.
powershell
cd "C:\kafka\kafka_2.13-4.3.1"

.\bin\windows\kafka-server-start.bat .\config\server.properties
Keep the Kafka terminal running. --- ## Step 4 — Start Consumer
powershell
venv\Scripts\python.exe kafka\consumer.py
--- ## Step 5 — Start Producer
powershell
venv\Scripts\python.exe producer\producer.py
You should see:
text
Sent: {...}
--- ## Step 6 — Start Flask API
powershell
venv\Scripts\python.exe api\app.py
Flask runs on:
text
http://127.0.0.1:5000
--- ## Step 7 — Open Dashboard Open:
text
http://127.0.0.1:5000/login
Login using your credentials. --- # ⚡ One-Click Startup The project contains:
text
start_project.bat
This file can automatically start:
text
Kafka
 ↓
Consumer
 ↓
Producer
 ↓
Flask API
 ↓
Browser
Therefore, instead of manually starting every service, the project can be launched using the batch file. --- # 🔄 Real-Time Processing Flow
text
1. Python generates an order
              ↓
2. Order is sent to Kafka
              ↓
3. Kafka Consumer receives order
              ↓
4. Order is inserted into PostgreSQL
              ↓
5. Flask API reads analytics
              ↓
6. Dashboard requests API data
              ↓
7. Charts and KPIs are updated
--- # 💼 Real-World Use Case This architecture can be adapted for: * E-commerce platforms * Banking transactions * Stock market monitoring * IoT systems * Logistics tracking * Online payment systems * Customer activity monitoring * Fraud detection * Real-time business intelligence --- # 🧪 Example Business Questions The platform can answer: ### Which product generates the most revenue? Product-wise sales analytics can identify the highest-performing product. ### How many orders have been received? The dashboard displays the total number of orders. ### What is the average order value? The system calculates the average revenue generated per order. ### Which city generates the highest sales? City-level analytics can be used to identify high-performing locations. --- # 🚀 Future Improvements The project can be extended with: * PySpark Structured Streaming integration * Apache Spark data transformation * Power BI dashboard * Azure Data Factory * Azure Databricks * Snowflake * Redis caching * Docker deployment * AWS deployment * User registration * Password hashing * Role-based authentication * Email notifications * Advanced data-quality checks * Real-time alerts * Machine-learning based fraud detection --- # 🔒 Security Improvements For a production environment: * Never store passwords directly in source code * Use password hashing * Store secrets in environment variables * Use HTTPS * Implement CSRF protection * Use secure session cookies * Add role-based access control * Use a production WSGI server --- # 📌 Project Status
text
✅ Python Data Generator
✅ Apache Kafka
✅ Kafka Consumer
✅ PostgreSQL
✅ SQL Analytics
✅ Flask REST API
✅ Real-Time Dashboard
✅ Login Authentication
✅ One-Click Startup
🔄 PySpark Streaming
🔄 Power BI
🔄 Cloud Deployment
--- # 👨‍💻 Author **Nikhil Shinde** B.Tech Computer Science Engineering Dr. Babasaheb Ambedkar Technological University ### Career Interest Data Engineering | Python | SQL | PySpark | ETL | Cloud --- # ⭐ Conclusion The **Real-Time E-Commerce Data Engineering Platform** demonstrates a complete data pipeline from data generation to visualization. It combines streaming, database management, backend API development, authentication, analytics, and visualization into one practical project. This project provides hands-on experience with technologies commonly used in modern data engineering architectures.