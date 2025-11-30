from abc import ABC, abstractmethod


class BaseConnector(ABC):
    def __init__(self, connector_type: str):
        self.connector_type = connector_type  # A name holder for type of connection

    @abstractmethod
    def prepare_session(self) -> None:
        """Prepare the session. Create headers or create session based on different platform"""
        pass

    @abstractmethod
    def close_session(self) -> None:
        """Closure the session. Remove headers or Remove session based on different platform"""
        pass

    # @abstractmethod
    # def ping(self):

class BasicAuthenticationConnector(BaseConnector):
    def __init__(self):
        super().__init__('basic')
        self.headers = {}
