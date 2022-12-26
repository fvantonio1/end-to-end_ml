from flask import Flask
from routes import urls_blueprint

app = Flask(__name__)
app.register_blueprint(urls_blueprint)

if __name__ == '__main__':
    app.run(debug=True)