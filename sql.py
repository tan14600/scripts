import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect("my_database.db")

# Create a cursor object
cursor = conn.cursor()

# Execute an SQL query
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# Insert a record
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))

# Commit changes and close connection
conn.commit()
conn.close()


SELECT customer_id
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '6 months'
GROUP BY customer_id
HAVING COUNT(DISTINCT DATE_TRUNC('month', order_date)) = 6;