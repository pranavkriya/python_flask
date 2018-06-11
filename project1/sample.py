#!/usr/bin/python3

# USE oF {{}}??

from  flask import Flask,render_template,request,redirect,url_for

# defining app 
app=Flask(__name__)
app1=Flask(__name__)


page222 = '''<h1> lol </h1>'''
page1 = '''<h1> hiiii </h1>'''


# start route
@app.route('/')
# below function is under the app object and only one function can be defined under one object
def webpage():	
	return page222


@app.route('/lol')
def lol():
	return page1



@app.route('/cal')
def cal():
	x=10
	y=20
	return str(x+y)


@app.route('/list1')
def list1():		
	list1 = ['1','2']
	return list1[0]


@app.route('/quiz',methods=['GET','POST'])
def page():
	if request.method == 'POST':
		return render_template('quiz.html')
	else :
		return render_template('a.html')


# to pass a variable
@app.route('/var<name>')	# <float:hi>  <int:id1>
def var_pass(name):
	return 'Hello!! %s(GUEST)' % name #  %f hi	%d id1



# to pass diff parameters
@app.route('/usr<name>')
def user(name):
	if name == 'admin':
		return 'Hello %s' % name	# here we can also use any othe app.route for defining admin fn
	else :
		return redirect(url_for('var_pass',name = name))






#  running  app (object)
if __name__  ==  "__main__" :
	app.run(debug=True,host='192.168.43.168')
		# if we define 2 diff objects the it will first load the first object then (ctrl + c) to close the connnection and it will load the next object if there is...






