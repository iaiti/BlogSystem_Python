#-*- coding:utf-8 -*-	

# Script Name : createtable.py
# Author : iaiti
# Created : 2015-10-28 18:00:48
# Description : use python to connect mysql and create table and insert data


import mysql.connector as connector
import mysql
import string
cnx = connector.connect(user='root',password='root',host='127.0.0.1',database='test')
pycursor = cnx.cursor()

tables = {}
tables['bloger'] = (
	"create table bloger ("
	"id int(20) not null auto_increment,"
	"name varchar(15) not null,"
	"password varchar(15) not null,"
	"primary key(id)"
	")engine=InnoDB")

tables['blog'] = (
	"create table blog ("
	"id int(20) not null auto_increment,"
	"blogerid int(20) not null,"
	"content text not null,"
	"primary key(id)"
	")engine=InnoDB")

def droptalbeblog():
	droptalbes = "drop table bloger"
	pycursor.execute(droptalbes)



#add table
# try:
# 	for name,content in tables.iteritems():
# 		#the tables sql statements is dict
# 		#print name,content
# 		pycursor.execute(content)
# except mysql.connector.errors.ProgrammingError as err:
# 	print "table exist"



def insertbloger():
	bloger_add = (
	"insert into bloger"
	"(id,name,password) values(%s,%s,%s)"
	)
	bloger_info=(1,"a","admina")
	blog_add = (
		"insert into blog"
		"(id,blogerid,content) values(%s,%s,%s)"
		)
	blog_info=(1,2,"this is a blog")
	pycursor.execute(bloger_add,bloger_info)
	cnx.commit()


# for n in range(11,20):
# 	blog_info = (n,1,"this is another blog"+str(n))
# 	print blog_info
# 	pycursor.execute(blog_add,blog_info)

def getbloger():
	query = "select * from bloger"
	m = None
	pycursor.execute(query)
	m = pycursor.fetchall()
	return m

def passwordisture(name,password):
	query = "select password from bloger where name = '%s'" %name
	pycursor.execute(query)
	m = pycursor.fetchall()
	if m == []:
		return False
	else:
		for n in m:
		 	if n[0] == password:
		 		return True
		
def close():
	pycursor.close()
	cnx.close()

