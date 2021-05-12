import datetime

from demo_api_pages.api_request_pages import live_response_page

from heimdal.entities.address import Address
from heimdal.entities.person import Person

import streamlit as st

states = [
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DC",
    "DE",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY",
]


def person_input(form_name):
    first_name = form_name.text_input("First Name:", help="Enter client first name")
    middle_name = form_name.text_input("Middle Name:", help="Enter client middle name")
    last_name = form_name.text_input("Last Name:", help="Enter client last name")
    date_of_birth = datetime.datetime.strftime(
        form_name.date_input(
            "Birthday",
            value=datetime.date(1970, 1, 1),
            min_value=datetime.date(1900, 1, 1),
            max_value=datetime.datetime.today(),
            help="Enter client date of birth",
        ),
        "%m/%d/%Y",
    )
    return first_name, middle_name, last_name, date_of_birth


def address_input(form_name):
    address = form_name.text_input("Address Line 1:", help="Enter client address")
    state = form_name.selectbox(options=states, label="State")
    city = form_name.text_input("City:", help="Enter client's city of residence")
    zip_code = form_name.number_input(
        "Zip Code:", value=12345, min_value=1000, help="Enter client zipcode"
    )
    return address, state, city, zip_code


def personal_request_form():
    api_endpoint = st.sidebar.selectbox(
        options=[
            "---",
            "Life Events",
            "PFR",
            "Auto Insurance Prefill",
            "Property Details",
        ],
        label="Select API",
    )
    refresh_page_to_response = False
    if not refresh_page_to_response:
        if api_endpoint == "---":
            st.write("Select an API to query on the sidebar at the left")
        elif api_endpoint != "---":
            st.write(f"Input for {api_endpoint} API")

            input_form = st.form(key="custom_request_form")

            address, state, city, zip_code = address_input(form_name=input_form)
            custom_address = Address(address, city, state, zip_code)

            body = custom_address

            if api_endpoint in ["Life Events", "PFR", "Auto Insurance Prefill"]:
                first_name, middle_name, last_name, date_of_birth = person_input(
                    form_name=input_form
                )
                custom_person = Person(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    date_of_birth=date_of_birth,
                    address=custom_address,
                )
                body = custom_person

            submit_button = input_form.form_submit_button(label="Submit")

            endpoint_mapper = {
                "PFR": "PFR",
                "Life Events": "LifeEvents",
                "Property Details": "PropertyDetails",
                "Auto Insurance Prefill": "AutoPrefill",
            }
            if submit_button:
                live_response_page.app(api=endpoint_mapper.get(api_endpoint), body=body)
