# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

prompt = """
    # Directive:
    For the attached file, extract the award ceiling or award ceilings strings. If award ceiling is specified for a certain period of time, but the project allows multiple periods of that time, calculate that total. For example, if an award ceiling is $500,000 for a single budget period of 12 months and the period of performance is 2 years, the total award ceiling is $1,000,000. If there are multiple award ceilings (for example, different award ceilings for different tracks), include each of the award ceilings separated by semicolons (ex. "Track 1: $20 million; Track 2: $3 million"). Also store the award ceiling as a number and store the number of awards as a number. If there are multiple award ceilings, pick the award ceiling number and number of awards associated with the highest award ceiling. If there is an ambiguous number of awards, such as "multiple", return null. Do NOT guess or make up an answer. In the RARE case no award ceiling information is present, return 'Information is not available'.

    # Examples:
    Input:
    --- PDF Page 9 ---
    Bonus Points
    Applications may receive up to nine total bonus points based on the following criteria:
    • Up to three bonus points may be awarded to proposals that are particularly data driven;
    • Up to three bonus points may be awarded to proposals that have never received a PTIG;
    • Up to three bonus points may be awarded to proposals that approach solutions from a
    human-centered design (HCD) perspective.
    Eligibility
    Any eligible entity that received a PTIG award in either of the last two fiscal years (FY 2023 or FY
    is ineligible to apply 2024) and receive a PTIG this fiscal year (FY 2025). This restriction only
    applies to the lead entity on the award (i.e., the recipient whose name appears in block 9 of the
    awarded project’s FNS-529) and not to partner organizations or government agencies on a
    particular project. See section on Eligible Applicants for more information.
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
    Please note:
    • Grant awards are subject to the availability of funding and/or appropriations of funds.
    • FNS reserves the right to use this RFA and results of this competition to award additional
    grants this or the subsequent fiscal year, should additional funds become available.
    Allowable Costs
    • Funds from this RFA are for new projects only. New projects may be an enhancement upon
    an existing PTIG project but must contain new project activities and outcomes.
    • Equipment and Supplies: Expenditures for equipment (i.e., items of personal property
    having a useful life of more than one year and a cost of $10,000 or more) are allowable
    expenses with prior approval by FNS. FNS reserves the right to approve/disapprove these
    expenditures based on needs as expressed by the proposed project. Supplies do not
    require a separate specific prior approval outside of the budget/proposal approval
    process.
    • If the activities funded under this grant are part of a larger eligibility system project with
    total projected costs exceeding $6 million, the applicant must submit, and FNS must
    approve, an Advance Planning Document (APD) prior to the expenditure of these grant
    funds. Guidance on the APD process is available at www.fns.usda.gov/apd/.
    Output:
    {
        "award_ceiling": {
            "award_ceiling_string": "$2,000,000",
            "award_ceiling_int": 2000000,
            "num_awards": 12
        }
    }
    Input:
    --- PDF Page 25 ---
    Section II. Federal Award Information
    (back to the Table of Contents)
    A. Number and Amount of Awards
    EPA anticipates awarding approximately $2 billion in funding through this NOFO depending on funding
    availability, quality of applications received, EPA priorities, and other applicable considerations. Awards
    under Track I are expected to be between $10-20 million each and cannot exceed $20 million. Awards under Track
    II are expected to be between $1-3 million each and cannot exceed $3 million. EPA expects to award approximately
    $1.96 billion for about 150 Track I awards, including those under the Target Investment Areas described below in
    B, and approximately $40 million for about 20 Track II awards. These amounts are estimates only, and EPA
    reserves the right to increase or decrease the total number of awards and funding amounts for each Track
    contingent on the quality of applications received, the amount of funds awarded to selected applicants,
    budget availability, and / or agency priorities and programmatic considerations. In addition, given that
    workforce development programs as described in Section I.G can be significant to achieving environmental
    and climate justice in many communities, EPA anticipates making a minimum of fifteen awards for high-
    ranking applications that include a workforce training program(s) as further described in Section V.E.
    Output:
    {
        "award_ceiling": {
            "award_ceiling_string": "Track 1: $20 million; Track 2: $3 million",
            "award_ceiling_int": 2000000,
            "num_awards": 150
        }
    }
    Input:
    Estimated Range of Awards: $400,000 4. Background: A Promise
    greatest increase has been in
    to $500,000. Neighborhood is a place-based,
    kindergarten, with the rate of chronic
    Estimated Average Size of Awards:
    collective impact approach to improving absenteeism now as high as 40 percent
    $450,000.
    results for children and families. The in some communities.2Research
    Maximum Award: We will not make
    transformative vision of the Promise suggests that children who are
    an award exceeding $500,000 for a
    Neighborhoods initiative is that all chronically absent for multiple years
    single budget period of 12 months. The
    children and youth growing up in between preschool and second grade are
    Department plans to fully fund awards
    Promise Neighborhoods have access to much less likely to read at grade level
    made under this notice with FY 2024
    great schools and strong systems of
    funds.
    1SECITON family and community support. Promise
    1Dee, T. S. (2023, August 10). Higher Chronic Estimated Number of Awards: 4–5.
    Neighborhoods weave together people, Absenteeism Threatens Academic Recovery from
    Note: The Department is not bound by any services, and organizations to create a the COVID–19 Pandemic. https://doi.org/10.31219/
    htiw estimates in this notice.
    osf.io/bfg3p. seamless cradle-to-career pipeline, along
    DORP32NQX11KSD 2https://edsource.org/2023/reaching-
    which community members have access Project Period: Up to 24 months.
    Output:
    {
        "award_ceiling": {
            "award_ceiling_string": "$1,000,000 over 24 months",
            "award_ceiling_int": 1000000,
            "num_awards": 5
        }
    }
    Input:
    [Start Table 1]
    Grant Name:	Supplemental Nutrition Assistance Program
    Education (SNAP-Ed)
    RFA No.:	HHS0015831
    Deadline for Submission of
    Applications:	June 2, 2025 by 10:30 a.m. Central Time
    Deadline for Submitting Questions
    or Requests for Clarifications:	May 12, 2025 by 5:00 p.m. Central Time
    Estimated Total Available Funding:	$124,618,585.00
    Estimated Total Number of
    Awards:	Multiple
    Estimated Max Award Amount:	$24,923,717.00 per Federal Fiscal Year
    Anticipated Project Start Date:	October 1, 2026
    [End Table 1]
    PCS 560 HHS RFA Template RFA No. HHS0015831 Page 5 of 42
    Version 1.70
    Revision Date 11/13/2024

    --- PDF Page 6 ---
    [Start Table 1]
    Length of Project Period:	Five (5) years
    Eligible Applicants:	To be eligible for a grant award, all Applicants
    must be qualified to do business in Texas and
    meet the requirements in Section III. Applicant
    Eligibility Requirements
    [End Table 1]
    Output:
    {
        "award_ceiling": {
            "award_ceiling_string": "$124,618,585.00 over 5 years",
            "award_ceiling_int": 124618585,
            "num_awards": null
        }
    }

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with an award_ceiling field containing an object with the following feilds:
        * award_ceiling_string (text)
        * award_ceiling_int (integer)
        * num_awards (integer or null)
"""
