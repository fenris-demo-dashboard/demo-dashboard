"""Match input to df row funcs."""
import pandas as pd


def match_person_to_row(name: str, sample_personas_df: pd.DataFrame) -> pd.Series:
    """Return a series (dataframe row) with address and demographic info."""
    first_name, last_name = name.split(" ")[0], name.split(" ")[1]
    name_match_condition = (
        sample_personas_df["person.firstName"].str.strip() == first_name
    ) & (sample_personas_df["person.lastName"].str.strip() == last_name)
    persona_row_match = sample_personas_df.loc[name_match_condition].iloc[0]
    return persona_row_match


def match_property_to_row(address: str, sample_address_df: pd.DataFrame) -> pd.Series:
    """Return a series (dataframe row) with address info."""
    address_line1 = address.split(",")[0].strip()
    address_match_condition = (
        sample_address_df["address.addressLine1"].str.strip() == address_line1
    )
    address_row_match = sample_address_df.loc[address_match_condition].iloc[0]
    return address_row_match


def match_business_to_row(business: str, sample_business_df: pd.DataFrame) -> pd.Series:
    """Return a series (dataframe row) with business info."""
    business_name = business.strip()
    business_match_condition = [
        business_name in b for b in sample_business_df["names"].apply(eval)
    ]
    business_row_match = sample_business_df.loc[business_match_condition].iloc[0]
    return business_row_match
