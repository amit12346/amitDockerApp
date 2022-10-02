import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)


try:
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="change-me",
      database="db_name"
    )
except Exception as er:
    print(er)

@app.route("/")
def home():
    print("hello")
    return render_template("mainpage.html")
    # Creating a cursor object using the cursor() method

    # # Dropping EMPLOYEE table if already exists.
    # #cursor.execute("DROP TABLE IF EXISTS Votes")
    # conn = mysql.connector.Connect(
    #     user='root', password='change-me', host='127.0.0.1', database='db_name'
    # )
    # try:
    #
    #     cursor = conn.cursor()
    #     # Creating table as per requirement
    #     sql = '''CREATE TABLE Votes(
    #        Dogs int(1)  NULL,
    #        Cats int(1)  NULL,
    #        Donkyes int(1)  NULL
    #     )'''
    #     cursor.execute(sql)
    # except Exception as er:
    #     print(er)
    #     conn.close()
    #     return render_template("mainpage.html")
    # # Closing the connection



#background process happening without any refreshing
@app.route('/updateleftbox')
def updateleftbox():
    mycursor = mydb.cursor()

    sql = "INSERT INTO Votes (Dogs) VALUES (1);"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

    mycursor = mydb.cursor()

    mycursor.execute("SELECT SUM(Dogs) FROM db_name.Votes")

    myresult = mycursor.fetchall()
    print((myresult[0][0]))
    res = str(myresult[0][0])



    return(res)

# if __name__ == "__main__":
#     app.run(debug=True)
#
if __name__ == '__main__':
    app.run( port=8000, debug=True)