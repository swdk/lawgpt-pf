from promptflow import tool
import os
import faiss
from pathlib import Path

from utils.lock import acquire_lock
from utils.index import FAISSIndex
from utils.logging import log
from utils.oai import OAIEmbedding
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

        # chunk_size = int(os.environ.get("CHUNK_SIZE", 1024))
        # chunk_overlap = int(os.environ.get("CHUNK_OVERLAP", 64))
        # log(f"Chunk size: {chunk_size}, chunk overlap: {chunk_overlap}")

        index_persistent_path = Path(INDEX_DIR).resolve().as_posix()
        lock_path = index_persistent_path + ".lock"
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
        return False
    return True


# Split the text into chunks with CHUNK_SIZE and CHUNK_OVERLAP as character count
def split_text(text, chunk_size):
    # # Calculate the number of chunks
    # num_chunks = (len(text) - chunk_overlap) // (chunk_size - chunk_overlap)

    # # Split the text into chunks
    # chunks = []
    # for i in range(num_chunks):
    #     start = i * (chunk_size - chunk_overlap)
    #     end = start + chunk_size
    #     chunks.append(text[start:end])

    # # Add the last chunk
    # chunks.append(text[num_chunks * (chunk_size - chunk_overlap):])
    # return chunks

    lines = text.split('\n')
    chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]
    return ['\n'.join(chunk) for chunk in chunks]
