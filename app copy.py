from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def test():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM inventory').fetchall()
    conn.close()
    return render_template('test.html', items=items)

@app.route('/add-item', methods=['POST'])
def add_item():
    # Get data from the form
    diet_coke = request.form['diet_coke_quantity']
    coke = request.form['coke_quantity']
    lacroix = request.form['lacroix_quantity']

    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Save the data to the database
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO inventory (date, diet_coke, coke, lacroix)
        VALUES (?, ?, ?, ?)
    ''', (current_date, diet_coke, coke, lacroix))
    conn.commit()
    conn.close()

    # Redirect to the home page to display the updated inventory
    return redirect(url_for('test'))

@app.route('/delete-item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM inventory WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()

    # Redirect to the home page to display the updated inventory
    return redirect(url_for('test'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
