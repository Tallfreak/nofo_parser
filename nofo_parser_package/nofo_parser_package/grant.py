"""Funding opportunity and NOFO domain types."""

from dataclasses import dataclass
from datetime import datetime

from contact import ContactInfo
from lifecycle import FundingCycle, GrantStatus


@dataclass(frozen=True)
class Grant:
    """Core funding opportunity entity - represents a complete grant opportunity.

    This is the central domain entity shared across all scrapers. Each scraper
    uses their own validation logic to construct this entity, but the entity
    itself is scraper-agnostic.
    """

    # Identity
    opportunity_id: str  # Scraper-specific ID (e.g., 'dced-26', 'HHS-2024-001')
    opportunity_number: str  # Generic opportunity number
    url: str

    # Basic info
    title: str
    summary: str
    status: GrantStatus

    # Agency
    agency_name: str
    agency_code: str = ''
    contact: ContactInfo | None = None

    # Dates
    cycle: FundingCycle | None = None

    # NOFO
    pdf_url: str = ''
    additional_info_url: str = ''

    # Metadata
    date_info_updated: str | datetime | None = None
    version: str = ''
    source: str = ''  # e.g., 'pa.gov', 'grants.gov', 'texas.hhs.gov'
    source_geography_level: str = ''  # e.g., 'state', 'federal', 'local'
    source_geography_state_abbr: str = ''  # e.g., 'PA', 'TX', 'CA'

    def to_dict(self) -> dict:
        """Convert to dictionary format for database storage.

        This bridges between domain objects and database layer.
        """
        result = {
            'grants_gov_id': self.opportunity_id,
            'opportunity_number': self.opportunity_number,
            'url': self.url,
            'title': self.title,
            'summary': self.summary,
            'grant_status': self.status.value,
            'agency_name': self.agency_name,
            'agency_code': self.agency_code,
            'pdf_url': self.pdf_url,
            'additional_info_url': self.additional_info_url,
            'date_info_updated': self.date_info_updated,
            'grant_version': self.version,
            'grant_source': self.source,
            'source_geography_level': self.source_geography_level,
            'source_geography_state_abbr': self.source_geography_state_abbr,
        }

        # Add contact info if available
        if self.contact:
            result['agency_contact_name'] = self.contact.name
            result['agency_contact_email'] = self.contact.email
            result['agency_contact_phone'] = self.contact.phone

        # Add cycle dates if available
        if self.cycle:
            result['posted_date'] = self.cycle.posted_date
            result['due_date'] = self.cycle.due_date
            result['open_date'] = self.cycle.open_date

        return result

    @classmethod
    def from_dict(cls, data: dict) -> 'Grant':
        """Create Grant from dictionary (e.g., from database).

        This bridges between database output and domain objects.
        """
        # Extract opportunity ID
        opportunity_id = data.get('grants_gov_id', '')

        # Parse status
        status_str = data.get('grant_status', '')
        try:
            status = GrantStatus(status_str)
        except ValueError:
            # Fallback for unknown statuses
            status = GrantStatus.POSTED

        # Extract contact info if available
        contact = None
        if any(data.get(f'agency_contact_{field}') for field in ['name', 'email', 'phone']):
            contact = ContactInfo(
                name=data.get('agency_contact_name', ''),
                email=data.get('agency_contact_email', ''),
                phone=data.get('agency_contact_phone', ''),
            )

        # Extract funding cycle if dates available
        cycle = None
        if any(data.get(field) for field in ['posted_date', 'due_date', 'open_date']):
            cycle = FundingCycle(
                posted_date=data.get('posted_date'),
                due_date=data.get('due_date'),
                open_date=data.get('open_date'),
            )

        return cls(
            opportunity_id=opportunity_id,
            opportunity_number=data.get('opportunity_number', ''),
            url=data.get('url', ''),
            title=data.get('title', ''),
            summary=data.get('summary', ''),
            status=status,
            agency_name=data.get('agency_name', ''),
            agency_code=data.get('agency_code', ''),
            contact=contact,
            cycle=cycle,
            pdf_url=data.get('pdf_url', ''),
            additional_info_url=data.get('additional_info_url', ''),
            date_info_updated=data.get('date_info_updated'),
            version=data.get('grant_version', ''),
            source=data.get('grant_source', ''),
            source_geography_level=data.get('source_geography_level', ''),
            source_geography_state_abbr=data.get('source_geography_state_abbr', ''),
        )
