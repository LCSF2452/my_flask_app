from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message=os.environ.get('APP_MESSAGE', 'No message'))

@app.route('/health')
def health():
    return render_template('health.html', health=os.environ.get('APP_HEALTH', 'No health status'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
