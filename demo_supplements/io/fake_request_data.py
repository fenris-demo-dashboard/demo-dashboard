from pathlib import Path

from heimdal.io.mappers.personal_input_maps import PersonAddressInputMap

import pandas as pd

import streamlit as st


# streamlit icon and page config setup
icon_link = "https://fenrisd.com/wp-content/uploads/2018/03/cropped-site-icon-32x32.png"
st.set_page_config(page_title="Fenris API Demo App", page_icon=icon_link, layout="wide")


@st.cache(show_spinner=False)
def fake_people_df() -> pd.DataFrame:
    """Load the dataframe with fake persona information."""
    sample_csv_path = Path("./demo_supplements/assets/postman_requests_data_file.csv")
    df = pd.read_csv(sample_csv_path)
    return df


@st.cache(show_spinner=False)
def fake_person_address_input_map() -> PersonAddressInputMap:
    """Establish a PfrInputMap for the fake people dataframe."""
    person_address_input_map = PersonAddressInputMap(
        first_name="person.firstName",
        middle_name="person.middleName",
        last_name="person.lastName",
        address_line1="address.addressLine1",
        city="address.city",
        state="address.state",
        zip_code="address.zipCode",
        date_of_birth="person.dateOfBirth",
    )
    return person_address_input_map


FAKE_PEOPLE_DF = fake_people_df()
FAKE_PERSON_ADDRESS_INPUT_MAP = fake_person_address_input_map()
