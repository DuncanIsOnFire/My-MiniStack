from flask import Flask

site = Flask(__name__)

@site.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    site.run()
