from flask import Flask , render_template, request
app = Flask (__name__)



@app.route ('/')
def home (): 
    return render_template('index.html')

@app.route ('/registro')
def registro (): 
    return render_template('registro.html')

if __name__ == '__main__': 
    app.run (debug=True)

    