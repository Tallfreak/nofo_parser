# Ruff line length limit should be disabled for this file.
# ruff: noqa: E501

# what kind of information do we want? what the grant can be used for and who's eligible?

prompt = r"""
    # Directive:
    For the attached file, provide a 2-3 sentence summary of the purpose and scope of this grant. Do NOT guess or make up an answer. In the RARE case the information is not present, return 'Information is not available'.

    # Audience:
    You are talking to a grant writer at an organization who wants information on this grant.

    # Output Formatting:
    Structure the output as a json object with a summary field containing text.
"""
