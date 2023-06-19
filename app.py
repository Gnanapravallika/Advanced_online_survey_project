from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'adminp'
app.config['MYSQL_DB'] = 'survey_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        # Get form data
        question1 = request.form['question1']
        question2 = request.form['question2']
        question3 = request.form['question3']

        # Save survey data to the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO surveys (question1, question2, question3) VALUES (%s, %s, %s)",
                    (question1, question2, question3))
        mysql.connection.commit()
        cur.close()

        return render_template('results.html')
    return render_template('survey.html')


if __name__ == '__main__':
    app.run(debug=True)

