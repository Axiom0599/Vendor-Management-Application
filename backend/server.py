from flask import Flask, jsonify, request, render_template, url_for, redirect
from prod_dao import delete_product, all_products, insert_product,update_product
from sqlConnection import get_connection
import json
import prod_dao
import orderdao
app = Flask(__name__)
connection = get_connection()
@app.route("/", methods=['GET', 'POST'])
def home_page():
    return render_template('home.html')

@app.route("/students", methods=['POST'])
def student_signup():
    data = request.json
    if not all(key in data for key in ('name', 'contact', 'id')):
        return jsonify({"success": False, "message": "Missing required fields"}), 400
    # Here you would typically save the data to a database
    # For now, we'll just return success
    return jsonify({"success": True})

@app.route("/insertOrder")
def student_portal():
    return render_template('insertOrder.html')  # You'll need to create this template


@app.route('/vendor_signup', methods=['POST'])
def vendor_signup():
    vendor_code = request.form.get('code')
    if vendor_code == '5729':
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route('/manageProducts')
def manage_products():
    connection = get_connection()
    products = prod_dao.all_products(connection)
    return render_template('manageProducts.html', products=products)




@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product_route(product_id):
    try:
        connection = get_connection()
        delete_product(connection, product_id)
        return jsonify({"success": True, "message": "Product deleted successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500



@app.route('/add_product', methods=['POST'])
def add_product_route():
    try:
        connection = get_connection()
        product_data = request.json
        product_id = insert_product(connection, product_data)
        return jsonify({"success": True, "message": "Product added successfully", "id": product_id})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/edit_product/<int:product_id>', methods=['POST'])
def edit_product_route(product_id):
    try:
        connection = get_connection()
        product_data = request.json
        update_product(connection, product_id, product_data)
        return jsonify({"success": True, "message": "Product updated successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500



@app.route('/insert_order', methods=['POST'])
def insert_order():
    order_data = request.json
    try:
        order_id = orderdao.insert_order(connection, order_data)
        if order_id:
            return jsonify({"success": True, "order_id": order_id})
        else:
            return jsonify({"success": False, "message": "Failed to insert order"}), 500
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# @app.route('/viewOrders')
# def view_orders():
#     orders = orderdao.get_all_orders(connection)
#     return render_template("viewOrders.html", orders=orders)
#
#
# @app.route('/order_details/<int:order_id>')
# def order_details(order_id):
#     details = orderdao.get_order_details(connection, order_id)
#     return jsonify(details)


if __name__ == "__main__":
    print("Starting server...")
    app.run(port=5000, debug=True)