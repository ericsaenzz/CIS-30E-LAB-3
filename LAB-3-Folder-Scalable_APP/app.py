from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return  render_template('home.html')

@app.route('/about')
def about():
    return "This is a simple scalable Flask app.The focus will be on setting up a scalable project structure with Python, creating reusable functions, and utilizing Flask for a basic web application setup."
if __name__ == '__main__':
    app.run(debug=True)