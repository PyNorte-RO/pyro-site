from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    a=23
    return 'Hello World!'


if __name__ == '__main__':
    app.config.update(
        TESTING=True,
        SECRET_KEY=b'insira_uma_key_aqui',
        DEBUG=True
    )

    app.run(
        host='0.0.0.0',
        port=5000
    )
