from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/client/<client_id>', methods=['GET'])
def get_client(client_id):
    return jsonify({
        "client_id": client_id,
        "name": "Иван Иванов",
        "email": "ivan@example.com"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

