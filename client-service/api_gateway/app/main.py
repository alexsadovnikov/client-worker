from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)

@app.route('/')
def index():
    return 'API Gateway works! Check /apidocs'

@app.route('/ping', methods=['GET'])
def ping():
    """
    Ping endpoint
    ---
    responses:
      200:
        description: OK
    """
    return jsonify({"status": "ok"})

swagger = Swagger(app)

if __name__ == '__main__':
    # flask запустится на порту 8080
    app.run(host='0.0.0.0', port=8080)
