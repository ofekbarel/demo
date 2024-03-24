from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def sql_table():
    return render_template('sq-data.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")

#rember the db is a container thtat runing on vm machine, so if the vm or the container are down,
#the app will not working.