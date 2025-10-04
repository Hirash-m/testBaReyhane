import unittest

def say_hello():
    return "Hello, CI/CD!"

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, CI/CD!")

if __name__ == '__main__':
    unittest.main()