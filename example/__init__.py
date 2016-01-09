from flask import Flask
from flask.ext.config import Config

app = Flask(__name__)
config = Config(app)

# or make instance and call Config.init_app(app)
# config = Config()
# config.init_app(app)

app.config.from_yaml('development')


@app.route('/')
def index():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run()