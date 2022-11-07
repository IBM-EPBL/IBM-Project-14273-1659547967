
from flask import *

app = Flask(__name__)  



@app.route('/')  
def home():  
      return render_template('index.html')  

@app.route('/contact')  
def contact():  
      return render_template('contact.html')

@app.route('/category')  
def category():  
      return render_template('category.html')

@app.route('/about')  
def about():
    return render_template('about.html')  

@app.route('/job-detail')  
def job_detail():
    return render_template('job-detail.html')  

@app.route('/job-list')  
def job_list():
    return render_template('job-list.html')  

@app.route('/testimonial')  
def testimonial():
    return render_template('testimonial.html')  

if __name__ == '__main__':  
   app.run(debug = True)  
