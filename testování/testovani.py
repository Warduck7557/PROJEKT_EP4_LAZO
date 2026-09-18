import unittest

def is_only_letters(text: str) -> bool:
    return text.isalpha()

class TestOnlyLetters(unittest.TestCase):
    
    def test_valid_letters(self):
        # Pouze malá a velká písmena
        self.assertTrue(is_only_letters("Hello"))
        self.assertTrue(is_only_letters("world"))
        
    def test_numbers_and_letters(self):
        # Obsahuje číslice
        self.assertFalse(is_only_letters("Hello123"))
        
    def test_spaces_and_symbols(self):
        # Obsahuje mezery nebo speciální znaky
        self.assertFalse(is_only_letters("Hello World"))
        self.assertFalse(is_only_letters("Hello!"))
        
    def test_empty_string(self):
        # Prázdný řetězec vrací False
        self.assertFalse(is_only_letters(""))

if __name__ == "__main__":
    unittest.main()

