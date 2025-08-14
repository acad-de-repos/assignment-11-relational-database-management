import unittest
from sqlalchemy import create_engine, inspect, text
from assignment import setup_database

class TestDatabaseSetup(unittest.TestCase):
    def setUp(self):
        """Set up a temporary in-memory SQLite database for testing"""
        self.engine = create_engine('sqlite:///:memory:')
        self.connection = self.engine.connect()

    def tearDown(self):
        """Close the database connection after each test"""
        self.connection.close()

    def test_setup_database(self):
        """Test the entire database setup process"""
        setup_database(self.connection)

        inspector = inspect(self.engine)

        # Test if tables are created
        self.assertTrue(inspector.has_table('departments'))
        self.assertTrue(inspector.has_table('employees'))

        # Test foreign key constraint
        foreign_keys = inspector.get_foreign_keys('employees')
        self.assertEqual(len(foreign_keys), 1)
        self.assertEqual(foreign_keys[0]['referred_table'], 'departments')

        # Test data insertion
        departments = self.connection.execute(text('SELECT * FROM departments')).fetchall()
        self.assertEqual(len(departments), 2)
        employees = self.connection.execute(text('SELECT * FROM employees')).fetchall()
        self.assertEqual(len(employees), 3)

if __name__ == '__main__':
    unittest.main()
