from dotenv import load_dotenv
from dataclasses import dataclass
from flask import Flask, request
from flask_cors import CORS
import psycopg2
import time
import json
import os

@dataclass
class Trading:
    insider_trading: str
    relationship: str
    date: time
    transaction: str
    cost: float
    shares: str
    value: str
    shares_total: str
    sec_form_4: str

app = Flask(__name__)
CORS(app)

load_dotenv()

DATABASE_PORT = os.getenv('DATABASE_PORT') if 'DATABASE_PORT' in os.environ else os.environ.get('DATABASE_PORT')
DATABASE_HOST = os.getenv('DATABASE_HOST') if 'DATABASE_HOST' in os.environ else os.environ.get('DATABASE_HOST')
connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host=DATABASE_HOST, port=DATABASE_PORT)
TABLE_COLUMNS = {"insider_trading", "relationship", "date", "transaction", "cost", "shares", "value", "shares_total", "sec_form_4"} 

@app.route("/healthcheck", methods=['GET'])
def healthcheck():
    return "OK", 200

# localhost:127.0.0.1/tradings?filter=value
@app.route("/tradings", methods=['GET'])
def get_tradings_filtered():
    print("Received GET request")
    try:
        args = request.args.to_dict()
        cursor = connection.cursor()
        if not args:
            cursor.execute("SELECT * FROM tesla_insider_trading;")
        else:
            filter, value = next(iter(args.items()))

            if filter not in TABLE_COLUMNS:
                return "Could not find a column with such name", 400
            
            cursor.execute(f"SELECT * from tesla_insider_trading WHERE {filter} = '{value}';")
        results = cursor.fetchall()
        return results, 200

    except Exception as e:
        print(f"Error occured: {e}")
        return "Couldn't load the resource", 500


@app.route("/tradings", methods=['POST'])
def post_traidings():
    print("Received POST request")
    try:
        cursor = connection.cursor()
        json_obj = json.loads(request.data)
        data = Trading(**json_obj)
        print(data)
        cursor.execute(f"""INSERT INTO tesla_insider_trading
                            (insider_trading, relationship, date, transaction, cost, shares, value, shares_total, sec_form_4)
                                VALUES
                            ('{data.insider_trading}', '{data.relationship}', '{data.date}', '{data.transaction}', {data.cost}, '{data.shares}', '{data.value}', '{data.shares_total}', '{data.sec_form_4}');""")  # noqa: F541
        connection.commit()
        cursor.close()
        return "Record created", 200
    except Exception as e:
        print(f"Error occured: {e}")
        return "Couldn't load the resource", 500

@app.route("/tradings/<int:id>", methods=['PUT'])
def put_trading(id):
    print("Received PUT request")
    try:
        cursor = connection.cursor()
        json_obj = json.loads(request.data)
        data = Trading(**json_obj)

        cursor.execute(f"""
            UPDATE tesla_insider_trading SET
                insider_trading = '{data.insider_trading}', relationship = '{data.relationship}', date = '{data.date}', transaction = '{data.transaction}',
                cost = {data.cost}, shares = '{data.shares}', value = '{data.value}', shares_total = '{data.shares_total}', sec_form_4 = '{data.sec_form_4}'
            WHERE id = {id};
        """)

        if cursor.rowcount == 0:
            return "Record not found", 404
        connection.commit()
        cursor.close()
        return "Record updated", 200

    except Exception as e:
        print(f"Error occured: {e}")
        return "Couldn't update the resource", 500


app.run(host="0.0.0.0", port=5000)