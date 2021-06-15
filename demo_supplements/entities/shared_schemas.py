"""Reusable base schemas for utilization by the various entity schemas."""

import marshmallow


class CamelCaseSchema(marshmallow.Schema):
    """A Schema that marshals data with camelcased keys."""

    def on_bind_field(self, field_name, field_obj):
        """Camelize field keys."""
        field_obj.data_key = self.camelize(field_obj.data_key or field_name)

    @staticmethod
    def camelize(snake_str: str):
        """Convert snake_string to camelCase Format."""
        first, *others = snake_str.split("_")
        return "".join([first.lower(), *map(str.title, others)])
