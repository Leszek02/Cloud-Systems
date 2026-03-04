from flask import Flask
import psycopg2

app = Flask(__name__)
connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port=5433)
app.run()

@app.route("/tradings", methods=['GET'])
def get_tradings():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * from tesla_insider_trading;")
        record = cursor.fetchall()
    except Exception as e:
        print(f"Something went wrong: {e}")
    return record

@app.route("/tradings/:filter", methods=['GET'])
def get_tradings_filtered():
    pass

@app.route("/tradings", methods=['POST'])
def post_traidings():
    pass

@app.route("/tradings", methods=['PUT'])
def put_traidings():
    pass