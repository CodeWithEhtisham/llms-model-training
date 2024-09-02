# Example: Combining text and tables from two chapters
book_knowledge = """
Book name Annual report 2023
[page 1]
Table of Contents
Chapter | Section | Title | Page
-------------------------
 |  | Abbreviations | 4
 |  | Acknowledgements | 6
 |  | About the IsDB Institute | 7
 |  | Letter of Transmittal | 8
 |  | Message from the Director General | 10
 |  | Board of Trustees | 12
 |  | Management Team | 13
 |  | Year-in-Review | 14
 |  | 2023 At A Glance | 16
1 |  | Strategic Orientation | 18
 | 1.1 | Background || 19
 | 1.2 | Strategic Objectives | 19
 | 1.3 | Main Functions | 20
 | 1.4 | Organizational Structure | 20
2 |  | Islamic Finance Sector Transformation | 22
 | 2.1 | Leading the Islamic Finance Industry | 23
 | 2.2 | Islamic Finance Grants Program | 23
 | 2.3 | Flagship Transformation Projects | 25
 | 2.4 | Islamic Finance Infrastructure Institutions | 25
 | 2.5 | Knowledge Creation & Dissemination | 26
 | 2.6 | Islamic Financial Products | 26
 | 2.7 | IsDB Prize for Impact Achievement in Islamic Economics | 26
3 |  | Islamic Finance Sector Transformation | 28
 | 3.1 | Training Programs | 29
 | 3.2 | Massive Open Online Courses (MOOCs) | 31
 | 3.3 | Development of Training Packages | 31
4 |  | Fintech Solutions | 32
 | 4.1 | Synergizing Tech with Islamic Finance | 33
 | 4.2 | Smart Stabilization System | 33
 | 4.3 | Islamic Finance AI Assistant | 34
 | 4.4 | Islamic Finance Pavilion Marketplace | 34
 | 4.5 | Fintech Initiative under GIFIIP | 35
 | 4.6 | Islamic Finance Regulatory Sandbox | 35
 | 4.7 | Global Innovation Hub | 35
5 |  | Global Outreach | 36
 | 5.1 | Partnerships for Delivery | 37
 | 5.2 | Publications | 38
 | 5.3 | Cloud Reader for e-Books | 40
 | 5.4 | IsDB Group Library | 40
 | 5.5 | Outreach Initiatives | 40
 | 5.6 | Conferences & Knowledge Events | 41
6 |  | Strengthening Institutional Effectiveness | 46
 | 6.1 | Board of Trustees | 47
 | 6.2 | IsDBI Project Management Center | 47
 | 6.3 | Driving Business Excellence | 48
 |  | Annexes
Annex | 1 | Publications | 51
Annex | 2 | IsDB Prize Laureates | 56
Annex | 3 | Training Programs | 58
Annex | 4 | Blog Articles | 59
Annex | 5 | Conferences & Knowledge Events | 60
[page 3]

Abbreviations: AAOIFI Accounting and Auditing Organization for Islamic Financial Institutions, AMF Arab Monetary Fund, BIBF Bahrain Institute of Banking & Finance, BOT Board of Trustees, CBDC Central Bank Digital Currencies, CIBAFI General Council for Islamic Banks and Financial Institutions, COMCEC Standing Committee for Economic and Commercial Cooperation of the OIC, CPT Corporate Performance Team, CWLS Cash Waqf Linked Sukuk, GCC Cooperation Council for the Arab States of the Gulf, GIFIIP Global Islamic Finance and Impact Investing Platform, GIH Global Innovation Hub, ICPSD Istanbul International Center for Private Sector in Development, ICRC International Committee of the Red Cross, IFAA Islamic Finance Artificial Intelligence Assistant, IFI Islamic Financial Industry, IF-MAP Islamic Finance Sector Mapping Framework, IFPM Islamic Finance Pavilion Marketplace, IFSB Islamic Financial Services Board, IICRA International Islamic Centre for Reconciliation and Arbitration, IIFM International Islamic Financial Market, III Islamic Infrastructure Institutions, IIRA Islamic International Ratings Agency, IPOS Intellectual Property Office of Singapore, IsDB Islamic Development Bank, IsDBI Islamic Development Bank Institute, KEC Knowledge Economic City, KSA Kingdom of Saudi Arabia, LDCs Least Developed Countries, MCPS Member-Country Partnership Strategy, MCs Member Countries, MOOCs Massive Open Online Courses, OECD Organisation for Economic Co-operation and Development, OMS Operations Management Solutions, OPHI Oxford Poverty and Human Development Initiative, PMC Project Management Center, SCMS Smart Credit Management System, SDGs Sustainable Development Goals, SMEs Small and Medium Enterprises, SSS Smart Stabilization System, UNDP United Nations Development Programme, WIPO World Intellectual Property Organization
[page 4,5]

Acknowledgements The 2023 Annual Report of the Islamic Development Bank Institute was prepared by the Knowledge Horizons Section, with inputs from the business units, based on the overall guidance of the Institute’s Management. UNDER THE SUPERVISION OF: Dr. Sami Al-Suwailem Acting Director General of IsDBI REPORT COORDINATOR: Habeeb Idris Pindiga CONTRIBUTORS ON BEHALF OF IsDBI BUSINESS UNITS: Mohammad Anamul Haque, Mehmet Fehmi Eken, Mohammad Khalid Jawahir, Syed Faiq Najeeb TRANSLATION COORDINATION: Wejdan Kenali, Mahmoud Bekri PRODUCTION SUPPORT Mahmoud Rashad Adel Al-Shotairy Majed Mahdi
[page 6]

About the IsDB Institute The Islamic Development Bank Institute is the knowledge beacon of the Islamic Development Bank Group. Guided by the principles of Islamic economics and finance, the IsDB Institute is mandated to lead the development of innovative knowledge-based solutions to support the sustainable economic advancement of IsDB Member Countries and various Muslim communities worldwide. The Institute enables economic development through pioneering research and original economic analysis, human capital development, and knowledge creation, dissemination and management. The Institute leads initiatives to enable Islamic finance ecosystems, ultimately helping Member Countries achieve their development objectives.
[page 7]

Letter of Transmittal In the Name of Allah, the Beneficent, the Merciful. H.E. the Chairman, Board of Governors of the Islamic Development Bank. Assalamu alaikum wa rahmatullahi wabarakatuh. In accordance with the Statute of the Islamic Development Bank Institute (IsDBI), I have the honour to submit to the esteemed Board of Governors, on behalf of the Board of Trustees, the Annual Report of IsDBI for the year ending 31 December 2023. The Annual Report covers the Institute’s activities and accomplishments in 2023. We are still counting on the Institute to be the knowledge beacon of the IsDB Group. Please accept, Mr. Chairman, the assurances of my highest consideration. Dr. Muhammad Al Jasser Chairman, Islamic Development Bank Group Chairman, IsDB Institute Board of Trustees
[page 8,9]


Message from the Director General H.E. Dr. Muhammad Al Jasser Chairman, IsDB Group Chairman,  As a knowledge organization, the Islamic Development Bank Institute (IsDBI) is committed to addressing socio-economic challenges through innovative solutions within the Islamic economics and finance framework. In 2023, our work focused on five key function areas: - Leading the Islamic finance sector transformation to develop Islamic finance ecosystems. - Synergizing knowledge technologies with Islamic finance for sustainable economic advancement. - Building human capital through diverse training and learning programs. - Reaching out to stakeholders worldwide through strategic partnerships, knowledge dissemination, and media initiatives. - Enhancing our institutional effectiveness to better serve our stakeholders. As the custodian of the Special Allocation to Support the Islamic Finance Industry, the Institute is leading several flagship projects to enhance the contribution of Islamic finance to the sustainable development of MCs and Muslim communities. Our colleagues work tirelessly to advance the flagship projects initiated previously and introduce innovative ones. The new and on-going initiatives include: - Islamic Finance Artificial Intelligence Assistant (IFAA), a tool that uses advanced AI algorithms to provide comprehensive insights into Islamic finance publications and data. - Islamic Finance Sector Mapping Framework (IF-MAP), a holistic diagnostic and remedial toolkit for strengthening Islamic finance ecosystems across MCs. - Awqaf Free Zones project to innovatively combine the concepts of Awqaf, Free Zones, and technology to unlock resources for sustainable development, focusing on food and energy security. - OIC Smart Countertrade System to facilitate trade transactions between parties to be settled through digital countertrade mechanisms. - Digital Postal Islamic Financial Services Project, exploring the opportunities for offering Islamic financial services through the vast postal network to enhance financial inclusion. - Smart Stabilization System, a patent- pending fintech solution to stabilize asset markets by effectively managing supply- demand gaps. - Islamic Finance Pavilion Marketplace, a platform to connect clients in need of Islamic finance, fintech, and development services with proficient suppliers. We are deeply grateful for the visionary leadership of H.E. Dr. Muhammad Al Jasser, the President of the Institute, and the guidance of our Board of Trustees. We are also thankful to our partners and stakeholders who helped enrich our work with their knowledge, expertise, and feedback. ANNUAL REPORT 2023 We are determined to build on our achievements and explore new possibilities in the years ahead. Our goal is to leverage the immense power of knowledge, innovation, and technology to address socio-economic challenges and create a better future.
[page 10,11]


Board of Trustees H.E. Dr. Muhammad Al Jasser Chairman, IsDB Group Chairman, IsDBI Board of Trustees Hon. Dr. Abdallah Souleymane Hon. Abdulghafar Agil Al-Awadhi Hon. Dr. Bambang Susantono Hon. Dr. Kazim Niaz Hon. Khalid Hamad A. Hamad Hon. Malick Ba Hon. Dr. Mohamad Hammour Hon. Rami Alkarmi * Photos of Board of Trustees Members are arranged in alphabetical order of their first names. Hon. Dr. Sabina Alkire ANNUAL REPORT 2023 Dr. Sami Al-Suwailem Acting Director General, IsDBI Secretary, IsDBI Board of Trustees
1. H.E. Dr. Muhammad Al Jasser Chairman, IsDB Group Chairman, IsDBI Board of Trustees
2. Dr. Sami Al-Suwailem Acting Director General, IsDBI Secretary, IsDBI Board of Trustees
3. Hon. Dr. Abdallah Souleymane
4. Hon. Abdulghafar Agil Al-Awadhi
5. Hon. Dr. Bambang SusantonoHon.
6. Dr. Kazim Niaz
7. Hon. Khalid Hamad A. Hamad
8. Hon. Malick Ba
9. Hon. Dr. Mohamad Hammour
10. Hon. Rami Alkarmi
11. Hon. Dr. Sabina Alkire
[page 12,13]


Management Team Dr. Sami Al-Suwailem Acting Director General ANNUAL REPORT 2023 Yahya Rehman Associate Manager, Knowledge Leaders Dr. Hilal M. Houssain Habeeb Idris Pindiga Associate Manager, Knowledge Horizons Basim Qasim Muhammad Associate Manager, Corporate Performance
[page 14,15]


The Islamic Development Bank Institute (IsDBI) is a knowledge organization that aims to address
the economic challenges in IsDB Member Countries (MCs) and communities through innovative
solutions within the Islamic economics and finance framework. The key areas of activities of the
Institute in 2023 include:
[page 14]

Islamic Finance Sector Transformation A program that supports the transformation and development of
the Islamic Financial Services Industry (IFSI) through implementing Islamic finance grant projects. The program
covers various technical work areas, including Islamic banking, capital markets, Takaful, and Islamic social
finance. In 2023, the Institute programmed and approved 14 new technical assistance projects worth about
US$ 2.3 million in Nigeria, Kyrgyzstan, Morocco, Tunisia, Libya, Mauritania, and with partner international
organizations. Twelve projects launched earlier were also completed worth a total of US$ 923,000.
[page 14]

An important tool for building the Islamic finance sector in MCs is the Islamic Finance Sector Mapping
Framework (IF-MAP). This is a holistic diagnostic and remedial Islamic finance ecosystem toolkit now under
the pilot implementation stage. In 2023, assessments were completed for Uzbekistan and Kazakhstan, and
preliminary discussions were held with Nigeria, Morocco and Turkiye for 2024 assessments.
[page 14]

Knowledge Creation & Dissemination The Institute provides market insights and practical analysis for
addressing the development challenges of MCs. This program involves conducting research and publishing
books, reports, and articles on diverse topics in Islamic economics, finance, and sustainable development. More
than 10 publications were issued in 2023. Furthermore, IsDBI developed a cloud reader that grants access to the
Institute’s online bookstore, a massive knowledge repository for Islamic economics and finance publications.
[page 14]

Capacity Building Developing human capital is a core mandate of the Institute through organization of
training programs, executive programs, knowledge seminars, and other forms of capacity building using both
traditional and modern technology-based learning methods. In 2023, the Institute organized 13 capacity-
building programs on diverse topics for the benefit of external as well as internal stakeholders. The Institute
also used the renowned e-learning platform edX to create and offer e-learning programs.
[page 14]

IsDB Prize for Impactful Achievement in Islamic Economics A novel financing mechanism, “Cash Waqf
Linked Sukuk (CWLS)”, was selected as the first-place winner of the prestigious IsDB Prize for Impactful
Achievement in Islamic Economics for the year 2023. CWLS, an initiative of the Indonesian Finance Ministry,
is the first large-scale program to finance social projects via non-profit instruments supervised by the
government. This form of financing enhances the diversity of the Islamic capital markets and supports the
integration between commercial and social Islamic finance. The winner received a US$100,000 cash award.
[page 14]

Strengthening Institutional Effectiveness The Institute achieved remarkable results by leveraging technology
for business intelligence that enhances efficiency and productivity. One of the key initiatives in 2023 is the
Project Management Center (PMC) that aims to centralize and streamline project management processes and
guide the business units towards the successful execution of projects.
[page 14]

Furthermore, in 2023, the Institute continued to leverage the latest technologies
and strategic partnerships to provide cutting-edge solutions to development
challenges. Below are some of the key projects and accomplishments in 2023.
[page 15]

Awqaf Free Zones
This project aims to innovatively combine the concepts of Awqaf, Free Zones,
and technology in mobilizing resources for sustainable development, focusing on food and energy
security. Feasibility reports for this project are expected to be completed by the end of 2024.
[page 15]

OIC Smart Countertrade System The project aims to facilitate trade transactions between parties in the
Organization of Islamic Cooperation (OIC), to be settled through digital countertrade means without using
currency. Feasibility reports are due for completion by the end of 2024.
[page 15]

Digital Postal Islamic Financial Services Project This project explores the opportunities for offering
Islamic financial services through the vast postal network to enhance financial inclusion. Seeking to combine
digital technology with Islamic financial instruments within postal networks, the project is expected to
revolutionize financial inclusion especially in underserved regions.
[page 15]

Smart Stabilization System This patent-pending fintech solution aims to stabilize asset markets by
effectively managing supply-demand gaps. The system uses proactive measures to reduce the volatility
of the traded asset without the need for capital or external reserves. The system has received a favorable
assessment from the World Intellectual Property Organization (WIPO) and is being developed in
collaboration with SettleMint, a leader in blockchain technology.
[page 15]

Islamic Finance Artificial Intelligence Assistant (IFAA) This is a tool that uses advanced AI algorithms
to provide comprehensive insights into Islamic finance publications and data, making complex concepts
accessible to a broader audience. IFAA can also summarize reports and explain Islamic financial principles
in a conversational manner. The tool is expected to be launched in Q1, 2024.
[page 15]

Islamic Finance Pavilion Marketplace (IFPM) This platform connects clients in need of Islamic finance,
fintech, and development services with proficient suppliers. The platform aims to enhance the accessibility
and availability of these services and promote knowledge-driven sustainable development in MCs. The
platform is expected to be launched in Q3, 2024.
[page 15]

2023 AT A GLANCE: Islamic Finance Grants Program
- $2.3 million Project Approvals (2013).
- $93,000 Completed Projects (2023).
- $21.7 million Cumulative Approvals (2013-2023).
- 95 Projects Completed (2013-2023).
- 35 Countries Benefitted.
- 10 International Organizations Supported.
[page 16]

New and On-Going Initiatives:
- Islamic Finance AI AssistantOIC Smart.
- OIC Smart Countertrade System Digital postal service.
- Digital Postal Islamic Financial Services Projectslamic Finance Industry Mapping.
- Smart Stabilization System.
- Islamic Finance Pavilion Marketplace.
- Awqaf Free Zones.
[page 16]

Capacity Building: 
- 13 Training Programs.
- +300 Participants.
[page 17]

Massive Open Online Courses:
- Number of Attendees 3,400.
- Number of Countries of Attendees 130.
- Number of Active Courses 4.
- Top 5 Countries of Attendees (Nigeria, Malaysia, Indonesia, Saudi Arabia and Pakistan)
[page 17]

IsDB Prize for Impactful Achievement in Islamic Economics:
- 1 Laureate; $100,000 Cash Award.
- 45 Winners To-Date.
[page 17]

Knowledge Events:
- 6 Conferences (Organized/Participated).
- 30 Knowledge Sessions.
[page 17]

"""

chapter1 = """

Chapter 1 Strategic Orientation This chapter presents the Institute's strategic objectives, functions, and organisational structure.
[page 18]

1.1 Background The Islamic Development Bank Institute (IsDBI) is a knowledge organization that aims to address the economic challenges in MCs and communities through innovative solutions within the Islamic economics and finance framework. Established in 1981 as the Islamic Research and Training Institute (IRTI), the Institute was renamed in April 2021 as the Islamic Development Bank Institute (IsDBI) to better align with the IsDB Group’s emerging priorities. The Institute leads initiatives to unleash the potential of Islamic finance as an efficient tool for social and economic development
[page 19]


1.2 Strategic Objectives The Institute’s strategic direction is formulated based on the “Blue Ocean Strategy.” This means searching for fresh (blue) waters with the potential for delivering high value, while avoiding crowded areas (red water). In practice, this refers to the pursuit of opportunities and activities that create added value at minimum cost. The Institute avoids replication of the work of other organisations, and capitalises on its comparative advantages to uniquely position itself. In light of this strategy, the Institute adopted four Strategic Objectives as follows:
1. Creating Value through Knowledge-based Innovations: The Institute primarily focuses on identifying innovative ways to make its business cost- effective, competitive, and client oriented. As the IsDB Group is fully committed to the SDGs, the Institute champions the implementation of the Global Goals according to the needs and priorities of the MCs. The Institute harnesses its intellectual expertise and teams up with leading industry partners to develop innovative, knowledge-based solutions that respond to MCs’ challenges. While guiding the innovation process toward maximum value for MCs, the Institute continues to uphold the principles of Islamic economics and finance.
2. Building Human Capital:The core of any sustainable development strategy is human capital. Therefore, the Institute employs frontier technologies, and applies a sustainable set of human values at the core of its business, to formulate unique programmes for building the next generation of knowledge leaders and entrepreneurs to lead the development of MCs. The Institute aims to lead in providing learning and capacity building to support MCs in achieving the SDGs.
3. Adopting a Problem-Solving Approach: IsDBI adopts an up-to-date problem-solving approach to find authentic and real-time solutions to MCs’ economic impediments. Hence, the Institute focuses on applied and productive studies, translating intellectual creativity to real- world applications. This will enable the Institute to distinguish itself from and complement academia, consulting firms, and related industry players.
4. Creating Strong Partnerships and Networks: Over the years, the Institute has leveraged its accumulated knowledge and experience in Islamic Finance to collaborate with local and international development institutions. IsDBI continues to play a unique role in working with its stakeholders and future partners to support MCs’ development via innovative systems and state-of-the-art technologies guided by the principles of Islamic Finance.
[page 19]


1.3 Main Functions:
- Leading Islamic finance sector transformation
- Synergizing knowledge technologies with Islamic finance
- Design of innovative solutions to address socio-economic challenges
- Building human capital in Islamic finance and development
- Publishing in Islamic economics and finance
- Fostering the development of Islamic finance ecosystems
[page 20]


1.4 Organizational Structure: IsDBI has a flat organisational structure that promotes agility of decision making. The Institute has four business units, namely: Knowledge Leaders Section, Knowledge Solutions Section, Knowledge Horizons Section, and Corporate Performance Section. An overview of the units is given below: Knowledge Leaders Section: This is the focal point for the Institute’s Islamic finance sector transformation program and capacity building programs. It is responsible for knowledge creation and dissemination in relation to Islamic economics and finance. The key responsibilities of the team include:
- Leading the development and execution of the Islamic Finance Grants Program to respond to the needs of, and find practical solutions to, economic developmental priorities of the IsDB MCs.
- Leading a problem-solving approach to knowledge creation and dissemination in Islamic economics and finance.
- Contributing to knowledge products aimed at capacity building and human capital formation, including books, manuals, training packages, and online courses that help the Institute achieve its objectives while maintaining sustainable revenue.
- Undertaking capacity building of future knowledge leaders in Islamic Economics and Finance who will lead the entrepreneurial development of MCs.
- Contributing to the development of the MCPS by providing input on the Islamic finance sector for the country diagnostics.
- Supervising and managing the development and delivery of innovative and effective learning and certification programs in partnership with other institutions inside and outside IsDB MCs.
- Designing and implementing the Institute’s e-Learning Programs to enhance the knowledge and skills of individuals, institutions and stakeholders in IsDB MCs and non-MCs. Chapter 2 Islamic Finance Sector Transformation This chapter reports the accomplishments in leading the transformation of the Islamic financial industry through various initiatives.
[page 20]

Knowledge Solutions Section: The team synergizes knowledge technologies with Islamic finance for the development of innovative solutions addressing challenges facing MCs and the Islamic finance industry. The key responsibilities of the team include:
- Leading the design and structuring of innovative, knowledge-based solutions to the development challenges of MCs in line with the principles of Islamic Economics and Finance.
- Serving as a focal point for knowledge management and innovative technologies for the IsDB Group and MCs.
- Leading the development and execution of the Islamic Finance Knowledge Pavilion Platform, which aims to be the leading marketplace for advisers, consultants, and fintech experts in Islamic finance and economic development.
- Overseeing and coordinating the provision of intellectual property protection for the Institute’s innovative solutions by way of patents and similar means, and capitalising on these patents to ensure the financial sustainability of the Institute.

Knowledge Horizons Section: This team is the focal point for the outreach, customer relations, and publishing activities of the Institute. The key responsibilities of the team include:
- Designing and implementing media and marketing programmes to enhance the visibility of the Institute and its knowledge products across target markets.
- Managing the Institute’s publications process and dissemination to ensure effective and efficient production of high-quality, high-value publications.
- Leading e-publishing products and processes to maintain the leadership of the Institute in the domain of Islamic Economics and Finance and to contribute to the Institute’s financial sustainability.
- Developing and maintaining the Institute’s website and social media channels and ensuring their effective use in disseminating the Institute’s messages and engaging stakeholders.
Corporate Performance Section: This team is responsible for translating the Institute’s strategy into measurable results. The key responsibilities of the team include:
- Leading and participating in the resource mobilisation function of the Institute to ensure sustainable funding for its programmes and activities.
- Coordinating the financial management of the Institute’s Fund as per the Statute of the IsDBI and related regulations approved by the President.
- Administering the development of the Institute’s financial plans and projections.
- Coordinating the IsDBI Islamic Finance Grants Program.
- Supervising and maintaining the proper implementation of the Rules and Regulations of the Institute.
- Establishing robust and agile systems and procedures for the Institute to ensure quality products and services to clients and stakeholders.
- Overseeing performance management for the IsDBI.
[page 21]

"""


chapter2= """
Chapter 2 Islamic Finance Sector Transformation This chapter reports the accomplishments in leading the transformation of the Islamic financial industry through various initiatives.
[page 22]

2.1 Leading the Islamic Finance Industry: One of the key functions of IsDBI is to lead the development of an enabling environment for Islamic finance to serve as a catalyst for achieving the development goals of MCs. In this respect, IsDBI supports diverse sectors through different types of interventions. The varying nature of interventions, depending on the needs of the beneficiary country/organisation, includes development of legal and regulatory frameworks, country masterplans, thematic policies, capacity building, products development, technology- aided solutions, and technical support in applying standards of best practices in the Islamic finance industry. The interventions aim to reinforce the impact of Islamic finance on sustainable development and to promote inclusive growth and economic stability.
[page 23]

Box 2.1: Objectives of the Islamic Finance Sector Transformation Program
A. To support the transformation and development of the Islamic finance industry to support sustainable development.
B. To contribute to the creation of an enabling environment (legal, regulatory, and supervisory frameworks) for the development of the Islamic financial services industry in the IsDB MCs.
C. To facilitate the standardization and harmonization of the practice of Islamic finance across IsDB MCs.
[page 23]




2.2 Islamic Finance Grants Program:
As part of its leadership role in developing Islamic finance ecosystems, the Institute has revitalised the Islamic Finance Grants Program to support the transformation and development of the Islamic Financial Services Industry (IFSI). The grants program, historically known as the Islamic finance technical assistance programme, has been one of the core intervention instruments of the IsDB Group in shaping the global Islamic finance landscape. The funding for the program comes from the Islamic Finance Special Allocation approved by the IsDB Board of Governors in 2013 and subsequently renewed over time with the latest extension for the use of the funds during the period 2022-25.
The objectives of the program include supporting IFSI stakeholders, through grant projects, to create an enabling environment for all the sectors of the Islamic finance industry in their respective jurisdictions. These stakeholders typically include central banks, ministries of finance, capital market authorities, other regulatory and supervisory agencies, commercial and investment banks, takaful companies, and other financial services stakeholders. In addition to IsDB Member and Non-Member Country stakeholders, Islamic finance grants are also offered to Islamic finance infrastructure institutions for developing standards, guidelines, and best practices for the Islamic Financial Services Industry (see more in Section 2.4).
[page 23]

Grant projects typically kick-off with scoping to
understand beneficiary needs and identifying
issue areas. Once these areas are identified, a
suitable intervention mechanism will be designed.
Afterward, the grant will be approved, and the
implementation stage will begin. This stage will
comprise the execution of the grant project,
financial disbursements, technical advisory, and
achievement of the program objectives leading to
project completion.
[page 23,24]

In the past 10 years (2013-23), a total of 175 Islamic
Finance Grant projects were programmed worth
nearly US$ 21.7 million in commitments1. Among
these, 95 projects have been successfully completed
benefiting more than 35 IsDB MCs and non-MCs.
The program has also supported more than 10
international partner organisations including the
Islamic finance infrastructure Institutions. These
interventions have paved the way for introducing and
strengthening Islamic finance worldwide by creating
the requisite enabling environment consisting of
legal, regulatory, and supervisory frameworks,
building local capacities, and transferring knowledge.
[page 23,24]

Focusing on the year 2023, the Institute
programmed and approved 15 new technical
assistance projects of about US$ 2.3 million for
various countries and international organizations.
[page 23,24]

These were Nigeria, Kazakhstan, Morocco, Tunisia,
Libya, Mauritania, International Committee of the
Red Cross (ICRC), International Islamic Financial
Market (IIFM), Islamic Financial Services Board
(IFSB), and Accounting and Auditing Organization
for Islamic Financial Institutions (AAOIFI). The new
projects approved in 2013 were in addition to
the 67 already approved projects that are under
implementation.
[page 23,24]

Additionally, 10 technical assistance  projects launched  earlier  were completed  in  2023  worth a total of US$ 923,000.
Overall, the technical
assistance portfolio supports a wide spectrum of
technical work areas including Islamic banking,
Islamic capital markets, Takaful as well as the
Islamic social finance sector.
[page 23,24]


Table 2.1: Islamic Finance Grants Projects completed in 2023
# | Country/ Institute | Type | Project Name
--------------------------------------------
1 | Palestine | CBA | Financing Capacity Building for Arab Islamic Bank
2 | IIRA | IFG |  Islamic Finance Grant for IIRA
3 | Gambia | CBA | Feasibility Study on IDB Islamic Microfinance Development Program for the Gambia
4 | Guinea Conakry | CBA | Feasibility Study on IDB Islamic Microfinance Development Program for Guinea Conakry
5 | Afghanistan | CBA | Feasibility Study on IDB Islamic Microfinance Development Program for Afghanistan
6 | Tunisia | CBA | Sponsoring 6th Sfax International Forum on Islamic Finance
7 | Mozambique | IFG | Creating Legal and Regulatory Environment for Islamic Finance
8 | Niger | CBA | Waqf Regulatory Framework in Niger
9 | Spain | CBA | Islamic Finance Changemakers Project
[page 24]

2.3 Flagship Transformation Projects: IsDBI’s flagship projects focus on identifying and aiming to address the most pressing challenges in the MCs. The projects leverage Islamic finance and technology to create strategic and holistic solutions to address the identified issues. The objectives are to engage in innovation and produce practical solutions to the development needs; help in facilitating the enhanced business and economic relations among IsDB MCs; and support mainstreaming Islamic finance in IsDB MCs. For each flagship project, the activities include identifying a specific development challenge, proposing innovative solutions, testing proof-of- concept, generating feasibility reports, and pilot implementation of the solution. Currently, four flagship projects are at various stages of implementation, as follows:
- Awqaf Free Zones: This project aims to innovatively combine the
concepts of Awqaf, Free Zones, and technology in
mobilizing resources for sustainable development,
focusing on food and energy security. Feasibility
reports for this project are expected to be
completed by the end of 2024.
- OIC Smart Countertrade System: The project aims to facilitate trade transactions
between parties in the Organization of Islamic
Cooperation (OIC), to be settled through digital
countertrade means without using currency.
Feasibility reports are due for completion by the
end of 2024.
- Digital Postal Islamic Financial Services Project: This project seeks to synergize digital technologies
with Islamic financial instruments within the
postal networks. This innovative approach aims
to revolutionize financial inclusion, especially in
underserved regions. The Institute has started
creating awareness about the project through its
participation in the first edition of the Africa Postal
Leaders Forum organized by the Universal Postal
Union in July 2023. Market studies are due for
completion by the end of 2024.
- Islamic Finance Sector Mapping Framework (IF-MAP):This important tool for building the Islamic finance
sector in MCs is a holistic diagnostic and remedial
Islamic finance ecosystem toolkit now under the
pilot implementation stage. In 2023, assessments
were completed for Uzbekistan and Kazakhstan,
and preliminary discussions were held with Nigeria,
Morocco and Turkiye for 2024 assessments.
[page 25]



2.4 Islamic Finance Infrastructure Institutions:The rapid expansion of the global Islamic
finance industry over the last decade or two
has brought about the need for regulatory and
policies standardization and harmonization across
different countries and jurisdictions. In response
to this need, the IsDB created the Islamic Finance
Infrastructure Institutions Program aiming to
coordinate, support, and technically contribute
towards the six institutions established by the
IsDB. These are AAOIFI, General Council for Islamic
Banks and Financial Institutions (CIBAFI), IFSB,
IIFM, Islamic International Ratings Agency (IIRA),
and International Islamic Centre for Reconciliation
and Arbitration (IICRA).
The key mode of engagement by IsDB is through
participation in the governing bodies of these
institutions, technical committees, working groups
and task forces, as well as other operational
and technical coordination activities. Through
this support, the IIIs have issued more than 200
standards of best practices on diverse technical
topics for the global Islamic financial services
industry covering all sectors including banking,
capital markets, takaful and social finance.
The IsDB Institute manages the IsDB Group’s
coordination with these institutions, including
membership matters, events coordination,
technical work programs, senior management
representation in meetings, and professional staff
inputs into the technical work programs. In 2023,
the IsDBI managed all the coordination matters
for these institutions on behalf of the IsDB.
[page 25]


Box 2.2: Goals of the Islamic Finance Infrastructure Institutions Program
A. To coordinate, support, and technically contribute towards the Islamic finance infrastructure institutions established by the IsDB.
B. To help the Islamic Infrastructure Institutions become credible standard-setting institutions that play an instrumental role in the harmonization and standardization of Islamic finance practice.
C. To support Islamic Finance Infrastructure Institutions become self-sustaining institutions and reliable points of reference.
[page 26]


2.5 Knowledge Creation & Dissemination: A key function of the Institute is to produce and
disseminate knowledge on how to tackle the
development issues facing MCs within the principles
of Islamic economics. This involves exploring
the areas where Islamic finance and sustainable
development can converge and benefit MCs’
economic and financial goals. The Institute publishes
its research findings in various formats, such as
books, reports, and articles, covering a wide range
of topics related to Islamic economics, finance and
sustainable development.
In 2023, more than 10 publications were issued
covering a range of topics in Islamic economics and
development. Furthermore, IsDBI completed the
Cloud Reader web platform that grants access to the
Institute’s online bookstore, a massive knowledge
repository for Islamic economics and finance
publications. [More details on the publications
issued are available in Chapter 5 and Annex 1].
The Institute similarly organizes or collaborates
in knowledge dissemination programs to raise
greater awareness and understanding of Islamic
finance, and promote Islamic financial literacy.
Such programs include conferences, workshops,
seminars, and webinars. Among the high-profile in 2023 were the AAOIFI-IsDB Annual Islamic
Finance Conference, AIFC-IsDBI Islamic Finance
Conference, IsDBI Activities in COP 28 in Dubai,
BILIF-IsDBI Seminar in Brunei and so on. [For
more, see Chapter 5 and Annex 5].
[page 26]


2.6 Islamic Financial Products: The Institute develops innovative Islamic finance
products aimed at addressing the market and
developmental needs of the IsDB MCs. This helps
champion breakthrough ideas and products
that can potentially become solutions to the
economic development problem of IsDB MCs. In
2023, the Institute worked on several innovative
products, namely Sukuk Enhancement Fund,
Results-Based Financing Mechanism, the use
of takaful as a resilient product for addressing
climate challenges, and a product for addressing
women’s financial inclusion through Islamic
finance. These initiatives were conducted in
coordination with various partners both within
the IsDB Group and externally.
[page 26]


2.7 IsDB Prize for Impactful Achievement in Islamic Economics:
The IsDB Prize for Impactful Achievement in
Islamic Economics, coordinated by the Institute,
aims to recognize outstanding achievements
in knowledge creation and innovative
development solutions guided by the principles
of Islamic economics. The Institute manages
the prestigious prize, including all processes
of nominations, screening, selection, award
approvals, and presentation ceremony.
In 2023, a novel financing mechanism, “Cash Waqf
Linked Sukuk (CWLS),” was selected as the first-
place winner of the prize under the Development
Achievement category. CWLS, an initiative of the
Indonesian Finance Ministry, is the first large-
scale program to finance social projects via non-
profit instruments supervised by the government.
This form of financing enhances the diversity of
the Islamic capital markets and supports the
integration between commercial and social Islamic
finance. The winner received a US$100,000 cash
award. However, the second and third-position
prizes were withheld in 2023.
[page 26,27]


Box 2.3: Cash Waqf Linked Sukuk:
The IsDB Prize winners are se-
lected by a committee of ex-
perts from outside the IsDB
Group. The Selection Commit-
tee for the 2023 Prize issued
the following citation on the
Cash Waqf Linked Sukuk:
• The concept of permanent and temporary cash
waqf has been around for centuries. However,
Cash Waqf Linked Sukuk (CWLS) is the first large-
scale program to finance public projects via non-
profit instruments supervised by the government.
This form of financing shall enhance the diversity
of the Islamic capital markets and support the
integration between commercial and social Islamic
finance.
• The present CWLS model can be enhanced in
many ways to make a stronger and more lasting
impact. The model has great potential, and the
prize aims to encourage the winner and other
Islamic financial institutions to capitalize on it and
take it to the next level.
Considering this, the IsDB Prize Selection
Committee decided to award the IsDB Prize for
Impactful Achievement in Islamic Economics
(1444H, 2023) to Cash Waqf Linked Sukuk as the
first-place winner.
[page 27]


Following the completion of the 2023 prize cycle, IsDBI opened the nominations for the 2024
cycle of the prize which is in the Knowledge Contribution category. This category of the prize
aims to recognize, reward, and encourage significant knowledge contributions in areas related to
Islamic economics that have the potential to solve major economic and financial challenges of IsDB
MCs. The winners will receive the award during the IsDB Group Annual Meetings, scheduled for
April 2024 in Riyadh, Saudi Arabia. More details are available on the dedicated IsDB Prize website:
https://prize.isdbinstitute.org
Knowledge Contribution 2:$ 30,000, 1:$ 50,000, 3:$ 20,000; Development Solution Achievement 2:$ 70,000, 1:$ 100,000, 3:$ 30,000 
[page 27]


"""

chapter3 ="""
Chapter 3 Capacity Development This chapter covers the Institute’s activities in human capital development, including training and learning programs.
[page 28]

3.1 Training Program:
sDBI leads in developing human capital in Islamic
economics and finance through a range of training
programs that include workshops, orientation,
executive programs, and knowledge seminars.
These training activities aim to improve the quality,
efficiency, impact and cost-effectiveness of capacity
development programs, resource mobilization,
developing training packages, and building
partnerships with institutions from the public and
private sectors.
A total of 13 training programs were organized
in 2023 across several IsDB MCs. These programs
covered diverse topics including capital markets,
sukuk, liquidity management, Shari’ah governance
standards, digital technologies and their application
in Islamic finance, Islamic social finance, and
microfinance. Through these sessions, up to 300
professionals gained hands-on knowledge on
tailored topics. The sessions were delivered by the
various IsDB Group professional staff and external
experts having profound knowledge in the subject
areas.
In organizing training programs, the Institute
works with esteemed national, regional, and
international institutions and centres of excellence
to ensure efficiency and effectiveness. IsDBI training
courses are offered in Arabic, English and French
languages. Some of the major training programs
are highlighted below, while a full list of training
programs completed in 2023 is in Annex 3.
Multidimensional Poverty Measurement:
IsDBI partnered with the Islamic Solidarity Fund
for Development (ISFD) and Oxford Poverty and
Human Development Initiative (OPHI) to organize a
training workshop on measuring multidimensional
poverty. The workshop was designed to build the
capacity of IsDB Group staff in producing data-
driven research that supports evidence-based
policymaking. Over 40 staff attended the program,
which was held on 24-25 January 2023 at the IsDB
Headquarters in Jeddah, KSA.
[page 29]


Managing Islamic Social Finance: This program
was delivered on 14-16 August 2023 in Kampala,
Uganda, through a technical assistance grant for
capacity development in Islamic social finance for
the House of Zakat and Waqf in Uganda (HZWU).
The objective of the grant is to develop the capacity
of the institution to properly manage zakat for the
benefit of the Muslim community in Uganda. The
grant also aims to contribute to human capital
development in Islamic social finance in Uganda.
Topics covered in the training included fiqh of
zakat, the governance of zakat institutions, the role
of zakat in achieving SDGs, the use of fintech in
zakat, and success stories in zakat management in
IsDB MCs.
[page 29]

AAOIFI Accounting Standards: IsDBI and the
Capacity Building and Training Institute of the
Arab Monetary Fund (AMF) jointly organized the
two trainings in a series of three virtual programs
covering all accounting standards issued by the
Accounting and Auditing Organization for Islamic
Financial Institutions (AAOIFI). The first training
was conducted on 25-28 September 2023, while
the second was delivered on 18-21 December
2023. The series is part of an ongoing strategic
collaboration between the two institutions to
support common member countries of the Islamic
Development Bank and AMF. Similarly, IsDBI and
the Saudi Central Bank jointly organized a 3-day
training workshop on 15-17 February 2023 on
“AAOIFI Financial Accounting Standards”, held
within the framework of the IsDB Islamic Finance
Grant Program to develop Islamic financial services
industry in IsDB MCs.
[page 30]


IsDBI-BIBF Joint Specialized Training: In
collaboration with the Bahrain Institute of Banking
and Finance (BIBF), IsDBI delivered a specialized
training workshop on Islamic Finance Product
Development for Islamic Financial Institutions. This
course, held virtually on 5 November 2023, covered
the product development process undertaken
in Islamic financial institutions. The program was part of a partnership to deliver specialized
training to a diverse range of professionals from
various financial institutions, regulatory bodies,
supervisory authorities, and legal experts within
the Islamic finance industry.
Islamic Finance Executive Program: The Institute
delivered high-level sessions under the theme
‘Islamic Finance and Socioeconomic Development’,
on 14 November 2023, as part of the 6th edition
of the Saudi-Spanish Center for Islamic Economics
and Finance (SCIEF) Islamic Finance Executive
Program. IsDBI collaborated with King Abdulaziz
University (KSA) and I.E. Business School (Spain) to
organize and support the executive program. One
of the sessions was on IsDBI’s Sukuk Enhancement
Fund.
[page 30]


Islamic Capital Markets in Nigeria: IsDBI joined forces with the Nigerian Exchange Limited (NGX)
to deliver an influential Islamic capital markets capacity-building workshop in Lagos, Nigeria.
Organized under the theme “Economic Growth and Business Development Opportunities through
the Islamic Capital Markets”, the workshop aimed to contribute to deepening the Nigerian capital
markets through the listings and issuances of Islamic financial instruments. The workshop, held
on 21 November 2023, attracted 90 participants from across the Nigerian economic and financial
sectors.
[page 30]


3.2 Massive Open Online Courses (MOOCs): 
Since 2015 when the IsDBI pioneered MOOCs in
Islamic economics and finance, the Institute has
remained the leader in this area, attracting tens
of thousands of learners to its course offerings on
the edX platform. Currently, IsDBI has three active
courses on various topics of Islamic finance on the
edX platform, with new courses at various stages of
development and expected to be launched in 2024.
More than 3,400 participants have enrolled onto
these active courses from over 130 countries, with
Nigeria, Malaysia, Indonesia, Saudi Arabia and
Pakistan being the top five countries of participants.
As well as the new courses currently being
developed, IsDBI is formulating a comprehensive
e-learning strategy that will target delivering
training programs online to a larger audience.
[page 31]


3.3 Development of Training Packages: 
IsDBI’s training packages are aimed to facilitate the
delivery of training programs and the development
of online training courses. In previous years, IsDBI
developed several training packages, one of them
entitled “Operational Aspects of Accounting
Standards of Islamic Financial Institutions”. In
2023, IsDBI initiated a process to update the
contents of the four components of this package
to align with the recent developments in AAOIFI’s
Financial Accounting Standards and their current
applications in Islamic financial institutions. The
objective of updating this package is to ensure all
stakeholders are exposed to the latest provisions of
AAOIFI’s Financial Accounting Standards.
[page 31]

Box 3.1: IsDBI Massive Open Online Courses (2023) 
- Number of Attendees:3,400 - Number of Countries of Attendees:130 
- Number of Active Courses:4 
- Top 5 Countries of Attendees (Nigeria, Malaysia, Indonesia, Saudi Arabia and Pakistan)
[page 31]

"""


chapter4 = """
Chapter 4 Fintech Solutions This chapter focuses on the Institute’s work in developing fintech solutions to address challenges facing IsDB MCs.
[page 32]

4.1 Synergizing Tech with Islamic Finance: 
IsDBI has continued to lead the way in synergizing
knowledge technologies with Islamic finance to
develop fintech solutions addressing contemporary
socio-economic challenges. Leveraging innovative
technologies and strategic partnerships, the
Institute in 2023 embarked on numerous ambitious
projects for cutting-edge solutions in Islamic
finance and technology.
[page 33]

4.2: The Smart Stabilization System: 
In 2023, IsDBI kicked off building a prototype for
the patent-pending Smart Stabilization System
(SSS). A groundbreaking innovation in the field
of financial technology, the SSS is designed to
stabilize asset markets by effectively managing
supply-demand gaps. This forward-looking
system contrasts traditional stabilization methods
by focusing on proactive rather than reactive
measures. The in-depth analysis conducted by the
Institute demonstrated the system’s potential to
significantly reduce the volatility of the traded asset
without the need for capital or external reserves.
The system has already gained international
recognition with a favorable assessment from the
World Intellectual Property Organization (WIPO)
on 11 December 2023, affirming its uniqueness and
potential for patentability. WIPO acknowledgement
is not only a testament to the system’s ingenuity
but also underlines IsDBI’s role as a leader in the
fintech sector.
In collaboration with SettleMint, a leader in
blockchain technology, a workable demonstration
of the SSS is being developed with a focus on
inclusivity and accessibility across various asset
classes, including shares, sukuk, digital currencies,
and Central Bank Digital Currencies (CBDCs). Phase
1 covers the development of the Proof-of-concept
of the SSS. This will be followed by “Developing
and Testing” (Phase 2) and “Production and
Deployment” (Phase 3).
This initiative is a significant step towards
enhancing financial stability in the digital and
crypto-based economy.


Box 4.1: The Smart Stabilization System
The Smart Stabilization System is an algorithm for
stabilizing the value of assets or coins traded on
centralized exchanges. The main idea of the System
is that the gap between supply and demand can be
managed to reduce the volatility of the price while
maintaining the role of the gap in adjusting prices.
The System is unique in several important aspects:
1. It is self-funded.
2. It acts before price changes.
3. It protects the rights of investors.
Simulation results show significant improvement in
the stability of not only price but also the volume
of transactions. The algorithm is currently patent
pending with the Intellectual Property Office of
Singapore (IPOS).
[page 33]

Box 4.2: Key Features of the Islamic Finance AI Assistant: 
• A tool that uses AI models to provide insights into Islamic finance knowledge from a variety of credible and reliable sources 
• Ability to query and summarize reports, and explain Islamic financial concepts in a conversational way 
• Shows remarkable capabilities in elucidation of Islamic financial principles 
• More functions to be added: AI-based assistants for legal and regulatory frameworks, Islamic finance training, etc.
[page 34]

4.3 Islamic finance AI assistant
The year 2023 witnessed the development
of the Islamic Finance Artificial Intelligence
Assistant (IFAA), a cutting-edge tool designed to
democratize access to Islamic finance knowledge.
Powered by advanced AI algorithms, IFAA provides
comprehensive insights into IsDB Group’s and other
publicly available publications and data, making
complex Islamic financial concepts accessible to
a broader audience. IFAA allows users to query
and summarize reports quickly to get to the main
points. It also offers insights into the intricacies of
Islamic financial principles in a conversational and
accessible manner using the latest AI technologies
and Large Language Models such as ChatGPT.
IFAA’s capabilities in report summarization and
elucidation of Islamic financial principles have been
remarkable. The IFAA is undergoing additional
testing and is expected to be launched in Q1, 2024.
Looking ahead, IsDBI plans to expand IFAA’s
functionalities into various realms, including
AI-based assistants for legal and regulatory
frameworks, the grants program, progress
reporting, and Islamic finance training. This
expansion is aimed at enhancing decision-making
processes and fostering a deeper understanding of
Islamic finance.
[page 34]


4.4 Islamic Finance Pavilion Marketplace:
The Islamic Finance Pavilion Marketplace (IFPM)
project is a strategic initiative aimed at enhancing
connections between clients in need of Islamic
finance, fintech, and development services, and
proficient suppliers capable of meeting these
demands. This initiative plays a critical role in making
these services more accessible and available. IFPM
offers a streamlined digital interface for effective
matching of suppliers with clients, serving as a
comprehensive hub. It will connect clients with
suitable suppliers, promoting knowledge-driven
sustainable development in IsDB MCs. It will
also feature a meticulously curated knowledge
base of verified solution providers, and spotlight
opportunities in relevant sectors.
EZ2Business, the selected consultancy company, is
responsible for conducting market and feasibility
studies, developing the platform, including web
and app development, and providing training and
support. The project, which started on 19 December
2023, aims for a launch in Q3 2024.
[page 34]

4.5 Fintech Initiative under GIFIIP:
IsDBI is collaborating with the UNDP's Istanbul International Center for Private Sector in Development (ICPSD) for a partnership with the Indonesian Shariah Fintech Association (AFSI) on the "Islamic Fintech Solutions for the LDCs" project. The project is under the Digital Solutions for Financial Inclusion component of the ISDB-UNDP Global Islamic Finance and Impact Investing Platform (GIFIIP). This initiative is focused on researching and developing Islamic fintech solutions, particularly targeting Least Developed Countries (LDCs). By exploring the potential and applicability of these solutions in countries like Afghanistan, Bangladesh, and Djibouti, the program aims to foster economic empowerment and financial inclusivity.
The research conducted under this initiative is expected to provide valuable insights into the unique challenges and opportunities within these economies. The findings are set to inform future projects and strategies aimed at integrating Islamic fintech solutions more broadly in LDCs, thereby enhancing their financial infrastructure and inclusivity. 
[page 35]


4.6 Islamic Finance Regulatory Sandbox:
This planned project is to create a conducive environment for testing innovative Islamic fintech solutions, to establish robust standards and guidelines.
Regulatory sandboxes have become instrumental platforms for fintech companies to test new solutions in a time-bound controlled environment, enabling regulators to understand the implications of these innovations. Typically, firms that apply to enter a regulatory sandbox have already developed an offering and wish to test its viability in the market.
While several countries have launched such initiatives with substantial success, there is a distinct gap for fintech solutions tailored to Islamic finance. Integrating the sandbox model with the distinct needs of Islamic finance could foster an environment conducive to developing Sharia- compliant fintech advancements. It can be linked to financial inclusion mandates and potentially encourage innovations that reduce barriers to inclusion.
By providing a controlled yet flexible regulatory framework, the sandbox is designed to encourage innovation while ensuring compliance with Islamic finance principles. This initiative is expected to accelerate the growth of fintech solutions in the Islamic finance sector. The project is planned to begin in Q2 of 2024 and be completed in one year.
[page 35]


4.7 Global Innovation Hub: 
This project aims to support the feasibility studies for the development of a Global Innovation Hub (GIH) within the Knowledge Economic City (KEC) in Madinah, Kingdom of Saudi Arabia. It marks an ambitious step towards establishing a leading center for Islamic finance innovation. The hub aims to support entrepreneurs from IsDB MCs and Muslim communities in non-member countries to create and expand value-creating projects in the areas of Islamic finance and the Halal economy. The project is planned to begin in Q1 2024 and be completed at the end of 2024.
The feasibility studies are expected to support the substantial potential for KEC and GIH to serve as catalysts in Islamic finance, fostering innovation and growth. The findings will guide strategic development, positioning KEC as a global leader in this sector.
[page 35]

"""

chapter5 = """
Chapter 5 Global Outreach This chapter reports on the global outreach initiatives that include partnerships, publishing, media, and events.
[page 36]

5.1 Partnerships for Delivery: 
n 2023, the Institute has harnessed the value of collaborations to amplify its influence in MCs. This
strategic approach has resulted in several noteworthy achievements through collaborations with major
partner institutions globally.
Three key collaborations with notable impact and contributions deserve mention here. The first is the
partnership with the Islamic Solidarity Fund for Development (ISFD) and Oxford Poverty and Human
Development Initiative (OPHI) on measuring multidimensional poverty. This partnership resulted in
organizing an important training program for IsDB Group staff on multidimensional poverty measurement
(see additional details in Chapter 3).
The second is with the Asian Development
Bank (ADB) for a report titled Transforming
Bangladesh’s Participation in Trade and Global
Value Chains. The report highlights how
Bangladesh can diversify its participation in
trade and global value chains to help promote
economic growth. It also explores how the
country can build on its recent economic
success by unlocking productivity gains from
technology adoption, narrowing the digital
divide, and expanding its participation in global
value chains.
[page 37]

In the third partnership, the Statistical,
Economic and Social Research and Training
Centre for Islamic Countries (SESRIC), in
collaboration with the Islamic Development
Bank (IsDB) Group, organized the 12th Session
of the OIC-StatCom. Bringing together 64
participants from the National Statistical
Offices of 39 OIC countries, the session also
saw the participation of representatives from
international and regional organizations.
These included the Arab Institute for Training
and Research in Statistics (AITRS), International
Labour Organization (ILO), United Nations
Economic Commission for Western Asia
(UNESCWA), United Nations Population
Fund (UNFPA), and United Nations Statistics
Division (UNSD). Deliberations covered three
key technical topics, namely 1) harnessing
geospatial technologies for robust census
activities, 2) effectively monitoring and
reporting progress on SDG 8 (Decent Work
and Economic Growth) indicators, and 3)
implementing best practices for impactful
e-learning programs in official statistics.
[page 37]

5.2 Publications: 
The Institute provides market insights and practical analysis for addressing the development challenges
of MCs. This includes identifying critical areas of MCs’ economic and financial interest to support their
development and respond to these with insights from research. The research output leads to publications
in the form of books, reports, and articles on diverse topics in Islamic finance and sustainable development.
In 2023, a number of publications were issued on diverse topics including Islamic finance industry
strategies, climate action, takaful, sukuk, and social entrepreneurship. Some of the major publications
are highlighted below under their respective categories, while a full list of publications issued in 2023 is
in Annex 1.
[page 38]

5.2.1 Islamic Finance & Development
Building Climate Resilience Through Takaful: This report from
the UNDP, IsDB, and IsDBI highlights opportunities, challenges,
and recommendations for Takaful—a shariah-compliant
insurance alternative—to build the financial resilience of at-
risk Muslim communities against rising climate risks. The report
lays out the evidence and key recommendations for Takaful to
be developed, implemented, and scaled to build the financial
resilience of at-risk Muslim communities on the frontlines of
climate change. It highlights significant potential in the Arab
States region and beyond for the development of Takaful,
achievable through innovative public-private partnerships
between the government and the insurance industry. The
report is available free on IsDBI website.
IFSI 10 Years Framework and Strategies: Anchored on three
core pillars, development, transformation, and access, this final
review presents an assessment of the effectiveness of the various
recommendations and initiatives in the mid-term review (MTR)
on the growth and development of the global Islamic financial
services industry over the past years since the MTR. In light of
the fast-changing dynamics of the global financial ecosystem, the
final review suggests that the Islamic financial services industry
should continue to adapt to digital transformation, support the
SDGs, complement various Environmental, Social, and Governance
(ESG) initiatives, fund infrastructural projects, and support post-
COVID-19 economic recovery across many jurisdictions. The report
is available free on IsDBI website.
Islamic Economic Studies Journal: The Institute’s Islamic Economic Studies (IES) journal publishes
leading research across all fields of Islamic Economics and Finance. Established in 1993, it is one of the
oldest and most respected scholarly journals in Islamic Economics and Finance. IES is a peer-reviewed
journal targeted at professional and academic economists and students. Since 2020, the journal has
been published in partnership with Emerald. In 2023, two issues of the journal were published and are
available on Emerald Insight website.
[page 38]

5.2.2 Economic Research & Analysis
A core component of the IsDB’s Member Country Partnership
Strategy is in-depth country diagnostic studies. These studies,
conducted by IsDBI, analyze the economic and development
issues that partner countries face and help in designing
customized interventions for each context. The goal is to promote
sustainable and inclusive development that responds to MCs’
diverse needs and aspirations. The country diagnostic studies
also inform strategic planning and enhance understanding of the
development dynamics of IsDB MCs. In 2023, IsDBI completed
diagnostic studies for Tajikistan, Uzbekistan, Côte d’Ivoire,
Cameroon, Kazakhstan, Oman, Brunei, Albania, Bahrain, Tunisia,
and the Gambia.
The Institute also produced or contributed to other key economic analysis reports. These include SDG
Progress Report for IsDB MCs, IsDBG Integration Report for Arab Countries, IsDB Member Country Macro-
Perspectives, and Quarterly Brief on Global Economic Trends. These publications serve as comprehensive
monitoring tools, pivotal in supporting evidence-based decision-making within the IsDB Group. These
reports guide the Bank’s strategic interventions by providing in-depth insights into the ever-evolving
landscape of IsDB MCs and the broader economic context.
[page 39]


5.2.3 Statistical Publications
Ensuring the reliability of statistics is a pivotal to the IsDB Group’s
operational efficiency and reporting processes. The provision
of data for evidence-based decision-making among internal
stakeholders constitutes a central function that is fundamental
to the seamless operation and reporting of the IsDB Group. In
an ever-evolving global landscape, the demand for accurate
and timely data has gained unprecedented significance.
Consequently, in 2023 IsDBI steadfastly upholds its role as
the custodian of data and the primary point of contact for all
IsDB Group-related data as well as data pertaining to the IsDB
MCs. This commitment underscores the Institute’s dedication
to maintaining the highest standards of data quality, reliability,
and accessibility, thereby contributing to the informed decision-
making processes essential for the IsDB Group’s continued
success.
In 2023, the Institute issued the IsDB Group in Brief and Country Snapshot, quarterly publications that
are designed to furnish timely and precise information on the macroeconomics, trade, socioeconomic
development, government finance, governance of MCs and non-MCs, and cumulative interventions
of IsDB Group. These publications serve as a valuable resource for internal partners and management,
ensuring they stay abreast of the most recent data. This up-to-date information aids in formulating
targeted strategies for effective engagement with MCs, aligning the IsDB Group’s initiatives with the
evolving needs and conditions of the countries it serves.
[page 39]


5.3 Cloud Reader for e-Books
The IsDBI e-book reader app, which was launched
in early 2022, is a dedicated platform for
reading publications on Islamic Economics and
development. The app leverages the Institute’s
expertise and experience in publishing and uses
innovative technologies to provide an enhanced
reading experience. The app is available on Apple
Store and Google Play for smart devices such as
tablets and phones.
To cater to the needs and preferences of readers
who use larger screens, such as personal
computers or laptops, the Institute developed
the cloud-based version of the e-book reader
app, which was completed in 2023. This is a web
application that allows users to read IsDBI e-books
on any compatible web browser, without having to
download them to their devices.
Both the smart devices app and the cloud version
are linked to the IsDBI website, where customers
can purchase and download the e-books. The app
has been well-received by users from around the
world, who have downloaded thousands of e-books
since its launch. The Cloud Reader is accessible
here: https://read.isdbinstitute.org
[page 40]

5.4 IsDB Group Library
The IsDB Group Library continues to serve as a hub
for knowledge, with a vast collection of resources
in various fields, including economics, finance,
investment, development, and technology. The
library provides access to a range of databases,
online information services, and periodicals, all
available to staff in both the HQ and regional
offices. Such databases and resources include IHS
Markit, Fitch Solutions, OECD i-library, World Bank
e-library, Economist Intelligence Unit database,
and PressReader newsstand platform, which offers
access to over 7,500 newspapers and magazines.
The library is easily accessible to staff members
through a convenient portal available on the
intranet. The year 2023 marks the completion of the
new library management system (Soutron). Staff
managing the library have already benefited from
training sessions and begun using the cataloguing
and loan modules of the system during the trial
phase. The system, available in English, Arabic, and
French languages, is currently being cleaned up, in
readiness for a full rollout to staff.
[page 40]


5.5 Outreach Initiatives
The Institute achieved a significant boost in
its public profile and impact through various
outreach initiatives in the past year. The Institute
focused on improving its online presence and
messaging, resulting in a remarkable increase in
the visibility of the Institute in the media. On social
media, IsDBI gained thousands of followers and
subscribers on various platforms such as LinkedIn,
Facebook, Twitter, and YouTube. The Institute used
these channels to disseminate information on its
knowledge solutions, products, and services; raise
awareness about its activities and events; and
gather feedback from the public.
The Institute’s main website (www.isdbinstitute.
org) continues to serve as a vital platform for
sharing knowledge and information, as well as
marketing and selling the knowledge products.
The website showcases the Institute’s products
and services to a wide range of audiences who are
interested in Islamic economics and finance, and
sustainable development. The website’s popularity
and engagement have remained stable over the
past three years.
Another platform that the Institute uses to
promote innovative ideas and new insights on
contemporary issues is the blog website (IsDBI
Blogs). The blog features posts from IsDB Group 
professionals and external experts on various topics
related to Islamic economics and finance, fintech,
and sustainable development. The blog, which
was launched in mid-2020, has been publishing
regularly and attracting readers from different
backgrounds and regions. Annex 4 contains a list of
blog articles published in 2023, while all published
articles are available on the blog site here:
https://blogs.isdbinstitute.org/
[page 40]


5.6 Conferences & Knowledge Events
The Institute participates in key conferences around the world to share and gain insights on
new developments in areas related to Islamic finance and development. Additionally, IsDBI
organizes knowledge events within the IsDB Group where global experts and staff address
various development issues. These events enable the IsDB Group experts to exchange ideas,
update their knowledge, and learn from best practices in different areas and sectors. Some of the
key conferences and knowledge events are highlighted below [See full lists in Annex 5].
17th Global Forum on Islamic Finance
The 17th IsDB Global Forum on Islamic Finance was a landmark side event held on 12 May 2023
during the 2023 IsDB Group Annual Meetings in Jeddah, Saudi Arabia. The forum focused on
the fusion of disruptive technologies with Islamic finance to foster economic resilience. The
forum brought together industry experts to discuss how digital innovations, like digital vouchers,
can drive financial inclusivity and resilience. The forum was co-organized with three knowledge
partners: King Abdullah University of Science and Technology (KAUST), Effat University, and
University of Business and Technology (UBT), Jeddah, KSA.
[page 41]

Particularly noteworthy were the panel discussion
sessions, the first on the application of smart
vouchers in Islamic finance, and the second on the
Sukuk Enhancement Fund (SEF) as a product that
aims to support the Islamic finance ecosystems. The
vouchers, seen as a bridge between technology and
financial services, have the potential to significantly
enhance economic resilience and inclusivity,
especially in underbanked populations.
During the forum, the Institute hosted a launching
ceremony of the book that documents the historical
evolution and significant accomplishments of the
IsDB Group over a period of four decades. The
launching was led by the current and former IsDB
Presidents, H.E. Dr Muhammad Al Jasser and H.E. Dr
Ahmad Mohammad Ali. The book was first published
in Arabic language in 2020, followed by the English
language version in 2022 and the French version in
2023.
[page 42]


Evolving Role of Central Banks in Times of Uncertainty
The Institute organized a public lecture on 17
August 2023 titled ‘The Changing Role of Central
Banks in Times of Uncertainty,’ delivered by Dr.
Ishrat Husain, a former Governor of Pakistan’s
Central Bank and Advisor to the Prime Minister.
Dr. Husain, a distinguished economist and
experienced central banker, discussed the current
global economic trends and challenges, and the
heightened responsibilities of central banks during
periods of economic turbulence and uncertainty.
He highlighted the need for collective action
among governments, the private sector, civil
society, academia, and financial markets to address
the complex global economic challenges. He
specifically emphasized the importance of bridging
wealth gaps, investing in the younger generation,
combating misinformation, and balancing climate
and development financing. Dr. Husain also shed
light on the trade-offs faced by central banks, such
as the need to balance curtailing inflation with
preventing unemployment and managing fiscal deficits with financing development. He called for
stakeholder collaboration to address the issues
so as to strengthen the role of Islamic finance in
promoting sustainable economic growth.
[page 42]


Current State of the Global Islamic Finance Industry
IsDBI and IsDB Financial Control Department
jointly organized this public lecture titled ‘Current
State and Challenges of the Global Islamic
Finance Industry’ on 14 September 2023. Mr.
Omar Ansari, the Secretary General of AAOIFI,
delivered the lecture, providing an overview of the
Islamic financial industry globally, the challenges
the industry faces, and suggestions on the way  forward. Mr. Ansari noted that the industry has
grown significantly over the past years, but
challenges persist in areas related to regulation,
standardization, awareness, governance, funding,
market fluctuations, and technology. He identified
collaboration among stakeholders as one of the
key steps towards finding solutions to ensure
sustainable development for the industry.
[page 43]

OIC COMCEC Central Banks Forum
IsDBI’s participated in the OIC COMCEC Central
Banks Forum focusing on Central Bank Digital
Currencies (CBDCs). The forum, held on 26
September 2023, provided an ideal platform
for IsDBI to showcase its expertise and insights
regarding the integration of Islamic finance
principles with digital currency solutions. The Institute’s contribution centered on the potential
of the smart voucher system and its applicability
within the CBDC framework. This participation
positioned IsDBI as a thought leader in the digital
currency space, and set the stage for future
collaborations and innovations in Islamic digital
finance.
[page 43]

IsDB Prize Laureates Lecture
This is part of a series in which the winners
(or their representatives) of the IsDBI Prize for
Impactful Achievement in Islamic Economics
make presentations on topics relevant to the prize
category. On 15 November 2023, a representative
of the Ministry of Finance of Indonesia, Dr.
Muhammad Iqbal Balatif, highlighted the novel
financing mechanism that won the 2023 IsDB Prize
for Impactful Achievement in Islamic Economics. An
initiative of the Indonesian Finance Ministry, “Cash
Waqf Linked Sukuk” (CWLS) won the prestigious
IsDB Prize for its immense impact in mobilizing
development finance.
[page 43]

Global Standards for Central Bank Digital Currency
The Institute was a knowledge partner in the
conference entitled “Exploring Central Bank Digital
Currency: Pathways to Global Standards”, which
took place on 28-29 November 2023 in Virginia,
United States. It brought together international
financial policymakers and launched new research
on important topics in CBDC field. The conference
aimed to share the main technology and policy
issues for developing a CBDC, identify areas where
public and private sectors can collaborate, and create a plan for reaching global standards. Dr.
Hilal Houssain, Associate Manager for Knowledge
Solutions at IsDBI, joined a roundtable session
called: “Defining Success: Achieving Safe, Efficient,
Connected Networks”. He talked about IsDBI’s
innovative Islamic financial solutions, such as
digital voucher and credit enhancement system,
and the development of a stabilization system
prototype.
[page 44]

18th AAOIFI - IsDB Annual Conference
Jointly organised with AAOIFI, this conference
was held on 29-30 November 2023 in Bahrain
with the theme, “Strategies for Impending
Economic Slowdown and a Post-Oil World:
Through Economic Diversification and
Leveraging Islamic Finance.” The conference
attracted more than 770 delegates from
over 35 countries, as well as a similarly large
number of online attendees. The participants
included representatives from 23 regulatory
and supervisory authorities, such as Bank
of Russia, Reserve Bank of South Africa,
Insurance Regulatory Authority of Uganda,
Capital Markets Authority of Saudi Arabia,
Qatar Financial Centre Regulatory Authority,
Maldives Monetary Authority, and National
Bank of Tajikistan. The conference featured
42 speakers in seven sessions, as well as
keynote addresses.
[page 44]

"""
chapter6 = """
Chapter 6 Strengthening Institutional Effectiveness This chapter covers the Institute’s programs and activities related to strengthening internal governance and operational effectiveness.
[page 46]

6.1 Board of Trustees
The Board of Trustees (BOT) is an advisory organ
mandated to provide guidance and direction
on the Institute’s strategy, medium-term work
program, and budget. The Board comprises
eminent personalities from various professional
backgrounds in both the public and private
sectors, who are appointed for a 3-year renewable
term. H.E. the Chairman of the IsDB Group is also
the Chairman of the Board of Trustees.
The Board meets at least once a year. In 2023,
the Board held its 12th meeting during which
the members commented on the Institute’s
groundbreaking smart projects dedicated to
advancing sustainable economic resilience in
IsDB MCs. The Board Members expressed delight
over the Institute’s performance, congratulating
its management and staff on the key initiatives
and achievements. Furthermore, the Board
commended the Institute’s leadership role in
integrating modern technologies with Islamic
finance to foster socio-economic development.
[page 47]

6.2 IsDBI Project Management Center
To enhance efficiency and effectiveness in
project execution, IsDBI has developed a
dedicated Project Management Center (PMC),
which marks an important stride towards
implementation of its strategy and facilitating
enhanced reporting to the Management on
core activities of the Institute. The center
aims to centralize and streamline project
management processes and is dedicated to
guiding the IsDBI business units towards the
successful execution of projects, ensuring
alignment with client expectations. PMC’s main
objectives are to (i) enhance the monitoring
of resources use to maximize efficiency, (ii)
refine project management processes, (iii)
improve the process flow and ensure robust
involvement of all stakeholders; (iv) increase
the productivity and operational efficiency of projects; and (v) offer a comprehensive
dashboard for effective reporting on project
progress.
In 2023, the first phase of this initiative
was successfully implemented for all IsDBI
projects. This phase involved integrating the
platform with the IsDB Knowledge Platform
in partnership with the IsDB IT Department.
The next phases will focus on improving
the user interface and developing reporting
dashboards. These dashboards will allow
Management and project members to
monitor and track programs and projects
more easily and quickly. The initiative will also
enable the generation of real-time quarterly
performance reports directly on the platform.
[page 47]


6.3 Driving Business Excellence
The Corporate Performance Team (CPT) of the Institute plays a vital role in advancing IsDBI’s strategic
goals, making sure that its activities support its vision and mission for the long term. In 2023, the
team made remarkable progress in improving IsDBI’s performance indicators, strengthening data-
based decision making, and fostering a culture of ongoing improvement across the Institute. The
following are some of the main accomplishments in 2023.
[page 48]

6.3.1 Strategic Alignment
The team successfully aligned institutional goals
with the IsDBI’s overarching strategy, ensuring a
unified direction and consistent focus on priority
areas. During the year, strategic administrative
decisions have been issued, such as updating
the Special Allocation Guidelines (SAG), creating
a new in-house projects committee, and
developing a new project completion report.
[page 48]

6.3.2 Performance Metrics Enhancement
Through rigorous analysis and stakeholder
engagement, the team enhanced IsDBI’s
suite of performance metrics, providing more
insights into operational efficiency, client
satisfaction, and financial performance. The
team worked closely with other business units
to develop, review, and recommend policies
and procedures for institutional effectiveness.
The team has coordinated and participated
in institutional development, performance
evaluation, assessment, and planning. The team
shared timely information accurately with the
management.
[page 48]

6.3.3 Process Optimization and Quality
Assurance
The team led several initiatives to streamline
processes, improving workflow efficiency and
cost savings. Notable achievements include the
implementation of a new project management
framework and the automation of key reporting
processes. IsDBI updated its monitoring
framework to screen the quality of the projects.
During the year, the team coordinated with the
project officers to apply the project guidelines
to the ongoing projects.
In 2023, the IsDBI initiated the harmonization
process of all the projects with IsDB’s digital
application, the Operations Management Solutions
(OMS) system, with its own Project Management
Center. Henceforth, the OMS system and PM Center
will be the co-source for Islamic finance grant
projects. Within both systems, the Institute will be
able to reduce the life cycle of the projects and
deliver effective coordination with the other relevant
departments of the IsDBG. In 2023, the Institute
initiated a new methodology for the pipeline, under
implementation, and “need to be closed” projects.
[page 48]


Additionally, the team managed the business
and OMS processes for the Institute’s entire
portfolio. It reviewed and cleared the deliverables,
disbursements, amendments of the Islamic finance
grant, capacity building, and awareness projects.
Integrating into the IsDBG operations and creating
its project management system helped the Institute
achieve high efficiency. In addition, the following
benefits have been achieved:
- More performance measurements have been
developed to improve project management and
effectiveness.
- The quality of the project deliverables has been
improved.
- Project life cycles have been shortened, thereby
boosting productivity.
- Possible project complications have been
minimized.
- Teams have enhanced the integration process, and
effective project execution and completion have
been achieved.
[page 48]

Ultimately, the Institute has operated its
projects more profitably and cost-effectively
from their creation to closures. During the
year, the checklists have been used for project
amendments, extensions, peer reviews, and
scope changes. Looking ahead, the team
remains committed to driving excellence across
the IsDBI. Key focus areas for the upcoming year
include:
- Further Enhancing Performance Metrics:
Continuously refining and expanding IsDBI’s
performance metrics to provide a comprehensive
view of organizational performance.
- Leveraging Technology: Exploring innovative
technologies and tools to further enhance IsDBI’s
analytics capabilities and drive operational
efficiency.
- Strengthening Collaboration: Fostering greater
collaboration across the IsDBI to ensure alignment
of goals, sharing of best practices, and collective
achievement of strategic objectives.
The CPT will continue to play a pivotal role in the
Institute in the years to come, through focus on
excellence, data-driven insights, and employee
engagement.
[page 49]

"""

annexes = """
Annex 1 Publications
[page 50]

Name of publications
--------------------
The Islamic Development Bank and Dr. Ahmad Mohammad Ali (French Edition)
IFSI Development Ten-Year Framework and Strategies: A Final Review
Insuring a Sustainable Future
[page 51]

Knowledge Review, Vol. 9 No. 2)
Islamic Economic Studies Journal (Vol. 30 Issue 2 & Vol. 31 Issue 1)
IsDB Annual Report 2022 (Arabic, English, and French)
[page 52]

IsDBI Annual Report 2022 (Arabic, English, and French)
Statistical Yearbook (2022)
Country Diagnostic Studies
[page 53]

Reaching the SDGs: Progress of the IsDB Member Countries (5 th Edition)
IsDB Group in Brief
Country Snapshot
[page 54]

IsDB Member Country Macro- Perspectives
Member Country Macroeconomic Vulnerabilities
Transforming Bangladesh’s participation in Trade and Global Value Chains
[page 55]


Annex 2: IsDB Prize Laureates
Year | Prize Category | Laureate | Citizenship/Country
------------------------------------------------------
1408H/ 1988 | Islamic Economics | Prof. Khurshid Ahmad | Pakistan
1408H/ 1988 | Islamic Banking and Finance | Dr. Sami Hasan Ahmad Homoud | Jordan
1408H/ 1988 | Islamic Economics | Dr. Muhammad Umar Chapra | Saudi Arabia
1408H/ 1988 | Islamic Banking and Finance | Tabung Haji | Malaysia
1408H/ 1988 | Islamic Economics | Dr. Muhammad Anas Zarqa | Syria
1408H/ 1988 | Islamic Banking and Finance | Dr. Ziauddin Ahmad | Pakistan
1408H/ 1988 | Islamic Economics | Dr. Yousuf Abdullah Al-Qaradawi | Egypt
1412H/ 1992 | Islamic Banking and Finance | Dr. Sabahuddin Zaim | Turkey
1413H/ 1993 | Islamic Economics | Centre for Research in Islamic Economics | Saudi Arabia
1414H/ 1994 | Islamic Banking and Finance | Dr. Ahmad Mohammed Ali | Saudi Arabia
1415H/ 1995 | Islamic Economics | Dr. Muhammad Omar Zubair | Saudi Arabia
1416H/ 1996 | Islamic Banking and Finance | Cheikh Saleh Abdullah Kamel | Saudi Arabia
1417H/ 1997 | Islamic Economics | Dr. Abdul Rahman Yousri | Egypt
1417H/ 1997 | Islamic Economics | Dr. Rafic Al-Misri | Syria
1418H/ 1998 | Islamic Banking and Finance | Dr. Tanzilur Rahman | Pakistan
1419H/ 1999 | Islamic Economics | Sheikh Dr. Mohammed Al Habib Ibn Al Khoja | Tunisia
1420H/ 2000 | Islamic Banking and Finance | International Institute of Islamic Economics | Pakistan
1421H/ 2001 | Islamic Economics | Dr. Monzer Kahf | USA
1421H/ 2001 | Islamic Economics | Dr. Syed Muhammad Hasanuzzaman | Pakistan
1421H/ 2001 | Islamic Economics | Sheikh Saeed Ahmed Lootah | UAE
1421H/ 2001 | Islamic Economics | Prof. John Presley | UK
1421H/ 2001 | Islamic Economics | Dr. Abbas Mirakhor | Iran
1421H/ 2001 | Islamic Economics | Dr. Mohsin Khan | Pakistan
1422H/ 2002 | Islamic Banking and Finance |  | 
1422H/ 2002 | Islamic Economics |  | 
1423H/ 2003 |  |  | 
1424H/ 2004 | Islamic Banking and Finance | Dr. Mohammad Ali Al Qari | Saudi Arabia
1425H/ 2005 | Islamic Economics | Dr. Shawqi Ahmed Dunya | Egypt
1426H/ 2006 | Islamic Banking and Finance | Prince Mohamad Alfaisal Al Saud | Saudi Arabia
1427H/ 2007 | Islamic Economics | Dr. Abdussalam Dawoud Al-Abbadi | Jordan
1428H/ 2008 | Islamic Banking and Finance | Sheikh Mohammed Mukhtar Al Salami | Tunisia
1428H/ 2008 | Islamic Banking and Finance | Sheikh Abdullah Bin Sulaiman Al Manee' | Saudi Arabia
1429H/  |  | [Withheld] | 
1430H/ 2009 | Islamic Economics | Dr. Zubair Hassan | India
1431H/ 2010 | Islamic Banking and Finance | Prof Rifaat Ahmad Abdul Karim | Sudan
1432H/ 2011 | Islamic Economics | Islamic Foundation | U.K.
1433H/ 2012 | Islamic Banking and Finance | Tan Sri Dr. Zeti Akhtar Aziz | Malaysia
1434H/ 2013 |  | [Withheld] | 
1435H/ 2014 | Islamic Banking and Finance | Sheikh Taqi Usmani | Pakistan
1436H/ 2015 | Islamic Economics | Dr. Saif El din Ibrahim Taj El din | UK
1437H/ 2016 | Islamic Banking and Finance | Prof. Mohammed Kabir Hassan | USA
1438H/ 2017 | Islamic Economics | [Withheld] | 
1439H/ 2018 | Islamic Banking and Finance | Dr. Ahmed Ali Abdullah | Sudan
1440H/ 2019 | Islamic Economics, Banking and Finance | Dr. Mabid Ali al-Jarhi | Egypt
1441H/ 2020 |  | [Not Awarded] | Egypt
1442H/ 2021 | Development Solutions Achievement | LaunchGood (first prize),Seed Out (second prize) | United States,Pakistan
1443H/ 2022 | Knowledge Contribution Achievement | Prof Habib Ahmed (first prize),Prof. Mansur Masih (second prize),Prof. Tariqullah Khan (third prize) | USA,Australia,Pakistan
1444H/ 2023 | Development Solutions Achievement | Ministry of Finance of the Republic of Indonesia | Indonesia
[page 56,57]

Annex 3: Training Programs
Title | Venue | Date | Language | Partner Institution | No. of Participants
---------------------------------------------------------------------------
AAOIFI Financial Accounting Standards | Saudi Arabia, Riyadh | 15-17/02/2023 | Arabic | Saudi Central Bank | 20
Takaful Training Workshop for Jaiz Takaful | Saudi Arabia, Riyadh | 17-19/01/2023 | English | Jaiz Bank | 24
Sukuk for liquidity management | Saudi Arabia, Jeddah | 01-04/05/2023 | Arabic | Central Bank of Yemen | 15
Zakat Management | Uganda, Kampala | 14-16/8/2023 | Arabic | House of Zakat and Waqf, Uganda | 30
AAOIFI Shari’ah Standards | Saudi Arabia, Riyadh | 17-21/9/2023 | Arabic | Saudi Central Bank | 12
Islamic Finance Basics | Saudi Arabia, Jeddah |  | Arabic | Saudi Central Bank | 12
Operational Aspects of Accounting Standards of Islamic Financial Institutions Part 1 | Virtual | 25-28/9/2023 | Arabic | Arab Monetary Fund | 45
Islamic Finance Executive Program | Saudi Arabia, Jeddah | 13-16/11/2023 | English | King Abdulaziz University (KSA) and I.E. Business School (Spain) | 15
Islamic Capital Markets Capacity-Building Workshop |  | 21-11-2023 | English | Nigerian Exchange Limited (NGX) | 90
Islamic Capital Markets Enabling Environment Roundtable | Nigeria, Lagos | 22-11-2023 | English | Nigerian Exchange Limited (NGX) | 12
Operational Aspects of Accounting Standards of Islamic Financial Institutions Part 2 | Institutions Virtual | 18-21/12/2023 | Arabic | Arab Monetary Fund | Prof. Khurshid Ahmad
Islamic Finance Product Development | Virtual | 5/11/2023 | English | BIBF | Prof. Khurshid Ahmad
Introduction to Multidimensional Poverty Measurement | Saudi Arabia, Jeddah | 24-25/1/2023 | English | IsDBI, ISFD & OPHI | 40
[page 58]

Annex 4: Blog Articles
S/No | Title | Author
---------------------
1 | Inflation: The Dog that Did not Bark | Sami Al-Suwailem
2 | Impact of Global Crises on Poverty: Measurement, Trends, and Challenges | Mustafa Yagci
3 | BRICS Consolidation Transforming Global Economic and Development Landscape | Musa Jega Ibrahim
4 | Global Crises, Central Bank Responses, and the Inversion of the Yield Curve | Mustafa Yagci
5 | US Banking Crisis and Risks of Global Contagion | Prof. Khurshid Ahmad
6 | The Challenge of Debt Sustainability in IsDB Member Countries amid Tightening Global Financing Conditions | Prof. Khurshid Ahmad
7 | A Paradigm Change for the Global Financial System | Sami Al-Suwailem
8 | Significance of Adopting Digital Financial Technologies in Egypt | Abdelrahman Elzahi Saaid Ali
9 | Unlocking the Access of SMEs to Capital Markets through Sukuk Enhancement Fund | Turkhan Ali Abdul Manap
10 | Expansion of BRICS and the Shifting Dynamics of the Global Economy | Ismaeel Naiya, Muhamed Zulkhibri
11 | Rationalizing Energy Consumption in Saudi Arabia towards an Energy-efficient, Green Economy | Bukhari Sillah, Abu Camara
12 | Unlocking the Potential of Islamic Finance: An In-Depth Look at IsDBI’s Islamic Finance Sector Mapping Framework | Turkhan Ali Abdul Manap, Syed Faiq Najeeb, Yahya Aleem ur Rehman
13 | Ending Hunger in Africa: Tracking Maputo Declaration in IsDB SSA Member Countries | Bukhari Sillah, Mohamed Elgoussi, Novia Budi Parwanto
14 | Fragility and Development Challenges in IsDB Member Countries: The Case of Niger | Cheikh Ahmed Diop, Mustafa Yagci
15 | Advancing Access to Digital Financial Services in Egypt | Abdelrahman Elzahi Saaid Ali
16 | Milestones and Challenges in Egypt's Digital Financial Technology Adoption | Abdelrahman Elzahi Saaid Ali
17 | ‫نحو هندسة مالية إسلامية خضراء ومستدامة‬ | Mahmoud Bekri
18 | ‫الحافز المنحرف: تلك الكوبرا التي تلدغ التنمية‬ | Mahmoud Bekri
[page 59]


Annex 5: Conferences & Knowledge Events Annex 5A
S/No | Title | Venue
--------------------
1 | 17th IsDB Global Forum on Islamic Finance | Jeddah, KSA
2 | 18th AAOIFI-IsDB Islamic Banking & Finance Conference | Bahrain
3 | Brunei Islamic Finance Summit 2023 | Brunei Darussalam
4 | IsDBI-AIFC Islamic Finance Conference | Astana, Kazakhstan
5 | UNDP-IsDB-IsDBI-AFGUND Side Event in COP 28 | Dubai, UAE
6 | ADB-IsDB Webinar on Islamic Finance and Climate Action | Online
7 | Exploring Central Bank Digital Currency: Pathways to Global Standards | Virginia, U.S.
8 | 1st Islamic Business and Investment Forum in Kyrgyz Republic | Kyrgyz Republic
9 | 6th Islamic Finance Forum | Algiers, Algeria
[page 60]

Annex 5: Conferences & Knowledge Events Annex 5B
No | Title/Theme | Organizers/Partners
--------------------------------------
1 | 20th SDGs Open Dialogue with U.S. President's Special Advisor Sarah Minkara | IsDBI & SDGs CoP
2 | Multidimensional Poverty Measurement | IsDBI, ISFD & OPHI
3 | Awareness Session on the IsDB Group Integration Report 2022 | IsDBI
4 | Nigeria: Diversifying Sources of Growth for Inclusive Development | IsDBI
5 | A Brightening Global Outlook, Easing Inflation, and its Impact on the Middle East | IsDBI & IHS Markit
6 | ‘Supporting Self-Reliance and Stability: Japan’s Official Development Assistance, NGOs Activities, and Approaches to Afghanistan’, presented by Professor Daisaku Higashi of Sophia University in Tokyo | IsDBI, IsDB & Japanese Consulate
7 | Tajikistan: Achieving Inclusive and Sustainable Development | IsDBI
8 | Uzbekistan: Structural Reforms for Inclusive and Sustainable Development | IsDBI
9 | IsDB Group Activity Dashboard | IsDBI
10 | Launch of IsDB Group Integration Report for Arab Countries | IsDB & IsDBI (Annual Meeting Side Event)
11 | Sustainable Development Disrupted - Advancing Impactful SDGs CoP | IsDBI (Annual Meeting Side Event)
12 | North Africa: 2023 Outlook and Beyond | IsDBI & Fitch Solutions
13 | Global Risk and MENA Regional Outlook | IsDBI, IsDB, and S&P Global
14 | Côte d'Ivoire: Economic Diversification for Higher-Sustained Growth to Reach Upper Middle-Income Status | IsDBI
15 | Kazakhstan: Working Towards a More Prosperous Future | IsDBI
16 | Brunei: Enhancing Fiscal Space, Advancing Structural Reforms and Strengthening Resilience | IsDBI
17 | Oman: Reviving Growth Toward a Competitive, Inclusive Economy | IsDBI
18 | IsDB Member Country Macroeconomic Vulnerabilities Report (9th Edition) | IsDBI
19 | Creating More Jobs by Integrating Employment Intensive Investment Approach through Public Investment in Infrastructure Projects | SDGs CoP, IsDBI & ILO
20 | A Recession Averted? Economic and Business Outlook for 2024 and Beyond | IsDBI & EIU
21 | The New Role of Central Banks in Turbulent Times (Presented by Dr. Ishrat Husain) | IsDBI & IsDB
22 | Albania: Upskilling the Labor Force and Diversifying Gains from Trade | IsDBI
23 | Current State and Challenges of the Global Islamic Finance Industry (Presented by Mr. Omar Ansari) | IsDBI & IsDB
24 | Global Economic Outlook with GCC Focus | IsDBI and S&P Global
25 | Global Economic & Emerging Market Commodities Outlook | IsDBI & Fitch Solutions
26 | Structural Transformation and Just Transition in Africa | IsDBI & Global Institute for Sustainable Prosperity
27 | Advanced Country Intelligence Monitor Service | IsDBI and S&P Global
28 | Cash Waqf-Linked Sukuk: A Novel Mechanism | IsDBI
29 | Regional Outlook for the Infrastructure & Construction Sector in MENA | IsDBI & EIU
[page 61,62]
"""
# Combine the content
# combined_content =  chapter2_text
with open("test.txt", "r") as file:
    combined_content = file.read()

prompt_template = f"""
You are an assistant that only answers questions based on the provided text and tables from two chapters of a book. The chapters are as follows:

{combined_content}

If a question is related to these chapters, answer based on the information provided. If the question is not related to these chapters, respond with "I don't know about it."
if you got the answer then you must mention therse things:
• Publication Title
• Page number
• Paragraph Information where you get this answer

and box and tables are different if i ask about table just give me table info if i ask about paragraph give me paragraph info and if i ask about box give me box info.
"""


import openai

# Set your OpenAI API key
# openai.api_key = ""  # Replace with your actual OpenAI API key


def ask_model(question, document_content,conditon=False):
    # Create the prompt with the document content and the user's question
    if conditon:
        prompt = f"""
You are an assistant that answers questions based on the provided text document. Here is the document:

{document_content}

Based on the above document, please answer the following question thoroughly and provide a complete response. If the user asks for a table or numerical data, present it clearly in a table format. 

Ensure that your response is formal, understandable, and provides all relevant details, including:

- **Publication Title:** Mention the title of the publication where the information was found.
- **Page Number:** Include the page number where the information appears.
- **Paragraph Information:** Describe the section or paragraph where you found the answer.

If the question is not related to the document or the information cannot be found, respond with: "Sorry! I did not understand your question. Please retry."

Question: {question}
"""

    else:
        prompt = f"""You are an assistant that answers questions based on the provided text document. Here is the document:

    {document_content}

    Based on the above document, please answer the following question:
    Question: {question}
    
    If a question is related to these chapters, answer based on the information provided. If the question is not related to these document, respond with "sorry! i did not understand your question. please retry"""
    

    # Call the OpenAI API with the prompt
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # Use the correct method and model name
        messages=[
            {"role": "system", "content": prompt}
        ],
        max_tokens=1000  # Adjust this as needed based on expected answer length
    )
    
    msg= response.choices[0].message.content
    # print("#"*100)
    # print(msg)
    # if msg=="I don't know about it.": return ""
    return msg
def main():
    # Example: List of chapters; replace with your actual chapter contents
    chapters = [
        book_knowledge,
        chapter1,
        chapter2,
        chapter3,
        chapter4,
        chapter5,
        chapter6,
        annexes
        # Add more chapters as needed
    ]

    while True:
        question = input("Enter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break

        all_responses = []

        # Ask the question for each chapter
        # for chapter in chapters:
        #     response = ask_model(question, chapter)
        #     all_responses.append(response)

        # # Merge all responses into one text
        # merged_response = "\n".join(all_responses)
        
        # Ask the same question again with the merged response
        final_answer = ask_model(question, book_knowledge+chapter1+chapter2+chapter3+chapter4+chapter5+chapter6+annexes,True)
        print(f"Answer: {final_answer}")

if __name__ == "__main__":
    main()
