import unittest

import main


class TrackliftTestCase(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()

    def tearDown(self):
        pass
    
    def test_get_nonexistent_workout(self):
        rv = self.app.get('/workouts/1/')
        assert b'error' in rv.get_data()


if __name__ == '__main__':
    unittest.main()
