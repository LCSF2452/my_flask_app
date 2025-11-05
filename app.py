from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    message = os.getenv('APP_MESSAGE', 'No message set')
    return message

@app.route('/health')
def health():
    health_status = os.getenv('APP_HEALTH', 'No health info set')
    return health_status

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)