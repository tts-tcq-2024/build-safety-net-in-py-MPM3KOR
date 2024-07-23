import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("J"), "J000")
        self.assertEqual(generate_soundex("R"), "R000")

    def test_double_character(self):
        self.assertEqual(generate_soundex("IT"), "I300")
        self.assertEqual(generate_soundex("AT"), "A300")

    def test_complete_word(self):
        self.assertEqual(generate_soundex("JOHN"), "J500")
        self.assertEqual(generate_soundex("BANGALORE"), "B524")
        self.assertEqual(generate_soundex("CHENNAI"), "C500")
        

    
if __name__ == '__main__':
    unittest.main()
