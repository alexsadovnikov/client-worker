from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/ping', methods=['GET'])
def ping():
    """
    Пинг эндпоинт
    ---
    responses:
      200:
        description: Возвращаем pong
        schema:
          type: object
          properties:
            status:
              type: string
              example: "pong"
    """
    return jsonify({"status": "pong"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
