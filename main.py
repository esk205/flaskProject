from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the initial page with form (index.html)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the name entered by the user
        name = request.form['name']
        # Redirect to the greet route with the name as a parameter
        return redirect(url_for('greet', name=name))
    # If it's a GET request or the form hasn't been submitted yet, render the template
    return render_template('index.html')

# Route for greeting page (greet.html)
@app.route('/greet/<name>')
def greet(name):
    return render_template('child.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)