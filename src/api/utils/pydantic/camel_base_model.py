"""Pydantic BaseModel to handle de/serialization of camel <> snake case field names.
For use in web APIs so they can be idiomatic. where the client sends camel case JSON and the server sends snake case JSON."""

from pydantic import AliasGenerator, BaseModel
from pydantic.alias_generators import to_camel

class CamelBaseModel(BaseModel):
    """Pydantic BaseModel configured to generate camel case serialization aliases
    for all fields on models that inherit from this class.

    Model classes can be instantiated with either camel case or original field names.

    Use model_dump(by_alias=True) to serialize the model with the serialization aliases i.e. camel case field names.
    """

    class Config:
        """Pydantic model configuration."""

        alias_generator = AliasGenerator(
            alias=to_camel,
        )
        populate_by_name = True  # Allow population by alias and original field name
