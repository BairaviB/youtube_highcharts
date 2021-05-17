from flask import Flask,render_template, jsonify, request
import random
import json
import data


app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():
    
    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    #return jsonify(result)
    return render_template("index.html") 

'''
http://0.0.0.0:3091/api/data
'''

@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = data.get_data()

    # result_dict = {

    #     ''       : year,
    #     'pytorch'    : pytorch,
    #     'tensorFlow' : tensorFlow

    # }

    return jsonify(result)

'''
http://0.0.0.0:3091/api/add
http://0.0.0.0:3091/api/add?year=2017&ontario_tourist=20345&quebec_tourist=200
http://0.0.0.0:3000/api/add?year=2021&pytorch=180&tensorFlow=90
'''
@app.route("/api/add", methods=["GET"])
def api_add_data():

    channel_var  = request.values.get('channel')
    subscriber_var         = request.values.get('subscriber')
   
    result = {
        'channel'          : channel_var,
        'subscriber'       : subscriber_var ,
        

    }
    result_data = data.add_row(channel_var, subscriber_var)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)