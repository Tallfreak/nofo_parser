# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

prompt = r"""
    # Directive:
    For the attached file, extract the contact information for the grant, including the contact name, the contact email, and the contact phone, if available. Do NOT guess or make up an answer. If contact information is not present, return 'Information is not available'.

    # Examples:
    Input:
    Contact Information
    For more information, contact the eGrants help desk at eGrants@gov.texas.gov or (512) 463-1919.
    Output:
    {
        "contact_info": {
            "agency_contact_name": "eGrants help desk",
            "agency_contact_email": "eGrants@gov.texas.gov",
            "agency_contact_phone": "(512) 463-1919"
        }
    }
    Input:
    Contact Information
    If additional information is needed concerning the grant program, contact the Texas Music Office at music@gov.texas.gov.
    Output:
    {
        "contact_info": {
            "agency_contact_name": "Texas Music Office",
            "agency_contact_email": "music@gov.texas.gov",
            "agency_contact_phone": null
        }
    }
    Input:
    G. Agency Contacts
    If you have questions about the program, contact:
    Division of Research Programs
    National Endowment for the Humanities

    20241127-FZ 23
    400 Seventh Street, SW
    Washington, DC 20506
    202-606-8200
    publicscholar@neh.gov
    If you have questions about administrative requirements contact:
    Office of Grant Management
    National Endowment for the Humanities
    400 Seventh Street, SW
    Washington, DC 20506
    202-606-8494
    grantmanagement@neh.gov
    If you are deaf or hard of hearing, you can contact NEH using telecommunications relay at 7-1-1.
    If you have questions about registering or renewing your registration with login.gov or SAM.gov,
    contact the Federal Service Desk, Monday – Friday, 8:00 a.m. to 8:00 p.m. Eastern Time, at:
    Federal Service Desk
    U.S. calls: 866-606-8220
    International calls: +1 334-206-7828
    For assistance in registering with or submitting your application through Grants.gov:
    Grants.gov Applicant Support
    Telephone: 1-800-518-4726
    International Calls: +1-606-545-5035
    support@grants.gov
    Always obtain a case number when calling for support.
    Output:
    {
        "contact_info": {
            "agency_contact_name": "Division of Research Programs National Endowment for the Humanities",
            "agency_contact_email": "publicscholar@neh.gov",
            "agency_contact_phone": "202-606-8200"
        }
    }
    Input:
    Contact Information
    Agency Contact Description
    For technical assistance with submitting the SF-424, please call the Grants.gov customer service hotline
    at 800-518-4726, send questions via email to support@Grants.gov, or consult the Grants.gov
    Organization Applicant User Guide. The Grants.gov Support Hotline operates 24 hours a day, 7 days a
    week, except on federal holidays.

    2 of 35

    For technical support with the Justice Grants System (JustGrants) application, please contact JustGrants
    Support at JustGrants.Support@usdoj.gov or 833-872-5175. JustGrants Support operates Monday
    through Friday between the hours of 5:00 a.m. and 9:00 p.m. Eastern Time (ET) and Saturday, Sunday,
    and federal holidays from 9:00 a.m. to 5:00 p.m. ET. Training on JustGrants can also be found at
    https://justicegrants.usdoj.gov/training-resources.
    For programmatic assistance with the requirements of this program, please call the COPS Office
    Response Center at 800-421-6770 or send questions via email to AskCopsRC@usdoj.gov. The COPS
    Office Response Center operates Monday through Friday, 9:00 a.m. to 5:00 p.m. ET, except on federal
    holidays. In addition, the COPS Office welcomes applicant feedback on this notice of funding
    opportunity, the application submission process, and the application review process. Provide feedback
    via email to AskCopsRC@usdoj.gov (Subject line: “FY25 CHP Feedback”).
    Output:
    {
        "contact_info": {
            "agency_contact_name": "COPS Office Response Center",
            "agency_contact_email": "AskCopsRC@usdoj.gov",
            "agency_contact_phone": "800-421-6770"
        }
    }

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with an contact_info field containing an object with the following feilds:
        * agency_contact_name (text)
        * agency_contact_email (text)
        * agency_contact_phone (text)
"""
