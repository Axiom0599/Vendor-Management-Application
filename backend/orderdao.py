
from sqlConnection import get_connection
def insert_order(connection, order_data):
    cursor = connection.cursor()
    try:
        # Insert order
        order_query = "INSERT INTO orders (customer_name, date_time) VALUES (%s, NOW())"
        cursor.execute(order_query, (order_data['customer_name'],))
        order_id = cursor.lastrowid

        # Insert order items
        item_query = "INSERT INTO order_details (order_id, product_id, quantity) VALUES (%s, %s, %s)"
        for item in order_data['items']:
            cursor.execute(item_query, (order_id, item['productId'], item['quantity']))

        connection.commit()
        return order_id
    except Exception as e:
        print(e)
        connection.rollback()
        return None

# def get_all_orders(connection):
#     cursor = connection.cursor()
#     query = """
#     SELECT o.id, o.customer_name, o.date_time, SUM(p.price_per_unit * oi.quantity) as total_amount
#     FROM orders o
#     JOIN order_items oi ON o.id = oi.order_id
#     JOIN products p ON oi.product_id = p.id
#     GROUP BY o.id
#     ORDER BY o.date_time DESC
#     """
#     cursor.execute(query)
#     return cursor.fetchall()
#
#
#
# def get_order_details(connection, order_id):
#     cursor = connection.cursor()
#     query = """
#     SELECT p.name, oi.quantity, p.price_per_unit, (oi.quantity * p.price_per_unit) as item_total
#     FROM order_items oi
#     JOIN products p ON oi.product_id = p.id
#     WHERE oi.order_id = %s
#     """
#     cursor.execute(query, (order_id,))
#     return cursor.fetchall()




if __name__ == '__main__':
    connection = get_connection()
