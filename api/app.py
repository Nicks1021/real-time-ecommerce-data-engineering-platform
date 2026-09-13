from flask import Flask, jsonify, send_from_directory, request, session, redirect
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

# Secret key
app.secret_key = os.getenv(
    "SECRET_KEY",
    "real-time-dashboard-secret-key"
)


# =========================
# PostgreSQL Connection
# =========================

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="ecommerce_realtime",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD"),
        port="5432"
    )


# =========================
# HOME
# =========================

@app.route("/")
def home():
    return redirect("/login")


# =========================
# LOGIN PAGE
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    if session.get("logged_in"):
        return redirect("/dashboard")

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Demo login
        if username == "admin" and password == "admin123":

            session["logged_in"] = True

            return redirect("/dashboard")

        else:

            return """
            <script>
                alert("❌ Invalid Username or Password!");
                window.location.href = "/login";
            </script>
            """

    return """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Login | Real-Time Data Platform</title>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

body {

    min-height: 100vh;

    display: flex;

    justify-content: center;

    align-items: center;

    overflow: hidden;

    background:
        linear-gradient(
            135deg,
            #0f172a,
            #1e3a8a,
            #2563eb,
            #0f172a
        );

    background-size: 400% 400%;

    animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

.circle {

    position: absolute;

    border-radius: 50%;

    background: rgba(255,255,255,0.08);

    backdrop-filter: blur(5px);

    animation: float 8s infinite ease-in-out;
}

.circle.one {

    width: 220px;
    height: 220px;

    top: -60px;
    left: -60px;
}

.circle.two {

    width: 300px;
    height: 300px;

    bottom: -100px;
    right: -80px;

    animation-delay: 2s;
}

.circle.three {

    width: 120px;
    height: 120px;

    top: 20%;
    right: 15%;

    animation-delay: 4s;
}

@keyframes float {

    0%, 100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-30px);
    }
}

.login-container {

    width: 400px;

    padding: 45px 40px;

    background: rgba(255,255,255,0.12);

    border: 1px solid rgba(255,255,255,0.25);

    border-radius: 25px;

    backdrop-filter: blur(20px);

    box-shadow:
        0 25px 60px rgba(0,0,0,0.35);

    color: white;

    position: relative;

    z-index: 5;

    animation: cardAppear 1s ease;
}

@keyframes cardAppear {

    from {

        opacity: 0;

        transform:
            translateY(40px)
            scale(0.95);
    }

    to {

        opacity: 1;

        transform:
            translateY(0)
            scale(1);
    }
}

.logo {

    width: 75px;

    height: 75px;

    margin: auto;

    display: flex;

    justify-content: center;

    align-items: center;

    border-radius: 20px;

    background: rgba(255,255,255,0.18);

    font-size: 35px;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.2);

    animation:
        logoFloat 3s ease-in-out infinite;
}

@keyframes logoFloat {

    0%, 100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-8px);
    }
}

h1 {

    text-align: center;

    margin-top: 20px;

    font-size: 28px;
}

.subtitle {

    text-align: center;

    margin-top: 8px;

    color: rgba(255,255,255,0.75);

    font-size: 14px;
}

.input-group {

    margin-top: 25px;

    position: relative;
}

.input-group span.icon {

    position: absolute;

    left: 15px;

    top: 14px;

    font-size: 18px;
}

input {

    width: 100%;

    padding: 14px 45px;

    border:
        1px solid rgba(255,255,255,0.25);

    border-radius: 12px;

    background:
        rgba(255,255,255,0.10);

    color: white;

    outline: none;

    font-size: 15px;

    transition: 0.3s;
}

input::placeholder {

    color:
        rgba(255,255,255,0.65);
}

input:focus {

    border-color: white;

    background:
        rgba(255,255,255,0.18);

    transform: scale(1.02);

    box-shadow:
        0 0 20px rgba(255,255,255,0.15);
}

.password-toggle {

    position: absolute;

    right: 15px;

    top: 14px;

    cursor: pointer;

    font-size: 17px;
}

button {

    width: 100%;

    margin-top: 28px;

    padding: 14px;

    border: none;

    border-radius: 12px;

    background: white;

    color: #1e3a8a;

    font-size: 16px;

    font-weight: bold;

    cursor: pointer;

    transition: 0.3s;
}

button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 12px 25px rgba(0,0,0,0.25);
}

button:active {

    transform: scale(0.97);
}

.security {

    text-align: center;

    margin-top: 22px;

    font-size: 12px;

    color:
        rgba(255,255,255,0.65);
}

.footer {

    text-align: center;

    margin-top: 25px;

    font-size: 12px;

    color:
        rgba(255,255,255,0.55);
}

@media (max-width: 500px) {

    .login-container {

        width: 90%;

        padding: 35px 25px;
    }
}

</style>

</head>

<body>

<div class="circle one"></div>

<div class="circle two"></div>

<div class="circle three"></div>

<div class="login-container">

    <div class="logo">
        📊
    </div>

    <h1>
        Welcome Back
    </h1>

    <p class="subtitle">
        Real-Time E-Commerce Data Platform
    </p>

    <form method="POST">

        <div class="input-group">

            <span class="icon">
                👤
            </span>

            <input
                type="text"
                name="username"
                placeholder="Username"
                required
            >

        </div>

        <div class="input-group">

            <span class="icon">
                🔒
            </span>

            <input
                id="password"
                type="password"
                name="password"
                placeholder="Password"
                required
            >

            <span
                class="password-toggle"
                onclick="togglePassword()"
            >
                👁️
            </span>

        </div>

        <button type="submit">
            Login to Dashboard →
        </button>

    </form>

    <div class="security">
        🔐 Secure Authentication
    </div>

    <div class="footer">
        Real-Time Data Engineering Platform
    </div>

</div>

<script>

function togglePassword() {

    const password =
        document.getElementById("password");

    if (password.type === "password") {

        password.type = "text";

    } else {

        password.type = "password";

    }

}

</script>

</body>

</html>
"""


# =========================
# ANALYTICS API
# =========================

@app.route("/api/analytics")
def analytics():

    if not session.get("logged_in"):

        return jsonify({
            "error": "Unauthorized"
        }), 401

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) AS total_orders,
            COALESCE(SUM(total_amount), 0) AS total_sales,
            COALESCE(AVG(total_amount), 0) AS average_order_value
        FROM orders;
    """)

    summary = cursor.fetchone()

    cursor.execute("""
        SELECT
            product,
            COUNT(*) AS total_orders,
            COALESCE(SUM(total_amount), 0) AS total_sales
        FROM orders
        GROUP BY product
        ORDER BY total_sales DESC;
    """)

    products = cursor.fetchall()

    cursor.close()

    conn.close()

    return jsonify({

        "total_orders":
            summary[0],

        "total_sales":
            float(summary[1]),

        "average_order_value":
            float(summary[2]),

        "products": [

            {

                "product":
                    row[0],

                "orders":
                    row[1],

                "sales":
                    float(row[2])

            }

            for row in products

        ]

    })


# =========================
# DASHBOARD
# =========================

@app.route("/dashboard")
def dashboard():

    if not session.get("logged_in"):

        return redirect("/login")

    return send_from_directory(
        "../dashboard",
        "index.html"
    )


# =========================
# LOGOUT
# =========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# =========================
# START FLASK
# =========================

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )