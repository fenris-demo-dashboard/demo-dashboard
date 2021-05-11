import pandas as pd

import streamlit as st


@st.cache(show_spinner=False)
def load_fake_response_df(path) -> pd.DataFrame:
    """Load sample response dataframe for the given path"""
    df = pd.read_csv(path, index_col="Unnamed: 0")
    return df


FAKE_PFR_RESPONSE_DF = load_fake_response_df(
    path="./demo_supplements/assets/sample_results/sample_pfr_results.csv"
)
FAKE_LIFE_EVENT_RESPONSE_DF = load_fake_response_df(
    path="./demo_supplements/assets/sample_results/sample_life_events_results.csv"
)
FAKE_AUTO_PREFILL_RESPONSE_DF = load_fake_response_df(
    path="./demo_supplements/assets/sample_results/sample_auto_prefill_results.csv"
)

api_to_fake_response_df_mapper = {
    "PFR": FAKE_PFR_RESPONSE_DF,
    "LifeEvents": FAKE_LIFE_EVENT_RESPONSE_DF,
    "AutoPrefill": FAKE_AUTO_PREFILL_RESPONSE_DF,
}
