from cassandra.cluster import Cluster
from cassandra.cluster import NoHostAvailable
import logging

logger = logging.getLogger(__name__)

class CassandraClient:
    def __init__(self, contact_points=['127.0.0.1'], keyspace='store'):
        self.contact_points = contact_points
        self.keyspace = keyspace
        self._cluster = None
        self._session = None

    def get_session(self):
        """Get or create a Cassandra session"""
        if self._session is None:
            try:
                self._cluster = Cluster(self.contact_points)
                self._session = self._cluster.connect(self.keyspace)
                logger.info("Successfully connected to Cassandra")
            except NoHostAvailable as e:
                logger.error(f"Failed to connect to Cassandra: {e}")
                raise
            except Exception as e:
                logger.error(f"Unexpected error connecting to Cassandra: {e}")
                raise
        return self._session

    def close(self):
        """Close the Cassandra connection"""
        if self._session:
            self._session.shutdown()
            self._session = None
        if self._cluster:
            self._cluster.shutdown()
            self._cluster = None

# Global client instance
_client = None

def get_client():
    """Get the global Cassandra client instance"""
    global _client
    if _client is None:
        _client = CassandraClient()
    return _client

def get_session():
    """Get the global Cassandra session"""
    return get_client().get_session()

# For backward compatibility, try to create a session but don't fail if Cassandra is not available
try:
    session = get_session()
except Exception as e:
    logger.warning(f"Could not establish Cassandra connection during import: {e}")
    session = None