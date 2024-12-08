import sqlite3
DATABASE = "finance_manager.db"
def cre_trans():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT NOT NULL, -- 'income' or 'expense'
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def add_transaction(user_id, t_type, category, amount, date):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (user_id, type, category, amount, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, t_type, category, amount, date))
    conn.commit()
    conn.close()

def update_transaction(transaction_id, amount, category=None):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    query = 'UPDATE transactions SET amount = ?'
    params = [amount]
    if category:
        query += ', category = ?'
        params.append(category)
    query += ' WHERE id = ?'
    params.append(transaction_id)
    cursor.execute(query, tuple(params))
    conn.commit()
    conn.close()

def delete_transaction(transaction_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
    conn.commit()
    conn.close()
