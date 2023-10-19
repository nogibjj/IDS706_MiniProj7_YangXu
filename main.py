import pymysql.cursors
import pandas as pd
from config import get_db_config
from dotenv import load_dotenv

# Load environment variables from the .env file
# for database credentials and other settings.
load_dotenv()


def connect_db():
    # Fetch the database configuration from the .env file.
    config = get_db_config()

    # Establish and return a connection to the MySQL database
    # using the provided credentials.
    return pymysql.connect(
        host=config["DB_HOST"],
        user=config["DB_USER"],
        password=config["DB_PASSWORD"],
        db=config["DB_NAME"],
        cursorclass=pymysql.cursors.DictCursor,
        ssl={"ssl": {"ssl-mode": "require"}},
    )


def create_tables_if_not_exists(connection):
    # Create the necessary tables if they do not already exist in the database.
    try:
        with connection.cursor() as cursor:
            # Main table
            # Create the main data table for the CSV data.
            sql_week6_mini = """
            CREATE TABLE IF NOT EXISTS week6_mini (
                Date DATE,
                Product VARCHAR(255),
                Price FLOAT,
                Quantity INT
            );
            """
            cursor.execute(sql_week6_mini)

            # Discount table
            # Create a separate table for product discounts.
            sql_discounts = """
            CREATE TABLE IF NOT EXISTS week6_mini_discounts (
                Product VARCHAR(255),
                Discount FLOAT
            );
            """
            cursor.execute(sql_discounts)

            connection.commit()
    except Exception as e:
        print(f"Error creating tables: {e}")


def clear_table(connection):
    # Clear any existing data from the week6_mini table to avoid duplications.
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM week6_mini;"
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(f"Error clearing table: {e}")


def insert_data_from_csv(connection, filepath="dataset_sample.csv"):
    # Insert data from the provided CSV file into the week6_mini table.F
    try:
        # Read the CSV into a pandas DataFrame.
        df = pd.read_csv(filepath)

        # Iterate over each row of the DataFrame
        # and insert it into the database.
        for _, row in df.iterrows():
            with connection.cursor() as cursor:
                sql = """INSERT INTO week6_mini
                (Date, Product, Price, Quantity) VALUES (%s, %s, %s, %s)"""
                cursor.execute(
                    sql, (row["Date"],
                          row["Product"],
                          row["Price"],
                          row["Quantity"])
                )
                connection.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")


def complex_query(connection):
    # Execute a complex SQL query involving joins, aggregation, and sorting.
    try:
        with connection.cursor() as cursor:
            # The SQL query joins the main table with the discounts table,
            # calculates total revenue, and sorts by revenue.
            sql = """
            SELECT w.Date, w.Product, w.Price, w.Quantity, d.Discount,
                   (w.Price * w.Quantity) * (1 - d.Discount) AS Total_Revenue
            FROM week6_mini w
            LEFT JOIN week6_mini_discounts d ON w.Product = d.Product
            ORDER BY Total_Revenue DESC;
            """
            cursor.execute(sql)
            results = cursor.fetchall()

            # Print the results of the query.
            for result in results:
                print(result)
    except Exception as e:
        print(f"Error performing complex query: {e}")


def main():
    # Main execution flow.
    # Connect to the database, set up tables, clear previous data,
    # insert new data, and run the complex query.
    connection = connect_db()
    create_tables_if_not_exists(connection)
    clear_table(connection)
    insert_data_from_csv(connection)
    complex_query(connection)
    connection.close()


if __name__ == "__main__":
    main()
