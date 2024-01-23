from flask import json
from flask import request
from flask import Flask
import subprocess
import os
import sys

app = Flask(__name__)

@app.route('/')
def api_root():
	return 'Welcome'

@app.route('/github', methods=['POST'])
def api_gh():
	if request.headers['Content-Type'] == 'application/json':
		subprocess.run(["/home/frank/GroovyServer/update_bot.sh"])
		return json.dumps(request.json)

if __name__ == '__main__':
	# restart bot in case its not running
	subprocess.run(["/home/frank/GroovyServer/update_bot.sh"])

	app.run(debug=True)
