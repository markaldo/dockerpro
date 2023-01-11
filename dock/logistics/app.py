import psycopg2, datetime
from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.secret_key = 'survival_$tv-shop#deal'

connection = psycopg2.connect(user="postgres",
                                  password="kit",
                                  host="db1",
                                  port="5432",
                                  database="postgres")

cursor = connection.cursor()
boo = cursor.execute(''' SELECT EXISTS (
    SELECT FROM 
        pg_tables
    WHERE 
        schemaname = 'public' AND 
        tablename  = 'supply'
    ); ''')

def table():
    create_table_query = '''CREATE TABLE supply
          (id INT PRIMARY KEY     NOT NULL,
          batch           TEXT    NOT NULL,
          price         REAL,
          date           DATE     NOT NULL); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    insert_query = """ INSERT INTO supply (batch, price, date) VALUES (Swiss75-B, 2500054, 12/09/2022)"""
    cursor.execute(insert_query)
    connection.commit()

if boo == False: 
    table()
    print("successfully created supply table")
 
       
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != '':
            flash("Crosscheck your credintials, account will be blocked after 3 trials")
            error = 'Invalid Credentials. Please try again.'
        else:
            return home()
    return render_template('login.html', error=error)

@app.route('/home', methods=['GET', 'POST'])
def home():
        cursor = connection.cursor()
        cursor.execute("SELECT * from supply")
        return render_template('home.html', data = cursor.fetchall())
    
@app.route('/create', methods=['GET', 'POST'])
def create():
        batch = request.form['batch']
        price = request.form['price']
        time = datetime.datetime.now()

        postgres_insert_query = """ INSERT INTO supply (batch, price, date) VALUES (%s,%s,%s)"""
        record_to_insert = (batch, price, time)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        flash("Record inserted successfully into supply table")
        return redirect('/home') 

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    print(id)
    sql_delete_query = """Delete from supply where id = %s"""
    cursor.execute(sql_delete_query, (id,))
    try:
        connection.commit()
        flash("1 record deleted!")  
        return redirect('/home') 
    except:
        return flash("an error occured in deleting record")  

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    postgreSQL_select_Query = "select * from supply where id = %s"
    cursor.execute(postgreSQL_select_Query, (id,))
    return render_template('edit.html', rec = cursor.fetchone())

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    batch = request.form['batch']
    price = request.form['price']
    sql_update_query = """Update supply set batch = %s, price = %s where id = %s"""
    cursor.execute(sql_update_query, (batch, price, id))
    try:
        connection.commit()
        return redirect('/home')
    except:
        return flash("an error occured in deleting record")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return login()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)