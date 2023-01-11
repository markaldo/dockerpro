import json, requests, random, psycopg2, string, datetime
from flask import Flask, jsonify

app = Flask(__name__)

connection = psycopg2.connect(user="postgres",
                                  password="kit",
                                  host="db1",
                                  port="5432",
                                  database="postgres")
cursor = connection.cursor() 

@app.route('/')
def prices():
    data = requests.get('http://kit').json()
    
    count = 0
    time = datetime.datetime.now()
    
    S = 8    
    ran = ''.join(random.choices(string.ascii_letters + string.digits, k = S)) 
    
    for i in range(len(data)):
        value = random.randint(170,429)
        data[i]['price'] = value
        count += value
        
    postgres_insert_query = """ INSERT INTO supply (batch, price, date) VALUES (%s,%s,%s)"""
    record_to_insert = (str(ran), count, time)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()   
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)