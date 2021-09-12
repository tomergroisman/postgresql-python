from typing import TypedDict


class Column(TypedDict):
    name: str
    data_type: str
    length: int
    constrains: list[str]


class ForignKey(TypedDict):
    name: str
    reference: str


class Instance(TypedDict):
    columns: list[str]
    values: list[str]
