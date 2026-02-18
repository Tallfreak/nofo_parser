"""Contact information domain types for grant funding agencies."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ContactInfo:
    """Agency or program contact information."""

    name: str = ''
    email: str = ''
    phone: str = ''
