from dataclasses import dataclass


@dataclass 
class Section:
    name: str
    content: str

    syntax: str = 'autodetect'
    size: int | None = None

