# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501


# probability refine this directive
prompt = r"""
    # Directive:
    For the attached file, extract the actual review criteria or evaluation rubric used to assess applications. Include and summarize info for each criteria if it exists. If there are criteria for different tracks, organize the criteria by track. Do NOT guess or make up an answer. In the RARE case the information is not present, return 'Information is not available'.

    # Examples:
    Input:
    5. APPLICATION REVIEW INFORMATION
    Evaluation of Grant Application Criteria
    Review Criteria
    FNS will pre-screen all applications to ensure the applicants are eligible entities and are in
    compliance with all Program regulations. FNS will not approve any waivers from Program
    regulations for any projects submitted in response to this solicitation.
    15

    --- PDF Page 16 ---
    Evaluation Factors and Criteria
    FNS will review all complete applications competitively and score them against the criteria listed
    below, including:
    • Project design (35 points)
    • Impact and evaluation (30 points)
    • Budget and economic efficiency (20 points)
    • Organizational experience, staff capability, and management (15 points)
    • Bonus points (up to 9 points)
    Total points: 109
    1. Project Design (35 points)
    Problem Analysis
    • The proposal clearly defines the problem facing the SNAP certification and eligibility
    determination process.
    • The proposal clearly defines the solution and provides evidence or compelling justification
    that the proposed project will solve or ameliorate the identified problem.
    Proposals may include any consultation with stakeholders, advocacy groups, public
    o
    comment, research, studies, or real-world examples.
    • Project proposals containing more than one sub-project must demonstrate how the sub-
    projects are related to each other and the overarching proposal’s goals. Additionally,
    applicants must provide a funding breakdown for each sub-project within the Budget
    section.
    Implementation
    • The proposal clearly articulates how the applicant will implement this project.
    • The proposal includes a project timeline that outlines proposed tasks and demonstrates
    that the applicant allotted sufficient time for each activity.
    Sustainability
    • The proposal shows that the applicant has a plan for sustaining the project after the grant
    period of performance ends.
    2. Impact & Evaluation (30 points)
    Impact
    • The proposal must:
    Clearly quantify the proposed project’s direct effect on the SNAP application and
    o
    eligibility determination processes;
    Provide measurable evidence that the proposed changes will benefit the applicant,
    o
    recipient, or caseworkers; and
    Identify how the proposed project will impact one or more of the following aspects
    o
    of SNAP and propose how to evaluate the impacts.
      Administrative cost Timeliness
      Interviews Program integrity
      Recertification Payment accuracy
      Client reporting Program access
      Application intake Application screening
      Notices Verification
    16

    --- PDF Page 17 ---
     Error rate
    • Proposed Activities and Indicators measuring success must be mapped to the objective(s)
    listed in the Fiscal Year 2025 Key Objectives using the Activities/Indicators Tracker.
    • The proposal should include a description of how the project integrates with and supports
    the State agency’s current or planned process improvement and/or technology initiatives.
    Evaluation
    FNS expects applicants to conduct their own evaluation independent of the Activities/Indicators
    Tracker that includes evaluating overall success of the project at completion. The proposed
    evaluation plan should describe how the applicant plans to measure the project’s impact and:
    • Include information from the Activities/Indicators Tracker;
    • Reflect how the applicant proposed to measure the impact of the proposed project;
    • Be comprehensive, specific, and data driven;
    • Identify how the applicant proposes to measure the impact of one or more of the above
    SNAP processes;
    • Include clear measures which assess whether the proposed project intervention addresses
    the problem identified;
    • Detail who will measure the goals of the project;
    • Detail what criteria the applicant will evaluate and how the applicant will evaluate the
    criteria; and,
    • Define the intervals at which the applicant will conduct evaluation during the grant period
    of performance.
    3. Organizational Experience, Staff Capability, and Management (15 points)
    Oversight
    • The proposal describes a plan for effective and consistent oversight by qualified project
    managers throughout the project.
    • The proposal includes an organizational chart for the project, including names of key
    personnel where applicable.
    Communication
    • The proposal includes an internal communication plan and, if applicable, a communication
    plan for communicating externally with partner organizations.
    Staff
    • The proposal identifies the project director or manager and other key staff.
    • The proposal includes resumes and project job descriptions that demonstrate that staff
    have the appropriate technical and experiential backgrounds to implement the project.
    • If staff are hired for this project, the proposal includes proposed job descriptions for these
    positions.
    • The proposal addresses contingency plans in the event of key staff departures.
    Time Commitment
    • The proposal identifies key staff and outlines the amount of time key staff will devote to
    the project, expressed as a percentage of Full Time Equivalents (FTE).
    • If applicable, the proposal identifies the amount of time key staff will spend managing
    partnering organizations.
    17

    --- PDF Page 18 ---
    Personally Identifiable Information (PII)
    • Proposals must delineate how all data and client personally identifiable information (PII)
    would be protected in accordance with Section 11(e)(8) of the Food and Nutrition Act of
    2008, Federal regulations at 7 CFR 272.1(c), and the Privacy Act of 1974.
    4. Budget Appropriateness and Economic Efficiency (20 points)
    Applications must include the required budget forms outlined in Application Checklist and a line-
    item budget narrative, formatted as a table with amounts in whole dollars, to receive the full
    point value for this criterion. If a discrepancy exists between the total funding request submitted
    on SF-424, SF-424A, and budget or budget narrative, FNS will only consider and evaluate the
    estimated funding request contained on SF-424.
    Cost Allocation
    Where necessary, identify programs other than SNAP that may benefit from the implementation of
    the project and allocate project costs across the benefiting programs to demonstrate that this
    grant is only going to fund SNAP’s share of project costs. For instance, if a project aimed to
    improve a joint application for SNAP and Medicaid, and SNAP represents 80 percent of
    applications received, the PTIG funding request should be 80 percent of the total project cost.
    Budget Narrative
    A well-written budget narrative provides line-item details for all of the activities under the award
    and justifies the proposed project expenditures and assists reviewers during the proposal review
    process. The budget narrative must meet the criteria noted in Section 4, Application Content
    Information and should:
    • Include a table that lists all line-item amounts in whole dollars;
    • Include all items listed on the checklist at the beginning of this RFA;
    • Correspond with the proposed project narrative and application budget;
    • Provide enough detail for reviewers to easily understand how costs were determined and
    derived and adequately justified based on current industry costs/standards or estimates
    from vendor(s) when possible. Applicants should obtain information on costs from
    applicable organizations or from online sources;
    • Align with the requested amounts in the submitted SF-424A; and,
    • Include separate tables for each sub-project, if applicable.
    No Sub-Projects Example:
    [Start Table 1]
            Line Item			Cost
    Personnel: (Person A: 0.25 FTE x $150,000/year x 2 years)			$ 75,000
    Fringe Benefits: (Person A: 20%% annual salary)			$ 15,000
    Travel			$0
    Equipment: (2 widgets at $5,000 each)			$ 10,000
    Supplies			$0
    Contractual / Consultant Costs: (3,200 hours of work at $125/hour)			$ 400,000
    Indirect Costs			$0
    Other			$0
            Total			$500,000
    [End Table 1]
    Total $500,000
    18

    --- PDF Page 19 ---
    Sub-Projects Example:
    [Start Table 1]
            Line Item			Sub-Project 1 Cost					Sub-Project 2 Cost
    Personnel
    (Sub-Project 2: Person A: 0.25 FTE x
    $150,000/year x 2 years)			$ 0					$ 75,000
    Fringe Benefits
    (Sub-Project 2: Person A: 20%% annual salary)			$ 0					$ 15,000
    Travel			$ 0					$ 0
    Equipment			$ 0					$ 10,000
    Supplies			$ 0					$ 0
    Contractual / Consultant Costs
    (Sub-Project 1: 2,400 hours x $125 / hour)
    (Sub-Project 2: 1,600 hours x $125 / hour)			$ 300,000					$ 200,000
    Indirect Costs			$ 0					$ 0
    Other			$ 0					$ 0
            Sub-Grant Total			$300,000					$300,000
            Project Total								$600,000
    [End Table 1]
    Project Total $600,000
    Indirect Cost Rate
    Applicants should use a current Negotiated Indirect Cost Rate Agreement (NICRA), negotiated
    [Start Table 2]
            The Office of Management
    and Budget assigns each organization to a single federal agency that acts on behalf of all federal
    agencies in indirect cost rate negotiations and is referred to as the “cognizant agency.”
    [End Table 2]
    agencies in indirect cost rate negotiations and is referred to as the “cognizant agency.” Indirect
    costs may not exceed the negotiated rate.
    • If an applicant uses a NICRA, applicants should indicate the percentage and base and
    provide a copy of the approved NICRA with the application.
    Efficiency
    • The proposal must demonstrate that the anticipated results are commensurate with the
    cost of the project.
    Contractual and Consultant Costs
    • Proposals that include hiring a consultant or contractor must provide the following
    information:
    Consultant’s name and description of service;
    o
    Itemized list of all direct costs and fees;
    o
    The number of personnel, including position titles;
    o
    Specialty and specialized qualifications as appropriate to the salary;
    o
    Number of estimated hours times hourly wage for each staff member; and
    o
    All expenses and fees directly related to the proposed services to be rendered for
    o
    the project.
    • FNS requires applicants that are required to issue a bid to include a narrative explaining
    the requirement and a detailed description of contractor responsibilities / consultant
    responsibilities / anticipated tasks and a reasonable estimate of contractual and
    consultant costs.
    19

    --- PDF Page 20 ---
    Bonus Points (up to nine points total)
    • FNS will award up to three bonus points to proposals that are particularly data driven.
    This can include conducting surveys, interviews, or other data collection or research in
    advance of submission of a proposal to determine more accurately what the quantifiable
    problem is that the proposed solution intends to solve. For example, specific quantifiable
    statistics may bolster the argument that the proposed project is necessary to improve
    payment accuracy or timeliness.
    • FNS will award up to three bonus points to proposals that have never received a PTIG as
    FNS believes such applicants would benefit from capacity building and modernization
    projects. Proposals received from new entities, i.e., those applicants that have not
    received a previous award, must demonstrate high need for the project in the Problem
    Analysis section. Additionally, the proposal must demonstrate a quantifiable and
    significant impact to receive the full three points.
    • FNS will award up to three bonus points to proposals that approach solutions from a
    human-centered design (HCD) perspective to modernize program delivery and improve
    the customer experience. Projects that incorporate HCD focus on usability through
    collaboration with program participants in usability testing, focus groups, user research, or
    end-users.9 other methods to improve SNAP processes for
    Review and Selection Process
    Following the initial screening process, FNS will assemble a panel group to review and determine
    the technical merits of each application. The panel will evaluate the proposals based on how well
    they address the required application components. After review, the panel will array the
    applications from highest to lowest score. The panel members will recommend applications for
    consideration for a grant award based on the evaluation scoring. FNS may request information
    [Start Table 1]
            The Selecting Official reserves the right
    to accept the panel’s recommendation or to select an application for funding out of order to meet
    agency priorities.
    [End Table 1]
    agency priorities. FNS reserves the right to use this RFA and the results of this competition to
    award additional grants in the next fiscal year should additional funds come available.
    Output:
    {
        "scoring_rubric": [
                {
                "track": null,
                "description": "Project Design",
                "points_or_percentage": "35 points",
                "info": "Applicants must clearly define the problem facing the SNAP certification and eligibility determination process, provide a compelling justification that the proposed project will solve or ameliorate the problem, and describe any stakeholder consultation or research. Proposals with multiple sub-projects must show how they relate to overall goals and provide a funding breakdown. The implementation plan must include a clear timeline with sufficient time for each activity, and the proposal must show a plan for sustaining the project after the grant period ends."
                },
                {
                "track": null,
                "description": "Impact & Evaluation",
                "points_or_percentage": "30 points",
                "info": "Applicants must quantify the project's direct effect on SNAP application and eligibility processes, provide measurable evidence of benefits to applicants, recipients, or caseworkers, and identify impacts on aspects such as administrative cost, timeliness, program integrity, payment accuracy, etc. Activities and indicators must be mapped to objectives. The evaluation plan should be comprehensive, specific, data-driven, and detail how and when the project's impact will be measured, including who will conduct the evaluation and what criteria will be used."
                },
                {
                "track": null,
                "description": "Budget Appropriateness and Economic Efficiency",
                "points_or_percentage": "20 points",
                "info": "Applicants must include required budget forms and a detailed line-item budget narrative. The budget must be justified, align with the project narrative, and show proper cost allocation if other programs benefit. The proposal must demonstrate that anticipated results are commensurate with project costs. For contractual/consultant costs, detailed information and justification are required."
                },
                {
                "track": null,
                "description": "Organizational Experience, Staff Capability, and Management",
                "points_or_percentage": "15 points",
                "info": "Applicants must describe effective oversight by qualified project managers, include an organizational chart, and provide an internal and (if applicable) external communication plan. Key staff must be identified, with resumes and job descriptions demonstrating relevant experience. The proposal should address contingency plans for staff departures and specify the time commitment of key staff. Proposals must also delineate how personally identifiable information (PII) will be protected."
                },
                {
                "track": null,
                "description": "Bonus Points",
                "points_or_percentage": "Up to 9 points (3 points each for three categories)",
                "info": "Up to 3 points for proposals that are particularly data driven (e.g., using surveys or research to define the problem); up to 3 points for applicants who have never received a PTIG before and demonstrate high need and significant impact; up to 3 points for proposals that use a human-centered design (HCD) approach to modernize program delivery and improve customer experience."
                }
        ]
    }
    Input:
    --- PDF Page 48 ---
    administrative issues related to the submission of the application, and requests for clarification about this NOFO.
    Section V. Application Review Information
    (back to the Table of Contents)
    Note: Additional provisions that apply to this section can be found at EPA Solicitation Clauses.
    A. Threshold Eligibility Review Process
    All applications will be evaluated for threshold eligibility purposes based on the threshold eligibility criteria
    described in Section III.D.
    B. Review Panel and Evaluation Process
    All applications that pass the threshold eligibility review process will be evaluated and scored by review
    panels using the track-specific evaluation criteria and processes described below. Review panels will be
    comprised of EPA staff and / or external reviewers. Track I applications will be reviewed by separate review
    panels for the written application and oral presentation. Track II applications will undergo only a written
    application review. See below for additional detail about the evaluation criteria and processes for each track.
    C. Track I Application Review Process, Evaluation Criteria, and Oral Presentations
    All eligible Track I applications (including those for the TIAs described in Section II.B) will be evaluated
    on a 200-point scale as follows—155 points for the written application review and 45 points for the oral
    presentation review:
    • The maximum points available for an application are 200 points—155 points for the written
    application based on the criteria specified below for Track I written applications, and 45 points for
    the oral presentation based on the criteria below.
    • Applicants whose written application scores at least 110 points will then proceed to an oral
    presentation. Oral presentations will be conducted consistent with the procedures described below.
    Applicants who proceed to an oral presentation will be provided further information about the
    process following the evaluation of the written application.
    • Applicants who do not proceed to an oral presentation will receive notification of non-selection
    from EPA and may request a debriefing as explained in the Section VI Debriefings and Disputes
    clauses included in the EPA Solicitation Clauses incorporated by reference in the NOFO.
    Applicants may resubmit an application in certain circumstances as noted in Section II.C.
    • The oral presentation will be worth 45 points and be evaluated based on the oral presentation criteria
    below.
    • Applications that receive a total score of 170 or more (based on the written application and oral
    presentation) will be referred to the Selection Official for final selection consideration as described
    in Section V.E below.
    • Applications that receive a total score between 110-169 (based on the written application and oral
    presentation) will be ranked and referred to the Selection Official, on an approximately monthly
    basis, for final selection consideration as described in Section V.E below.
    • Applications not selected for award based on the monthly review will receive notification from
    EPA and may request a debriefing as explained in the Section VI Debriefings and Disputes clauses
    48

    --- PDF Page 49 ---
    included in the EPA Solicitation Clauses incorporated by reference in the NOFO. Applicants may
    resubmit an application in certain circumstances as noted in Section II.C.
    Track I Written Application Criterion
    [Start Table 1]
    Section				Possible
                    Points
        Part 1. Community Driven Investments for Change			80 total
        1.1 Community Overview			10
        1.2 Selected Strategies			45
        1.3 Community Engagement and Collaborative Governance Plan			15
        1.4 Community Strength Plan			10
        Part 2. Program Management, Capability, and Capacity			35 total
        2.1 Performance Management Plan, Outputs / Outcomes			6
        2.2 Project Linkages to the EPA Strategic Plan			4
        2.3 CBO Experience and Commitment			5
        2.4 Programmatic and Managerial Capability and Resources			15
        2.5 Past Performance			5
        Part 3. Readiness to Perform, Feasibility, and Sustainability			40 total
        3.1 Readiness Approach			8
        3.2 Feasibility			9
        3.3 Sustainability			5
        3.4 Program Budget Description			8
        3.5 Compliance Plan			10
        TOTAL			155
    [End Table 1]
    TOTAL 155
    Evaluation Criteria for Track I Written Applications (155 points total)
    Part 1. Community Driven Investments for Change (80 points total)
    1.1 Community Vision Description (10 points)
    • Applications will be evaluated based on their description of the Community Description:
    Project Area including its resources, assets, and local characteristics, as well as how the
    project activities in the Project Area are designed and focused to maximize benefits for the
    residents of disadvantaged communities in the Project Area. Please note that in evaluating
    applications under this criterion, EPA will evaluate the extent and quality to which project
    benefits will accrue to the residents of the disadvantaged communities in the Project Area,
    as defined in Appendix A, in an impactful manner. (4 points)
    • Applications will be evaluated based on how well they describe Community Challenges:
    the challenges and needs the residents of the disadvantaged communities in the Project
    Area, as defined in Appendix A, are facing, including climate impacts, climate change risks
    / exposures, and / or localized pollution, and the impact these challenges have on priority
    populations within the Project Area who are acutely exposed to and impacted by climate,
    pollution, and weather-related threats, and / or who exhibit acute vulnerabilities or
    susceptibilities to the impacts of environmental pollution. See footnote 3 for more
    information on priority populations. (3 points)
    • Applications will be evaluated based on the quality and extent to Community Vision:
    which they articulate an overall and clear vision for the impacts and benefits the grant
    49

    --- PDF Page 50 ---
    would have on the residents of the disadvantaged communities in the Project Area as
    defined in Appendix A in the near and long term. (3 points).
    1.2 Selected Strategies (45 points)
    • Applications will be evaluated based on the quality and Strategy Overview (15 points).
    extent to which they:
    Provide an overview of the strategies and associated projects and describe how they
    o
    will be implemented during the grant term. (5 points)
    Describe how the strategies and associated projects in the application are integrated
    o
    and / or designed to complement each other to benefit the residents of the
    disadvantaged communities in the Project Area, and how the scale and scope of the
    Project Area was developed to accomplish this. (7 points)
    Explain how the amount / proportion of the requested funding was determined for each
    o
    strategy and aligned project in the application. (3 points)
    • Applications will be evaluated based on the quality Climate Action Strategies (15 points).
    and extent to which they:
    Describe how the associated projects will address the identified climate impacts and /
    o
    or climate change risk(s) / exposure(s) within the Project Area, and especially those
    facing residents of disadvantaged communities in the Project Area as defined in
    Appendix A and explain how the project(s) will decrease GHG emissions within the
    Project Area and / or increase overall Project Area resilience to current and anticipated
    climate impacts. (8 points)
    Describe how the selected Climate Action Strategies and associated projects help meet
    o
    the needs and challenges of the Project Area as articulated in the Community Vision
    Description. (7 points)
    • Applications will be evaluated based on the Pollution Reduction Strategies (15 points).
    quality and extent to which they:
    Describe how the associated project(s) will address the identified localized pollution
    o
    challenges facing the Project Area, and especially the residents of disadvantaged
    communities within the Project Area as defined in Appendix A, and will make
    substantial and measurable (i.e., quantifiable) progress towards preventing, reducing,
    and / or mitigating existing and future sources of pollution to benefit the Project Area.
    (8 points)
    Describe how the selected Pollution Reduction Strategies help meet the needs and
    o
    challenges of the Project Area as articulated in the Community Vision Description. (7
    points)
    1.3 The Community Community Engagement and Collaborative Governance Plan (15 points):
    Engagement and Collaborative Governance Plan described in Section I.G will be evaluated based
    on the quality and extent to which it demonstrates:
    • How the applicant’s past Past Community Outreach and Engagement Conducted:
    engagement with the Project Area community impacted the Strategy and associated project
    selection and implementation approach included in the application, including the outreach
    50

    --- PDF Page 51 ---
    and engagement methods used for the Project Area and specific neighborhoods or groups
    within the Project Area. (4 points)
    • Implementation: The specific community engagement Community Engagement Plan
    methods used by the applicant, as well as how they will mitigate barriers and involve
    relevant governmental stakeholders necessary to support overall project implementation.
    (6 points)
    • Structure: The details regarding the roles and responsibilities Collaborative Governance
    of the Lead Applicant, Collaborating Entities, and community residents and / or
    community-selected representatives for implementing, managing, and overseeing the
    application’s project activities, including how regularly they will meet to discuss project
    implementation. (5 points)
    1.4 The Community Strength Plan as described in Section Community Strength Plan (10 points):
    I.G will be evaluated based on the quality and extent to which it demonstrates:
    • How the projects included in the application Maximizing Economic Benefits of Projects:
    are intended to provide economic benefits for individuals in the Project Area, including
    priority populations as defined in footnote 3. (5 points)
    • The measures for mitigating potential near-term and long-term Displacement Avoidance:
    risks associated with the proposed projects to residents, small businesses, nonprofits, and
    other community members, the vulnerability the community faces to rising costs
    attributable to their proposed project, and the potential project impacts to households, small
    businesses, and other existing groups. (5 points)
    Part 2. Program Management, Capability, and Capacity (35 points total)
    Applications will be 2.1 Performance Management Plan and Outputs / Outcomes (6 points):
    evaluated based on:
    • Whether the application describes an effective plan, with associated timeframes, for
    tracking and measuring progress in achieving the expected project outcomes and outputs
    including those identified in Appendix F, as appropriate, and any additional ones identified
    in the application. (2 points)
    • The quality and specificity of the proposed outputs and outcomes and how they will lead
    to improvements to the environmental conditions and public health of the disadvantaged
    communities in the short and long term. (2 points)
    • Whether, and how, the applicant has incorporated program evaluation activities (e.g.,
    utilizing proper evaluation tools and personnel / organizations with experience in
    evaluating program and project progress / success) from project initiation through project
    completion to meaningfully document and measure their progress towards achieving
    project goals and how they will use the results of the evaluations to meet the project goals
    within the required timeframes. (2 points)
    2.2 Applications will be evaluated based on Project Linkages to the EPA Strategic Plan (4 points):
    the extent and quality to which the proposed project activities support and advance EPA Strategic
    Plan Goal 2 (Take Decisive Action to Advance Environmental Justice and Civil Rights), Objective
    51

    --- PDF Page 52 ---
    2.1, (Promote Environmental Justice and Civil Rights at the Federal, Tribal, State, and Local
    Levels).
    In addition, applications, depending on the projects included in them, will also be evaluated based
    on the quality and extent to which they also support and advance the following EPA Strategic Plan
    Goals as applicable:
    • Goal 1 - Tackle the Climate Crisis
    • Goal 4 - Ensure Clean and Healthy Air for All Communities
    • Goal 5 - Ensure Clean and Safe Water for All Communities
    • Goal 6 - Safeguard and Revitalize Communities; and
    • Goal 7 - Ensure Safety of Chemicals for People and the Environment
    2.3 The CBO(s) that are either the Lead Applicant CBO Experience and Commitment (5 points):
    and / or Statutory Partner for the proposed grant will be evaluated based on their history and
    experience as a CBO and the depth of their commitment, connections, and relationships with the
    disadvantaged communities the application is intended to benefit.
    2.4 points): The Lead Applicant and Programmatic and Managerial Capability and Resources (15
    Statutory Partner will be evaluated based on their ability to successfully complete, oversee, and
    manage the award considering:
    • Their organizational experience and capacity related to performing the proposed project(s)
    or similar activities (e.g., experience in managing projects and activities like those in the
    application). (4 points)
    • Their resources, capacity, capabilities, staff (e.g., project manager and other key
    personnel), expertise, and skills to perform and manage the award activities effectively
    during the three-year award period. For Lead Applicants submitting two applications under
    this NOFO, this includes how they demonstrate they have the above attributes to perform,
    manage, and oversee two awards effectively within the three-year award period (4 points)
    • The milestone schedule for the proposed projects (up to three years) including the breakout
    of the project activities into phases and timeframes for completion of tasks, and the
    approach, procedures, and controls for ensuring that the award funds will be expended in
    a timely and efficient manner while ensuring that costs are eligible, reasonable, and
    allowable. (3 points)
    • Their financial stability, controls in place, and capacity to manage taxpayer dollars
    ethically and efficiently as well as the policies and controls for project oversight and
    program risk. This includes the extent and quality to which the application includes
    controls to identify waste, fraud, and abuse, and reduce the potential for waste, fraud, and
    abuse by including plans and policies for program oversight, including confidential
    reporting (e.g., whistleblower protections). (4 points)
    2.5 points): The Lead Applicant will be evaluated based on their ability to Past Performance (5
    successfully complete and manage the proposed projects considering their:
    • Past performance in successfully completing and managing the assistance agreements
    identified in response to Section IV.B. (3 points)
    • History of meeting the reporting requirements under the assistance agreements identified
    in response to Section IV.B including whether the applicant submitted acceptable final
    technical reports under those agreements and the extent to which the applicant adequately
    52

    --- PDF Page 53 ---
    and timely reported on their progress towards achieving the expected outputs and outcomes
    under those agreements and if such progress was not being made whether the applicant
    adequately reported why not. (2 points)
    Note: The focus of this criterion is on the Lead Applicant’s past performance and not that of any
    other Collaborating Entities or contractors / consultants who may be assisting the applicant with
    performance of the award. In evaluating the Lead Applicant under these factors, EPA will consider
    the information provided in the application and may also consider relevant information from other
    sources, including information from EPA files and from current / prior grantors. If the Lead
    Applicant does not have any relevant or available past performance related to federal or non-federal
    grants, this should be stated explicitly in the application (e.g., our organizations have no relevant
    past grants experience). Including this statement will ensure you receive a neutral score for these
    factors (a neutral score is half of the total points available in a subset of possible points). Failure to
    include this statement may result in your receiving a score of 0 for these factors.
    Part 3. Readiness to Perform, Feasibility, and Sustainability (40 points total):
    Applications will be evaluated based on the applicant's ability 3.1 Readiness Approach (8 points):
    and readiness to proceed with grant performance for the projects in the application, based on the
    Readiness Approach Requirements described in Section I.G, upon receiving an award, or generally
    no later than 120 days after award, to ensure that the projects can be completed within the statutory
    three-year grant period. As appropriate, this may include evaluating the description of the
    completed project planning and design phases related to the project(s) as well as demonstrating that
    the applicant has obtained and / or complied with the necessary approvals, permits, permissions,
    and any other applicable requirements, to commence project performance upon award, and if not
    generally within 120 days of award.
    Applications will be evaluated based on whether it is demonstrated that all 3.2 Feasibility (9 points):
    the projects in the application can be successfully and effectively performed within the three-year
    grant period of performance, and the degree of risk that they cannot be. This includes also
    evaluating how the strategies and associated projects can individually and collectively be
    completed within three years.
    Applications will be evaluated based on whether it is demonstrated that 3.3 Sustainability (5 points):
    the benefits and outcomes from the projects in the application can be sustained after the three-year
    grant period of performance based on factors including but not limited to whether (i) the Applicant
    will leverage funding and / or resources from other sources to ensure the sustainability of the
    projects beyond the three-year grant term and (ii) the description of an operations and maintenance
    approach including the plans and commitments to ensure there is continued funding available for
    operation and maintenance activities of infrastructure activities for the projects after the grant term
    is over (e.g., are there demonstrated commitments for continuing operation and maintenance
    funding / resources from the appropriate parties after the three year grant term is over) including
    coordination with appropriate responsible parties.
    The program budget will be evaluated based on: 3.4 Program Budget Description (8 points):
    • The reasonableness of the budget and allowability of the costs for each component / activity
    of the projects in the application. This includes evaluating whether funding is well balanced
    and equitably distributed to project partners, including sub-awardees, commensurate with
    their role in the project, and whether funding is categorized into the proper budget
    53

    --- PDF Page 54 ---
    categories providing clarity, accuracy, and granularity on the applicant’s planned use of
    the grant funds during the project period. (4 points)
    • The cost effectiveness of the budget / project in terms of maximizing the share of funds
    used for the delivery of benefits to disadvantaged communities (both the direct costs of
    funds passed through for financial assistance as well as associated indirect costs to the
    greatest extent practicable). (4 points)
    Applications will be evaluated based on the quality and extent to 3.5 Compliance Plan (10 points):
    which the Compliance Plan addresses the elements for the Compliance Plan described in Section
    I.G.
    Track I Oral Presentation (45 points total)
    The oral presentation is intended to supplement the written application. and provide an opportunity for
    applicants to further explain their projects. The oral presentations will be conducted through video
    teleconferencing; however, requests for a telephone-only conference will be considered, provided the
    applicant describes why video teleconferencing is a barrier that cannot be overcome with technical
    assistance provided through EPA as noted in Section I.E. Pre-recorded presentations that lack real-time
    interaction will not be allowed. EPA will also provide interpretive services for the oral presentation upon
    request.
    Further instructions and details about the oral presentation (e.g., date, time, requirements, limitations and /
    or prohibitions on the use of written material or other media to supplement the oral presentations, the time
    permitted for each oral presentation) will be provided to those applicants selected to participate in an oral
    presentation. EPA will maintain a record of the oral presentation (e.g., transcription) and relevant
    information from the oral presentation may be incorporated into the grant award terms and conditions as
    appropriate.
    Applicants are responsible for determining who will represent them at the oral presentation, but it must
    include a representative(s) of the Lead Applicant and should include Collaborating Entity and community
    representatives as necessary. Contractors, including consultants, cannot attend the oral presentation for the
    applicant.
    The oral presentation will be approximately 45 minutes including an introduction and closing. It is expected
    it will be conducted by two EPA and / or external reviewers who will evaluate the oral presentation based
    on the criteria below. The reviewers may ask clarifying questions during the presentation to enhance their
    understanding of the application, but they will be limited to clarifying issues related only to the areas listed
    below. The oral presentation cannot be used to change the scope of the applicant’s written application, make
    any substantive changes to it, cure material omissions in the written applications, and / or otherwise revise
    the written application. The oral presentation will be evaluated on the below criteria.
    Oral Presentation Criteria (45 points total)
    • Overview: Can you further elaborate on how you developed the scope and scale of Community
    the Project Area as described in Appendix A to help ensure that the project benefits will accrue to
    residents of disadvantaged communities in the Project Area in an impactful manner and will not be
    dispersed and minimized throughout the Project Area? What are the greatest needs for these
    residents within the Project Area, and, if your application is not selected for funding what would
    be the adverse consequence to them? (9 points)
    54

    --- PDF Page 55 ---
    • Why did you select the strategies and projects within the application, and how Strategy Rationale:
    will they (collectively and individually) transform the Project Area to address environmental and
    climate justice challenges now and in the future (beyond the three-year grant term)? Also, when
    the three-year grant term is complete, how will you assess whether the grant was successful in
    achieving its objectives to benefit the Project Area and what will success look like? (9 points)
    • Describe your commitment, as well Community Engagement and Collaborative Governance:
    of that of the Collaborating Entities as described in Section III.A of the NOFO, to efficiently and
    effectively perform the projects in the application within three years and describe how all entities
    will work together to achieve the project objectives within the three-year grant performance period.
    (9 points)
    • Explain how you have the programmatic, technical, administrative, and Management Capacity:
    managerial capability, experience, and resources to properly manage the grant consistent with grant
    regulations and requirements including those in 2 CFR §200 (9 points)
    • What do you anticipate are the greatest challenges to completing the Performance Challenges:
    projects in the application within the three-year time frame, and what are your plans for overcoming
    them? (9 points)
    D. Track II Application Review Process and Evaluation Criteria
    All eligible Track II application will be evaluated on a 100-point scale using the criteria specified below.
    There will be no oral presentation component for the Track II applications.
    Track II applications that score at least 85 points will be referred to the Selection Official for final selection
    consideration as described in Section V.E below. Those Track II applications whose total score is below 85
    will be ranked by EPA staff and reviewed on an approximately monthly basis by the Selection Official.
    Those not selected for award during the monthly review will receive notification from EPA and may request
    a debriefing as explained in the Section VI: Debriefings and Disputes clauses are included in the EPA
    Solicitation Clauses incorporated by reference in the NOFO. Applicants may resubmit an application in
    certain circumstances as noted in Section II.C.
    Evaluation Criteria for Track II Applications
    Track II applications will be evaluated using the criteria below on a 100-point scale.
    Track II Evaluation Criteria
    [Start Table 1]
        Section			Possible Points
        1. Program Objectives			35
        2. Project Collaboration and Participation			20
        3. Project Linkages		4	4
        4. Budget		8
        5. Environmental Results		6
        6. CBO Experience & Commitment		5
        7. Programmatic and Managerial Capability and Resources		16
        8. Past Performance		6
        TOTAL			100
    [End Table 1]
    TOTAL 100
    55

    --- PDF Page 56 ---
    1. Applications will be evaluated based on the quality Track II Program Objectives (35 points):
    and extent to which they demonstrate:
    • How the project(s) in the application address the Track II objectives identified in Section
    I.H. (10 points)
    • The methods, tools, and trainings, the applicant will use to facilitate the engagement of
    disadvantaged communities in state and Federal advisory groups, workshops, rulemakings,
    and / or other public processes, including local, Tribal, and other governmental processes,
    related to environmental and climate justice. (10 points)
    • How the project(s) in the application address and improve the disadvantaged community’s
    lack of access to, or weak relationships with, governmental entities and changes those
    relationships to increase points of access for disadvantaged communities with government
    to work cooperatively to promote environmental and climate justice. (8 points)
    • Will result in governmental entities better understanding the root causes of environmental
    and climate justice issues that impact disadvantaged communities, so the communities are
    better prepared to proactively address them before the issues materialize. (7 points)
    2. Under this criterion, applications will be Project Collaboration and Participation (20 points):
    evaluated based on the quality and extent to which they:
    • Demonstrate that meaningful input and feedback was considered from the disadvantaged
    community and other stakeholders in designing and developing the applications and how
    feedback / input will continue to be obtained and considered during grant performance. (10
    points)
    • Describe the facilitation and accountability measures to establish and maintain trust
    between the disadvantaged community and government officials to ensure the community
    can collaborate in a meaningful manner on environmental and climate justice issues with
    governmental bodies. (5 points)
    • Demonstrate the applicant’s and Collaborating Entities relationships and history of
    collaborations with disadvantaged communities, governmental bodies, and other
    stakeholders to address environmental and environmental / climate justice issues. (5 points)
    3. Applications will be evaluated based on the extent and quality to Project linkages (4 points):
    which the proposed project activities support and advance EPA Strategic Plan Goal 2 (Take
    Decisive Action to Advance Environmental Justice and Civil Rights), Objective 2.1, (Promote
    Environmental Justice and Civil Rights at the Federal, Tribal, State, and Local Levels).
    4. Under this criterion, applicants will be evaluated based on: Budget (8 points):
    • The reasonableness of the budget and allowability of the costs for each component / activity
    of the project and their approach, procedures, and controls for ensuring that awarded grant
    funds will be expended in a timely and efficient manner to comply with the statutory 3-
    year project period limitation. (4 points)
    56

    --- PDF Page 57 ---
    • The cost effectiveness of the budget / project in terms of maximizing the share of funds
    used for the delivery of benefits to disadvantaged communities (both the direct costs of
    funds passed through for financial assistance as well as associated indirect costs to the
    greatest extent practicable). (4 points)
    5. Applications will be evaluated based on the quality and extent Environmental Results (6 points):
    to which:
    • They describe an effective plan, with associated timeframes, for tracking and measuring
    their progress in achieving the expected project outcomes and outputs for Track II
    applications including those identified in Appendix F. (2 points)
    • They demonstrate that the project can ensure sustainability of outcomes beyond the three-
    year grant period, and how they will leverage resources, community support, etc. to
    facilitate this. (2 points)
    • The quality and specificity of the proposed outputs and outcomes, and how they will lead
    to the success of the grants, are described. (2 points)
    6. The CBO(s) that are either the Lead Applicant CBO Experience and Commitment (5 points):
    and / or Statutory Partner for the grant will be evaluated based on their history and experience as a
    CBO and the depth of their commitment, connections, and relationships with the disadvantaged
    communities the application is intended to benefit.
    7. The Lead Applicant and Programmatic and Managerial Capability and Resources (16 points):
    Statutory Partner will be evaluated based on their ability to successfully complete, oversee, and
    manage the award considering:
    • Their organizational experience and capacity related to performing the proposed projects
    or similar activities (e.g., experience in managing projects and activities like those in the
    application). (4 points)
    • Their resources, capacity, capabilities, staff (e.g., project manager and other key
    personnel), expertise, and skills to perform and manage the award activities effectively
    during the three-year award period. For Lead Applicants submitting two applications under
    this NOFO, this includes how they demonstrate they have the above attributes to perform,
    manage, and oversee two awards effectively within the three-year award period. (4 points)
    • The milestone schedule for the proposed projects (up to three years) including the breakout
    of the project activities into phases and timeframes for completion of tasks, and the
    approach, procedures, and controls for ensuring that the award funds will be expended in
    a timely and efficient manner while ensuring that costs are eligible, reasonable, and
    allowable. (3 points)
    • Their legal and financial controls in place, and capacity to manage taxpayer dollars
    ethically and efficiently as well as the policies and controls for project oversight and
    program risk. This includes the extent and quality to which the application includes
    controls to identify waste, fraud, and abuse, and reduce the potential for waste, fraud, and
    abuse by including plans and policies for program oversight, including confidential
    reporting (e.g., whistleblower protections). (5 points)
    57

    --- PDF Page 58 ---
    8. The Lead Applicant will be evaluated based on their ability to Past Performance (6 points total):
    successfully complete and manage the proposed projects considering their:
    • Past performance in successfully completing and managing the assistance agreements
    identified in response to Section IV. (3 points)
    • History of meeting the reporting requirements under the assistance agreements identified
    in response to Section IV including whether the applicant submitted acceptable final
    technical reports under those agreements and the extent to which the applicant adequately
    and timely reported on their progress towards achieving the expected outputs and outcomes
    under those agreements and if such progress was not being made whether the applicant
    adequately reported why not. (3 points)
    The focus of this criterion is on the Lead Applicant’s past performance and not that of any other
    Collaborating Entities or contractors / consultants who may be assisting the applicant with
    performance of the project. In evaluating the Lead Applicant under these factors, EPA will consider
    the information provided in the application and may also consider relevant information from other
    sources, including information from EPA files and from current / prior grantors. If you do not have
    any relevant or available past performance related to federal or non-federal grants, you should state
    this explicitly in your application (e.g., our organization has no relevant past grants experience).
    Including this statement will ensure you receive a neutral score for these factors (a neutral score is
    half of the total points available in a subset of possible points). Failure to include this statement
    may result in your receiving a score of 0 for these factors.
    E. Final Selection Process and Other Factors
    The Selection Official will make the final selection recommendations for Track I and II applications
    based on the evaluation criteria and process described above. In addition, in making the final selection
    recommendations for award, the Selection Official may also consider any of the “other” factors below.
    Further, as noted in Sections I.G and II.A, EPA anticipates making a minimum of fifteen awards for
    high-ranking applications that include a workforce training project(s) as described in Section I.G. In
    addition, as noted in Sections II.B and Appendix H, EPA anticipates making a minimum of five awards
    for high-ranking applications under the Target Investment Area A-Tribes in Alaska (projects benefitting
    Alaska Tribal lands) that include projects to assess and/or clean up lands conveyed under the Alaska
    Native Claims Settlement Act that were contaminated at the time of their conveyance from the federal
    government to an Alaska Native Corporation.
    In making the final selection recommendations for award, the Selection Official may consider any of the
    following “other factors”:
    1. Geographic diversity to promote a mix of high-scoring applications benefitting disadvantaged
    communities located in urban, rural, or remote areas, different regions of the country, territories, as
    well as the geographical nature or impact of the project(s).
    2. Program priorities- how the application supports and advances EPA and OEJECR’s goals and
    priorities, including those in EPA’s Strategic Plan that focus on environmental climate and justice
    issues. This may also include considering how the application promotes Community Change Grant
    program objectives, the depth and extent of community involvement in project development and
    implementation, the extent and quality to which the project activities will provide impactful benefits
    58

    --- PDF Page 59 ---
    to the residents of disadvantaged communities in the Project Area as defined in Appendix A rather
    than attenuated benefits spread out throughout a large Project Area, the priority that the grants and
    must be able to be successfully completed within three years to meet CAA § 138 statutory
    requirements.
    3. Organizational diversity in terms of applicant type and size to ensure a broad representation of
    applicants receiving awards to improve program effectiveness and equity.
    4. Whether the applicant is participating in a federal capacity building program as part of the Thriving
    Communities Network (please see complete list at Federal Interagency Thriving Communities
    Network or the Rural Partners Network).
    5. Whether the projects support, advance, or complement funding related to Community Disaster
    Resilience Zones (CDRZs) as designated by FEMA.
    6. The capacity and capabilities of Lead Applicants, who are selected for two awards under this NOFO,
    to successfully perform, manage, and oversee both grants within the three-year grant term and the
    risks posed by multiple awards to successful grant performance.
    7. The extent to which the EPA funding may complement or be coordinated with other EPA funding
    or other Federal and / or non-Federal sources of funds / resources to leverage additional resources
    to contribute to the performance and success of the grant. This includes but is not limited to funds
    and other resources leveraged from businesses, labor organizations, non-profit organizations,
    education and training providers, and / or Federal, state, Tribal, and local governments, as
    appropriate.
    8. Duplicate funding considerations as stated in Section IV of the EPA Solicitation Clauses
    incorporated by reference in this NOFO. This includes considering whether funding for the projects
    in the application is available under the Infrastructure Investments and Jobs Act (IIJA), other IRA
    programs, or other funding streams and if so the applicant’s reasons for seeking funding for these
    projects under this NOFO.
    9. Consistent with the language in Section II.B and Appendix H for Target Investment Area A-Tribes
    in Alaska (projects benefitting Alaska Tribal lands), whether an application includes projects to
    assess and/or clean up lands conveyed under the Alaska Native Claims Settlement Act that were
    contaminated at the time of their conveyance from the federal government to an Alaska Native
    Corporation.
    10. Availability of funds.
    In addition, because the objectives of this NOFO are part of a government-wide effort to address
    environmental and climate justice concerns and challenges, information pertaining to proposed selection
    recommendations may be shared by EPA with other Federal, state, local, territorial, or Tribal governmental
    departments or agencies before final selections are made in order to determine whether potential selections
    under this NOFO: (1) are expected to be funded by another department or agency to minimize the possibility
    of duplicate funding, (2) could be affected by permitting, regulatory or other issues involving another
    department or agency, and / or (3) will complement or can be used to leverage funding and capacity-building
    by another department or agency to maximize value. Note that this process is separate from the
    Intergovernmental Review requirements in 40 CFR Part 29.
    Output:
    {
        "scoring_rubric": [
             {
                "track": "Track I",
                "description": "Community Driven Investments for Change",
                "points_or_percentage": "80 points",
                "info": "Includes evaluation of the Community Vision Description (10 points), Selected Strategies (45 points), Community Engagement and Collaborative Governance Plan (15 points), and Community Strength Plan (10 points). Reviewers assess the clarity and impact of the project area description, the integration and rationale for selected Climate Action and Pollution Reduction Strategies, the quality of community engagement and governance planning, and the extent to which economic benefits and displacement avoidance are addressed for disadvantaged communities."
            },
            {
                "track": "Track I",
                "description": "Program Management, Capability, and Capacity",
                "points_or_percentage": "35 points",
                "info": "Includes Performance Management Plan, Outputs/Outcomes (6 points), Project Linkages to the EPA Strategic Plan (4 points), CBO Experience and Commitment (5 points), Programmatic and Managerial Capability and Resources (15 points), and Past Performance (5 points). Reviewers evaluate the applicant's plan for tracking outputs/outcomes, alignment with EPA Strategic Plan goals, organizational experience and commitment to the community, capacity to manage the award, and history of successful grant performance and reporting."
            },
            {
                "track": "Track I",
                "description": "Readiness to Perform, Feasibility, and Sustainability",
                "points_or_percentage": "40 points",
                "info": "Includes Readiness Approach (8 points), Feasibility (9 points), Sustainability (5 points), Program Budget Description (8 points), and Compliance Plan (10 points). Reviewers assess the applicant's readiness to begin work, feasibility of completing the project within three years, sustainability of project benefits, reasonableness and clarity of the budget, and adequacy of compliance planning."
            },
            {
                "track": "Track I",
                "description": "Track I Oral Presentation",
                "points_or_percentage": "45 points",
                "info": "Applicants who pass the written review present orally on: Community Overview (9 points), Strategy Rationale (9 points), Community Engagement and Collaborative Governance (9 points), Management Capacity (9 points), and Performance Challenges (9 points). Reviewers assess the applicant's ability to articulate project impact, rationale for strategies, collaboration plans, management capability, and plans to overcome challenges."
            },
            {
                "track": "Track II",
                "description": "Track II Program Objectives",
                "points_or_percentage": "35 points",
                "info": "Reviewers evaluate how well the project addresses Track II objectives, the methods/tools/trainings for community engagement in government processes, improvements in community-government relationships, and the project's potential to help governments understand and address root causes of environmental and climate justice issues."
            },
            {
                "track": "Track II",
                "description": "Track II Project Collaboration and Participation",
                "points_or_percentage": "20 points",
                "info": "Assesses the extent of meaningful community and stakeholder input in project design and implementation, measures to build trust and accountability between community and government, and the applicant's history of collaboration with disadvantaged communities and stakeholders."
            },
            {
                "track": "Track II",
                "description": "Track II Project Linkages",
                "points_or_percentage": "4 points",
                "info": "Evaluates how well the project supports and advances EPA Strategic Plan Goal 2 (Environmental Justice and Civil Rights)."
            },
            {
                "track": "Track II",
                "description": "Track II Budget",
                "points_or_percentage": "8 points",
                "info": "Assesses the reasonableness and allowability of costs, clarity and detail of the budget, and procedures to ensure timely and efficient expenditure of funds."
            },
            {
                "track": "Track II",
                "description": "Track II Environmental Results",
                "points_or_percentage": "6 points",
                "info": "Evaluates the applicant's plan for tracking and measuring outputs and outcomes, sustainability of project outcomes, and the specificity and relevance of proposed outputs/outcomes."
            },
            {
                "track": "Track II",
                "description": "Track II CBO Experience and Commitment",
                "points_or_percentage": "5 points",
                "info": "Assesses the history, experience, and depth of commitment of the CBO(s) to the disadvantaged community."
            },
            {
                "track": "Track II",
                "description": "Track II Programmatic and Managerial Capability and Resources",
                "points_or_percentage": "16 points",
                "info": "Evaluates organizational experience, staff capacity, project management plans, and financial/legal controls to ensure effective and ethical management of the award."
            },
            {
                "track": "Track II",
                "description": "Track II Past Performance",
                "points_or_percentage": "6 points",
                "info": "Assesses the applicant's past performance in managing grants, meeting reporting requirements, and achieving expected outputs and outcomes. Applicants with no relevant past performance should state so to receive a neutral score."
            }
        ]
    }
    Input:
    7. Selection Criteria: The selection programming with postsecondary
    understanding, all applicants must criteria are from 34 CFR 75.210, the PN education and workforce readiness.
    detail each partner’s financial, NFP, and the notice of final priorities, (k) Measurable annual objectives and
    programmatic, and long-term requirements, definitions, and selection outcomes for the grant, in accordance
    commitment with respect to the criteria published in the Federal with the metrics described in the
    strategies described in the application. Register on July 6, 2011 (76 FR 39589) Promise Neighborhoods Performance
    Under section 4624(c) of the ESEA, (2011 PN NFP). Each selection criterion Indicators for each year of the grant.
    applicants that are nonprofit entities includes the factors that reviewers will (l) An explanation of how the eligible
    must submit a preliminary consider in determining the extent to entity will continuously evaluate and
    memorandum of understanding signed which an applicant meets the criterion. improve the continuum of high-quality
    by each partner entity or agency, which The maximum score for each criterion is pipeline services to provide for
    must include at least one of the included in parentheses following the continuous program improvement and
    following: A high-need LEA; an IHE, as title of the specific selection criterion. potential expansion.
    defined in section 102 of the HEA (20 Points awarded under these selection (m) In addressing the application
    U.S.C. 1002); the office of a chief elected criteria are in addition to any points an requirements in paragraphs (d), (e), and
    official of a unit of local government; or applicant earned under the competitive (f), an applicant must clearly
    an Indian Tribe or Tribal organization as preference priorities in this notice. The demonstrate needs, including a
    defined in section 4 of the Indian Self- maximum score that an application may segmentation analysis, gaps in services,
    Determination and Education receive on the selection criteria is 100 and any available data from within the
    Assistance Act (25 U.S.C. 5304).10 points. last 3 years to demonstrate needs. The
    (h) A description of the process used The selection criteria are as follows:
    applicant must also describe proposed
    to develop the application, including (a) Need for project (up to 20 points).
    activities that address these needs and
    the involvement of family and In determining the need for the
    the extent to which these activities are
    community members. In addressing this proposed project, the Secretary
    evidence-based (as defined in this
    paragraph, an applicant must provide a considers the following factors:
    notice). The applicant must also
    description of the process used to (1) The magnitude or severity of the
    describe its experience, or its partner
    develop the application, which must problem to be addressed by the
    organizations’ experience, if applicable,
    include the involvement of an LEA(s) proposed project (34 CFR 75.210).
    providing these activities, including any
    (including but not limited to the LEA’s (2) The extent to which specific gaps
    data demonstrating effectiveness.
    or LEAs’ involvement in the creation or weaknesses in services,
    Program Requirements: Each
    and planning of the application and a infrastructure, or opportunities have
    applicant that receives a grant award for
    signed Memorandum of Understanding) been identified and will be addressed by
    the PN competition must use the grant
    and at least one public elementary or the proposed project, including the
    funds to implement the pipeline
    secondary school that is located within nature and magnitude of those gaps or
    services and continuously evaluate the
    the identified geographic area that the weaknesses (34 CFR 75.210).
    success of the program and improve the
    grant will serve. 1SECITON (b) Quality of project services (up to
    program based on data and outcomes.
    (i) A description of the strategies that
    30 points). Section 4624(d) of the ESEA. Applicants
    will be used to provide pipeline services
    The Secretary considers the quality of may use not less than 50 percent of
    htiw
    the services to be provided by the grant funds in year one, and not less
    DORP32NQX11KSD 10The original citation in ESEA section 4622 was
    proposed project. In determining the than 25 percent of grant funds in year
    to 25 U.S.C. 450b, but 25 U.S.C. 450b was
    quality of the project services, the two, for planning activities to develop
    editorially reclassified as 25 U.S.C. 5304. We use
    Secretary considers: and implement pipeline services. the updated citation throughout this notice.
    no
    rettol
    VerDate Sep<11>2014 20:13 Jun 26, 2024 Jkt 262001 PO 00000 Frm 00015 Fmt 4703 Sfmt 4703 E:\FR\FM\27JNN1.SGM 27JNN1

    --- PDF Page 6 ---
    53600 Federal Register/Vol. 89, No. 124/Thursday, June 27, 2024/Notices
    appropriate entities to such support (34 from other programs or policies (1) The quality and sufficiency of
    CFR 75.210). supported by community, State, and strategies for ensuring equal access and
    Federal resources (34 CFR 75.210). treatment for eligible project (2) The extent to which the applicant
    participants who are members of groups (d) Quality of the management plan identifies existing neighborhood assets
    that have traditionally been (up to 15 points). and programs supported by Federal,
    underrepresented based on race, color, State, local, and private funds that will The Secretary considers the quality of
    national origin, gender, age, or disability be used to implement a continuum of the management plan for the proposed
    (34 CFR 75.210). solutions (2011 PN NFP). project. In determining the quality of the
    (2) The extent to which the proposed management plan for the proposed (3) The applicant’s capacity (e.g., in
    project involves the development or project, the Secretary considers the terms of qualified personnel, financial
    demonstration of promising new following factors: resources, or management capacity) to
    strategies that build on, or are (1) The adequacy of the management further develop and bring to scale the
    alternatives to, existing strategies (34 plan to achieve the objectives of the proposed process, product, strategy, or
    CFR 75.210). proposed project on time and within practice, or to work with others to
    (3) The likelihood that the proposed
    budget, including clearly defined ensure that the proposed process,
    project will result in system change or
    responsibilities, timelines, and product, strategy, or practice can be
    improvement (34 CFR 75.210).
    milestones for accomplishing project further developed and brought to scale,
    (4) The extent to which the services
    tasks (34 CFR 75.210). based on the findings of the proposed
    to be provided by the proposed project
    project (34 CFR 75.210). (2) The adequacy of procedures for
    involve the collaboration of appropriate
    ensuring feedback and continuous 8. Performance Measures: The
    partners for maximizing the
    improvement in the operation of the Secretary has established performance
    effectiveness of project services (34 CFR
    proposed project (34 CFR 75.210). indicators (i.e., performance measures)
    75.210).
    (3) The experience, lessons learned, for the PN program under section
    (c) Quality of project design (up to 20
    and proposal to build capacity of the 4624(h) of the ESEA and 34 CFR 75.110.
    points).
    applicant’s management team and Performance indicators established by
    In determining the quality of project
    project director in collecting, analyzing, the Secretary include improved
    design for the proposed project, the
    and using data for decision making, academic and development outcomes
    Secretary considers the following
    learning, continuous improvement, and for children, including indicators of
    factors:
    accountability, including whether the school readiness, high school (1) The extent to which the applicant
    applicant has a plan to build, adapt, or graduation, postsecondary education describes a plan to create a complete
    expand a longitudinal data system that and career readiness, and other pipeline of services, without time and
    integrates student-level data from academic and developmental outcomes. resource gaps, that is designed to
    multiple sources in order to measure These outcomes promote data-driven prepare all children in the
    progress while abiding by privacy laws decision-making and access to a neighborhood to attain a high-quality
    and requirements (2011 PN NFP). community-based continuum of high- education and successfully transition to
    quality services for children living in (e) Adequacy of resources (up to 15 college and a career (PN NFP).
    the most distressed communities of the points). (2) The potential and planning for the
    United States, beginning at birth. All The Secretary considers the adequacy incorporation of project purposes,
    grantees will be required to submit data of resources for the proposed project. In activities, or benefits into the ongoing
    annually against these performance determining the adequacy of resources work of the applicant beyond the end of
    measures as part of their annual for the proposed project, the Secretary the grant (34 CFR 75.210).
    performance report. considers: (3) The extent to which the proposed
    The Secretary establishes, in Table 1, (1) The potential for continued project will integrate with or build on
    the following performance indicators support of the project after Federal similar or related efforts to improve
    under section 4624(h) of the ESEA and funding ends, including, as appropriate, relevant outcomes (as defined in 34 CFR
    77.1Ö), 34 CFR 75.110: the demonstrated commitment of using existing funding streams
    Output:
    {
         "scoring_rubric": [
            {
                "track": null,
                "description": "Need for project",
                "points_or_percentage": "Up to 20 points",
                "info": "The magnitude or severity of the problem to be addressed by the proposed project, and the extent to which specific gaps or weaknesses in services, infrastructure, or opportunities have been identified and will be addressed by the proposed project, including the nature and magnitude of those gaps or weaknesses."
            },
            {
                "track": null,
                "description": "Quality of project services",
                "points_or_percentage": "Up to 30 points",
                "info": "The quality of the services to be provided by the proposed project, including: (1) the quality and sufficiency of strategies for ensuring equal access and treatment for eligible project participants who are members of groups that have traditionally been underrepresented; (2) the extent to which the project involves development or demonstration of promising new strategies; (3) the likelihood that the project will result in system change or improvement; and (4) the extent to which the services involve collaboration of appropriate partners for maximizing effectiveness."
            },
            {
                "track": null,
                "description": "Quality of project design",
                "points_or_percentage": "Up to 20 points",
                "info": "(1) the extent to which the applicant describes a plan to create a comprehensive pipeline of services, without time and resource gaps, designed to prepare all children in the neighborhood to attain a high-quality education and successfully transition to college and a career; (2) the potential and planning for the incorporation of project purposes, activities, or benefits into the work of the applicant beyond the period of the grant; and (3) the extent to which the proposed project will integrate with or build on similar or related efforts to improve relevant outcomes, using existing funding streams from other programs or policies supported by community, State, and Federal resources."
            },
            {
                "track": null,
                "description": "Quality of the management plan",
                "points_or_percentage": "Up to 15 points",
                "info": (1) the adequacy of the management plan to achieve the objectives of the proposed project on time and within budget, including clearly defined responsibilities, timelines, and milestones; (2) the adequacy of procedures for ensuring feedback and continuous improvement in the operation of the proposed project; and (3) the experience, lessons learned, and proposal to build capacity of the applicant's management team and project director in collecting, analyzing, and using data for decision making, learning, continuous improvement, and accountability, including plans to build, adapt, or expand a longitudinal data system."
            },
            {
                "track": null,
                "description": "Adequacy of resources",
                "points_or_percentage": "Up to 15 points",
                "info": "(1) the potential for continued support of the project after Federal funding ends, including the demonstrated commitment of appropriate entities to such support; and (2) the applicant's capacity (e.g., in terms of qualified personnel, financial resources, or management capacity) to further develop and bring to scale the proposed process, product, strategy, or practice, or to work with others to ensure that the proposed process, product, strategy, or practice can be further developed and brought to scale, based on the findings of the proposed project."
            }
        ],
    }
    Input:
    --- PDF Page 12 ---
    2.5 ELIGIBLE ACTIVITIES
    This grant program funds activities and costs as permitted by the laws, regulations, rules,
    and guidance governing the use of funds, as identified in the relevant sections of this RFA.
    Only activities authorized under this RFA are eligible for reimbursement and payment
    under any Grant Agreement awarded as a result of this Solicitation.
    The Grantee must provide evidence-based nutrition education and obesity prevention
    activities to SNAP Eligible Populations. The activities must be provided through the
    implementation of strategies and interventions for the selected approaches for the Project
    Priorities.
    The Grantee must provide the services as required and in accordance with the requirements
    in this RFA, and Requirements. Exhibit B, Grant
    2.6 PROGRAM REQUIREMENTS
    All activities funded under this RFA must meet all the requirements set forth in Exhibit B,
    Grant Requirements.
    The Grantee must carry insurance in accordance with the requirements set forth in Exhibit
    throughout the duration of the Contract. L, Insurance Requirements
    REPORTS 2.7 REQUIRED
    HHSC will monitor the Grantee’s performance, including, but not limited to, through
    review of financial and programmatic reports and performance measures, under any Grant
    Agreement awarded as result of this RFA.
    The Grantee must complete and submit all the applicable Required Reports in Exhibit C,
    in the format and by the date specified by HHSC. The Required Required Reports,
    Reports must be supported by documentation of the activities and services provided.
    Grantee must provide all applicable reports in the format specified by HHSC in an accurate,
    complete, and timely manner and shall maintain appropriate supporting backup
    documentation. Failure to comply with submission deadlines for required reports, Financial
    Status Reports (FSRs) or other requested information may result in System Agency, in its
    sole discretion, placing the Grantee on financial hold without first requiring a corrective
    action plan in additional to pursuing any other corrective or remedial actions under the
    Grant Agreement.
    PCS 560 HHS RFA Template RFA No. HHS0015831 Page 12 of 42
    Version 1.70
    Revision Date 11/13/2024

    --- PDF Page 19 ---
    6.1 NARRATIVE PROPOSAL
    Using attached to this RFA, Applicants are required to use Form C, Narrative Proposal
    this template for submitting the personnel, and organizational narrative. All Applicants
    must use this form to detail the Applicant’s mission and purpose, experience, and capacity
    in managing similar Projects, approach to meeting the Projects requirements, and Key
    Personnel and Organizational Staffing Plans. This form is essential as it ensures that all
    Applicants deliver consistent and comprehensive services, enabling a thorough evaluation
    of their ability to successfully execute the Supplemental Nutrition Assistance Program
    Education (SNAP-Ed) Project.
    6.2 ANNUAL WORK PLAN
    The Applicant must complete and submit Form C-1, SNAP-Ed Annual Project Work
    included in this RFA with their grant Application. All Applicants are required to use Plan
    this form and provide detailed responses to the questions outlined, including Project
    Description, State Priority Goals, and Intervention Approaches. Form C-1, SNAP-Ed
    is required as it ensures that all Applicants deliver consistent Annual Project Work Plan
    and comprehensive services, enabling a thorough evaluation of their ability to successfully
    execute the Supplemental Nutrition Assistance Program Education (SNAP-Ed) Project.
    6.3 EXPENDITURE PROPOSAL
    Attached of this RFA is the template for Exhibit E, Expenditure Proposal Template,
    submitting the Expenditure Proposal. Applicants must develop the Expenditure Proposal
    to support their Proposed Project and in alignment with the requirements described in this
    RFA.
    Applicants must ensure that Project costs outlined in the Expenditure Proposal are
    reasonable, allowable, allocable, and developed in accordance with applicable State and
    federal Grant Requirements. Reasonable costs are those if, in nature and amount, do not
    exceed that which would be incurred by a prudent person under the circumstances
    prevailing at the time the decision was made to incur the cost. A cost is allocable to a
    particular cost objective if the cost is chargeable or assignable to such cost objective in
    Cost accordance with relative benefits received. See 2 CFR Part 200.403 or TxGMS
    Principles, Basic Considerations (pgs. 32-33), for additional information related to factors
    affecting allowability of costs.
    Applicants must utilize the Budget template provided, Exhibit E, Expenditure Proposal
    and identify all Budget line items and matching costs, if applicable. Budget Template,
    categories must be broken out into specific Budget line items that allow HHSC to
    determine if proposed costs are reasonable, allowable, and necessary for the successful
    performance of the Project. Applicants must enter all costs in the Budget tables and explain
    PCS 560 HHS RFA Template RFA No. HHS0015831 Page 19 of 42
    Version 1.70
    Revision Date 11/13/2024

    9.4 EVALUATION CRITERIA
    Applications will be evaluated and scored in accordance with the following scoring
    criteria using Exhibit O, Evaluation Tool.
    Qualified Applications shall be evaluated based upon: Scoring Criteria:
    A. Personnel and Organization (15%);
    B. Required Interventions (30%);
    C. Grant Requirement (10%)
    D. Annual Project Work Plan (15%); and
    E. Cost (30%).
    Output:
    {
        "scoring_rubric": [
            {
                "track": null,
                "description": "Personnel and Organization",
                "points_or_percentage": "15%",
                "info": "Evaluation of the applicant's personnel and organizational capacity, including mission, purpose, experience, and staffing plans as detailed in the Narrative Proposal (Form C)."
            },
            {
                "track": null,
                "description": "Required Interventions",
                "points_or_percentage": "30%",
                "info": "Assessment of the applicant's approach to implementing required nutrition education and obesity prevention interventions for the SNAP-Ed target population, as described in the application."
            },
            {
                "track": null,
                "description": "Grant Requirement",
                "points_or_percentage": "10%",
                "info": "Evaluation of the applicant's ability to meet all grant requirements as outlined in the RFA and supporting exhibits."
            },
            {
                "track": null,
                "description": "Annual Project Work Plan",
                "points_or_percentage": "15%",
                "info": "Review of the applicant's Annual Project Work Plan (Form C-1), including project description, state priority goals, and intervention approaches."
            },
            {
                "track": null,
                "description": "Cost",
                "points_or_percentage": "30%",
                "info": "Assessment of the proposed budget for reasonableness, allowability, allocability, and alignment with project goals, as submitted in the Expenditure Proposal (Exhibit E)."
            }
        ]
    }

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a JSON object with a scoring_rubric field. The scoring_rubric field should contain an array of JSON objects with the following fields:
        * track (text or null)
        * description (text)
        * ponts_or_percentage (text)
        * info (text)
    If scoring criteria are not grouped by track, track should be null.
"""
