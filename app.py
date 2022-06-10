import pickle
import numpy as np

from flask import Flask,render_template,request

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('indes.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    cgpa = float(request.form['CGPA'])
    iq = int(request.form['IQ'])
    profile_score = int(request.form['profile_score'])
    result = model.predict(np.array([cgpa,iq,profile_score]).reshape(1,3))
    if result==1:
        result='Placed'
    else:
        result='Not Placed'
    return render_template('indes.html',result=result)


if __name__=='__main__':
    app.run(debug=True)