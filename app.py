from flask import Flask
from flask import request

import model 
app = Flask(__name__)

@app.route('/get-img', methods = ['POST'])
def get():
    if request.method == 'POST':
        arg1=request.get_json()['url']

        
    # return arg1    
    return model.pridict(arg1)

app.run()