from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from app.config import get_settings
import os
import shutil
import tiktoken
import json
from urllib.parse import urlparse

settings = get_settings()

embeddings = OpenAIEmbeddings(
    openai_api_key = settings.openai_api_key
)

tokenizer = tiktoken.get_encoding('cl100k_base')


# create the length function
def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)


def load_directory():
    loader = DirectoryLoader('bot_data/data', glob="**/*.txt", loader_cls=lambda file_path: TextLoader(file_path, encoding='utf-8'))
    pages = loader.load()
    print(f"loaded {len(pages)} pages.")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=30, length_function=tiktoken_len)
    docs = text_splitter.split_documents(pages)
    print(f"loaded {len(docs)} docs.")
    db = FAISS.from_documents(docs, embeddings)
    if os.path.exists("bot_data/faiss_index"):
        shutil.rmtree("bot_data/faiss_index")
        print("Deleted existing vector store")
    db.save_local("bot_data/faiss_index")
    print("Saved vector store")

def download_links(urls):
    loader = WebBaseLoader(urls,
    header_template={
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    })
    pages = loader.load()
    for page in pages:
        parsed_url = urlparse(page.metadata['source'])
        resource = parsed_url.path.split("/")[-1]
        file_name = resource.replace(".html", ".txt")
        with open(f"bot_data/data/{file_name}", "w", encoding='utf-8') as file:
            file.write(page.page_content)

if __name__== '__main__':
    # Open the JSON file
    with open('bot_data/links.json', 'r') as file:
        data = json.load(file)

    # Read the array into the links variable
    links = data['links']

    #download_links(links)
    load_directory()

    # Print the links to verify
    #load_web(links)