from sqlalchemy import text

def setup_database(db_connection):
  """
  Sets up the relational database by creating tables and inserting data.

  This function covers fundamental database management tasks:
  1. Table creation with primary keys
  2. Establishing foreign key relationships
  3. Inserting data into tables

  Args:
    db_connection: An active database connection object.
  """
  # Task 1: Create the departments table
  # Hint: Use a CREATE TABLE statement with id and name columns
  # Your code here

  # Task 2 & 3: Create the employees table with a foreign key
  # Hint: Use a CREATE TABLE statement with a FOREIGN KEY constraint
  # Your code here

  # Task 4: Insert data into the departments table
  # Hint: Use INSERT INTO statements
  # Your code here

  # Task 5: Insert data into the employees table
  # Hint: Use INSERT INTO statements, linking to departments
  # Your code here

  pass
