from flask import Flask, render_template, request, redirect, url_for, session, jsonify

import pyodbc

import re
import json
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

import time
import os



    # Code of your program here

app = Flask(__name__)
database=['test','test1']
cnxn=[]
cursor=[]
i=1
# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'
for x in database:
	server = 'LAPTOP-GVHJQI6G\MSSQLSERVER01' 
	database = x
	print(database)
	username = 'renato' 
	password = 'root' 
	globals()['cnxn%s' % i] = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	globals()['cursor%s' % i] = globals()['cnxn%s' % i].cursor()
	i=i+1
print(cursor1)
cursor=cursor1
cursor1 = cnxn1.cursor()
station20=cursor1.execute("select TOP 1 * from dbo.test")
for x in station20:
	print(x[1])
cursor=cursor2
cursor2 = cnxn2.cursor()
station20=cursor2.execute("select TOP 1 * from dbo.test1")
for x in station20:
	print(x[1])

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/dados/home',methods=['GET', 'POST'])
def home():

	# Check if user is loggedin
	list_ger=[]
	time=datetime.now()
	date=[]
	for x in range(6):
		y = time - timedelta(days = x)
		list_ger.append(y.strftime("%m/%d/%Y"))

	for x in list_ger:
		print(x)	

	print(list_ger)
	if request.method == 'POST' and 'data1' and 'data2' and 'random' in request.form:
		data1 = request.form['data1']
		data2 = request.form['data2']
		random = request.form['random']
		date1=data1.split(' ')
		date2=data2.split(' ')
		
		date1_m=month_string_to_number(date1[1])
		date2_m=month_string_to_number(date2[1])
		print(date1)
		date1=date1[3]+"-"+str(date1_m)+"-"+date1[2]+" 00:00:00"
		date2=date2[3]+"-"+str(date2_m)+"-"+date2[2]+" 23:59:59"
		print(random)
		if random==2:
			#cursor = conn.cursor()
			#station20=cursor.execute("select TOP 5 * from dbo.settings_Audit where Op_dateTime between '"+date1+"' and '"+date2+"' ORDER BY NEWID()")
			
			print(station20)
			print(grafico)
			grafico=1
			return render_template('home.html')
		else:
			#cursor = conn.cursor()
			#station20=cursor.execute("select * from dbo.settings_Audit where Op_dateTime between '"+date1+"' and '"+date2+"'")
			data = ['username', 'Pang', 'site', 'stackoverflow.com']
			number = [1000, 2000, 3000, 4000]
			return jsonify({'tasks': tasks})
	else:
		#cursor = conn.cursor()
		#station20=cursor.execute("select * from dbo.products")
		data = ['username', 'Pang', 'site', 'stackoverflow.com']
		number = [1000, 2000, 3000, 4000]
    	
			# User is loggedin show them the home page
		return render_template('home.html',data=list_ger,number=number)
	# http://localhost:5000/safetyrace/profile - this will be the profile page, only accessible for loggedin users
@app.route('/dados/search',methods=['GET', 'POST'])
def search():
	order = request.args.get('order')
	part = request.args.get('part')
	id_product = request.args.get('id_product')
	print(order)
	print(part)
	print(id_product)
	#cursor = conn.cursor()
	#station20=cursor.execute("select * from dbo.products where order like '%"+order+"%' and part like '%"+part+"%' and order like '%"+id_product+"%'")
	data = ['username', 'Pang', 'site', 'stackoverflow.com']
	number = [1000, 2000, 3000, 4000]
    # User is loggedin show them the home page
	return render_template('home.html',data=data,number=number)
def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')


def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")

