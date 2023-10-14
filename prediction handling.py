from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
    return app.send_static_file('score predictor.html')

if __name__ == '__main__':
    app.run(debug=True)