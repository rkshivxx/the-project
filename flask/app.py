from flask import Flask, request,render_template
import mysql.connector
model=pickle.load(open("model.pkl","rb"))

app=Flask(__name__)

cnx=mysql.connector.connect(user='root', password='1234', host='127.0.0.1' , port='3306', database='logins')

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/signup",methods=['POST'])
def signup():
    return render_template("register.html")
@app.route("/reg", methods=['POST'])
def reg():
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    cursor=cnx.cursor()
    cursor.execute("INSERT INTO users (name,email,password)"
                   "values(%s,%s,%s)",(str(name),str(email),str(password)))
    cnx.commit()
    return render_template("index.html")
@app.route("/login",methods=["POST"])
def login():
    n=request.form["name"]
    p=request.form["password"]
    cursor=cnx.cursor()
    cursor.execute('SELECT * FROM users WHERE name=%s and password=%s',(n,p))
    check=cursor.fetchone()
    if check:
     return render_template("mainpage.html")
    else:
        error="Invalid Username or Password"
        return render_template("index.html",error=error)

@app.route("/predict",methods=["post"])
def predict():
    movie=request.form["movie-name"]
    N=request.form["num-movies"]
    try:
     x=model.rec(movie,N)
     print(x)
     return render_template("mainpage.html", x=x)
    except:
     return render_template("mainpage.html",err="looks like we dont have it yet,we ll update it soon")
if __name__=='__main__':

    app.run(host='localhost',port=5000)




