"""Defines dialects used to translate Labels."""
from abc import ABC, abstractmethod
import json


class Dialect(ABC):
    """Abstract base class for printer dialects.

    Dialect instances must support a encode() method. Other methods may be
    defined, but a Dialect need not implement them all.

    Dialects rarely need instantiation, instead favoring class methods.
    """

    @classmethod
    @abstractmethod
    def encode(cls, label):
        """Returns a UTF-8 encoded bytes object representing the encoded label.

        @param label Label object to encode.
        """
        pass


class JSON(Dialect):
    """JSON-based representation of Label.

    This is specific to the `print-label` module and does not correspond to any
    real-world printer dialect.
    """

    @classmethod
    def encode(cls, label):
        """Returns a UTF-8 encoded bytes object representing the encoded label.

        @param label Label object to encode.
        """
        label_dict = label._label.copy()

        label_dict['__meta__'] = {
            'width': label.width,
            'height': label.height,
            'units': label.units.value,
        }

        return json.dumps(label_dict)
