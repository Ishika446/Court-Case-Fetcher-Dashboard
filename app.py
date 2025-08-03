from flask import Flask, render_template, request, jsonify
import requests
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    case_type TEXT,
                    case_number TEXT,
                    case_year TEXT,
                    status TEXT,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        case_year = request.form['case_year']

        payload = {
            "state_cd": "07",      
            "dist_cd": "3",        
            "court_cd": "1",       
            "case_type": case_type,
            "case_no": case_number,
            "case_year": case_year
        }

        try:
            res = requests.post("https://services.ecourts.gov.in/ecourtindia_v6/cases/case_no.php", data=payload)
            if res.status_code == 200 and res.text:
                result = res.json()
                status = "Success"
            else:
                result = {"error": "No data or error fetching."}
                status = "Failed"
        except Exception as e:
            result = {"error": str(e)}
            status = "Error"

        conn = sqlite3.connect('queries.db')
        c = conn.cursor()
        c.execute('INSERT INTO logs (case_type, case_number, case_year, status, timestamp) VALUES (?, ?, ?, ?, ?)', 
                  (case_type, case_number, case_year, status, datetime.now()))
        conn.commit()
        conn.close()

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
