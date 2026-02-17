# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

# may need to add business logic
# make this more specific. eg. say something other than summaraize this information. explain what eligiblity criteria is more.

categories = ', '.join(
    [
        'non-profit organization',
        'institute of higher education',
        'school district',
        'local government entity',
        'state government entity',
        'council of governments',
        'public housing authority',
        'healthcare organization',
        'for-profit institution',
    ]
)

prompt = (
    """
    # Directive:
    For the attached file, extract the full eligibility criteria for applicants. Summarize the information. Do NOT guess or make up an answer. In the RARE case the information is not present, return 'Information is not available'. In addition, categorize the eligibility criteria into the following categories:"""
    + categories
    + """

    # Examples:
    Input:
    3. ELIGIBILITY INFORMATION
    Eligible Applicants
    [Start Table 1]

    The entities eligible to receive grants under this competition are:
    [End Table 1]
    The entities eligible to receive grants under this competition are:
    • SNAP;5 The 53 State agencies that administer
    • governments;6 State or local
    • Public and private agencies providing health or welfare services;
    • (ITOs);7 Indian Tribal Organizations
    • Public health or educational entities; and
    • Private non-profit entities such as community-based or faith-based organizations, food
    organizations.8 banks, or other emergency feeding
    a letter of Unless the applicant is a State agency submitting an application on its own,
    commitment or letter of endorsement from the relevant State SNAP agency must be included in
    the application package to be considered for funding.
    5 State agencies should have the necessary approvals of State officials (such as councils or legislatures) of
    funding prior to submitting the application. Applicants should also acknowledge in their application that
    they have obtained all necessary approvals for funding.
    6 State and local governments should have the necessary approvals of State officials (such as councils or
    legislatures) of funding prior to submitting the application. Applicants should also acknowledge in their
    application that they have obtained all necessary approvals for funding.
    7 If an ITO applies for a PTIG, they must apply in partnership with their SNAP State Agency and provide a
    letter of endorsement from their State SNAP agency. Alternatively, the State agency can apply for a PTIG
    project with an ITO, and the ITO would need to provide a letter of commitment.
    8 Non-profit organizations must submit a copy of the IRS Determination Letter, form 501(c)(3) or proof of
    application for exempt status under section 501(c)(3) of the Internal Revenue Code, and a list of their Board
    of Directors, if applicable. If any other non-profit status applies, i.e., 501©(4) please describe here. All
    corporations, including nonprofit corporations, must complete an AD-3030.
    10

    --- PDF Page 11 ---
    Ineligible Applicants
    FNS will deem entities that do not meet the eligibility definitions ineligible and remove them from
    competition without further consideration. In cases where an applicant is deemed nonresponsive
    for failing to submit required elements or documents associated with this RFA, they will be
    considered ineligible and removed from consideration.
    Additionally, any eligible entity that received a PTIG award in either of the last two fiscal years
    is ineligible to apply for (FY 2023 or FY 2024) and receive a PTIG this fiscal year (FY 2025). This
    restriction only applies to the lead entity on the award (i.e., the recipient whose name appears in
    block 9 of the awarded project’s FNS-529) and not to partner organizations or government
    agencies on a particular project.
    Output:
    {
        "eligibility_requirements": {
            "eligible": [
                "The 53 State agencies that administer SNAP",
                "State or local governments",
                "Public and private agencies providing health or welfare services",
                "Indian Tribal Organizations (ITOs) (must apply in partnership with their SNAP State Agency and provide a letter of endorsement from their State SNAP agency, or the State agency can apply with an ITO, and the ITO would need to provide a letter of commitment)",
                "Public health or educational entities",
                "Private non-profit entities such as community-based or faith-based organizations, food banks, or other emergency feeding organizations (must submit a copy of the IRS Determination Letter, form 501(c)(3) or proof of application for exempt status under section 501(c)(3) of the Internal Revenue Code, and a list of their Board of Directors, if applicable; all corporations, including nonprofit corporations, must complete an AD-3030)"
            ],
            "ineligible": [
                "Any eligible entity that received a PTIG award in either of the last two fiscal years (FY 2023 or FY 2024) as the lead entity (i.e., the recipient whose name appears in block 9 of the awarded project's FNS-529) is ineligible to apply for and receive a PTIG this fiscal year (FY 2025)"
            ],
            "eligible_categories": [
                "non-profit organization",
                "local government entity",
                "state government entity",
                "healthcare organization",
            ]
            }
    }
    Input:
    --- PDF Page 29 ---
    Section III. Eligibility Information
    (back to the Table of Contents)
    Note: Additional provisions that apply to this section of the NOFO can be found in the EPA Solicitation
    Clauses.
    A. Eligible Applicants
    Consistent with CAA §138(b)(3) and Assistance Listing 66.616, applicants eligible to apply and receive
    grants under this NOFO are (1) a partnership between two community-based nonprofit organizations
    (CBOs) as defined below, or (2) a partnership between a CBO and one of the following: a federally
    recognized Tribe, a local government, or an institution of higher education. These types of partnerships for
    eligibility purposes are known as Statutory Partnerships. Further eligibility requirements are described
    below.
    Community-Based Non-Profit Organization (CBO) 1.
    To qualify as a CBO for eligibility purposes, an organization must demonstrate that they are a “nonprofit
    organization” as defined at 2 CFR 200.1, which “means any corporation, trust, association, cooperative, or
    other organization that is operated mainly for scientific, educational, service, charitable, or similar purpose
    in the public interest and is not organized primarily for profit; and uses net proceeds to maintain, improve,
    or expand the operation of the organization.”
    Applicants must include documentation in their application demonstrating that they are a nonprofit
    organization by one of two ways: 1) a written determination by the Internal Revenue Service that they are
    exempt from taxation under Section 501 of the Internal Revenue Code, or 2) based on a written
    determination by the state, territory, commonwealth, Tribe, or other United States governmental entity in
    which they are located. This can be done, for example, by submitting a letter, certificate, or articles of
    incorporation from the state where the organization is located that recognizes them as a nonprofit
    organization. Nonprofit organizations described in Section 501I(4) of the Internal Revenue Code that
    engage in lobbying activities as defined in Section 3 of the Lobbying Disclosure Act of 1995 are not eligible
    to apply. Foreign non-profit organizations cannot qualify as a CBO for eligibility purposes.
    In addition to being considered a nonprofit organization, an organization must demonstrate that they are a
    public or private nonprofit organization that supports and / or represents a community and/or certain
    populations within a community through engagement, education, and other related services provided to
    individual community residents and community stakeholders. A “community,” for these purposes, can be
    characterized by a particular geographic area and / or by the relationships among members with similar
    interests and can be characterized as part of a local, regional, or national community where organizations
    are focused on the needs of urban, rural, and / or Tribal areas, farmworkers, displaced workers, children
    with high levels of lead, people with asthma, subsistence fishers, and other similar groups. For purposes of
    this NOFO, the CBO must have a geographic presence or connection in, or relationship with, the specified
    community that the projects are intended to benefit. For example, national or statewide CBOs must
    demonstrate the CBO’s connection to the community that will benefit from the grants.
    For the purposes of this NOFO, applicants that demonstrate that they are Alaska Native Nonprofit
    Organizations or Alaska Native Nonprofit Associations are considered CBOs. In addition, Intertribal
    Consortia may be able to qualify as CBOs if they meet the above requirements and 40 CFR 35.504(a) and
    (c). The for-profit Alaskan Native Corporations are not eligible under the CBO definition and therefore are
    unable to apply as CBOs.
    29

    --- PDF Page 30 ---
    Local Government (in partnership with a CBO) 2.
    The following units of government within a state, as defined by the regulations in 2 CFR 200.1, are eligible
    to enter a Statutory Partnership with a CBO:
    • County
    • Borough
    • Municipality
    • City
    • Town
    • Township
    • Parish
    • Local public authority, including any public housing agency under the United States Housing Act
    of 1937
    • Special district
    • School district
    • Intrastate district
    • Council of governments, whether incorporated as a nonprofit corporation under State law; and
    • Any other agency or instrumentality of a multi-, regional, or intra-State or local government.
    Federally Recognized Tribe (in partnership with a CBO) 3.
    For the purposes of eligibility for entering into a Statutory Partnership with a CBO, EPA uses the definition
    of “Indian Tribe” in §302I of the CAA which provides that the term “...means any Indian Tribe, band,
    nation, or other organized group or community, including any Alaska Native village, which is Federally
    recognized as eligible for the special programs and services provided by the United States to Indians
    because of their status as Indians.” Note that this definition does not include Alaskan Native Corporations
    or State-recognized Tribes.
    Institutions of Higher Education (in partnership with a CBO) 4.
    For the purposes of eligibility for entering into a Statutory Partnership with a CBO, the grant regulations at
    2 CFR 200.1 state that Institutions of Higher Education (IHEs) are defined at 20 U.S.C. § 1001.
    EPA also recognizes that it is important to engage all available minds to address the environmental and
    climate justice challenges the nation faces. Accordingly, EPA encourages Minority Serving Institutions
    (MSIs) to participate in the grants under this NOFO, including by partnering with a CBO.
    For purposes of this NOFO, the following are considered MSIs:
    1. Historically Black Colleges and Universities, as defined by the Higher Education Act (20 U.S.C. §
    1061(2)). A list of these schools can be found at Historically Black Colleges and Universities.
    2. Tribal Colleges and Universities (TCUs), as defined by the Higher Education Act (20 U.S.C. §
    1059c(b)(3) and (d)(1)). A list of these schools can be found at American Indian Tribally Controlled
    Colleges and Universities.
    3. Hispanic-Serving Institutions (HSIs), as defined by the Higher Education Act (20
    U.S.C. § 1101a(a)(5)). A list of these schools can be found at Hispanic-Serving Institutions.
    4. Asian American and Native American Pacific Islander-Serving Institutions; (AANAPISIs), as
    defined by the Higher Education Act (20 U.S.C. § 1059g(b)(2)). A list of these schools can be
    30

    --- PDF Page 31 ---
    found at Asian American and Native American Pacific Islander-Serving Institutions.
    5. Predominantly Black Institutions (PBIs), as defined by the Higher Education Act of 2008, 20
    U.S.C. § 1059e(b)(6). A list of these schools can be found at Predominantly Black Institutions.
    Output:
    {
        "eligibility_requirements": {
            "eligible": [
                "A partnership between two community-based nonprofit organizations (CBOs)",
                "A partnership between a community-based nonprofit organization (CBO) and a federally recognized Tribe",
                "A partnership between a community-based nonprofit organization (CBO) and a local government",
                "A partnership between a community-based nonprofit organization (CBO) and an institution of higher education (including Minority Serving Institutions)",
            ],
            “ineligible": [],
            "eligible_categories": [
                "non-profit organization",
                "institute of higher education",
                "local government entity",
            ]
        }
    }
    Input:
    3. Eligible Applicants: Under section Telephone: (202)453–6709. Email: and career success.
    4622 of the ESEA, an eligible entity PromiseNeighborhoods@ed.gov.
    The PN program’s successes in
    must be one of the following: If you are deaf, hard of hearing, or
    helping communities respond to the
    (a) An institution of higher education have a speech disability and wish to
    COVID–19 pandemic highlight the
    (IHE), as defined in section 102 of the access telecommunications relay
    importance of ensuring place-based
    Higher Education Act of 1965, as services, please dial 7–1–1.
    supports for children and families.
    amended (HEA) (20 U.S.C. 1002); SUPPLEMENTARYINFORMATION:
    When the pandemic hit, Promise
    (b) An Indian Tribe or Tribal
    Neighborhoods became an important Full Text of Announcement
    organization, as defined in section 4 of
    source of funding for local governments
    the Indian Self-Determination and I. Funding Opportunity Description
    to quickly respond to community needs
    Education Assistance Act (25 U.S.C.
    1. Purpose of Program: The PN and have confidence that available
    5304); or
    program is authorized under the resources would benefit the hardest hit
    (c) One or more nonprofit entities
    Elementary and Secondary Education community members.
    working in formal partnership with not
    Act of 1965, as amended (ESEA). The
    less than one of the following entities: Promise Neighborhoods is
    purpose of the PN program is to (i) A high-need local educational
    particularly apt for addressing issues
    significantly improve the academic and agency (LEA).
    that worsened during the pandemic,
    developmental outcomes of children (ii) An IHE, as defined in section 102
    such as chronic absenteeism and
    and youth living in the most distressed of the HEA (20 U.S.C. 1002).
    community violence, due to three key
    communities of the United States, (iii) The office of a chief elected
    characteristics: (1) a strong backbone
    including ensuring school readiness, official of a unit of local government.
    organization to support families, which
    high school graduation, and access to a (iv) An Indian Tribe or Tribal
    can take years to build; (2) flexible
    community-based continuum of high- organization, as defined under section 4
    funding targeted for year-round K–12
    quality services. The program serves of the Indian Self-Determination and
    interventions; and (3) networks of
    neighborhoods with high concentrations Education Assistance Act (25 U.S.C.
    partnerships that draw on the internal
    of individuals with low incomes; 5304).
    resources of the community, such as
    Output:
    {
        "eligibility_requirements": {
            "eligible": [
                "An institution of higher education (IHE)",
                "An Indian Tribe or Tribal organization",
                "One or more nonprofit entities working in formal partnership with not less than one of the following: a high-need local educational agency (LEA); an IHE; the office of a chief elected official of a unit of local government; or an Indian Tribe or Tribal organization"
            ],
            “ineligible: [],
            "eligible_categories": [
                "non-profit organization",
                "institute of higher education",
                "school district",
                "local government entity",
            ]
        }
    }
    Input:
    --- PDF Page 15 ---
    3.2 APPLICATION SCREENING REQUIREMENTS
    Eligible Applicants include state, tribal and local governments, school districts, and public
    or private non-profit 501(c)(3) organizations. All Applicants must comply with the criteria
    listed below in this RFA at the time the Application is submitted.
    In order to be considered an Applicant eligible for evaluation, Application must meet the
    following criteria:
    A. Submit a complete and signed Application by the Deadline for Submission of
    Applications stated in Events. Section 7.1, Schedule of
    B. Provide documentation from the U.S. Internal Revenue Service to support the
    organizations legal entity type (i.e., government, non-profit).
    C. Provide documentation from the U.S. Internal Revenue Service and the Texas Secretary
    of State to support the organization is in good standing.
    D. Provide documented evidence that the Applicant has a current physical location and
    provides services within the State of Texas.
    3.3 GRANT AWARD ELIGIBILITY
    By submitting an Application in response to this RFA, Applicant certifies that:
    A. Applicant and all of its identified subsidiaries intending to participate in the Grant
    Agreement are eligible to perform grant-funded activities, if awarded, and are not
    subject to suspension, debarment, or a similar ineligibility determined by any State or
    federal entity;
    B. Applicant is in good standing under the laws of Texas and has provided HHS with any
    requested or required supporting documentation in connection with this certification;
    C. Applicant shall remain in good standing and eligible to conduct its business in Texas
    and shall comply with all applicable requirements of the Texas Secretary of State and
    the Texas Comptroller of Public Accounts;
    D. Applicant is currently in good standing with all licensing, permitting, or regulatory
    bodies that regulate any or all aspects of Applicant’s operations; and
    E. Applicant is not delinquent in taxes owed to any taxing authority of the State of Texas
    as of the effective date of this Grant Agreement.
    Output:
    {
        "eligibility_requirements": {
             "eligible": [
                "State governments",
                "Tribal governments",
                "Local governments",
                "School districts",
                "Public non-profit 501(c)(3) organizations",
                "Private non-profit 501(c)(3) organizations"
            ],
            "ineligible": [],
            "eligible_categories": [
                "non-profit organization",
                "state government entity",
                "tribal government entity",
                "local government entity",
                "school district",
            ]
        }
    }

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with an eligibility_requirements field containing an object with the following fields:
        * eligible (array of strings)
        * ineligible (array of strings)
        * eligible_categories (array of strings)
"""
)
