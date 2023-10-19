# IDS706_MiniProj6_YangXu

## Project Overview

This project showcases complex SQL queries using an external Azure MySQL database. The goal is to demonstrate proficiency in constructing SQL queries that involve operations like joins, aggregation, and sorting. The project further integrates Continuous Integration and Continuous Deployment (CI/CD) pipelines to automate testing and formatting processes.

## Table of Contents

- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setting Up](#setting-up)
- [Sample Output](#sample-output)

## Project Structure

```bash
IDS706_MiniProj6_YangXu (Root Directory)
│
├── .devcontainer
│ ├── Dockerfile
│ └── devcontainer.json
│
├── .github
│ └── workflows
│ └── cicd.yml
│
├── .env
│
├── env.example
│
├── config.py
│
├── dataset_sample.csv
│
├── main.py
│
├── test_main.py
│
├── requirements.txt
│
├── Makefile
│
├── README.md
│
└── .gitignore
```

## Requirements

This project uses several libraries and tools which are listed in the `requirements.txt`. Notably:

- Basic utilities: `requests` and `pandas`.
- Data visualization: `matplotlib`.
- Testing: `pytest`, `pytest-cov`, and `nbval`.
- Code formatting: `black`.
- Code linting: `pylint`.
- Database: `pymysql`, `psycopg2-binary`, and `python-dotenv`.

## Setting Up

1. Clone this repository.
2. Create a `.env` file using `env.example` as a template. Fill in your database credentials.
3. Install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the main script to execute the complex SQL queries:
    ```bash
    python main.py
    ```

## Complex Query Explanation

The complex SQL query used in this project performs the following operations:

1. Joins the main data table (`week6_mini`) with the discounts table (`week6_mini_discounts`) using the "Product" column.
2. Calculates the total revenue by multiplying price and quantity, considering any available discount.
3. Sorts the results by the calculated total revenue in descending order.

    ```sql
    SELECT w.Date, w.Product, w.Price, w.Quantity, d.Discount,
        (w.Price * w.Quantity) * (1 - d.Discount) AS Total_Revenue
    FROM week6_mini w
    LEFT JOIN week6_mini_discounts d ON w.Product = d.Product
    ORDER BY Total_Revenue DESC;
    ```

## Sample Output

- **Descriptive Statistics**:

    ```bash
    {'Date': datetime.date(2023, 9, 1), 'Product': 'Apple', 'Price': 1.2, 'Quantity': 50, 'Discount': None, 'Total_Revenue': None}
    {'Date': datetime.date(2023, 9, 1), 'Product': 'Banana', 'Price': 0.5, 'Quantity': 40, 'Discount': None, 'Total_Revenue': None}
    {'Date': datetime.date(2023, 9, 1), 'Product': 'Cherry', 'Price': 2.5, 'Quantity': 20, 'Discount': None, 'Total_Revenue': None}
    {'Date': datetime.date(2023, 9, 2), 'Product': 'Apple', 'Price': 1.3, 'Quantity': 45, 'Discount': None, 'Total_Revenue': None}
    {'Date': datetime.date(2023, 9, 2), 'Product': 'Banana', 'Price': 0.6, 'Quantity': 50, 'Discount': None, 'Total_Revenue': None}
    {'Date': datetime.date(2023, 9, 2), 'Product': 'Cherry', 'Price': 2.4, 'Quantity': 22, 'Discount': None, 'Total_Revenue': None}
    {'Date': datetime.date(2023, 9, 3), 'Product': 'Apple', 'Price': 1.1, 'Quantity': 55, 'Discount': None, 'Total_Revenue': None}
    {'Date': datetime.date(2023, 9, 3), 'Product': 'Banana', 'Price': 0.7, 'Quantity': 42, 'Discount': None, 'Total_Revenue': None}
    {'Date': datetime.date(2023, 9, 3), 'Product': 'Cherry', 'Price': 2.6, 'Quantity': 19, 'Discount': None, 'Total_Revenue': None}
    ```

[![example workflow](https://github.com/nogibjj/IDS706_MiniProj6_YangXu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_MiniProj6_YangXu/actions/workflows/cicd.yml)
