### Integrate HTML with Flask
### HTTP verb GET and POST 
### Jinja2 template engine

"""
{%...%} any kind statements
{{   }} expression to print output
{#....#} this is for comments
"""
from deprecated import deprecated
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    
    res=""
    if score>=50:
        res = "Pass"
    else:
        res="fail"
        
    exp = {'score':score, 'res':res}
    
    return render_template('result.html', result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the mark is: "+str(score)

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""    
    if marks<40:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result, score = marks))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    
    total_score = 0
    if request.method=='POST':
         
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        cs = float(request.form['cs'])
        datascience = float(request.form['datascience'])
        total_score = (science + maths + cs + datascience)/4
        print(total_score)

        return redirect(url_for('success', score=total_score))
        


if __name__=='__main__':
    app.run(debug=True)