import json

from flask import Flask, send_from_directory
from flask.wrappers import Response

from apis import api
from apis.wrapper import secure

app = Flask(__name__)
api.init_app(app)

@app.route('/')
@secure
def homePage():
    dict = {"message":"hello"}
    return Response(json.dumps(dict), mimetype='application/json')
    # return send_from_directory('client', 'index.html')

@app.route('/<path:path>')
def staticFiles(path):
    return send_from_directory('client', path)

# ! ANY OTHER ROUTES MUST BE WRITTEN IN THE /apis DIRECTORY!
if __name__ == "__main__":
    app.debug = False
    app.run(debug=False, host='0.0.0.0')
