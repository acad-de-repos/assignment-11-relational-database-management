# Relational Database Management Assignment

## Problem Description

In this assignment, you will practice fundamental relational database management tasks. You will create tables with specified schemas, insert data into them, and establish relationships between the tables using foreign keys. This assignment will solidify your understanding of how to structure and populate a relational database.

## Learning Objectives

By completing this assignment, you will learn:
- How to create tables with different data types and constraints
- How to insert data into tables
- How to define primary and foreign keys to create relationships between tables
- How to use SQL Data Definition Language (DDL) and Data Manipulation Language (DML)

## Setup Instructions

1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Make sure you have the following packages installed:
    -   sqlalchemy (>=1.4.0)

## Instructions

1.  Open the `assignment.py` file.
2.  You will find a function definition: `setup_database(db_connection)`.
3.  The function takes a database connection object as input.
4.  Your tasks are to:
    *   **Task 1**: Create a `departments` table with `id` (primary key) and `name` columns.
    *   **Task 2**: Create an `employees` table with `id` (primary key), `name`, `age`, `salary`, and `department_id` columns.
    *   **Task 3**: Add a foreign key constraint to the `employees` table that links `department_id` to the `id` of the `departments` table.
    *   **Task 4**: Insert at least two departments into the `departments` table.
    *   **Task 5**: Insert at least three employees into the `employees` table, making sure to link them to the departments you created.

## Hints

*   Use `CREATE TABLE` statements for Tasks 1 and 2.
*   Use `ALTER TABLE` or include the `FOREIGN KEY` constraint directly in your `CREATE TABLE` statement for Task 3.
*   Use `INSERT INTO` statements for Tasks 4 and 5.
*   You can execute raw SQL statements using the `db_connection.execute(text(...))` method from SQLAlchemy.

## Testing Your Solution

Run the test file to verify your implementation:

```bash
python test.py
```

The tests will check:

-   That the `departments` and `employees` tables are created correctly
-   That the foreign key relationship is established
-   That the data is inserted correctly into both tables

## Expected Output

The function should modify the database by creating the specified tables and inserting the data. There is no direct return value, but the tests will inspect the database to verify the changes.

## Sample Data Format

### `departments` table:

| id  | name    |
| :-- | :------ |
| 1   | IT      |
| 2   | HR      |

### `employees` table:

| id  | name    | age | salary | department_id |
| :-- | :------ | --: | -----: | ------------: |
| 1   | Alice   | 30  | 80000  | 1             |
| 2   | Bob     | 45  | 95000  | 2             |
| 3   | Charlie | 28  | 72000  | 1             |

## Troubleshooting

### Common Errors

-   `DatabaseError: syntax error`: Carefully check your SQL syntax for typos or missing keywords.
-   `IntegrityError: FOREIGN KEY constraint failed`: This can happen if you try to insert an employee with a `department_id` that does not exist in the `departments` table.

## Further Exploration (Optional)

*   Explore other table constraints, such as `NOT NULL`, `UNIQUE`, and `CHECK`.
*   How would you update existing records in the tables?
*   Can you write a query to delete a department and all its associated employees?
*   Look into database normalization and different normal forms.

## Resources

-   [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
-   [SQLAlchemy Core Tutorial](https://docs.sqlalchemy.org/en/14/core/tutorial.html)
-   [SQL Data Definition Language (DDL)](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/)
