from promptflow import tool
import os
import faiss
from pathlib import Path

from utils.lock import acquire_lock
from utils.index import FAISSIndex
from utils.logging import log
from utils.oai import OAIEmbedding
from utils.hash import compute_hash
from promptflow.connections import OpenAIConnection
from constants import INDEX_DIR

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


@tool
def create_faiss_index(connection: OpenAIConnection, case_text: str) -> str:
    try:
        os.environ["OPENAI_API_KEY"] = connection.api_key
        if not os.path.exists(INDEX_DIR):
            os.makedirs(INDEX_DIR)

        hash_result = compute_hash(case_text)

        index_persistent_path = Path(INDEX_DIR)/hash_result
        index_persistent_path = index_persistent_path.resolve().as_posix()
        lock_path = index_persistent_path + f"_{hash_result}.lock"
        log("Index path: " + os.path.abspath(index_persistent_path))

        with acquire_lock(lock_path):
            if os.path.exists(os.path.join(index_persistent_path, "index.faiss")):
                log("Index already exists, bypassing index creation")
                return index_persistent_path
            else:
                if not os.path.exists(index_persistent_path):
                    os.makedirs(index_persistent_path)

            log("Building index")

            segments = split_text(case_text, chunk_size=5)

            log(f"Number of segments: {len(segments)}")

            index = FAISSIndex(index=faiss.IndexFlatL2(1536),
                               embedding=OAIEmbedding())
            index.insert_batch(segments)

            index.save(index_persistent_path)

            log("Index built: " + index_persistent_path)
    except Exception as e:
        print(e)
        return None
    return index_persistent_path


def split_text(text, chunk_size):
    lines = text.split('\n')
    chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]
    return ['\n'.join(chunk) for chunk in chunks]
