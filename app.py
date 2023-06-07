from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    # Retrieve data from the HTML form
    data = request.form['input_data']

    # Execute your Jupyter Notebook backend code here
    # ...

    # Return the result
    result = "Processed data: " + data
    return result
if __name__ == '__main__':
    app.run(debug=True)