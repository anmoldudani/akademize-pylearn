from P import pal

def test_pallindrome():
    """Test Is Pallindrome."""
    assert pal(1234) is False
    assert pal(1221) is True