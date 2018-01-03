import unittest

import testing.postgresql

import main

Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True)

class TrackliftTestCase(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()
        self.postgresql = Postgresql()

    def tearDown(self):
        self.postgresql.stop()
    
    def test_get_nonexistent_workout(self):
        rv = self.app.get('/workouts/1/')
        assert b'error' in rv.get_data()

    def test_post_workout(self):
        assert False


if __name__ == '__main__':
    unittest.main()
