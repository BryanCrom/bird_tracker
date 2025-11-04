from bird_identifier.identifier import Identifier
import pytest

@pytest.fixture
def identifier():
    """create an identifier object for testing"""

    return Identifier()

def test_identifier(identifier):
    """test the identifier function"""

    # valid file
    identifier.identify("../assets/fantail.mp3")

    #invalid file
    with pytest.raises(FileNotFoundError, match="No such file or directory"):
        identifier.identify("")