import sqlite3
DATABASE = "finance_manager.db"
def generate_monthly_report(user_id, year, month):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT type, SUM(amount)
        FROM transactions
        WHERE user_id = ? AND strftime('%Y', date) = ? AND strftime('%m', date) = ?
        GROUP BY type
    ''', (user_id, str(year), f'{month:02}'))
    report = cursor.fetchall()
    conn.close()
    return {row[0]: row[1] for row in report}

def generate_yearly_report(user_id, year):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT type, SUM(amount)
        FROM transactions
        WHERE user_id = ? AND strftime('%Y', date) = ?
        GROUP BY type
    ''', (user_id, str(year)))
    report = cursor.fetchall()
    conn.close()
    return {row[0]: row[1] for row in report}
