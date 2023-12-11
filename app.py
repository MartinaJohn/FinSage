from flask import Flask, request, url_for, redirect, render_template
import pickle

import numpy as np

from gradio_client import Client
client = Client("https://fingpt-fingpt-forecaster.hf.space/--replicas/vzfr2/")

app = Flask(__name__, template_folder='./templates', static_folder='./static')

Pkl_Filename = "rf_tuned.pkl" 
with open(Pkl_Filename, 'rb') as file:  
    model = pickle.load(file)
@app.route('/')

def hello_world():
    return render_template('index.html')


@app.route('/calc', methods=['POST','GET'])
def predict():
    features = [int(x) for x in request.form.values()]

    print(features)
    final = np.array(features).reshape((1,6))
    print(final)
    pred = model.predict(final)[0]
    print(pred)

    # render_template('home.html',result=pred)
    if pred < 0:
        return render_template('op.html', pred='Error calculating Amount!')
    else:
        return render_template('op.html', pred='Expected amount is {0:.3f}'.format(pred))


@app.route('/forecaster', methods=['GET', 'POST'])
def index():
     result = None
     if request.method == 'POST':
         ticker = request.form['ticker']
         date = request.form['date']
         n_weeks = int(request.form['n_weeks'])
         use_latest_basic_financials = request.form['use_latest_basic_financials'] == 'on'
         result = client.predict(ticker, date, n_weeks, use_latest_basic_financials, api_name="/predict")
     return render_template('stockForecaster.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)