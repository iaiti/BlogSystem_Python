#-*- coding:utf-8 -*-	

# Script Name : server.py
# Author : iaiti
# Created : 2015-10-28 18:00:48
# Description : use flask to build a web app

from flask import Flask
from flask import render_template
from flask import request
import createtable

#Flask is wsgi application 
app = Flask(__name__)

#route decorator tell the what url trigger function,the return will display in user browser
@app.route('/')
def hellflask():
	return "%s" %createtable.getbloger()

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/checklogin',methods=['POST'])
def checklogin():
	return '%s' %createtable.passwordisture(request.form['name'], request.form['password'])

#@app.route('/<int:info>') info must be an integer
# @app.route('/<info>')
# def anyinfo(info):
# 	return '%s'%info

#test get post method
@app.route('/delete',methods=['GET','POST'])
def function():
	if request.method == 'POST':
		return request.form['name']
	else:
		return 'GET'

@app.route('/jinja')
@app.route('/jinja/<name>')
def hellojinja(name=None):
	return render_template('hellojinja.html',name = name)

@app.route('/jinja_data')
def jinjadata(name=None):
	return render_template('hellojinja.html',name = createtable.getbloger())



if __name__ == '__main__':
	app.run(debug=True)