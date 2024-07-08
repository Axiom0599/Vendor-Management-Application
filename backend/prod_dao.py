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

def insert_product(connection, product):
    cursor = connection.cursor()
    query = "INSERT INTO products (productscol, unit_of_measure_id, price_per_unit) VALUES (%s, %s, %s);"
    data = (product['productscol'], product['unit_of_measure_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE products.id = %s;"
    cursor.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = get_connection()
    print(insert_product(connection,{
        'productscol': 'hello',
        'unit_of_measure_id': '1',
        'price_per_unit': '100',
    }))



