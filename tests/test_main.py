# import pymysql.cursors
# import pandas as pd
from main import (
    connect_db,
    create_tables_if_not_exists,
    clear_table,
    insert_data_from_csv,
    # complex_query,
)


def test_db_connection():
    # Test if the function successfully connects to the database
    connection = connect_db()
    assert connection.open, "Database connection failed"
    connection.close()


def test_table_creation():
    connection = connect_db()

    # Create tables if they don't exist
    create_tables_if_not_exists(connection)

    # Test if the tables have been created
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES LIKE 'week6_mini';")
        result = cursor.fetchone()
        assert result, "Table week6_mini not found"

        cursor.execute("SHOW TABLES LIKE 'week6_mini_discounts';")
        result = cursor.fetchone()
        assert result, "Table week6_mini_discounts not found"

    connection.close()


def test_data_insertion():
    connection = connect_db()

    # Clear any existing data and insert new data from the CSV
    clear_table(connection)
    insert_data_from_csv(connection)

    # Test if data has been inserted
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) as total FROM week6_mini;")
        result = cursor.fetchone()
        # You can adjust the expected number based on your CSV data
        assert result["total"] == 9, "Data insertion from CSV failed"

    connection.close()


def test_complex_query():
    connection = connect_db()

    # Run the complex query and check the results
    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT w.Date, w.Product, w.Price, w.Quantity, d.Discount,
                   (w.Price * w.Quantity) * (1 - d.Discount) AS Total_Revenue
            FROM week6_mini w
            LEFT JOIN week6_mini_discounts d ON w.Product = d.Product
            ORDER BY Total_Revenue DESC;
            """
            cursor.execute(sql)
            results = cursor.fetchall()
            assert results, "No results from the complex query"
    except Exception as e:
        assert False, f"Error performing complex query: {e}"

    connection.close()
