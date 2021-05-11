from dataclasses import dataclass


@dataclass
class Descriptor:

    explanation: str = ""
    caption: str = ""


pfr_field_info = {
    "trend": Descriptor(
        explanation="Returns an indicator of whether the data returned is trending"
        " upward or downward, based on historical entries",
        caption="**Note**: You may see the trend returned as 'Not Enough Data'",
    ),
    "score": Descriptor(
        explanation="Returns a prediction of the individual's overall financial status"
    ),
    "creditLevel": Descriptor(
        explanation="Returns a prediction of the individual's overall financial status",
        caption="""
            * __Poor__: Approximately 300-579
            * __Fair__: Approximately 580-669
            * __Good__: Approximately 670-739
            * __Very Good__: Approximately 740-799
            * __Exceptional__: Above 800
        """,
    ),
    "insuranceTier": Descriptor(
        explanation="Returns a prediction of the individual's "
        "overall insurance risk rating",
    ),
    "financeTier": Descriptor(
        explanation="""Returns an indicator for financial product fit to the
    individual based on their financial fitness.""",
    ),
    "decile": Descriptor(
        explanation="""Provides a score (1-10) indicating the individual's
        financial score as compared to the general population."""
    ),
}
