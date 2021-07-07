from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hola mundo desde Flask! ¿Corto y directo al punto no?"

if __name__ == "__main__":
	app.run()