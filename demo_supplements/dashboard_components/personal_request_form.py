import datetime
from typing import Tuple

from demo_api_pages.api_request_pages import live_response_page

from heimdal.constants import service_names
from heimdal.entities.address import Address
from heimdal.entities.business import Business
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

personal_apis = ["PFR", "Life Events", "Auto Insurance Prefill", "Life Prefill"]
property_apis = ["Property Details", "Property Replacement Cost", "Property Risks"]

business_apis = ["Small Business"]


def person_input(form_name: st.form) -> Tuple[str, str, str, str]:
    """Personal input form."""
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
    return str(first_name), str(middle_name), str(last_name), date_of_birth


def address_input(form_name: st.form) -> Tuple[str, str, str, str]:
    """Address input form."""
    address = form_name.text_input("Address Line 1:", help="Enter client address")
    state = form_name.selectbox(options=states, label="State")
    city = form_name.text_input("City:", help="Enter client's city of residence")
    zip_code = form_name.number_input(
        "Zip Code:", value=12345, min_value=1000, help="Enter client zipcode"
    )
    return address, state, city, zip_code


def personal_request_form() -> None:
    api_endpoint = st.sidebar.selectbox(
        options=[
            "---",
            *personal_apis,
            *property_apis,
            *business_apis,
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

            if api_endpoint in personal_apis:
                first_name, middle_name, last_name, date_of_birth = person_input(
                    form_name=input_form
                )

                address, state, city, zip_code = address_input(form_name=input_form)
                custom_address = Address(address, city, state, zip_code)

                custom_person = Person(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    date_of_birth=date_of_birth,
                    address=custom_address,
                )
                body = custom_person

            elif api_endpoint in property_apis:
                address, state, city, zip_code = address_input(form_name=input_form)
                custom_address = Address(address, city, state, zip_code)
                body = custom_address

            elif api_endpoint in business_apis:
                business_names = input_form.text_input(
                    "Business Name (or names, separated by commas):"
                )
                address, state, city, zip_code = address_input(form_name=input_form)
                custom_address = Address(address, city, state, zip_code)
                business = Business(
                    names=[name.strip() for name in business_names.split(",")],
                    address=custom_address,
                )
                st.write(business)
                body = business

            submit_button = input_form.form_submit_button(label="Submit")

            endpoint_mapper = {
                "PFR": service_names.pfr,
                "Life Events": service_names.life_events,
                "Auto Insurance Prefill": service_names.auto_prefill,
                "Life Prefill": service_names.life_prefill,
                "Property Details": service_names.property_details,
                "Property Replacement Cost": service_names.property_replacement,
                "Property Risks": service_names.property_risks,
                "Small Business": service_names.smb,
            }
            if submit_button:
                live_response_page.app(
                    api=str(endpoint_mapper.get(api_endpoint)), body=body
                )
