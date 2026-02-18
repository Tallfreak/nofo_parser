# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

prompt = r"""
    # Directive:
    For the attached file, return a list of up to 20 keywords and/or phrases that represent the grant's focus. Some examples of keywords and phrases include health, environment, housing, criminal record sealing, air pollution, food insecurity. Do NOT guess or make up an answer.

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with a keywords field containing an array of strings.
"""

no_nofo_prompt = """
    # Directive:
    For the description in the following input text, return a list of up to 20 keywords and/or phrases that represent the grant's focus. Some examples of keywords and phrases include health, environment, housing, criminal record sealing, air pollution, food insecurity. Do NOT guess or make up an answer.

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with a keywords field containing an array of strings.
"""
