from app import app
from flask import render_template, request
from random import randint
from .cat import Cat

n=randint(1,3)

scared_cat=Cat('scared')
smile_cat=Cat('smile')
tongue_cat=Cat('tongue')

cat_dict={1:scared_cat,2:smile_cat,3:tongue_cat}
@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def index():
    global cat_dict
    global n
    cat = cat_dict[n]
    if request.method == 'GET':
        cat.view()

    if request.method == 'POST':
        if request.form['vote'] == 'yes':
            cat.vote()
        n=randint(1,3)
        cat = cat_dict[n]
        cat.view()
        #return render_template('index.html', title='Home',n=n,cat_dict=cat_dict)




    #elif request.method == 'GET':

    #    return render_template('index.html', title='Home',score_dict=score_dict,name_string=name_string)

    return render_template('index.html', title='Home',n=n,cat_dict=cat_dict)
