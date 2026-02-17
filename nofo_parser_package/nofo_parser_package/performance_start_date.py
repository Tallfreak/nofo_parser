# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

prompt = r"""
    # Directive:
    For the attached file, extract the expected start date of the award/project. Do NOT guess or make up an answer. In the RARE case the information is not present, return 'Information is not available'.

    # Examples:
    Input:
    2. FEDERAL AWARD INFORMATION
    The following information provides applicants with information to help make informed decisions
    about proposal submissions.
    • Total amount of funding expected to award: $5,000,000
    • Anticipated number of awards: Not to exceed 12 awards
    • Minimum award amount (award floor): $20,000
    • Maximum award amount (award ceiling): $2,000,000
    • Anticipated award announcement date: September 2025
    • Anticipated period of performance: September 2025 through September 2028
    • Application due date: August 6, 2025; 11:59 PM, Eastern Daylight Time
    Output:
    {
        "performance_start_date": {
            "date_string": "September 2025",
            "date": "2025-09-01"
        }

    }
    Input:
    DATES: IMPORTANT
    November 21, 2023 NOFO Opening Date
    November 21, 2024 Application Closing Date
    April 2024 Anticipated Initial Award Selections
    June 2024 Anticipated Start of Period of Performance for Initial
    Output:
    {
        "performance_start_date": {
            "date_string": "June 2024",
            "date": "2024-06-01"
        }
    }
    Input:
    7.1 SCHEDULE EVENTS OF
    [Start Table 1]
    EVENT	DATE/TIME
    Funding Announcement Posting Date
    Posted to HHS Open Grant
    Opportunities (RFA) website.	May 1, 2025
    [End Table 1]
    PCS 560 HHS RFA Template RFA No. HHS0015831 Page 21 of 42
    Version 1.70
    Revision Date 11/13/2024

    --- PDF Page 22 ---
    [Start Table 1]

    Applicant Conference
    Attendance is Optional	May 7, 2025 at 11:00 a.m. Central Time
    Deadline for Submitting Questions or
    Requests for Clarification	May 12, 2025 by 5:00 p.m. Central Time
    Tentative Date Answers to Questions
    or Requests for Clarification Posted	May 16, 2025 by 5:00 p.m. Central Time
    Deadline for Submission of
    Applications
    NOTE: To be considered compliant
    and eligible, Applications must be
    RECEIVED by HHSC by this
    deadline if not changed by
    subsequent Addenda.	June 2, 2025 by 10:30 a.m. Central
    Time
    Anticipated Notice of Award	May 2026
    Anticipated Project Start Date	October 2026
    [End Table 1]
    Output:
    {
        "performance_start_date": {
            "date_string": "October 2026",
            "date": "2026-10-01"
        }
    }

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with a performance_start_date field containing an object with the following fields:
        * date_string (text)
        * date (YYYY-MM-DD)
"""
