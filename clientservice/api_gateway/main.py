from flask import Flask, send_from_directory, jsonify
import yaml
import os

app = Flask(
    __name__,
    static_folder="app/static",
    static_url_path="/static"
)

# 🔹 Маршрут для Swagger UI (страница документации)
@app.route("/apidocs/")
def swagger_ui():
    return send_from_directory(app.static_folder, "swagger-ui.html")

# 🔹 Маршрут для отдачи openapi.yaml как JSON
@app.route("/openapi.json")
def openapi_json():
    with open(os.path.join(app.static_folder, "openapi.yaml"), "r") as f:
        spec = yaml.safe_load(f)
    return jsonify(spec)

# 🔹 Проверочный корневой маршрут
@app.route("/")
def index():
    return {"message": "API Gateway is running"}

# 🔹 Статусный маршрут
@app.route("/ping")
def ping():
    return {"status": "ok"}

# 🔹 Точка входа
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)