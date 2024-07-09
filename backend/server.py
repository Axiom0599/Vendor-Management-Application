from flask import Flask, jsonify, make_response
import prod_dao
from sqlConnection import get_connection

app = Flask(__name__)

connection = get_connection()

@app.route("/getProducts", methods=['GET'])
def get_products():
    products = prod_dao.all_products(connection)
    response = make_response(jsonify(products))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

if __name__ == "__main__":
    print("Starting server...")
    app.run(port=5000, debug=True)
