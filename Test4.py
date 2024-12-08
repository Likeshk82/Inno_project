import sqlite3
DATABASE = "finance_manager.db"
def cre_bud():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def set_budget(user_id, category, amount):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO budgets (user_id, category, amount)
        VALUES (?, ?, ?)
    ''', (user_id, category, amount))
    conn.commit()
    conn.close()

def check_budget_exceeded(user_id, category, current_spending):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT amount FROM budgets WHERE user_id = ? AND category = ?', (user_id, category))
    budget = cursor.fetchone()
    conn.close()
    if budget and current_spending > budget[0]:
        print(f"Warning: You have exceeded your budget for {category}!")
