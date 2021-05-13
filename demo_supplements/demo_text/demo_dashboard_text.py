"""Homepage text for demo app features."""

api_descriptions = {
    "Recent Life Events API": """
        Recent Life Events checks your applicant
        or policyholder against our complete reference data on 255 million
        adults and 130 million households. In real-time, the API returns all of
        the recent life events detected, including new mover
        (and former address), household changes, financial changes, and more.""",
    "Life Events Monitor": """
        Leveraging our Recent Life Events API service, the life events monitor 
        displays a list of policy holders who have experienced recent life events.""",
    "Auto Insurance Prefill API": """
        The Fenris Auto Insurance Prefill API fetches applicant data and pre-fills that
        information for the client to confirm, rather than require manual
        data entry from the client. Errors and application drop-off are
        eliminated, leading to more completed applications
        and a cleaner book of business at bind.
        This service provides the data
        and scores needed to inform decisions, evaluate risk,
        and improve the experience of applying for, rating, and
        servicing commercial insurance.""",
    "PFR API": """
        Fenris has created a suite of scores that inform financial
        service providers on how to engage potential customers based
        on data quality, financial predictors, customer performance metrics,
        and fraud indicators. Leveraging this advanced insight when
        quoting enables firms to direct resources efficiently,
        saving time and money while prioritizing the best customers.
        This service provides for an in-depth, thorough early
        understanding of potential customers.""",
    "Small Business API": """
        When provided a business name and address, the Small Business
        API (SMB) queries Fenris' comprehensive record collection to
        return extensive business details. The SMB service utilizes
        the Fenris best-in-class match rates to return a robust set of
        data fields in just seconds. This service provides time-saving insight to
        agents and brokers who are in the high-stakes quote/close policy
        phase. SMB also has access to micro-business data, allowing users
        to monitor the fast-growing gig economy.""",
    "Custom Request": """
    Query one of the following APIs with custom input:
    Auto Insurance Prefill, Life Events, Scoring, or Property Details.""",
}

sample_persona_names = [
    "Carissa Sharma",
    "Hugo Danner",
    "Guy Kleinert",
    "Carlita Hovenden",
    "Freida Marcinkus",
    "Fowler Schubert",
]

event_names = [
    "NEWLY ENGAGED",
    "NEWLY SINGLE",
    "NEW BABY",
    "NEWLY MARRIED",
    "PRENATAL",
    "PREMOVER AT CONTRACT",
    "PREMOVER AT LIST",
    "NEW MOVER",
]
