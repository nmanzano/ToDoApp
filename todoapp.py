from flask import Flask, render_template
from flask import request, redirect, url_for

app = Flask(__name__)
to_do_list = [];

@app.route('/')
def home():
    return render_template('index.html', to_do_list=to_do_list)

# @app.route('/clear')
@app.route('/submit', methods=['POST'])
def submit():
    individual_task = []
    if request.method == "POST":
        individual_task.append(request.form['task'])
        individual_task.append(request.form['email'])
        individual_task.append(request.form['priority'])
        to_do_list.append(individual_task) 
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
