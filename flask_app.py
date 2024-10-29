from flask import Flask

### WSGI application

app = Flask(__name__)

@app.route('/')

def welcome():
    
    return"Welcome to Flask. Let's complete the Flask course"

@app.route('/learners')
def Students():
    return"Hello students, what's your thought about Flask Tutorial"

if __name__ == '__main__':
    app.run(debug=True)
