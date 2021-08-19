from flask import Flask,request

app=Flask(__name__)

# there is a difference between request.args.get() and request.args[]
@app.route('/query_example')
def query_example():
    language=request.args.get('language') #not mandatory argument. will return None if no value is passed
    framework=request.args['framework']# will throw an error if no value is passed
    website =request.args.get('website')

    return '''<h1>The langauge is :{} </h1>
                <h1>The framework is :{}</h1>
                <h1> The website is : {}</h1>'''.format(language,framework,website)

@app.route('/form_example',methods=['POST','GET'])
def form_example():
    if request.method=='POST':
        l=request.form.get('language')
        f=request.form.get('framework')
        return '<h1>The language is {}. The framework is {}. </h1>'.format(l,f)

    return '''<form method='POST' >
        Language <input type='text' name='language'>
        Framework <input type ='text' name='framework'>
        <input type='submit query'>
        </form>'''

if __name__=='__main__':
    app.run(debug=True)

# write with the url = http://127.0.0.1:5000/query_example?language='english'&framework='flask'&website='anaconda.com'

