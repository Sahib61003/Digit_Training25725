from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Hardcoded credentials
VALID_USERNAME = 'sahib.singh@godigit.com'
VALID_PASSWORD = '1402DLI'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['user'] = username
            flash('✅ Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('❌ Invalid credentials. Please try again.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('🔒 Logged out successfully.', 'info')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
