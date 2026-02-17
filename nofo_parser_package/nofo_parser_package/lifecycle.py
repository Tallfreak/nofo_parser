"""Funding opportunity lifecycle domain types."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class GrantStatus(Enum):
    """Lifecycle status of a funding opportunity."""

    # Pre-release
    FORECASTED = 'forecasted'  # Announced but not yet open

    # Active
    POSTED = 'posted'  # Open for applications

    # Closed
    CLOSED = 'closed'  # Past deadline or explicitly closed
    ARCHIVED = 'archived'  # Historical record
    DELETED = 'deleted'  # Removed from system


@dataclass(frozen=True)
class FundingCycle:
    """Timeline for a funding opportunity."""

    posted_date: datetime | str | None  # When applications open
    due_date: datetime | str | None  # Application deadline
    open_date: datetime | str | None = None  # When first announced
    forecast_date: datetime | str | None = None  # When forecasted
    performance_start: datetime | str | None = None  # When funded work begins
    performance_end: datetime | str | None = None  # When funded work ends


class ChangeReason(Enum):
    """Why a grant needs attention."""

    NEW_OPPORTUNITY = 'new_opportunity'
    TITLE_UPDATED = 'title_updated'
    STATUS_CHANGED = 'status_changed'
    NO_CHANGES = 'no_changes'
