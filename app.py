from flask import Flask  
#WSGI Application

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hi Thomas Welcome Home. Feel at home, welcome again hey tgjfts fgychjb '

@app.route('/members')
def nice():
    return "I think i like flask"

if __name__=='__main__':
    app.run(debug=True)
# msg = "New in flask"
# print(msg)