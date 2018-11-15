from flask import Flask, render_template
from flask import request, redirect, url_for

app = Flask(__name__)
to_do_list = []
error = {
        'priority':'none',
        'email': 'none'
        }

@app.route('/')
def home():
    print(error, '10')
    return render_template('index.html', to_do_list=to_do_list, error=error)


@app.route('/submit', methods=['POST'])
def submit():
    individual_task = []
    if request.method == "POST":
        error['priority'] = 'none'
        error['email'] = 'none'
        if request.form['priority'] == 'select priority':
            error['priority'] = 'show'
        if '@' not in request.form['email']:
            error['email'] = 'show'
        else:
            individual_task.append(request.form['task'])
            individual_task.append(request.form['email'])
            individual_task.append(request.form['priority'])
            to_do_list.append(individual_task)
            item_index = to_do_list.index(individual_task)
            to_do_list[item_index].append(item_index)
    return redirect('/')


@app.route('/clear_single', methods=['POST'])
def clear_single():
    if request.method == "POST":
        response = request.form['list_item']
        number_index = int(response[-2])
        for item_index in to_do_list:
            if item_index[3] == number_index:
                remove_item = to_do_list.index(item_index)
                to_do_list.pop(remove_item)

    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    count = 0
    if request.method == "POST":
        while len(to_do_list) > count:
            to_do_list.remove(to_do_list[count])

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
