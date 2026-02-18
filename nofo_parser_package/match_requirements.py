# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

prompt = r"""
    # Directive:
    For the attached file, determine if cost sharing or matching funds is required. If either is required, summarize the requirement information, including amounts or percentages. Do NOT guess or make up an answer. In the RARE case the information is not present, return 'Information is not available'.

    # Examples:
    Input:
    Cost Sharing or Matching Considerations
    There is no cost sharing or matching required for this grant.
    Output:
    {
        "match_requirements": {
            "requires_match": false,
            "match_info": null
        }
    }
    Input:
    C. Cost-Sharing or Matching Funds
    No cost-sharing or matching is required as a condition of eligibility under this NOFO.
    Output:
    {
        "match_requirements": {
            "requires_match": false,
            "match_info": null
        }
    }
    Input:
    1. a. Cost Sharing or Matching: Under standards can meet WWC standards
    ESEA.
    section 4623(d)(1)(A) of the ESEA, to be without reservations, meet WWC
    An applicant should review the
    eligible for a grant under this standards with reservations, or not meet
    Department’s cost-sharing and cost
    competition, an applicant must WWC standards. WWC practice guides
    matching regulations, which include
    demonstrate a commitment from one or and intervention reports include
    specific limitations, in 2 CFR 200.306,
    more entities in the public or private findings from systematic reviews of
    and the cost principles regarding
    sector, which may include Federal, evidence as described in the WWC
    donations, capital assets, depreciations,
    State, and local public agencies, Handbooks documentation.
    and allowable costs, in subpart E of 2
    philanthropic organizations, and private Note: The What Works Clearinghouse
    CFR part 200.
    sources, to provide matching funds. Procedures and Standards Handbook
    b. Indirect Cost Rate Information: This An applicant proposing a project that
    (Version 4.1), as well as the more recent
    program uses an unrestricted indirect meets Absolute Priority 1—Non-Rural
    What Works Clearinghouse Handbooks
    cost rate. For more information and Non-Tribal Communities must
    released in August 2022 (Version 5.0),
    regarding indirect costs, or to obtain a obtain matching funds or in-kind
    are available at https://ies.ed.gov/ncee/
    negotiated indirect cost rate, please see donations equal to at least 100 percent
    wwc/Handbooks.
    https://www2.ed.gov/about/offices/list/ of its grant award. Section 4623(d)(1)(A)
    10. Program Authority and Applicable
    ocfo/intro.html. of the ESEA.
    Regulations:
    c. Administrative Cost Limitation: An applicant proposing a project that Program authority: 20 U.S.C. 7273–
    This program does not include any meets Absolute Priority 2—Rural 7274.
    program-specific limitation on Applicable regulations: (a) The Applicants or Absolute Priority 3—
    administrative expenses. All Education Department General Tribal Communities must obtain
    administrative expenses must be Administrative Regulations (EDGAR) in matching funds or in-kind donations
    reasonable and necessary and conform 34 CFR parts 75, 77, 79, 81, 82, 84, 86, equal to at least 50 percent of its grant
    to Cost Principles described in 2 CFR 97, 98, and 99. (b) The Office of award. Section 4623(d)(1)(C) of the
    part 200 subpart E. Management and Budget (OMB) ESEA.
    2. Subgrantees: The grantee may Eligible sources of matching funds Guidelines to Agencies on
    award subgrants to entities it has include sources of funds used to pay for Governmentwide Debarment and
    identified in an approved application or solutions within the pipeline services, Suspension (Nonprocurement) in 2 CFR
    that it selects through a competition initiatives supported by the LEA, or part 180, as adopted and amended as
    under procedures established by the public health services for children in regulations of the Department in 2 CFR
    grantee. the neighborhood. At least 10 percent of part 3485. (c) The Guidance for Federal
    an applicant’s total match must be cash Financial Assistance in 2 CFR part 200,
    III. Application and Submission
    or in-kind contributions from the as adopted and amended as regulations
    Information
    private sector, which may include of the Department in 2 CFR part 3474.
    1. Recommended Page Limit: The philanthropic organizations or private (d) The PN NFP. (e) The 2011 PN NFP.
    1SECITON application narrative is where you, the sources. Section 4623(d)(1)(B) of the (f) The Administrative Priorities. (g) The
    applicant, address the selection criteria ESEA. Supplemental Priorities.
    that reviewers use to evaluate your Applicants must demonstrate a Note: The regulations in 34 CFR part
    htiw
    application. We recommend that you (1) commitment of matching funds in the 79 apply to all applicants except
    DORP32NQX11KSD
    limit the application narrative to no application. Applicants must specify the federally recognized Indian Tribes.
    more than 50 pages and (2) use the source of the funds or contributions Note: The regulations in 34 CFR part
    following standards: and, in the case of a third-party in-kind 86 apply to IHEs only.
    no
    rettol
    VerDate Sep<11>2014 20:13 Jun 26, 2024 Jkt 262001 PO 00000 Frm 00020 Fmt 4703 Sfmt 4703 E:\FR\FM\27JNN1.SGM 27JNN1
    Output:
    {
        "match_requirements": {
            "requires_match": true,
            "match_info": "For projects meeting Absolute Priority 1: Non-Rural and Non-Tribal Communities, applicants must obtain matching funds or in-kind donations equal to at least 100 percent of the grant award. For projects meeting Absolute Priority 2: Rural Applicants or Absolute Priority 3: Tribal Communities, applicants must obtain matching funds or in-kind donations equal to at least 50 percent of the grant award. At least 10 percent of an applicant's total match must be cash or in-kind contributions from the private sector, which may include philanthropic organizations or private sources. The Secretary may consider decreasing the matching requirement in exceptional circumstances, on a case-by-case basis."
        }
    }
    Input:
    5.4 COST SHARING MATCHING REQUIREMENTS OR
    There is no match requirement for this grant program.
    Output:
    {
        "match_requirements": {
            "requires_match": false,
            "match_info": null
        }
    }

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with a match_requirements field containing an object with the following fields:
        * requires_match (boolean)
        * match_info (text or null)
"""
