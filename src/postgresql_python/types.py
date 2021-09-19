from typing import TypedDict, List


class Column(TypedDict):
    """
    A table column type

    - *name*: string
    - *data_type*: string
    - *length*: int
    - *constrains*: List[string]

    """
    name: str
    data_type: str
    length: int
    constrains: List[str]


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

    - *columns?*: List[string]
    - *values*: List[string]

    """
    columns: List[str]
    values: List[str]
