from abc import ABC, abstractmethod


class Connection(ABC):
    """Abstract base class for printer connections.

    Connection instances must support a .open(), a .close(), and a .send()
    method.
    """

    def __init__(self):
        self._is_connected = False

    def __enter__(self):
        """Opens connection via context manager.

        @returns self
        """
        self.open()
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        """Closes connection via context manager.

        @param exec_type Type of exception, by context manager
        @param exec_value Value of exception, by context manager
        @param traceback Exception traceback, by context manager
        """
        self.close()

    @abstractmethod
    def close(self):
        """Abstract method for closing connection.

        Must be defined by child class - the definition should check
        `self._is_connected` upon entry & call this implementation upon
        successful completion
        """
        self._is_connected = False

    @abstractmethod
    def open(self):
        """Abstract method for opening connection.

        Must be defined by child class - the definition should check
        `self._is_connected` upon entry & call this implementation upon
        successful completion
        """
        self._is_connected = True

    @abstractmethod
    def send(self, bytes):
        """Abstract method for sending data

        Must be defined by child class - the definition should check
        `self._is_connected` upon entry.
        """
        raise NotImplementedError('Cannot send bytes w/o definition.')
