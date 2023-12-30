from promptflow import tool
import re
import nltk
# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


# import nltk
# nltk.download('punkt')

# def find_sentences_with_word(text, word):
#     sentences = nltk.sent_tokenize(text)
#     result_sentences = [sentence for sentence in sentences if word in nltk.word_tokenize(sentence)]
#     return result_sentences


@tool
def find_references(main_text: str, reference_text: str) -> str:
    # Replace text like [12]-[14] with [12], [13], [14]
    main_text = re.sub(r'\[(\d{1,3})\]-\[(\d{1,3})\]', lambda match: ', '.join(
        [f'[{i}]' for i in range(int(match.group(1)), int(match.group(2)) + 1)]), main_text)
    footnotes_data = []

    if reference_text:
        reference_dict = {}
        references = re.findall(
            r'\[(\d+)\]\s*(.*?)\n(?=\[\d{1,3}\]|\Z)', reference_text, re.DOTALL)
        for reference in references:
            ref_number = reference[0].strip()
            ref_text = reference[1].strip().replace('\n', '').removesuffix('.')

            # Replace ibid with source from previous number
            if 'ibid' in ref_text.lower():
                prev_ref_text = reference_dict[str(int(ref_number)-1)]
                # Using regular expression to remove non-alphabetic characters at the end
                prev_ref_text = re.sub(r'[^a-zA-Z]*$', '', prev_ref_text)
                ref_text = re.sub('ibid', prev_ref_text,
                                  ref_text, flags=re.IGNORECASE)
                # [7] CA judgment, [62]
                # [8] Ibid, [84]
                # ->
                # [7] CA judgment, [62]
                # [8] CA judgment, [84]
            reference_dict[ref_number] = ref_text

        # Extract sentences containing footnotes and their respective footnotes
        main_sentences = nltk.sent_tokenize(main_text)

        for sentence in main_sentences:
            footnotes = re.findall(r'\[(\d{1,3})\]', sentence)
            if footnotes:
                footnotes_data.append({
                    'sentence': sentence,
                    'footnotes_texts': ' ,'.join(set(reference_dict[f] for f in footnotes if f in reference_dict))
                })

    # Replace references in the main text
    # main_text = re.sub(
    #     r'\[(\d{1,3})\]', lambda match: f' ** {reference_dict.get(match.group(1), "")} **', main_text)

    return {'main_text': main_text, 'footnotes_data': footnotes_data}
