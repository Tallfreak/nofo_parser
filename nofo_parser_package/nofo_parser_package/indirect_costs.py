# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

prompt = r"""
    # Directive:
    For the attached file, determine if indirect costs are allowed. If indirect costs are allowed, summarize indirect cost information, such as how they are treated or calculated. Do NOT guess or make up an answer. In the RARE case the information is not present, return 'Information is not available'.

    # Examples:
    Input:
    --- PDF Page 15 ---
    match those listed on the SF-424A form. The budget table must be formatted to fit on an 8.5 x
    11-inch page, with a font no smaller than 11-point Times New Roman. All funding requests must
    be in whole dollars.
    Indirect Cost Rate
    Negotiated Indirect Cost Rate Agreement (NICRA), A current negotiated with a cognizant
    Federal agency, should be used to charge indirect costs. Indirect costs may not exceed the
    negotiated rate. If a NICRA is used, the percentage and base should be indicated. If the
    applicant does not have a current Federal negotiated indirect cost rate (including provisional
    rate) they may elect to charge a de minimis rate of up to 15 percent of modified total direct costs
    (MTDC). In this instance, the applicant must indicate they are requesting the de minimis rate. An
    applicant may elect not to charge indirect costs and instead use all grant funds for direct costs.
    If indirect costs are not charged, the phrase “none requested” should be stated in the budget
    narrative. For questions related to the indirect cost rate, please work with the Federal Awarding
    Agency Contact.
    Note: Each organization is assigned to a single federal agency (by the Office of Management and
    [Start Table 1]
    Budget) that acts on behalf of all federal agencies in indirect cost rate negotiations and is referred
    to as the “cognizant agency.”
    [End Table 1]
    to as the “cognizant agency.”
    Output:
    {
        "indirect_costs": {
            "allowed": true,
            "info": "Indirect costs are allowed. Applicants should use a current Negotiated Indirect Cost Rate Agreement (NICRA), negotiated with a cognizant Federal agency, to charge indirect costs. Indirect costs may not exceed the negotiated rate. If a NICRA is used, the percentage and base should be indicated, and a copy of the approved NICRA must be provided with the application. If the applicant does not have a current Federal negotiated indirect cost rate, they may elect to charge a de minimis rate of up to 15 percent of modified total direct costs (MTDC). Applicants may also elect not to charge indirect costs, in which case 'none requested' should be stated in the budget narrative."
        }
    }
    Input:
    Indirect Costs
    If indirect costs are budgeted, indicate the approved rate and distribution base. Indirect costs are those
    incurred by the grantee for a common or joint purpose that benefit more than one cost objective or project
    and are not readily assignable to specific cost objectives or projects as a direct cost. Indirect costs must be
    based on a rate approved by the applicant’s cognizant federal agency, or the 10%% de-minimus rate
    Indirect Cost Guidance authorized by 2 CFR § 200.414(f). Additional indirect cost guidance is available in
    for Recipients of EPA Assistance Agreements and in Section VI.u, “IDC Competition Clause,” of the EPA
    Solicitation Clauses.
    Notwithstanding this, indirect costs have been capped as described below based on a deviation approved
    per 2 CFR 200.414:
    Limitation on indirect costs for grants and cooperative agreements
    a. In general: Except as otherwise provided by statute, indirect costs charged against any grant and /
    or cooperative agreement awarded under this NOFO shall not exceed 20 percent of the total amount
    of the federal award.
    b. Exception: Subsections (a) and (c) shall not apply to Indian Tribes as defined in section 302(r) of
    the Clean Air Act who serve in the role of direct recipient and / or subrecipient under the program
    or to Intertribal consortia that meet the requirements of 40 CFR 35.504(a) and (c) even if the
    Intertribal consortia is eligible for funding as a Community Based Nonprofit Organization.
    c. Treatment of subawards: In the case of a grant and / or cooperative agreement described in
    subsection (a), the limitation on indirect costs specified in such subsection shall be applied to both
    the initial direct assistance award amount and any subaward of the federal funds provided under
    the initial assistance award so that the total of all indirect costs charged to each of the federal awards
    (i.e., both the initial direct assistance award amount and any subawards) funded under the initial
    assistance award does not exceed such limitation. As provided in 2 CFR 200.332(a)(2) pass-through
    entities are responsible for ensuring compliance with the indirect cost limitation by their
    subrecipients.
    Note: This limit does not extend to indirect costs on procurement contracts.
    Output:
    {
        "indirect_costs": {
            "allowed": true,
            "info": "Indirect costs are allowed under this NOFO, but are subject to a 20%% cap. Indirect costs must be based on a rate approved by the applicant's cognizant federal agency, or the 10%% de minimis rate authorized by 2 CFR 200.414(f)."
        }
    }
    Input:
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
    Output:
    {
        "indirect_costs": {
            "allowed": true,
            "info": "Unrestricted."
        }
    }
    Input:
    6.4 INDIRECT COSTS
    Applicants must have an approved Indirect Cost rate (ICR) or request the de minimis rate
    to recover Indirect Costs. All Applicants are required to complete and submit Form E,
    with the required Texas HHS System Indirect Costs Rate (ICR) Questionnaire,
    supporting documentation. The questionnaire initiates the acknowledgment or approval of
    an ICR for use with HHSC cost-reimbursable Contracts. Entities declining the use of
    Indirect Cost cannot recover Indirect Costs on any HHSC award or use unrecovered
    Indirect Costs as Match.
    HHSC typically accepts the following approved ICRs:
    A. Federally Approved Indirect Cost Rate Agreement; and
    B. State of Texas Approved Indirect Cost Rate
    HHSC, at its discretion, may request additional information to support any approved ICR
    agreement.
    If the Applicant does not have an approved ICR agreement, the Applicant may be eligible
    for the 15% de minimis rate or may request to negotiate an ICR with HHSC.
    For Applicants requesting to negotiate an ICR with HHSC, the ICR Proposal Package will
    be provided by the HHS Federal Funds Indirect Cost Rate Group to successful Grantees.
    The ICR Proposal Package must be completed and returned to the HHS Federal Funds
    Indirect Cost Rate Group no later than three (3) months Post-Award.
    The HHS Federal Funds Indirect Cost Rate group will contact applicable Grantees after
    Grant Agreement execution to initiate and complete the ICR process. Grantees must
    respond within 30 Calendar Days, or the request will be cancelled, and Indirect Costs may
    be disallowed.
    Once HHSC acknowledges an existing rate or approves an ICR, the Grantee will receive
    one of the three Indirect Cost approval letters: ICR Acknowledgement Letter, ICR
    Acknowledgement Letter – Fifteen Percent De Minimis, or the ICR Agreement Letter.
    If an Indirect Cost Rate Letter is required but it is not issued at the time of Grant Agreement
    execution, the Grant Agreement will be amended to include the Indirect Cost Rate Letter
    after the ICR Letter is issued.
    PCS 560 HHS RFA Template RFA No. HHS0015831 Page 20 of 42
    Version 1.70
    Revision Date 11/13/2024

    --- PDF Page 21 ---
    Approval or acceptance of an ICR will not result in an increase in the amount awarded or
    affect the agreed-upon service or performance levels throughout the life of the award.
    6.5 ADMINISTRATIVE APPLICANT INFORMATION
    Using through attached to this RFA, Applicant must provide Forms A, Form B-2,
    satisfactory evidence of its ability as an organization to manage and coordinate the types
    of activities described in this RFA. should include the Form A, Applicant Information
    supporting documentation in Requirements, to prove Section 3.2, Application Screening
    that the Applicant meets the criteria.
    Output:
    {
        "indirect_costs": {
            "allowed": true,
            "info": "Applicants must have an approved Indirect Cost rate (ICR) or request the de minimis rate to recover Indirect Costs. All Applicants are required to complete and submit Form E, Texas HHS System Indirect Costs Rate (ICR) Questionnaire, with supporting documentation. HHSC typically accepts Federally Approved Indirect Cost Rate Agreements or State of Texas Approved Indirect Cost Rates. If the Applicant does not have an approved ICR, they may be eligible for the 15%% de minimis rate or may request to negotiate an ICR with HHSC. Approval or acceptance of an ICR will not result in an increase in the amount awarded or affect the agreed-upon service or performance levels throughout the life of the award."
        }
    }

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with an indirect_costs field containing an object with the following fields:
        * allowed (boolean)
        * info (text or null)
"""
