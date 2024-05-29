from flask import Flask, render_template, url_for, request, redirect

import csv

app = Flask(__name__)

print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
  with open('database.txt', mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    file = database.write(f'\n{'Email:', email},\n{'Subject:', subject},\n {'Message:', message}') 

def write_to_csv(data):
  with open('database.csv', newline='', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])       


##THIS CODE COPY FROM FLASK DOCS ALLOW MESSAGES TO BE SENT.
## Note that we also import request and add line 22 to 27

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Failed to save to database'
        else:
            return 'Something went wrong. Please try again.'       


## We can make this dynamic instead of writting them individually.The above code does that.

# @app.route('/about.html')
# def about_me():
#     return render_template('about.html') 



# @app.route('/works.html')
# def my_works():
#     return render_template('works.html')


# @app.route('/contact.html')
# def contact_me():
#     return render_template('contact.html')


# @app.route('/work.html')
# def all_work():
#     return render_template('work.html')


# @app.route('/components.html')
# def all_components():
#     return render_template('components.html')

# @app.route('/thankyou.html')
# def thank_you():
#     return render_template('thankyou.html')