from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the name entered by the user
        name = request.form['name']
        # Render the template with the 'name' variable
        return render_template('index.html', name=name)
    # If it's a GET request or the form hasn't been submitted yet, render the template without 'name'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)