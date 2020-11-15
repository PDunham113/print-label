from enum import Enum


class Unit(Enum):
    """Supported units for label design"""
    MM = 'mm'
    IN = 'in'
    DOT = 'dot'


class LabelError(Exception):
    pass
    """Generic Exception for label-related issues."""


class Label(object):
    """Dialect-agnostic label representation."""

    def __init__(self, width, height, unit):
        """Create an empty label object.

        @param width Width of label, in specified units
        @param height Height of label, in specified units
        @param unit Specified units, using Unit enum
        """
        self.width = width
        self.height = height
        self.units = unit

        self._label = {}

    def create_field(self, loc_x, loc_y, field_name=None):
        """Create an empty field in the label.

        Location of field is defined in terms of label units, in the upper-left
        corner.

        @param loc_x Location of field in X
        @param loc_y Location of field in Y
        @param field_name Unique name of field. Autogenerated if unspecified.

        @raises LabelError if field name is not unique

        @returns Field name
        """
        if field_name is None:
            field_name = self.generate_field_name()

        if field_name in self.get_field_names():
            raise LabelError('Field name already exists!')

        self._label[field_name] = {
            'loc_x': loc_x,
            'loc_y': loc_y,
        }

    def generate_field_name(self):
        """Autogenerates a unique field name.

        Default format is "field-<#>"

        @returns Unique field name
        """
        return 'field-{}'.format(len(self.get_field_names()))

    def get_field_names(self):
        """Returns lsit of all field names

        @returns List of field names
        """
        return [field_name for field_name in self._label]