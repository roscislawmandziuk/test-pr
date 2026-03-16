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
            status TEXT DEFAULT 'open'
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

@app.route('/tickets', methods=['GET'])
def get_tickets():

    page = int(request.args.get('page', 1))
    size = int(request.args.get('size', 10))
    status = request.args.get('status')
    offset = (page - 1) * size
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if status:
        cursor.execute('SELECT * FROM tickets WHERE status = ? LIMIT ? OFFSET ?', (status, size, offset))
    else:
        cursor.execute('SELECT * FROM tickets LIMIT ? OFFSET ?', (size, offset))
    tickets = cursor.fetchall()
    conn.close()
    results = []
    for ticket in tickets:
        results.append({
            'id': ticket[0],
            'title': ticket[1],
            'description': ticket[2],
            'status': ticket[3]
        })
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)
