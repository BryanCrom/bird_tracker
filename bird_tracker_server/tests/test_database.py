from src.bird_identifier.identifier import Identifier
from src.database.database import Database
from datetime import datetime
from tests.index import return_values

import pytest

@pytest.fixture
def database():
    """create a database object for testing"""
    return Database(Identifier())

def test_get_calls(database):
    """test getting data from database"""

    assert (database.get_calls(
        datetime(2025, 11, 2).timestamp() * 1000,
        datetime(2025, 11, 8).timestamp() * 1000,
        "The Auckland Botanical Gardens",
        "all") == return_values["database_get_calls_correct"])