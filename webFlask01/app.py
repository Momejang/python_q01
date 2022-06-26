from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user')
def user1():
    return render_template('user.html')

@app.route('/user/<userId>')
def user(userId):
    return render_template('user.html')
    #return f'입력된 유저ID 파라미터 :  {userId}'

if __name__ == '__main__':
    app.run(debug=True)
