import unittest
from postgresqlconnector.connector import DB


class TestConnector(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_all_query = '''SELECT * FROM test_table ORDER BY id ASC'''

    def __call__(self, *args, **kwargs):
        # savepoint_name = 'TestConnectorSavepoint'
        # create transaction
        # DB.query('''SAVEPOINT {};'''.format(savepoint_name))
        # prepare test data
        DB.query('''
            CREATE TABLE test_table (
                id INT,
                name TEXT
            );
        ''')
        DB.query('''
            INSERT INTO test_table
            VALUES 
                (1, 'test_1'),
                (2, 'test_2'),
                (3, 'test_3');
        ''')
        # main part
        super().__call__(*args, **kwargs)
        # rollback transaction
        DB.query('''DROP TABLE test_table;''')
        # DB.query('''RELEASE SAVEPOINT {};'''.format(savepoint_name))

    def test_basic(self):
        result = DB.query('''SELECT * FROM pg_stat_activity;''')
        self.assertIsNotNone(result)

    def test_query(self):
        result = DB.query(self.get_all_query)
        self.assertEqual(len(result), 3)

        result = DB.query('''SELECT * FROM test_table WHERE id=0''')
        self.assertEqual(len(result), 0)

    def test_row(self):
        result = DB.row(self.get_all_query)
        self.assertEqual((result[0], result[1]), (1, 'test_1'))

    def test_scalar(self):
        result = DB.scalar(self.get_all_query)
        self.assertEqual(result, 1)

    def test_transaction(self):
        try:
            with DB.create_transaction():
                DB.query('''INSERT INTO test_table VALUES (4, 'test_4');''')

                result = DB.query(self.get_all_query)
                self.assertEqual(len(result), 4)
                raise Exception('my_exc')
        except Exception as e:
            self.assertTrue('my_exc' in str(e))

        result = DB.query(self.get_all_query)
        self.assertEqual(len(result), 3)
