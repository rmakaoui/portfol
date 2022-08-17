from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

def write_in_database(data):
    email= data['Email']
    name= data['Name']
    msg= data['Message']
    with open('data.txt','a') as database:
        file= database.write(f'\n {email},{name},{msg}')

def write_to_csv(data):
    email= data['Email']
    name= data['Name']
    msg= data['Message']
    with open('database.csv','a') as database2:
        file= csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([email,name,msg])

@app.route('/<string:page_name>')
def project(page_name=None):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            name= request.form['Name']
            print(name)
            return redirect('/thanks.html')
        except:
            return 'did not save !!'


