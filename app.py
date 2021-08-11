from flask import Flask, render_template, redirect, request

import emoji_finder

# __name__ == __main__
app = Flask(__name__, template_folder='template', static_url_path = '/static', static_folder = 'static')


@app.route('/')
def hello():
	return render_template("index.html")


@app.route('/', methods= ['POST'])
def marks():
	if request.method == 'POST':

		str = request.form['emojfile']
		emoji_get = emoji_finder.predict_this(str)
		emoji_dic = {
		'emoji' : emoji_get,
		'text' : str
		}

	return render_template("index.html", your_result = emoji_dic)

if __name__ == '__main__':
	app.run(debug = True)