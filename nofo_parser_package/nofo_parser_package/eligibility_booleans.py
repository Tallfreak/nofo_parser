# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

prompt = r"""
    # Directive:
    For the attached file, determine who is eligible to apply for this grant and answer the following questions related to eligibility with true or false.
    * Is the grant only eligible to applicants in a region that does not include the United State?
    * Is the grant only eligible to applicants in a region that does not include Texas?
    * Is the grant only eligible for Tribal/Indian/Indigenous/Native entities?
    Do NOT guess or make up an answer. If you are not sure of the answer, return false.
    # Examples:
    Input:
    Community Development Block Grant Program for Indian Tribes and Alaska Native Villages
    II. ELIGIBILITY
    You are invited to apply if your organization is an eligible entity type and meets the funding conditions included in the NOFO. HUD will review applications from eligible applicants using the criteria in Section V. of this NOFO.
    A. Eligible Applicants
    1. Eligible Entity Types:
    07 (Native American tribal governments (Federally recognized))
    11 (Native American tribal organizations (other than Federally recognized tribal governments))
    Additional Information on Eligibility
    Individuals are ineligible applicants.
    Eligible Tribes and tribal organizations are:
    V. Application Review Information
    VI. Submission Requirements and Deadlines
    VII. Post-Award VIII. Contact and Requirements and Support
    Administration
    Appendix
    • Tribes: Eligible applicants are any Indian tribe, band, group, or nation, including Alaska Indians, Aleuts, and Eskimos, and any Alaska Native village of the United States which is considered an eligible recipient under Title I of the Indian Self- Determination and Education Assistance Act (25 U.S.C. 450) or which had been an eligible recipient under the State and Local Fiscal Assistance Act of 1972 (31 U.S.C. 1221). Eligible recipients under the Indian Self-Determination and Education Assistance Act will be determined by the Bureau of Indian Affairs and eligible recipients under the State and Local Fiscal Assistance Act of 1972 are those that have been determined eligible by the Department of Treasury, Office of Revenue Sharing. For more information, see “Indian Entities Recognized by and Eligible To Receive Services From the United States Bureau of Indian Affairs” (89 Fed. Reg. 238, December 11, 2024, https://www.govinfo.gov/content/pkg/FR-2024-12-11/pdf/2024- 29005.pdf).
    • Tribal Organizations: Tribal organizations that are eligible under Title I of the Indian Self-Determination and Education Assistance Act may apply on behalf of any Indian tribe, band, group, nation, or Alaska Native village eligible under that act for funds under this NOFO when one or more of these entities have authorized the tribal organization to do so through concurring resolutions. Such resolutions must accompany the application for funding (1003.5(b)). See instructions in Section IV.C.b., of this NOFO. HUD will not review an application from a tribal organization if the tribe it represents also applies for the same round of funding.
    o Applicants must be eligible by the application submission date.
    Output:
    {
        "eligibility_booleans": {
            "only_outside_united_states": false,
            "only_outside_texas": false,
            "only_tribal": true
            }
    }
    Input:
    2. Eligibility
    A. Eligible Applicants
    Only these types of organizations may apply. Under this announcement, applications will be accepted from:
    • Indian Tribes as defined in 33 U.S.C. 4201 and section 4 of the Indian Self-Determination and Education Assistance Act (25 U.S.C. 5304), which includes Alaskan Native Villages and Alaska Native Corporations, and former Indian reservations in Oklahoma, as determined by the Secretary of the Interior, and
    • Intertribal consortia, consistent with the requirements in 40 CFR Part 35.504(a).
    Intertribal consortia will be eligible to receive grants under this program only if the consortium demonstrates that all members of the consortium meet the eligibility requirements for the grant and authorize the consortium to apply for and receive assistance by submitting to EPA documentation of:
    (1) the existence of the partnership between Indian Tribal governments, and
    (2) authorization of the consortium by all its members to apply for and receive the grant.
    Documentation can be in the form of letters signed by all member Tribes, approved by-laws that contain language that specifically address the eligibility requirements, and/or other forms of documentation approved by the EPA Point of Contact that adequately meet the eligibility requirements.
    Output:
    {
        "eligibility_booleans": {
            "only_outside_united_states": false,
            "only_outside_texas": false,
            "only_tribal": true
            }
    }
    Input:
    Strengthening Ghana Health Service laboratory systems activities under the President's Emergency Plan for AIDS Relief (PEPFAR)
    The Award Ceiling for Year 1 is 0 (none). CDC anticipates an Approximate Total Fiscal Year Funding amount of $500,000 for Year 1, subject to the availability of funds.This Notice of Funding Opportunity (NOFO) will provide technical assistance to the Ghana Health Service (GHS)/Ministry of Health (MoH) to coordinate, consolidate, and improve laboratory capacity to advance HIV testing, treatment, retention, and viral suppression. This will be accomplished by providing financial and technical resources to build systems to enhance laboratory capacity to deliver HIV prevention and control best practice strategies that are efficient and effective. This NOFO will build and strengthen laboratories equipped with the appropriate diagnostic technologies, trained and skilled staff, and systems having capability to provide quality and efficient services such as viral load (VL) testing and early infant diagnosis (EID), quality management systems, continuous quality improvement (CQI)/Accreditation mentorship and post accreditation mentorship sample transport system, workforce capacity building towards next generation sequencing training for HIV DR, laboratory data management (e-Tracker and lab dashboard maintenance), Multiplex EID and VL testing assay interface and barcoding for sample tracking and support proficiency testing/EQA. This NOFO will allow the CDC to work directly and bilaterally with the Government of Ghana (GoG) MoH as part of (PEPFAR) to save lives, provide accurate laboratory diagnostic results, support treatment continuity and build capacity for sustainable transition to government for epidemic control by 2030.
    Output:
    {
        "eligibility_booleans": {
            "only_outside_united_states": true,
            "only_outside_texas": true,
            "only_tribal": false
            }
    }
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
        "eligibility_booleans": {
            "only_outside_united_states": false,
            "only_outside_texas": false,
            "only_tribal": false
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
        "eligibility_booleans": {
            "only_outside_united_states": false,
            "only_outside_texas": false,
            "only_tribal": false
            }
    }
    Input:
    FY24 Port of Rosedale Multimodal Expansion: Great River Railroad Restoration Project
    This Project is part of a larger effort to restore function to the Great River Railroad that runs from the Port of Rosedale to the Columbus and Greenville Railroad (CAGY) in Metcalf, MS. The larger effort is divided into two Phases. Under this Agreement, the Project will complete environmental review for both phases. Additionally, this Project will complete preliminary engineering, final design, and construction activities for Phase 1 of the larger effort. Under this Agreement, Phase 1 activities will include preliminary engineering, final design, and construction activities to repair the 31 mile railroad to be a functional track for maintenance equipment by replacing ties (approximately one-third of the timber rail ties), repairing 33 grade crossings, installing additional supplemental ballast rock, resurfacing track, repairing 4 timber bridges, replacing 1 timber bridge with culverts, and installing 1 concrete culvert. Phase 2 of the restoration effort is anticipated to include installing approximately 31 miles of new 112–115-pound rail, additional tie replacement, the replacement of 4 bridges, and improvements to sidings (Port of Rosedale spur) in order to restore the track to a full operation. Besides environmental review, this Agreement does not fund activities for Phase 2. Successful completion of the Project will enhance resiliency and redundancy for both the Port of Rosedale and the wider region.
    Output:
    {
        "eligibility_booleans": {
            "only_outside_united_states": false,
            "only_outside_texas": true,
            "only_tribal": false
            }
    }
    Input:
    F25AS00218 Aquatic Invasive Species Interjurisdictional Grants to the Great Lakes States and Tribes - Fiscal Year 2025 Great Lakes Restoration Initiative
    ELIGIBILITY
    Eligible Applicants
    Others (see text field entitled "Additional Information on Eligibility" for clarification)
    Unrestricted (i.e., open to any type of entity above), subject to any clarification in text field
    entitled "Additional Information on Eligibility"
    Additional Information on Eligibility
    We are seeking one application from a state and tribal natural resource agency in the Great Lakes
    Basin. However, that agency may designate an entity (of any type) to apply for the award on
    their behalf. This funding opportunity is available for cooperative agreements with Cooperative
    Fish and Wildlife Research Units and/or Cooperative Ecosystem Studies Unit Network members.
    Output:
    {
        "eligibility_booleans": {
            "only_outside_united_states": false,
            "only_outside_texas": true,
            "only_tribal": false
            }
    }

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.
    # Output Formatting:
    Structure the output as a json object with an eligibility_booleans field containing an object with the following fields:
        * only_outside_united_states (boolean)
        * only_outside_texas (boolean)
        * only_tribal (boolean)
"""
