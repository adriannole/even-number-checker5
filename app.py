from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        number = int(request.form['number'])
        if number % 2 == 0:
            result = f"El número {number} es par."
        else:
            result = f"El número {number} es impar."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
