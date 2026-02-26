# test_wikiquantum.py
"""
Tests for WikiQuantum module.
"""

import unittest
from wikiquantum import WikiQuantum

class TestWikiQuantum(unittest.TestCase):
    """Test cases for WikiQuantum class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WikiQuantum()
        self.assertIsInstance(instance, WikiQuantum)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WikiQuantum()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
