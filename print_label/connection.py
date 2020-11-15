from abc import ABC, abstractmethod
import socket
import sys


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

        @param bytes A bytes-like iterable to send over open connection
        """
        raise NotImplementedError('Cannot send bytes w/o definition.')


class FileConnection(Connection):
    """Debug connection - prints to a file-like object."""

    def __init__(self, fd=sys.stdout):
        """Create a FileConnection using a specified file descriptor.

        If no descriptor is given, defaults to stdout

        @param fd File descriptor to write to. Default sys.stdout
        """
        self.fd = fd
        super().__init__()

    def close(self):
        """Does nothing other than implement the _is_connected flag."""
        if self._is_connected:
            super().close()

    def open(self):
        """Does nothing other than implement the _is_connected flag."""
        if not self._is_connected:
            super().open()

    def send(self, bytes):
        """Write date to file descriptor.

        UTF-8 encoding is expected

        @param bytes A bytes-like iterable to send over open connection

        @raises ConnectionError when called on a closed connection
        """
        if self._is_connected:
            self.fd.write(bytes.decode('utf-8'))
        else:
            raise ConnectionError('Connection not open')


class TCPConnection(Connection):
    """Printer connection over TCP/IP."""

    def __init__(self, address, timeout=None):
        """Create a TCPConnection at the specified Internet address.

        Supports non-numeric hostnames as well as both IPv4 & IPv6 addresses.

        @param address A 2-tuple (host, port) in the style of the socket lib
        """
        self.address = address
        self.timeout = timeout

        self.socket = None

        super().__init__()

    def close(self):
        """Close socket."""
        if self._is_connected:
            self.socket.shutdown(socket.RDWR)
            self.socket.close()
            super().close()

    def open(self):
        """Open socket."""
        if not self._is_connected:
            self.socket = socket.create_connection(
                self.address,
                self.timeout
            )
            super().open()

    def send(self, bytes):
        """Send data over open connection

        @param bytes A bytes-like iterable to send over open connection

        @raises ConnectionError when called on a closed connection
        """
        if self._is_connected:
            self.socket.send(bytes)
        else:
            raise ConnectionError('Connection not open')
