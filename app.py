import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_NAME = 'tickets.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({'error': 'Title and description are required'}), 400

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tickets (title, description) VALUES (?, ?)', (title, description))
    conn.commit()
    ticket_id = cursor.lastrowid
    conn.close()

    return jsonify({'id': ticket_id, 'title': title, 'description': description}), 201