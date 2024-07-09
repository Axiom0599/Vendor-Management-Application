from flask import Flask, jsonify, request, render_template

import prod_dao
from sqlConnection import get_connection

app = Flask(__name__)
connection = get_connection()

@app.route("/", methods=['GET'])
def home():
    products = prod_dao.all_products(connection)
    return render_template('manageProducts.html', products=products)

@app.route("/home", methods=['GET'])
def home_page():
    return render_template('home.html')

@app.route("/student", methods=['GET'])
def student():
    return render_template('student.html')

@app.route("/vendor", methods=['GET'])
def vendor():
    return render_template('vendor.html')

@app.route("/insertOrder", methods=['GET'])
def insert_order():
    return render_template('insertOrder.html')

@app.route("/viewOrders", methods=['GET'])
def view_order():
    return render_template('viewOrders.html')


@app.route("/getProducts", methods=['GET'])
def get_products():
    products = prod_dao.all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/deleteProduct/<int:product_id>", methods=['DELETE'])
def delete_product(product_id):
        try:
            prod_dao.delete_product(connection, product_id)
            return jsonify({"success": True}), 200
        except Exception as e:
            print(e)
            return jsonify({"success": False}), 500

if __name__ == "__main__":
    print("Starting server...")
    app.run(port=5000, debug=True)



