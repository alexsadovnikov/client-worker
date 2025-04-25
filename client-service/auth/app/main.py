from flask import Flask, request, jsonify
import jwt
import datetime
from flasgger import Swagger

SECRET_KEY = "supersecret"  # В реальном проекте лучше вынести в env-переменную

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/login", methods=["POST"])
def login():
    """
    Авторизация пользователя
    ---
    tags:
      - Auth
    parameters:
      - name: username
        in: formData
        type: string
      - name: password
        in: formData
        type: string
    responses:
      200:
        description: Авторизация успешна, возвращаем JWT
      401:
        description: Неверные учётные данные
    """
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "admin" and password == "123":
        token = jwt.encode({
            "user": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "invalid credentials"}), 401

@app.route("/verify", methods=["GET"])
def verify():
    """
    Проверка JWT
    ---
    tags:
      - Auth
    parameters:
      - name: Authorization
        in: header
        description: "Bearer <JWT>"
        required: true
        type: string
    responses:
      200:
        description: Токен валиден
      401:
        description: Токен невалиден или просрочен
    """
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing Bearer token"}), 401

    token = auth_header.split(" ")[1]
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"user": decoded["user"], "exp": decoded["exp"]}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
EOF
