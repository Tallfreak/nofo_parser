# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

prompt = r"""
    # Directive:
    For the attached file, extract the project activities that are eligible to receive funds and the project activities that are ineligible to receive funds. Summarize this information. If there are activities for different tracks, organize the activities by track. Do NOT guess or make up an answer. In the RARE case the information is not present, return 'Information is not available'.

    # Examples:
    Input:
    Fiscal Year 2025 Key Objectives
    at least one Application proposals must include of the three objectives identified below. Proposals
    may contain more than one objective. As noted in Section 4, applicants must map their proposed
    activities and indicators measuring success to the objective(s) using the “Activities/Indicators
    Tracker.” If awarded, grantees will be required to use the FNS-908 Performance Progress Report
    to report on progress towards activities that align with the required objective(s) listed on the
    “Activities/Indicators Tracker.” Carefully considering proposed activities and indicators will
    prepare grantees for their performance progress reporting requirements if awarded.
    6

    --- PDF Page 7 ---
    The project examples aligned with each objective listed below are only suggestions. A PTIG
    project may assist State agencies in making investments in systems to improve efficiency, provide
    excellent customer service, and meet Federal standards as they face operational challenges. FNS
    welcomes other projects that support these objectives and encourages applicants to propose
    innovative ideas to solve both common and unique problems associated with the SNAP
    processes.1 application and eligibility
    Modernize SNAP customer service and client communication to improve efficiency, 1.
    transparency, and accuracy in application processing and eligibility determinations.
    Proposals will use technology-based tools to improve the customer experience and allow
    households to manage their cases. Proposals may include activities such as:
    Creating or improving client self-service options, such as scripted chat bots or
    o
    “virtual agents” to answer questions in alignment with FNS’ guidance on the use of
    personnel,2 non-merit updating personal information via a client portal, or tracking
    their application status online;
    Improving communication with applicants and participants with electronic notices
    o
    (eNotices) and text messaging reminders;
    Ensuring applications, verification requirements, notices, and other client
    o
    communications are clear, in plain language, and accompanied by guides or
    instructions for easy understanding;
    Reducing technology-based barriers to improve service delivery, such as
    o
    expanding mobile document upload options, or expanding partnerships with local
    agencies; or
    Developing and/or enhancing mobile responsive websites, mobile applications,
    o
    online applications, and online portals to streamline self-service options.
    Improve administrative infrastructure and day-to-day SNAP operations in processing 2.
    applications and determining eligibility. Proposals will employ technology to improve
    service levels, and accurate and timely case processing, as required by law. Proposals may
    include activities such as:
    Increasing State call center capacity, such as by adding phone lines, improving
    o
    establishing automated telephone systems like phone trees, or enhancing
    telephonic interview and telephonic signature capabilities, or implementing
    2 Interactive Voice Response (IVR) technology or “virtual agents”;
    Improving paper document processing using intelligent or optical character
    o
    recognition (I/OCR), or robotic process automation (RPA) technology to process
    no-change periodic reports, automate data match evaluation and clearance (as
    allowable),;
    Developing workload management dashboards or data analysis tools to monitor
    o
    workload, case status, outstanding tasks, timeliness, and other key metrics;
    Creating a hard-coded or scripted policy chat bot that would give eligibility
    o
    workers answers to SNAP policy questions; or
    Enhancing eligibility systems and applications, such as using an Application
    o
    Programming Interface (API) or software bot to automatically register an
    1 Links to FNS resources related to these examples and other potential projects are in Appendix A: Tips for Proposal
    Writers.
    2 See Appendix E: Glossary of Advanced Automation Terms for more information.
    7

    --- PDF Page 8 ---
    application in the eligibility system, eliminate duplicate entry, or prepopulate
    eligibility systems from an online application.
    Invest in technology and systems to coordinate application and eligibility determination 3.
    processes, including verification practices, between SNAP and other Federal, State, and
    local assistance programs. Proposals will improve administrative efficiency, as allowable
    by program requirements, when processing combined applications. Proposals may include
    activities such as:
    Developing combined applications and partnerships across State-operated
    o
    assistance programs to increase administrative efficiency and alignment between
    programs;
    Enhancing cross-program enrollment through integrated mobile applications,
    o
    online portals, and automated technologies for data population such as
    Application Programming Interfaces (APIs) or robotic process automation (RPA);
    Improving data sharing and verification between SNAP and other Federal, State,
    o
    and local assistance programs within the State agency; or
    Creating a technology improvement plan to enhance or develop accurate cross-
    o
    enrollment or administration between SNAP and other programs, as permitted by
    law.
    Output:
    {
        "eligible_activities":
            [
                {
                    "track": null,
                    "eligible": [
                        "Modernize SNAP customer service and client communication to improve efficiency, transparency, and accuracy in application processing and eligibility determinations (e.g., client self-service options, chat bots, virtual agents, client portals, online application status tracking, eNotices, text messaging reminders, plain language communications, mobile document upload, mobile responsive websites, mobile applications, online portals).",
                        "Improve administrative infrastructure and day-to-day SNAP operations in processing applications and determining eligibility (e.g., increasing call center capacity, adding phone lines, automated telephone systems, telephonic interview/signature capabilities, Interactive Voice Response (IVR) technology, intelligent or optical character recognition (I/OCR), robotic process automation (RPA), workload management dashboards, data analysis tools, policy chat bots, enhancing eligibility systems and applications, APIs, software bots for application registration, eliminating duplicate entry, prepopulating eligibility systems).",
                        "Invest in technology and systems to coordinate application and eligibility determination processes, including verification practices, between SNAP and other Federal, State, and local assistance programs (e.g., developing combined applications, integrated mobile applications, online portals, automated technologies for data population such as APIs or RPA, improving data sharing and verification, technology improvement plans for cross-enrollment or administration).",
                            ],
                    "ineligible": [
                        "Ongoing costs to carry out an existing project (PTIG funds are for new projects only).",
                        "Budgeting more than 25%% of grant funds towards SNAP outreach activities.",
                        "Drafting or printing of informational materials.",
                        "Pure application assistance",
                        "Screening or pre-qualifying applicants.",

                        "Pre-award costs (costs incurred before the grant is awarded).",
                        "Any project activities that require waivers of SNAP regulations.",
                        "Any costs or activities not allowable, reasonable, necessary, or allocable under 2 CFR Part 200 Subpart E - Cost Principles.",
                        "Projects that are predicated on waivers of SNAP regulations.",
                    ]
                }
            ]
        }
    }
    Input:
    Details of Track I Application Requirements
    Applicants must include at least one project aligned with at Requirement 1. Climate Action Strategies:
    least one of the Climate Action Strategies identified below. When addressing the strategy in their
    application, applicants should describe relevant challenges faced in the Project Area and how the selected
    Climate Action Strategy(ies) and associated project(s) will address those challenges. Each Climate Action
    Strategy outlined below is focused on building short-term and long-term climate resilience, reducing GHGs,
    and providing additional co-benefits so that impacted communities can adapt to the changing climate.
    Applicants are also encouraged, as applicable, to integrate processes that minimize burdens to human health
    and the environment while maximizing benefits to the Project Area through such means as integrating
    nature-based solutions, utilization of low-carbon building materials, or sourcing sustainable products and
    materials to perform the projects. When selecting a Climate Action Strategy and designing their climate
    action projects, applicants may refer to the National Climate Resilience Framework released in September
    2023.
    Examples of project activities and guidelines associated with the strategies can be found in Appendix C.
    While applicants may select from among the examples in the Appendix, applicants may also submit other
    types of project activities as long as they are consistent with a Climate Action Strategy described in Section
    I.G of the NOFO and are eligible for funding under §138(b)(2) of the CAA.
    Strategy 1: Green Infrastructure and Nature-Based Solutions
    Many disadvantaged communities face complex climate challenges, such as urban heat island effects
    and flooding risks. Strategy 1 supports using nature-based solutions (NBS), also referred to as green
    infrastructure, to address such climate risks. Nature-based solutions are generally actions to protect,
    sustainably manage, or restore natural systems to address the impacts of climate change, while
    environment.4 simultaneously providing benefits for people and the Projects under this strategy can
    include planting shade trees, restoring native plants and wetlands to capture stormwater, and deploying
    other green infrastructure solutions that often have the co-benefit of reducing GHG emissions.
    Communities also may incorporate vegetation or similar natural features into traditional infrastructure.
    Strategy 2: Mobility and Transportation Options for Preventing Air Pollution and Improving
    Public Health and Climate Resilience
    Many disadvantaged communities lack access to affordable low- or zero-emission transportation
    options, leading to disproportionate difficulties in daily life, limiting access to educational and
    4 Applicants may use the White House’s Nature-Based Solutions Resource Guide as a resource for integrating nature-
    based solutions.
    11

    --- PDF Page 12 ---
    economic opportunities, and creating vulnerability to climate risks. Strategy 2 focuses on providing
    community members with access to low- and zero-emission technologies to improve their overall health
    and well-being, reduce emissions, and increase access to important community destinations such as
    schools, workplaces, health care centers, and community spaces. Projects funded under this strategy
    may include installing protected bike lanes or walking paths, supplying traditional or electric bikes to
    community members, and deploying other low- or zero-emission transportation solutions. The impact
    of such projects could include improved public health outcomes, reduced GHG emissions from the
    transportation sector, more equitable access to community resources, increased community
    connectivity and safety, and greater community resilience to extreme weather events.
    Strategy 3: Energy-Efficient, Healthy, and Resilient Housing and Buildings
    Residential and commercial buildings are a significant source of GHG emissions due to the large
    amounts of electricity consumed for heating, cooling, lighting, and other similar functions. Many
    disadvantaged communities also face a disproportionately high energy burden, defined as the
    percentage of gross household income spent on energy costs. Many factors can influence high energy
    burden, including higher-cost fuels, such as propane or other bottled fuels, and energy-inefficient homes
    due to a lack of insulation in older homes or older appliances. Strategy 3 supports investments in low-
    and zero-emission technologies and energy efficiency upgrades that can help decarbonize residential
    and commercial buildings, decrease energy burden, and increase resilience for communities. Many of
    these activities also contribute to positive public health outcomes by improving indoor air quality and
    the safety and comfort of buildings. Co-benefits associated with this strategy can be maximized by
    combining additional Climate Action and Pollution Reduction Strategies to improve indoor air quality
    and / or produce additional resiliency benefits. This strategy can support a range of residential and
    commercial buildings, including single-family homes, multi-family housing buildings, small
    businesses, community health facilities, community centers, nonprofit offices, schools, and other
    similar community-serving buildings.
    Strategy 4: Microgrid Installation for Community Energy Resilience
    Many disadvantaged communities suffer from unreliable access to electricity, a problem that is
    becoming more acute due to increased heating and cooling demands during extreme weather events
    driven by climate change. Strategy 4 supports the installation of microgrids powered by low- and zero-
    emission renewable energy to improve electric reliability, enhance overall energy efficiency, reduce
    emissions of GHG and other air pollutants, and build a community’s capacity to prepare for and
    withstand power disruptions. The U.S. Department of Energy defines microgrids as “a group of
    interconnected loads and distributed energy resources within clearly defined electrical boundaries that
    acts as a single controllable entity with respect to the grid.” A microgrid can operate autonomously
    when disconnected from the grid or when there is no grid to connect to, such as in some remote
    communities. When connected and operated with the grid, a microgrid can provide grid ancillary
    services.
    Strategy 5: Community Resilience Hubs
    Many disadvantaged communities lack the resources to evacuate in a safe and timely manner when
    disaster strikes or is imminent. Strategy 5 supports the creation of, or upgrades to, community-level
    resilience hubs, which are public-serving spaces that provide shelter and essential services during
    extreme weather, natural hazards, or other events causing or contributing to an emergency or disaster,
    such as dangerous wildfire woodsmoke, toxic releases, industrial fires, or similar hazardous chemical
    incidents. These community-level resilience hubs can also serve as community-convening spaces that
    provide educational activities and related emergency and disaster preparedness resources to community
    residents year-round.
    12

    --- PDF Page 13 ---
    Strategy 6: Brownfield Redevelopment for Emissions Reduction and Climate Resilience
    Many disadvantaged communities contain brownfield sites that impede economic development.
    Redeveloping brownfields provides an opportunity to make investments that contribute to community
    revitalization, resilience, and GHG emissions reduction. Redeveloping brownfield sites also supports
    infill development that significantly reduces residential vehicle use and the associated GHG emissions.
    Strategy 6 supports the redevelopment of brownfield sites that have already been cleaned up, or where
    a site assessment indicates that cleanup is not necessary for reuse. These projects should seek to improve
    energy efficiency through investments in low- and zero-emission technologies, integrate climate
    resiliency, and / or mitigate climate change impacts while also promoting economic development and
    improving public health for residents. Examples could include construction of a public park or
    partnering on a LEED Certified low-income housing project on a former brownfield site.
    Note: Projects funded under this Climate Action Strategy must be performed on sites where, at the time
    of application submission, the applicant demonstrates that cleanup is complete or that the site does not
    require any cleanup activities for the intended use or reuse of the site. See Section III.D.8 and
    Appendix C section on this Strategy.
    Strategy 7: Waste Reduction and Management to Support a Circular Economy
    Disadvantaged communities often bear the brunt of environmental contamination from improper
    disposal of physical waste, or from disposal in landfills adjacent to those communities. This strategy
    economy5 supports circular activities and promotes sustainable use of natural resources to keep
    materials and products in circulation for as long as possible, resulting in the reduction of GHG
    emissions and other pollution across a product’s lifecycle. Examples of these projects may include
    efforts to reduce food waste (e.g., composting, anaerobic digestors), or to promote the reduction, reuse,
    and recycling of disaster debris, construction and demolition debris, and other materials and products.
    Project activities should demonstrate that they will result in materials being diverted from end-disposal
    facilities (e.g., landfills, incinerators) to reduce GHG emissions, toxic air pollution, and soil and water
    pollution.
    Strategy 8: Workforce Development Programs for Occupations that Reduce Greenhouse Gas
    Emissions and Air Pollutants
    Individuals in disadvantaged communities often lack pathways into fast-growing and well-paying job
    opportunities related to environmental and climate justice. This strategy allows applicants to propose
    workforce development programs to enable individuals in these communities to pursue career pathways
    in fields related to the reduction of GHG emissions and other air pollutants. Strong workforce
    development proposals should include all three of the following features, as detailed in Appendix C:
    (1) multi-sectoral partnerships that bring together workforce expertise and enable pathways into high-
    quality careers that help reduce GHG emissions and other air pollutants; (2) high-quality training
    models, such as pre-apprenticeships or Registered Apprenticeship Programs, that are worker-centered,
    demand-driven, and lead to good jobs that help reduce GHG emissions and other air pollutants; and
    (3) strategies for recruiting and retaining individuals from disadvantaged communities, especially for
    populations that face barriers to employment. Given that workforce development opportunities can be
    significant to achieving environmental and climate justice in many communities, EPA anticipates
    making a minimum of fifteen awards for high-ranking applications that include a workforce training
    program as further described in Section V.E. Note that it is a statutory requirement that workforce
    development activities funded under this program be focused specifically on reducing greenhouse gas
    emissions and other air pollutants.
    5 A circular economy keeps materials, products, and services in circulation for as long possible.
    13

    --- PDF Page 14 ---
    Applications must include at least one project aligned Requirement 2. Pollution Reduction Strategies:
    with at least one of the Pollution Reduction Strategies identified below. When addressing the strategy in
    their application, applicants should describe relevant challenges faced in the Project Area and how the
    selected Pollution Reduction Strategy(ies) will address those challenges. Each Pollution Reduction Strategy
    outlined below is focused on pollution monitoring, prevention, and remediation of quantifiable and health-
    harming pollutants.
    Applications that include activities to increase monitoring capabilities or raise community awareness of
    pollution must also include an associated remediation, implementation, or infrastructure pollution reduction
    project that addresses the identified pollution issue.
    Examples of project activities and guidelines associated with the strategies can be found in Appendix D.
    While applicants may select from among the examples in the Appendix, applicants may also submit other
    types of project activities as long as they are consistent with a Pollution Reduction Strategy described in
    Section I.G of the NOFO and are eligible for funding under §138(b)(2) of the CAA.
    Strategy 1: Indoor Air Quality and Community Health Improvements
    Disadvantaged communities often face high levels of indoor air pollution from several sources,
    including mold, lead paint, radon, asbestos, fossil fuel combustion, and pollution from outdoors that
    seeps inside. These pollutants can have a detrimental impact to human health, particularly for
    vulnerable populations including children, the elderly, and people with health conditions like asthma
    [Start Table 1]
        air toxins / toxics and how to
    curriculum development, outreach strategies, public education activities) and direct
    [End Table 1]
    monitor them (e.g., curriculum development, outreach strategies, public education activities) and direct
    assessment and remediation to reduce harmful air pollution (e.g., installation of filtration systems,
    building retrofits that address multiple sources of pollution, replacement of wood heaters that do not
    meet EPA standards, asbestos abatement in schools).
    Strategy 2: Outdoor Air Quality and Community Health Improvements
    Outdoor air pollution from mobile and stationary sources can compromise human health and the
    environment in many ways, including by triggering asthma attacks and heart attacks, exacerbating
    respiratory disease, and causing children and adults to miss school and work on bad air days. Activities
    funded under Strategy 2 could include: funding the purchase, upgrade, and / or maintenance of
    equipment and technology to allow for the inspection, testing, monitoring, and sampling of air
    pollution; purchasing equipment that limits community exposure to outdoor air pollutants; and reducing
    exposure to near-road pollution, pollution from airports and ports, and mobile source pollution. This
    could include land use and zoning policies that enable households to live in affordable, dense, and
    vibrant communities within urban and rural areas. These activities can be bolstered by educating the
    public on air toxins / toxics and how to monitor them (e.g., curriculum development, outreach, public
    education), and communication of air pollution assessment results to reduce exposure, including during
    environmental emergencies or events where the risk of pollution exposure is high.
    Strategy 3: Clean Water Infrastructure to Reduce Pollution Exposure and Increase Overall
    System Resilience
    Disadvantaged communities often lack access to clean water and clean drinking water. Functional water
    infrastructure is essential for protecting the quality of drinking water resources as well as the safety of
    recreational waters communities use for subsistence fishing, swimming, and other activities everyone
    deserves to enjoy. Strategy 3 addresses challenges communities face in accessing clean, reliable
    drinking water and wastewater treatment. Projects funded under this strategy may include focused
    6 Indoor Air Quality (IAQ).
    14

    --- PDF Page 15 ---
    infrastructure investments that can be completed within the three-year project period and within the
    funding amounts specified in this NOFO, as well as assessment and planning that will enable
    communities to better access tens of billions of dollars in federal water infrastructure funding from
    other sources such as EPA’s Clean Water and Drinking Water State Revolving Funds. Targeted
    infrastructure projects can include identification and replacement of lead pipes in homes and public
    spaces, improved resilience of water systems through deployment of backup power such as onsite
    renewable energy and storage, targeted efficiency upgrades, septic to sewer conversions, lining waste
    lagoons, and investments in redundancy such as backup wells. Assessment and planning efforts could
    include, for example, a leak detection and pipe replacement plan, or a PFAS monitoring program that
    informs a funding application to one of several sources of state and federal funding.
    Strategy 4: Safe Management and Disposal of Solid and Hazardous Waste
    Disadvantaged communities are disproportionately exposed to solid and hazardous waste, which
    negatively impacts public health. This strategy supports pollution prevention, recycling, and disposal
    activities related to the management of solid and hazardous waste, such as discarded electronics, tires,
    single-use plastics, and other disposable items. Community-level responses to these challenges could
    include, for example, the purchase of equipment and the development of facilities to manage solid and
    hazardous waste to improve public health outcomes. Brownfields cleanup is not contemplated under
    this strategy and is not a Community Change Grants program priority.
    Track I applications Requirement 3. Community Engagement and Collaborative Governance Plan:
    must include a Community Engagement and Collaborative Governance Plan. Successful implementation
    of environmental and climate justice projects requires relationships and meaningful engagement among an
    ecosystem of community leaders and members alongside partners across many sectors. This plan is required
    to help ensure that grant activities are driven and informed by the views of the Project Area community and
    are accomplished through collaboration among key stakeholders, The plan should describe how the
    applicant will engage, educate, and be responsive to community members throughout project development
    and / or implementation. Additionally, the plan should incorporate a Collaborative Governance Structure
    that demonstrates how the Lead Applicant and Collaborating Entities (as described in Section III.A) will
    work together to successfully implement the grant in a timely, effective, and equitable manner.
    The Community Engagement and Collaborative Governance Plan cannot exceed 10 single spaced pages –
    excess pages will not be reviewed. It should address the following elements and any others the applicant
    deems relevant to their projects:
    • Conducted: The applicant should demonstrate Past Community Outreach and Engagement
    what outreach and engagement methods were used to engage with the Project Area community,
    including any with specific neighborhoods or groups, and how this impacted the selection of the
    strategies and associated projects as well as the applicant’s implementation approach.
    • The applicant should demonstrate the specific Community Engagement Plan Implementation:
    community engagement methods, as well as how they will mitigate barriers and involve relevant
    governmental stakeholders, necessary to support overall implementation including:
    The applicant should describe the Clear Methods for Engagement and Transparency:
    o
    following elements:
     Outreach methods that provide opportunities for broad and diverse community
    member involvement in project development and / or implementation and
    feedback during grant performance.
     Transparent mechanisms that will promote meaningful accountability to the needs
    and preferences of residents in the Project Area.
    15

    --- PDF Page 16 ---
     Mechanism(s) that will be used to continuously inform the community before and
    during project implementation on project status, benefits available to them through
    the project, and indicators being tracked, such as air quality improvements or trees
    planted.
    Barriers: The applicant should describe measures to minimize and mitigate Mitigating
    o
    barriers around community engagement and participation in project development and / or
    implementation including but not limited to those related to linguistic differences,
    communication challenges, disabilities, inaccessible technology, lack of trust or awareness,
    care.7 transportation, childcare, and elderly / adult
    Involvement: As applicable, the applicant should demonstrate the support Government
    o
    and involvement of government agencies needed to facilitate successful grant performance.
    For example, projects that intersect with local-government authorities such as permitting,
    planning, and zoning are encouraged to demonstrate the involvement and cooperation of
    local government authorities.
    • Structure: The applicant should provide details regarding the roles Collaborative Governance
    and responsibilities of the Lead Applicant, Collaborating Entities, and community residents and /
    or community-selected representatives for implementing, managing, and overseeing the
    application’s project activities, including how they should meet regularly to discuss project
    implementation. The description should include at a minimum:
    Outreach methods to solicit community representatives and processes to choose
    o
    representatives to enable a broad cross-section of community representatives to participate
    so different voices are heard.
    An explanation of how the Lead Applicant and Collaborating Entities will coordinate with
    o
    each other and community members to inform and engage the community on project
    development and progress.
    An outline of the planned decision-making processes between the Lead Applicant and
    o
    Collaborating Entities, including procedures to ensure that decisions are transparent and
    can be made in an expedited manner when necessary.
    Processes for replacing a Collaborating Entity to ensure that the replacement entity has
    o
    comparable skills, qualifications, expertise, community support, and experience to avoid
    any adverse impact on grant performance. EPA approval of the qualifications, expertise,
    and experience of the replacement Collaborating Entity will be required pursuant to 2 CFR
    200.308I(2) and / I(c)(6).

    --- PDF Page 21 ---
    Track II Project Examples
    The following are examples of activities that may be proposed under Track II. Applicants may expand or
    refine these examples or submit projects that are not listed below if they demonstrate how they will facilitate
    the engagement of disadvantaged communities in governmental processes.
    Example 1. Educational and Training Programs
    These projects prepare, train, and educate members of disadvantaged communities on how to engage in
    government processes related to environmental and climate justice activities.
    Examples of activities that could be performed under this type of project include but are not limited to:
    • Creating a leadership development program that trains community members to identify
    environmental and climate justice challenges, devise strategies to address them, and recommend
    actions to governmental authorities. Example topics could include how to review public sector
    budgets, navigate specific processes such as land-use ordinances or National Environmental Policy
    Act (NEPA) reviews, and participate effectively in public meetings. The EPA EJ Academy is an
    example of a type of project applicants may consider developing for their own community.
    • Designing and implementing a training program to help members of disadvantaged communities
    effectively participate in advisory boards, commissions, land use authorities, or other bodies that
    involve community members in environmental and climate related policy making.
    • Partnering with a government to develop and / or implement Equity Action Plans that identify and
    address barriers to equity and opportunity and discrimination that disadvantaged communities may
    face. Equity Action Plans should meaningfully incorporate community input and result in city-or-
    statewide transformational, equitable change in environmental or climate related policies. For
    informational purposes only, please find here a link to Equity Action Plans developed by federal
    agencies that may help applicants with designing and preparing these types of projects.
    Example 2. Environmental Advisory Boards (EABs)
    These are projects that facilitate the engagement of disadvantaged communities in environmental decision-
    making by establishing advisory councils, taskforces, or similar bodies to engage with government. These
    boards should have regular meetings to create consistent opportunities for disadvantaged communities to
    provide recommendations on actions government entities should take to address environmental and climate
    justice challenges. These bodies should include members from disadvantaged communities, may include
    additional representatives from other stakeholder groups that can effectively represent important and related
    perspectives (including Tribal, academia, youth / elderly / disability populations, government, etc.).
    Examples of activities under an EAB-type project may include but are not limited to facilitating the
    engagement and involvement of disadvantaged communities in governmental processes at different levels
    of government to provide input, recommendations, and advice on matters such as:
    • Permitting decisions for factories or industrial sites.
    • Community infrastructure upgrades to address pollution and climate concerns.
    21

    --- PDF Page 22 ---
    communities11 • Zoning and siting guidance for fence-line / frontline such as new school placements,
    highway construction, and industrial and commercial uses of land.
    • Issues and actions of municipal and public utilities related to workforce development, drinking
    water shutoffs, drinking water quality and affordability, and aging wastewater treatment
    infrastructure in / near disadvantaged communities.
    Example 3. Collaborative Governance Activities
    These are projects that facilitate the process of providing recommendations and implementing decisions
    that will benefit disadvantaged communities. Projects can focus on creating collaborative bodies with
    members from and / or representing the interests of disadvantaged communities, governmental entities, and
    other stakeholders to work on environmental and climate justice issues.
    Functions these bodies may focus on include co-producing solutions with disadvantaged communities to
    identify and address environmental issues. This could be done through obtaining feedback from a wide
    range of experts and stakeholders, including but not limited to those working in public health, housing,
    economic development, environmental justice, and other relevant fields, to identify environmental and
    directly related public health issues, develop solutions, and then work towards implementing the ideas with
    the necessary parties.
    Examples of activities under a collaborative governance project may include but are not limited to
    facilitating the engagement and involvement of disadvantaged communities in governmental processes on
    matters such as:
    • Participating in the development of one or more community benefits agreements to help ensure that
    environmental projects funded by federal, state, and / or private entities meaningfully engage and
    account for community needs. For informational purposes only, the resource here from the
    Department of Energy provides information that may help applicants with designing and preparing
    these types of projects.
    • Creating a governance body or “development community” for a brownfields post-cleanup
    project.12 redevelopment
    • Creating a source water protection plan to protect public health and reduce burdens on water
    systems.
    • Recommending organizational changes to government entities that make them more receptive and
    sensitive to the environmental and climate justice concerns of disadvantaged communities.
    Example 4. Participation in Governmental Funding and Budgeting Processes
    These are projects that use participatory budgeting to inform public spending on environmental priorities.
    Participatory budgeting is an approach to making decisions about governmental spending that is focused
    on meaningfully and deeply engaging the community in governmental funding processes. Projects can
    enable community-based organizations to partner with a public entity to design and implement processes
    whereby members of disadvantaged communities have input into, and influence, decisions about how to
    allocate public budgets for environmental and climate justice priorities. An example of a project using
    participatory budgeting could involve designing a program where the community identifies problems,
    11 A fence-line community or frontline community is generally one immediately adjacent to high polluting facilities
    such as industrial parks, manufacturing facilities, or commercial facilities and is directly affected by the noise, odors,
    traffic, and chemical and pollution emissions of the operations of these entities.
    12 U.S. Department of Health & Human Services. Build a Development Community.
    22

    --- PDF Page 23 ---
    evaluates proposals, and recommends decisions for public funding of projects that implicate environmental
    and climate justice issues.
    Output:
    {
        "eligible_activities": [
            {
                "track": "Track I",
                "eligible": [
                    "Green infrastructure and nature-based solutions (e.g., tree planting, restoring wetlands, permeable surfaces, green roofs, new parks, greening schoolyards)",
                    "Mobility and transportation options for preventing air pollution and improving public health and climate resilience (e.g., bikeways, walkways, non-motorized trails, zero-emission vehicles, infrastructure for low/zero-emission transportation)",
                    "Energy-efficient, healthy, and resilient housing and buildings (e.g., insulation, ventilation, electrification, weatherization, cool roofs, HVAC upgrades)",
                    "Microgrid installation for community energy resilience (e.g., renewable energy microgrids, battery storage, ancillary infrastructure)",
                    "Community resilience hubs (e.g., backup power, structural retrofits, emergency communications, educational activities)",
                    "Brownfield redevelopment for emissions reduction and climate resilience (only if cleanup is complete or not necessary for intended use)",
                    "Waste reduction and management to support a circular economy (e.g., composting, recycling, food waste reduction, disaster debris management)",
                    "Workforce development programs for occupations that reduce greenhouse gas emissions and air pollutants (e.g., training, apprenticeships, supportive services)",
                    "Indoor air quality and community health improvements (e.g., remediation of lead, asbestos, mold, HVAC upgrades, wood heater replacement)",
                    "Outdoor air quality and community health improvements (e.g., vegetative barriers, alternate truck routes, zero-emission equipment, clean air zones, sustainable construction practices)",
                    "Clean water infrastructure to reduce pollution exposure and increase system resilience (e.g., lead pipe replacement, septic to sewer conversions, water fountains, water reuse technologies, emergency interventions)",
                    "Safe management and disposal of solid and hazardous waste (e.g., hazardous waste collection, recycling, safe disposal technologies, reducing single-use plastics)",
                ],
                "ineligible": []
            },
            {
                "track": "Track II",
                "eligible": [
                    "Educational and training programs to build capacity for engagement in government processes",
                    "Establishing environmental advisory boards or collaborative governance bodies",
                    "Participatory budgeting and community engagement in governmental funding processes",
                    "Community engagement and collaborative governance planning and implementation",
                    "Community strength planning to maximize economic benefits and avoid displacement",
                    "Operations and maintenance planning for infrastructure investments",
                ],
                "ineligible": []
            }
        ]
    }
    Input:
    Application Requirements: The (i) Providing opportunities for
    (iii) Middle school.
    application requirements are as follows: families to acquire the skills to promote (iv) High school.
    (a) A plan to significantly improve the early learning and child development; (v) Career and technical education
    academic outcomes of children living in and programs.
    the geographically defined area (ii) Ensuring appropriate diagnostic (vi) Out-of-school-time settings.
    (neighborhood) that is served by the assessments and referrals for children (vii) Alternative schools and
    eligible entity by providing pipeline with disabilities and children aged 3 programs.
    services that address the needs of through 9 experiencing developmental (viii) Juvenile justice system or
    children in the neighborhood, as delays, consistent with the Individuals correctional facilities.
    identified by the needs analysis, and with Disabilities Education Act (IDEA) (ix) Adult learning;
    that is supported by effective practices. (2) That examines the sources of (20 U.S.C. 1400 et seq.), where
    1SECITON (b) A description of the neighborhood inequity and inadequacy and applicable.
    the eligible entity will serve. (2) Supporting, enhancing, operating, implements responses, and that
    or expanding rigorous, comprehensive, Note: Applicants may propose to includes establishing, expanding, or
    htiw
    effective educational improvements, serve multiple, non-contiguous improving the engagement of
    DORP32NQX11KSD
    which may include high-quality geographically defined areas. In cases underserved community members
    academic programs, expanded learning where target areas are non-contiguous, (including underserved students and
    time, and programs and activities to the applicant should explain its families) in informing and making
    no
    rettol
    VerDate Sep<11>2014 20:13 Jun 26, 2024 Jkt 262001 PO 00000 Frm 00014 Fmt 4703 Sfmt 4703 E:FRFM27JNN1.SGM 27JNN1

    --- PDF Page 5 ---
    53599 Federal Register/Vol. 89, No. 124/Thursday, June 27, 2024/Notices
    Each eligible entity that receives a (including a description of which prepare students for postsecondary
    grant under this program must prepare programs and services will be provided education admissions and success.
    (3) Supporting partnerships between and submit an annual report to the to children, family members,
    schools and other community resources Secretary that includes the following: community members, and children
    with an integrated focus on academics (1) information about the number and within the neighborhood) to support the
    and other social, health, and familial percentage of children in the purpose of the PN program.
    supports. neighborhood who are served by the (j) An explanation of the process the
    (4) Providing social, health, nutrition, grant program, including a description eligible entity will use to establish and
    and mental health services and of the number and percentage of maintain family and community
    supports, for children, family members, children accessing each support service engagement, including:
    and community members, which may offered as part of the pipeline of (1) Involving representative
    include services provided within the services; and (2) information relating to participation by the members of such
    school building. the metrics established under the neighborhood in the planning and
    (5) Supporting evidence-based Promise Neighborhood Performance implementation of the activities of each
    programs that assist students through Indicators. grant awarded;
    school transitions, which may include In addition, grantees must make these (2) The provision of strategies and
    expanding access to postsecondary data publicly available, including practices to assist family and
    education courses and postsecondary through electronic means. To the extent community members in actively
    education enrollment aid or guidance, practicable, and as required by law, supporting student achievement and
    and other supports for at-risk youth. such information must be provided in a child development;
    (g) Each applicant must submit, as form and language accessible to parents (3) Providing services for students,
    part of its application, a preliminary and families in the neighborhood served families, and communities within the
    memorandum of understanding, signed under the PN grant. Data on academic school building; and
    by each organization or agency with indicators pertinent to the PN program (4) Collaboration with IHEs,
    which it would partner in implementing already will be, in most cases, part of workforce development centers, and
    the proposed PN program. Within the statewide longitudinal data systems. employers to align expectations and
    preliminary memorandum of 7. Selection Criteria: The selection programming with postsecondary
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
    VerDate Sep<11>2014 20:13 Jun 26, 2024 Jkt 262001 PO 00000 Frm 00015 Fmt 4703 Sfmt 4703 E:FRFM27JNN1.SGM 27JNN1
    Output:
    {
        "eligible_activities": [
            {
                "track": null,
                 "eligible": [
                    "Providing pipeline services that address the needs of children in the neighborhood, as identified by the needs analysis, and that are supported by effective practices",
                    "Providing high-quality early childhood education programs",
                    "Providing high-quality school and out-of-school-time programs and strategies",
                    "Supporting a child’s transition to elementary school, from elementary school to middle school, from middle school to high school, and from high school into and through postsecondary education and into the workforce, including any comprehensive readiness assessment determined necessary",
                    "Family and community engagement and supports, which may include engaging or supporting families at school or at home",
                    "Activities that support postsecondary and workforce readiness, which may include job training, internship opportunities, and career counseling",
                    "Community-based support for students who have attended the schools in the area served by the pipeline, or students who are members of the community, facilitating their continued connection to the community and success in postsecondary education and the workforce",
                    "Providing social, health, nutrition, and mental health services and supports for children, family members, and community members, which may include services provided within the school building",
                    "Supporting partnerships between schools and other community resources with an integrated focus on academics and other social, health, and familial supports",
                    "Collecting and using data to evaluate and improve the continuum of high-quality pipeline services",
                ],
                "ineligible": []
            }
        ]
    }
    Input:
    SUMMARY 1.1 EXECUTIVE
    The Texas Health and Human Services Commission (HHSC) seeks qualified Applicants to
    provide Supplemental Nutrition Assistance Program Education (SNAP-Ed) Services.
    The SNAP-Ed mission is to work with partners to provide food and nutrition education to
    eligible individuals that promotes healthy food choices and physical activity consistent
    with the most current dietary and physical activity federal guidelines. SNAP-Ed conducts
    these efforts to improve the likelihood that eligible persons will make healthy food choices
    within a limited budget and choose physically active lifestyles that support obesity
    prevention and reduced diet-related chronic disease. The SNAP-Ed vision is to educate,
    connect, and support individuals as they attempt to live healthier lives on a budget through
    Direct Education, targeted Social Marketing efforts, environmental strategies to encourage
    healthy food selection, and use of technology to reach people and communities.
    Applicants must reference for detailed information Section II, Scope of Grant Project
    regarding the purpose, background, Eligible Population, eligible activities, and
    requirements.

    2.1 PURPOSE
    This funding opportunity invites grant Applications requesting funding for the SNAP-Ed
    Program. The purpose of this program is to provide nutrition education, obesity prevention,
    and physical activity interventions to low-income individuals who are eligible for benefits
    under SNAP or other means-tested federal assistance programs, such as Medicaid or
    TANF, across the State of Texas.

    2.2 PROGRAM BACKGROUND
    Texas SNAP-Ed is an evidence-based program designed to help low-income, eligible
    individuals make healthier nutrition choices despite Budget constraints. By teaching
    participants how to shop for, cook nutritious meals, and maintain physically active
    lifestyles, SNAP-Ed plays a key role in reducing nutrition-related chronic illnesses and
    obesity. The program partners with state and local organizations to meet individuals where
    they are in their journey toward healthier nutrition. SNAP-Ed initiatives include nutrition
    education classes, sustained physical activity programs, Social Marketing campaigns, and
    multi-level, multi-sector efforts to improve policies, systems, and environments that
    support better nutrition outcomes for targeted populations across Texas.

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
    Output:
    {
        "eligible_activities": [
            {
                "track": null,
                 "eligible": [
                    "Evidence-based nutrition education and obesity prevention activities to SNAP Eligible Populations",
                    "Implementation of strategies and interventions for the selected approaches for the Project Priorities",
                    "Nutrition education classes",
                    "Sustained physical activity programs",
                    "Social Marketing campaigns",
                    "Multi-level, multi-sector efforts to improve policies, systems, and environments that support better nutrition outcomes for targeted populations",
                    "Direct Education (evidence-based, behavior-focused nutrition education and physical activity intervention conducted at the individual and interpersonal levels)",
                    "Targeted Social Marketing efforts",
                    "Environmental strategies to encourage healthy food selection",
                    "Use of technology to reach people and communities"
                ],
                "ineligible": []
            }
        ]
    }

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with an eligible_activities field. The eligible_activities field should contain an array of JSON objects with the following fields:
        * track (text or null)
        * eligible (array of strings)
        * ineligible (array of strings)
    If eligible activities are not grouped by track, track should be null.
"""
