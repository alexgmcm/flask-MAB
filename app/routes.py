from app import app
from flask import render_template, request
from random import randint
n=randint(1,3)
score_dict={'a':0,'b':0,'c':0}
name_dict={1:'a',2:'b',3:'c'}
@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def index():
    global score_dict
    global n
    name_string = name_dict[n]

    if request.method == 'POST':
        if request.form['vote'] == 'yes':
            score_dict[name_string] = score_dict[name_string] + 1


        else:
            pass
        n=randint(1,3)
        name_string = name_dict[n]
        return render_template('index.html', title='Home',score_dict=score_dict,name_string=name_string)




    #elif request.method == 'GET':

    #    return render_template('index.html', title='Home',score_dict=score_dict,name_string=name_string)

    return render_template('index.html', title='Home',score_dict=score_dict,name_string=name_string)
