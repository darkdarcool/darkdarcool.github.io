from flask import Flask, render_template, request
app = Flask('app')
import os
@app.route('/')
def hello_world():
	return render_template(
		'index.html',
		user_name=os.environ["REPL_OWNER"]
	)
app.run(host='0.0.0.0', port=8080)
