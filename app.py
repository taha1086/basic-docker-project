from flask import Flask
import redis

app = Flask(__name__)

@app.route('/')
def say_hello():
    r = redis.Redis(host='redis',port=6379)
    name=r.get('name').decode()
    return f'Hello {name}\n'


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)


