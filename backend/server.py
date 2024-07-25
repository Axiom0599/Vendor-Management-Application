import prod_dao
app = Flask(__name__)

    connection = get_connection()
    products = prod_dao.all_products(connection)

if __name__ == "__main__":
    print("Starting server...")
    app.run(port=5000, debug=True)