import pytest
from backend.database.client import CassandraClient, get_client, get_session
from cassandra.cluster import NoHostAvailable

def test_cassandra_client_creation():
    """Test that CassandraClient can be created without connecting"""
    client = CassandraClient()
    assert client is not None
    assert client.contact_points == ['127.0.0.1']
    assert client.keyspace == 'store'

def test_get_client():
    """Test that get_client returns a client instance"""
    client = get_client()
    assert isinstance(client, CassandraClient)

def test_get_session_with_cassandra():
    """Test getting a session when Cassandra is available"""
    try:
        session = get_session()
        assert session is not None
    except NoHostAvailable:
        pytest.skip("Cassandra is not available")

def test_get_session_without_cassandra():
    """Test that get_session raises appropriate exception when Cassandra is not available"""
    client = CassandraClient()
    with pytest.raises(NoHostAvailable):
        client.get_session()

def test_client_close():
    """Test that client can be closed properly"""
    client = CassandraClient()
    # Should not raise an exception even if not connected
    client.close()