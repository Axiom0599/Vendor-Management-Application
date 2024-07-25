from sqlConnection import get_connection
def all_products(connection):
    cursor = connection.cursor()

    query = "SELECT products.idproducts, products.productscol, products.unit_of_measure_id, products.price_per_unit, uom.uomcol FROM products inner join uom on products.unit_of_measure_id = uom.iduom;"

    cursor.execute(query)

    response = []

    for (idproducts, productscol, unit_of_measure_id, price_per_unit,uomcol) in cursor:
        response.append(
            {
                'idproducts': idproducts,
                'productscol': productscol,
                'unit_of_measure_id': unit_of_measure_id,
                'price_per_unit': price_per_unit,
                'uomcol': uomcol
            }
        )

    return response
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE products.idproducts = %s;"
    cursor.execute(query, (product_id,))
    connection.commit()


def insert_product(connection, product):
    cursor = connection.cursor()
    query = "INSERT INTO products (productscol, unit_of_measure_id, price_per_unit) VALUES (%s, %s, %s);"
    data = (product['productscol'], product['uomcol'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def update_product(connection, product_id, product):
    cursor = connection.cursor()
    query = "UPDATE products SET productscol = %s, unit_of_measure_id = %s, price_per_unit = %s WHERE idproducts = %s;"
    data = (product['productscol'], product['uomcol'], product['price_per_unit'], product_id)
    cursor.execute(query, data)
    connection.commit()



if __name__ == '__main__':
    connection = get_connection()




