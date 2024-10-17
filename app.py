from flask import Flask, request, render_template,jsonify
import psycopg2
from psycopg2 import sql

app=Flask(__name__,template_folder='template')
DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',  
    'password': 'kumar@10S',  
    'host': 'localhost',
    'port': 5432
}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    use = request.form['use']
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute(sql.SQL("SELECT * FROM users WHERE use = %s"), [use])
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()
    users = [{'use': user[0], 'password': user[1]} for user in results]
    
    return jsonify(users)

    
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
