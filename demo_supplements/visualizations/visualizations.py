from matplotlib import pyplot as plt, ticker as mtick

import pandas as pd

import seaborn as sns

import streamlit as st

finance_tier_indicator_distribution = {
    "Deep Subprime": 25,
    "Sub Prime": 7,
    "Near Prime": 8,
    "Prime": 13,
    "Super Prime": 47,
}

insurance_tier_indicator_distribution = {
    "Non-standard": 40,
    "Standard": 40,
    "Preferred": 20,
}

credit_level_distribution = {
    "Poor": 15,
    "Fair": 17,
    "Good": 21,
    "Very Good": 25,
    "Exceptional": 22,
}

indicator_distributions = {
    "financeTier": finance_tier_indicator_distribution,
    "insuranceTier": insurance_tier_indicator_distribution,
    "creditLevel": credit_level_distribution,
}

colors = {"fenris_green": "#8CC641", "fenris_teal": "#21ABAD"}


def generate_highlight_barplot(
    indicator_value: str,
    indicator_distribution: dict,
    expander: st.beta_expander,
    x_label: str,
    y_label: str = "Proportion of Population",
):
    sns.set_theme(font="sans serif", style="ticks", context="notebook")
    finance_df = pd.DataFrame.from_dict(
        indicator_distribution, orient="index", columns=["count"]
    ).transpose()
    fig, ax = plt.subplots(figsize=(10, 4))

    cmap = {}
    for i in indicator_distribution.keys():
        if i == indicator_value:
            cmap[i] = colors["fenris_green"]
        else:
            cmap[i] = colors["fenris_teal"]

    sns.barplot(data=finance_df, palette=cmap)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    sns.despine()
    expander.pyplot(fig)
