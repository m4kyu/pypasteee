from dataclasses import dataclass
from .section import Section


@dataclass
class Paste:
    description: str
    encrypted: bool
    sections: list[Section] | None = None

    
    id: str | None = None

    views: int | None = None
    created_at: str | None = None
    expires_at: str | None = None
    
