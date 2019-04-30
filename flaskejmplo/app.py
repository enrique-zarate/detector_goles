from flask import Flask,render_template
app=Flask(__name__)



def sensor():
	return "goool"


@app.route('/')
def index():
	dato=sensor()
	return render_template('index.html',dat=dato)
	


if __name__=='__main__':
	app.run()
