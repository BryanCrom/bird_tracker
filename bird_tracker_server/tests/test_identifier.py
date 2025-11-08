from src.bird_identifier.identifier import Identifier
from tests.index import return_values

import pytest

@pytest.fixture
def identifier():
    """create an identifier object for testing"""
    return Identifier()

def test_identifier(identifier):
    """test the identifier function"""

    # valid file
    assert identifier.identify("assets/fantail-1.mp3") != return_values["identify_unmerged"]
    assert identifier.identify("assets/fantail-1.mp3") == return_values["identify_merged"]

    #invalid file
    with pytest.raises(FileNotFoundError, match="No such file or directory"):
        identifier.identify("")