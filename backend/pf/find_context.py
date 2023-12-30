from constants import INDEX_DIR

from promptflow import tool
from promptflow.connections import OpenAIConnection

from utils.index import FAISSIndex
from utils.oai import OAIEmbedding, render_with_token_limit
from utils.hash import compute_hash

import faiss
import os
import re
import nltk
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('stopwords')

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


@tool
def find_context(connection: OpenAIConnection, index_dir: str, case_summary: str, case_text: str) -> str:
    if not index_dir:
        return dict()
    context_dict = dict()
    os.environ["OPENAI_API_KEY"] = connection.api_key

    bullet_points = extract_bullet_points(case_summary)
    for bp in bullet_points:
        index = FAISSIndex(index=faiss.IndexFlatL2(
            1536), embedding=OAIEmbedding())
        index.load(path=index_dir)
        snippets = index.query(bp, top_k=5)

        word_match_thrshold = 1

        # score is the distance between vector so the smaller the better
        best_sentenece = find_sentence_with_most_relevant_words(
            bp, '\n'.join([s.text for s in snippets if s.score < 0.35]), threshold=0)

        if not best_sentenece:
            find_sentence_with_most_relevant_words(
                bp, case_text, threshold=word_match_thrshold)

        if best_sentenece:
            context_dict[bp] = best_sentenece

    return context_dict


def extract_bullet_points(case_summary) -> list[str]:
    case_summary = case_summary[:case_summary.find('**Keywords**')]
    pattern = re.compile(r'^\s*(-\s*.*)$', re.MULTILINE)
    matches = pattern.findall(case_summary)
    return matches


def find_sentence_with_most_relevant_words(bullet_point, paragraph, threshold):
    # Function to tokenize and filter words in a sentence
    stop_words = set(stopwords.words('english'))

    def tokenize_and_filter(sentence):
        return [word.lower() for word in nltk.word_tokenize(sentence) if word.lower() not in stop_words and len(word) > 1]

    bp_words = tokenize_and_filter(bullet_point)

    # Tokenize the paragraph into sentences
    sentences = nltk.sent_tokenize(paragraph)

    # Count relevant words in each sentence
    sentence_word_counts = {}
    for sentence in sentences:
        filtered_words = tokenize_and_filter(sentence)
        count = sum(1 for word in filtered_words if word in bp_words)
        if count > threshold:
            sentence_word_counts[sentence] = count
    # print(bullet_point, sentence_word_counts)

    # Find the sentence with the maximum count only if the count is greater than or equal to 2
    max_sentence = max(sentence_word_counts, key=sentence_word_counts.get) if len(
        sentence_word_counts) else None

    return max_sentence
