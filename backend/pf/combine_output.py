from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(case_summary: str, case_reference: dict, llm_reference: str) -> str:
    # Enrich each line in the case summary if it is in the case reference
    enriched_summary = enrich_summary_lines(case_summary, case_reference)

    # Combine the enriched summary with the LL.M. reference
    result = f"{enriched_summary}\n\n{llm_reference}"

    return result


def enrich_summary_lines(summary, reference):
    # Replace each line in the summary with the reference value if it exists
    print(summary.split('\n'))
    return '\n'.join(enrich_line(line, reference) for line in summary.split('\n'))


def enrich_line(line, ref_dict):
    # If the line is in the reference dictionary, append the reference to the end of the line
    return f"{line} | *{ref_dict[line]}*" if line in ref_dict else line
