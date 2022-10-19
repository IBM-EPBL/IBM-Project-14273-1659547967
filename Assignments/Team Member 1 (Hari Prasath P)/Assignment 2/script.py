
from flask import *
import sqlite3 as sql
app = Flask(__name__)  



@app.route('/')  
def home():  
      return render_template('home.html')  

@app.route('/sign_up')  
def signUp():  
      return render_template('sign_up.html')

@app.route('/sign_in')  
def signIn():  
      return render_template('sign_in.html')

@app.route('/about')  
def about():  
    email = request.cookies.get('email')  
    name = request.cookies.get('name') 
    dob = request.cookies.get('dob') 
    if email != None:
      resp = make_response(render_template('about.html',loggedin = True,name = name, email = email, dob = dob))
    else:
      resp = make_response(render_template('about.html',loggedin = False))
    
    return resp 

@app.route('/logout')  
def logout():  
      
      email = request.cookies.get('email')
      if email != None:
            resp = make_response(render_template('logout.html',loggedin = True))
            resp.set_cookie('name', '', expires=0)
            resp.set_cookie('email', '', expires=0)
            resp.set_cookie('dob', '', expires=0)
            
      else:
            resp = make_response(render_template('logout.html',loggedin = False))

      return resp

@app.route('/add_user',methods = ['POST', 'GET'])
def add_user():
   if request.method == 'POST':
      try:
         name = request.form['name']
         email = request.form['email']
         password = request.form['password']
         dob = request.form['dob']

         
         with sql.connect("/home/hari/database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO users (name,email,password,dob) VALUES (?,?,?,?)",(name, email, password, dob) )
            
            con.commit()
            msg = "You are successfully Signed Up"
      except Exception as e :
         con.rollback()
         msg = repr(e)
      
      finally:
         con.close()
         return render_template("post_signup.html",msg = msg)
         

@app.route('/validate_user',methods = ['POST', 'GET'])
def validate_user():
   if request.method == 'GET':
      try:
            args = request.args
            email = args.get('email')
            password = args.get('password')
            print(email)
         
            con = sql.connect("/home/hari/database.db")
            con.row_factory = sql.Row
   
            cur = con.cursor()
            cur.execute("select * from users where email="+"'"+email+"'")
   
            row = cur.fetchone()
 
            if row != None:
                  if  len(row) ==4:
                        if(row["password"]== password):
                               resp = make_response(render_template("post_signin.html"))  
                               resp.set_cookie('email', row["email"]) 
                               resp.set_cookie('name',row["name"])  
                               resp.set_cookie('dob',row["dob"])  
                               return resp 
                               
                        else:
                              return "Incorrect Password"
            else:
                  return "User does not exists"
            con.close()

      except Exception as e :
         con.rollback()
         return repr(e)
      
    


if __name__ == '__main__':  
   app.run(debug = True)  
