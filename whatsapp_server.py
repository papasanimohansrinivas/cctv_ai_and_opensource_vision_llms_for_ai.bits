from flask import Flask
from flask import send_file
from flask import make_response
# Flask constructor takes the name of
# current module (__name__) as argument
app = Flask(__name__)


# Use of <converter: variable name> in the
# route() decorator.
@app.route('/fire/<string:filename>/',methods = ['GET'])
def allow(filename):
    response = make_response(send_file("./multimodal_llm_pilot_test_outputs/{}".format(filename,as_attachement=True)))
    response.headers['Content-Type'] = 'image/png'
    return response

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0",port=5000,debug=False)
