from promptflow import tool
import re

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def find_references(input1: str) -> str:
    _, reference_text = re.split(r'\n\s*\n(?=\[\d{1,3}\])', input1, maxsplit=1)
    reference_dict = {}
    references = re.findall(r'\[(\d+)\]\s*(.*?)\n(?=\[\d{1,3}\]|\Z)', reference_text, re.DOTALL)
    for reference in references:
        ref_number = int(reference[0].strip())
        ref_text = reference[1].strip().replace('\n', '').removesuffix('.')
        
        # Replace ibid with source from previous number
        if 'ibid' in ref_text.lower():
            prev_ref_text =  reference_dict[ref_number-1]
            # Using regular expression to remove non-alphabetic characters at the end
            prev_ref_text = re.sub(r'[^a-zA-Z]*$', '', prev_ref_text)
            ref_text = re.sub('ibid', prev_ref_text, ref_text, flags=re.IGNORECASE)
            #[7] CA judgment, [62]
            #[8] Ibid, [84]
            # ->
            # [7] CA judgment, [62]
            # [8] CA judgment, [84]

        reference_dict[ref_number] = ref_text

    return reference_dict
