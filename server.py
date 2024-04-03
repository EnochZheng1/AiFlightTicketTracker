from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_results')
def search_results():
    # Logic for fetching and displaying search results goes here
    return render_template('search_results.html')

@app.route('/dashboard')
def dashboard():
    # Logic for user-specific data goes here
    return render_template('dashboard.html')

@app.route('/login')
def login():
    # Logic for user login form goes here
    return render_template('login.html')

@app.route('/register')
def register():
    # Logic for user registration form goes here
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
