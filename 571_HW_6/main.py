from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html', title="Project 6")

if __name__=='__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

