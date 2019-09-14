from app import app
from flask import render_template, request
from random import randint
from .cat import Cat
from .bayes import plot_distributions
import os, sys


def getCatIndex(cat_dict):
    draws=[(tup[0],tup[1].drawBeta()) for tup in cat_dict.items()]
    draws.sort(key=lambda tup: tup[1], reverse=True)
    print(draws, file=sys.stderr)
    n=draws[0][0]
    print(n, file=sys.stderr)
    return n


n=randint(1,3)

scared_cat=Cat('scared')
smile_cat=Cat('smile')
tongue_cat=Cat('tongue')

cat_dict={1:scared_cat,2:smile_cat,3:tongue_cat}

n = getCatIndex(cat_dict)


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
        elif request.form['vote'] == 'no':
            cat.fail()
        #n=randint(1,3)
        n = getCatIndex(cat_dict)
        cat = cat_dict[n]
        cat.view()
        #return render_template('index.html', title='Home',n=n,cat_dict=cat_dict)

    plot_distributions(cat_dict)


    #elif request.method == 'GET':

    #    return render_template('index.html', title='Home',score_dict=score_dict,name_string=name_string)

    return render_template('index.html', title='Home',n=n,cat_dict=cat_dict,rand=randint(0,100000000))
