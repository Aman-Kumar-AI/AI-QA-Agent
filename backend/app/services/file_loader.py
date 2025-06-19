# OLD:
# from llama_index import SimpleDirectoryReader

# NEW:
from llama_index.core import SimpleDirectoryReader


def load_documents(upload_dir: str):
    reader = SimpleDirectoryReader(input_dir=upload_dir)
    return reader.load_data()