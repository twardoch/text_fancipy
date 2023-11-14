import pytest
from text_fancipy.fancipy import unfancipy_all

# test_unfancipy.py

def test_unfancipy_all():
    """
    Test the unfancipy_all function.
    """
    test_string = "𝗔𝘈𝘼𝙰A"  # Represents A in snbl, snit, snbi, mono, and dflt styles
    expected = "AAAAA"
    assert unfancipy_all(test_string) == expected

