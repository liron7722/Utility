import pytest
from utility.mongo_handler import MongoDBHandler

@pytest.fixture
def mongo_client():
    client = MongoDBHandler('test')
    yield client
    

def test_connection(mongo_client):
    assert mongo_client.client is not None
    
def test_db_exists(mongo_client):
    db_list = mongo_client.get_db_names()
    assert len(db_list) > 0
