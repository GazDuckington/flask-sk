from flask import Flask, send_from_directory
from apis import api
import os

app = Flask(__name__)
api.init_app(app)

# TODO: add svelte frontend
@app.route('/')
def homePage():
    return send_from_directory('build', 'index.html')

# TODO: add routes to static files
@app.route('/<path:path>')
def staticFiles(path):
    return send_from_directory('build', path)

# ! ANY OTHER ROUTES MUST BE WRITTEN IN THE /apis DIRECTORY!
if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    # app.debug = True
    # app.run(debug=True, host='0.0.0.0', port=int(port)) 
    app.debug = False
    app.run(debug=False, host='0.0.0.0', port=int(port))
