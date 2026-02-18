# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

prompt = r"""
    # Directive:
    For the attached file, extract the full eligibility criteria and application requirements for applicants. Determine if any of the eligibility criteria or application requirements are unique to this grant or not common in other grants. Summarize this information and return the summary. Be very brief and summarize in one or two sentences. Most grants won't have more than one or two unique aspects. Do NOT guess or make up an answer. In the RARE case the information is not present, return 'Information is not available'.

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with a unique_aspects field containing text.
"""
