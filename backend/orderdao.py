# def get_customers(connection):
#     cursor = connection.cursor()
#     query = "SELECT orders.order_id, orders.customer_name, orders.total, orders.date_time FROM orders;"
#     cursor.execute(query)
#     return [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
#
# def insert_order(connection, order_data):
#     cursor = connection.cursor()
#     try:
#         # Insert order
#         order_query = "INSERT INTO orders (customer_name, date_time) VALUES (%s, NOW())"
#         cursor.execute(order_query, (order_data['customer_name'],))
#         order_id = cursor.lastrowid
#
#         # Insert order items
#         item_query = "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)"
#         for item in order_data['items']:
#             cursor.execute(item_query, (order_id, item['productId'], item['quantity']))
#
#         connection.commit()
#         return order_id
#     except Exception as e:
#         print(e)
#         connection.rollback()
#         return None
#
# def get_all_orders(connection):
#     cursor = connection.cursor()
#     query = """
#     SELECT o.id, c.name, o.order_date, SUM(p.price_per_unit * oi.quantity) as total_amount
#     FROM orders o
#     JOIN customers c ON o