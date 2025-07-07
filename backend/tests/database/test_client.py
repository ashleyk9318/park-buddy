import pytest
from unittest.mock import Mock, patch, MagicMock
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

@patch('backend.database.client.Cluster')
def test_get_session_without_cassandra(mock_cluster):
    """Test that get_session raises appropriate exception when Cassandra is not available"""
    # Mock Cluster to raise NoHostAvailable
    mock_cluster.side_effect = NoHostAvailable("No hosts available", errors={})
    
    client = CassandraClient()
    with pytest.raises(NoHostAvailable):
        client.get_session()

def test_client_close():
    """Test that client can be closed properly"""
    client = CassandraClient()
    # Should not raise an exception even if not connected
    client.close()

class TestCassandraClient:
    
    @patch('backend.database.client.Cluster')
    def test_client_initialization(self, mock_cluster):
        """Test Cassandra client initialization"""
        mock_session = Mock()
        mock_cluster_instance = Mock()
        mock_cluster_instance.connect.return_value = mock_session
        mock_cluster.return_value = mock_cluster_instance
        
        client = CassandraClient(contact_points=['localhost'], keyspace='test_keyspace')
        session = client.get_session()
        
        assert session == mock_session
        mock_cluster.assert_called_once_with(['localhost'])
        mock_cluster_instance.connect.assert_called_once_with('test_keyspace')
    
    @patch('backend.database.client.Cluster')
    def test_client_reuses_session(self, mock_cluster):
        """Test that client reuses the same session"""
        mock_session = Mock()
        mock_cluster_instance = Mock()
        mock_cluster_instance.connect.return_value = mock_session
        mock_cluster.return_value = mock_cluster_instance
        
        client = CassandraClient()
        session1 = client.get_session()
        session2 = client.get_session()
        
        assert session1 == session2
        # Should only connect once
        mock_cluster_instance.connect.assert_called_once()
    
    @patch('backend.database.client.Cluster')
    def test_client_close(self, mock_cluster):
        """Test client close method"""
        mock_session = Mock()
        mock_cluster_instance = Mock()
        mock_cluster_instance.connect.return_value = mock_session
        mock_cluster.return_value = mock_cluster_instance
        
        client = CassandraClient()
        client.get_session()  # Create session
        client.close()
        
        mock_session.shutdown.assert_called_once()
        mock_cluster_instance.shutdown.assert_called_once()
    
    @patch('backend.database.client.Cluster')
    def test_get_client_singleton(self, mock_cluster):
        """Test that get_client returns singleton instance"""
        mock_session = Mock()
        mock_cluster_instance = Mock()
        mock_cluster_instance.connect.return_value = mock_session
        mock_cluster.return_value = mock_cluster_instance
        
        client1 = get_client()
        client2 = get_client()
        
        assert client1 is client2
    
    @patch('backend.database.client.get_client')
    def test_get_session(self, mock_get_client):
        """Test get_session function"""
        mock_client = Mock()
        mock_session = Mock()
        mock_client.get_session.return_value = mock_session
        mock_get_client.return_value = mock_client
        
        session = get_session()
        
        assert session == mock_session
        mock_client.get_session.assert_called_once()