from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/switch_tab', methods=['POST'])
def switch_tab():
    tab = request.form['tab']

    return {'success': True, 'tab': tab}

if __name__ == '__main__':
    app.run()
