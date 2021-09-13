from typing import TypedDict


class Column(TypedDict):
    """
    A table column type

    - *name*: string
    - *data_type*: string
    - *length*: int
    - *constrains*: list[string]

    """
    name: str
    data_type: str
    length: int
    constrains: list[str]


class ForignKey(TypedDict):
    """
    A forign key type

    - *name*: string
    - *reference*: string
    
    """
    name: str
    reference: str


class Instance(TypedDict):
    """
    A table instance type

    - *columns?*: list[string]
    - *values*: list[string]
    
    """
    columns: list[str]
    values: list[str]
