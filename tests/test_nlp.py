import unittest
from app import normalize_input

class TestNLP(unittest.TestCase):
    def test_normalize_input(self) -> None:
        # Authorities
        assert normalize_input("What if ICE stops me?") == "what if immigration stops me"
        assert normalize_input("cop stopped me") == "police stopped me"
        assert normalize_input("border patrol question") == "immigration question"
        assert normalize_input("homeland security agent") == "immigration police"

        # Documents
        assert normalize_input("show my papers") == "show my document"
        assert normalize_input("where is my ead") == "where is my work permit"
    
        # Actions
        assert normalize_input("they inspected my car") == "they search my car"
        assert normalize_input("held in custody") == "detained"
    
    def test_punctuation_normalization(self) -> None:
        assert normalize_input("ICE!!!") == "immigration"
        assert normalize_input("What's my right?") == "whats my rights"
        assert normalize_input("U.S. citizen") == "us citizen"

    def test_edge_casses(self) -> None:
        assert normalize_input("") == ""
        assert normalize_input("123") == "123"
        assert normalize_input("!@#$") == ""
