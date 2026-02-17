# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

prompt = r"""
    # Directive:
    For the attached file, extract key dates such as deadlines (e.g., for letters of intent, pre-applications, etc.), notice of selection, etc. If a key date is an optional deadline, note that it is optional. Do NOT guess or make up an answer. In the RARE case the information is not present, return ''.

    # Examples:
    Input:
    --- PDF Page 1 ---
    OMB Number: 0584-0512
    Expiration Date: 07/31/2025
    Supplemental Nutrition Assistance Program (SNAP)
    Process and Technology Improvement Grants (PTIGs)
    Fiscal Year 2025 Request for Applications (RFA)
    Assistance Listing Number (ALN): 10.580
    July 7, 2025 Release Date:
    Application Due Date: August 6, 2025; 11:59 PM, Eastern Daylight
    Time
    Anticipated Award Date: September 2025
    Output:
    {
        "key_dates": [
            {
            "description": "Release date",
            "date_string": "July 7, 2025",
            "date": "2025-07-07"
            },
            {
                "description": "Application due date",
                "date_string": "August 6, 2025; 11:59 PM, Eastern Daylight Time",
                "date": "2025-08-06"
            },
            {
                "description": "Anticipated award announcement date",
                "date_string": "September 2025",
                "date": "2025-09-01"
            }
        ]
    }
    Input:
    DATES: IMPORTANT
    November 21, 2023 NOFO Opening Date
    November 21, 2024 Application Closing Date
    April 2024 Anticipated Initial Award Selections
    June 2024 Anticipated Start of Period of Performance for Initial
    Selections
    DEADLINE: Application packages will be accepted on a rolling basis, as further explained in the NOFO,
    until November 21, 2024, at 11:59 PM (Eastern Time) through Grants.gov. Applications received after the
    closing date and time will not be considered for funding.
    In alignment with EPA’s commitment to conducting business in an open and transparent manner, copies of
    applications selected for award under this NOFO may, as appropriate, be made publicly available on the
    OEJECR website or other public website for a period after the selected applications are announced.
    Therefore, applicants should clearly indicate which portion(s) of the application, if any, they are claiming
    contains confidential, privileged, or sensitive information. As provided at 40 CFR § 2.203(b), if no claim
    of confidential treatment accompanies the information when it is received by EPA, it may be made available
    to the public by EPA without further notice to the applicant.
    Output:
    {
        "key_dates": [
            {
                "description": "NOFO Opening Date",
                "date_string": "November 21, 2023",
                "date": "2023-11-21"
            },
            {
                "description": "Application Closing Date",
                "date_string": "November 21, 2024 at 11:59 PM (Eastern Time)",
                "date": "2024-11-21"
            },
            {
                "description": "Anticipated Initial Award Selections",
                "date_string": "April 2024",
                "date": "2024-04-01"
            },
            {
                "description": "Anticipated Start of Period of Performance for Initial Selections",
                "date_string": "June 2024",
                "date": "2024-06-01"
            }
        ],
    }
    Input:
    Average Burden per Response: 45 (Department) is issuing a notice inviting
    received without change, including any
    minutes. applications for fiscal year (FY) 2024 for
    personal identifiers or contact
    Frequency: On occasion.
    the PN program. information.
    Dated: June 20, 2024. DATES:
    FORFURTHERINFORMATIONCONTACT: To
    Aaron T. Siegel, Applications Available: June 27, 2024.
    request more information on this
    Deadline for Notice of Intent to Apply: Alternate OSD Federal Register Liaison
    proposed information collection or to
    July 29, 2024. Officer, Department of Defense.
    obtain a copy of the proposal and
    Date of Pre-Application Meetings: The [FR Doc. 2024–14073 Filed 6–26–24; 8:45 am]
    associated collection instruments,
    Department will hold pre-application
    BILLING CODE 6001–FR–P please write to the Naval Health
    meetings via webinar for prospective
    Research Center, 140 Sylvester Road,
    applicants. Detailed information
    San Diego, CA 92106, Dr. Kristen
    DEPARTMENT OF DEFENSE regarding pre-application webinars will
    Walter, (619) 540–4108.
    be provided on the PN website at
    SUPPLEMENTARYINFORMATION:
    Department of the Navy https://oese.ed.gov/offices/office-of-
    Title; Associated Form; and OMB
    discretionary-grants-support-services/ [Docket ID: USN–2024–HQ–0009]
    Number: Social Determinants of Health
    school-choice-improvement-programs/
    Study; OMB Control Number 0703–
    Proposed Collection; Comment promise-neighborhoods-pn/.
    SDOH.
    Deadline for Transmittal of Request
    Needs and Uses: Many service
    Application: September 10, 2024.
    members face adverse social AGENCY: Department of the Navy,
    Deadline for Intergovernmental
    determinants of health (SDOH), such as Department of Defense (DoD).
    Review: November 12, 2024.
    financial, housing, and food insecurity,
    ACTION: 60-Day information collection
    ADDRESSES: For the addresses for isolation or distance from others, and
    notice.

    2. Notice of Intent to Apply: The competition to receive an award that amended). Because we plan to make
    Department will be able to review grant over the course of the project period successful applications available to the
    applications more efficiently if we know may exceed the simplified acquisition public, you may wish to request
    the approximate number of applicants threshold (currently $250,000), under 2 confidentiality of business information.
    that intend to apply. Therefore, we CFR 200.206(a)(2) we must make a Consistent with Executive Order
    strongly encourage each potential judgment about your integrity, business 12600 (Predisclosure Notification
    applicant to notify us of their intent to ethics, and record of performance under Procedures for Confidential Commercial
    submit an application. To do so, please Federal awards—that is, the risk posed Information), please designate in your
    email the program contact person listed by you as an applicant—before we make application any information that you
    under FORFURTHERINFORMATION an award. In doing so, we must consider believe is exempt from disclosure under
    CONTACTwith the subject line ‘‘Intent to any information about you that is in the Exemption 4. In the appropriate
    Apply,’’ and include the applicant’s integrity and performance system Appendix section of your application,
    name and a contact person’s name and (currently referred to as the Federal under ’’Other Attachments Form,’’
    email address. Applicants that do not Awardee Performance and Integrity please list the page number or numbers
    submit a notice of intent to apply may Information System (FAPIIS)), on which we can find this information.
    still apply for funding; applicants that accessible through the System for For additional information please see 34
    do submit a notice of intent to apply are Award Management. You may review CFR 5.11(c).
    not bound to apply or bound by the and comment on any information about 6. Intergovernmental Review: This
    information provided. yourself that a Federal agency program is subject to Executive Order
    Output:
    {
        "key_dates": [
             {
                "description": "Applications available",
                "date_string": "June 27, 2024",
                "date": "2024-06-27"
            },
            {
                "description": "Deadline for Optional Notice of Intent to Apply",
                "date_string": "July 29, 2024",
                "date": "2024-07-29"
            },
            {
                "description": "Application due date",
                "date_string": "September 10, 2024",
                "date": "2024-09-10"
            },
    ]}
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
        "key_dates": [
            {
                "description": "Funding announcement posting date",
                "date_string": "May 1, 2025",
                "date": "2025-05-01"
            },
            {
                "description": "Applicant conference (attendance optional)",
                "date_string": "May 7, 2025 at 11:00 a.m. Central Time",
                "date": "2025-05-07"
            },
            {
                "description": "Deadline for submitting questions or requests for clarification",
                "date_string": "May 12, 2025 by 5:00 p.m. Central Time",
                "date": "2025-05-12"
            },
            {
                "description": "Tentative date answers to questions or requests for clarification posted",
                "date_string": "May 16, 2025 by 5:00 p.m. Central Time",
                "date": "2025-05-16"
            },
            {
                "description": "Deadline for submission of applications",
                "date_string": "June 2, 2025 by 10:30 a.m. Central Time",
                "date": "2025-06-02"
            },
            {
                "description": "Anticipated notice of award",
                "date_string": "May 2026",
                "date": "2026-05-01"
            },
            {
                "description": "Anticipated project start date",
                "date_string": "October 2026",
                "date": "2026-10-01"
            }

        ]
    }

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with a key_dates field containing an array of json objects with the following fields:
        * description (text)
        * date_string (text)
        * date (YYYY-MM-DD)
"""
