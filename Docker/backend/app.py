from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to SQLite DB (creates 'data.db' if it doesn't exist)
conn = sqlite3.connect('data.db', check_same_thread=False)
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

@app.route("/", methods=["GET", "POST"])
def save_name():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")

        if name:
            conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
            conn.commit()
            return f"Hello, {name}! Your name has been saved.", 200
        else:
            return "No name provided", 400
    else:
        return "Server is running. Send a POST request to save a name.", 200

@app.route("/users", methods=["GET"])
def list_users():
    cursor = conn.execute("SELECT id, name FROM users")
    users = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
    return jsonify(users)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
