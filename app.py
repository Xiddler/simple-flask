
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
	return ('<h2>This is the fabulous flask app. It is Thursday and it is working </h2>')


if __name__ == '__main__':
	app.run(debug=True)


