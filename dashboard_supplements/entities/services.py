from types import SimpleNamespace

import pandas as pd

from dashboard_supplements.demo_text.demo_dashboard_text import (
    business_label_mapper,
    persona_names_label_mapper,
    property_label_mapper,
    sample_business_names,
    sample_persona_names,
    sample_property_names,
)
from dashboard_supplements.io.input_to_row_matchers import (
    match_business_to_row,
    match_person_to_row,
    match_property_to_row,
)
from dashboard_supplements.io.request_handlers.fake_request_data import (
    FAKE_ADDRESS_DF,
    FAKE_BUSINESS_DF,
    FAKE_PEOPLE_DF,
)
from dashboard_supplements.io.request_handlers.mock_requests import (
    mock_business_query,
    mock_personal_query,
    mock_property_query
)
from dashboard_supplements.io.deserializers.address import load_address_from_string
from dashboard_supplements.io.deserializers.business import load_business_from_name
from dashboard_supplements.io.deserializers.person import load_person_from_name

class ServiceCategory:
    def __init__(
        self,
        sample_information: list,
        select_prompt_specification: str,
        image_path: str,
        display_label_mapper: dict,
        select_row_from_user_query_func: callable,
        mock_query_func: callable,
        sample_information_df: pd.DataFrame,
        deserialization_process_func: callable,
    ) -> None:
        self.sample_information = sample_information
        self.prompt = select_prompt_specification
        self.image_path = image_path
        self.display_label_mapper = display_label_mapper
        self.select_row_from_user_query_func = select_row_from_user_query_func
        self.sample_information_df = sample_information_df
        self.deserialization_process_func = deserialization_process_func
        self.mock_query_func = mock_query_func


personal_service_category = ServiceCategory(
    sample_information=sample_persona_names,
    select_prompt_specification="policy holder",
    image_path="demo_persona_photos",
    display_label_mapper=persona_names_label_mapper,
    select_row_from_user_query_func=match_person_to_row,
    mock_query_func=mock_personal_query,
    sample_information_df=FAKE_PEOPLE_DF,
    deserialization_process_func=load_person_from_name,
)

property_service_category = ServiceCategory(
    sample_information=sample_property_names,
    select_prompt_specification="property",
    image_path="demo_property_photos",
    display_label_mapper=property_label_mapper,
    select_row_from_user_query_func=match_property_to_row,
    mock_query_func=mock_property_query,
    sample_information_df=FAKE_ADDRESS_DF,
    deserialization_process_func=load_address_from_string
)

business_service_category = ServiceCategory(
    sample_information=sample_business_names,
    select_prompt_specification="business",
    image_path="demo_business_photos",
    display_label_mapper=business_label_mapper,
    select_row_from_user_query_func=match_business_to_row,
    mock_query_func=mock_business_query,
    sample_information_df=FAKE_BUSINESS_DF,
    deserialization_process_func=load_business_from_name,
)

service_names = SimpleNamespace(
    pfr="PFR",
    life_events="LifeEvents",
    property_details="PropertyDetails",
    property_risks="PropertyRisks",
    auto_prefill="AutoPrefill",
    life_prefill="LifePrefill",
    property_replacement="PropertyReplacement",
    smb="SMB",
)

service_category_mapper = {
    service_names.pfr: personal_service_category,
    service_names.life_events: personal_service_category,
    service_names.life_prefill: personal_service_category,
    service_names.auto_prefill: personal_service_category,
    service_names.smb: business_service_category,
    service_names.property_details: property_service_category,
    service_names.property_risks: property_service_category,
    service_names.property_replacement: property_service_category,
}
