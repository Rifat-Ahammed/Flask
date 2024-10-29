from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def Welcome():
    return"Welcome to Flask Learning Path"

@app.route('/success/<int:score>')
def success(score):
    return "The Person has passed and the mark is: "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the mark is: "+str(score)

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    
    if marks<40:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result, score = marks))
if __name__=='__main__':
    app.run(debug=True)