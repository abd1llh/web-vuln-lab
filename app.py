from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# إنشاء قاعدة البيانات
def init_db():
    conn = sqlite3.connect("users.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    """)
    conn.execute("DELETE FROM users")
    conn.execute("INSERT INTO users VALUES (1, 'admin', 'secret123')")
    conn.execute("INSERT INTO users VALUES (2, 'john', 'pass456')")
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Web Vuln Lab</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0f0f0f;
            color: #fff;
            font-family: 'Segoe UI', sans-serif;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        h1 { color: #00ff64; font-size: 32px; margin-bottom: 10px; }
        p { color: #666; margin-bottom: 30px; font-size: 15px; }
        a {
            background: #00ff64;
            color: #000;
            padding: 12px 30px;
            border-radius: 8px;
            font-weight: bold;
            text-decoration: none;
            font-size: 15px;
        }
        a:hover { background: #00cc50; }
        footer { margin-top: 40px; font-size: 12px; color: #444; }
    </style>
</head>
<body>
    <h1>🔐 Web Vulnerability Lab</h1>
    <p>A cybersecurity project demonstrating SQL Injection attack and defense</p>
    <a href="/login">Enter Lab →</a>
    <footer>© 2026 abd1llh — Web Vulnerability Lab</footer>
</body>
</html>
""")

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # الثغرة الحقيقية - SQL Injection
        conn = sqlite3.connect("users.db")
        query = "SELECT * FROM users WHERE username=? AND password=?"
        print(f"Query: {query}")  # نشوف الـ query في terminal
        result = conn.execute(query, (username, password)).fetchone()
        conn.close()

        if result:
            message = f"Welcome {result[1]}!"
        else:
            message = "Invalid credentials"

    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Web Vuln Lab</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0f0f0f;
            color: #fff;
            font-family: 'Segoe UI', sans-serif;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .card {
            background: #1a1a1a;
            border: 1px solid #333;
            border-radius: 12px;
            padding: 40px;
            width: 360px;
            box-shadow: 0 0 30px rgba(0,255,100,0.05);
        }
        h1 {
            font-size: 22px;
            margin-bottom: 8px;
            color: #00ff64;
        }
        p.sub {
            font-size: 13px;
            color: #666;
            margin-bottom: 24px;
        }
        label {
            font-size: 13px;
            color: #aaa;
            display: block;
            margin-bottom: 6px;
        }
        input {
            width: 100%;
            padding: 10px 14px;
            background: #111;
            border: 1px solid #333;
            border-radius: 8px;
            color: #fff;
            font-size: 14px;
            margin-bottom: 16px;
            outline: none;
        }
        input:focus { border-color: #00ff64; }
        button {
            width: 100%;
            padding: 11px;
            background: #00ff64;
            color: #000;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 15px;
        }
        button:hover { background: #00cc50; }
        .message {
            margin-top: 16px;
            font-size: 14px;
            color: {% if 'Welcome' in message %}#00ff64{% else %}#ff4444{% endif %};
            text-align: center;
        }
        footer {
            margin-top: 40px;
            font-size: 12px;
            color: #444;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🔐 Login</h1>
        <p class="sub">Web Vulnerability Lab</p>
        <form method="POST">
            <label>Username</label>
            <input name="username" placeholder="Enter username">
            <label>Password</label>
            <input name="password" type="password" placeholder="Enter password">
            <button type="submit">Login</button>
        </form>
        {% if message %}
        <p class="message">{{ message }}</p>
        {% endif %}
    </div>
    <footer>© 2026 abd1llh — Web Vulnerability Lab</footer>
</body>
</html>
""", message=message)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)