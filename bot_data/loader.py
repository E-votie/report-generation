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


def load_web(urls):
    loader = WebBaseLoader(urls,
    header_template={
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    })
    pages = loader.load()
    print(f"loaded {len(pages)} pages.")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=30, length_function=tiktoken_len)
    docs = text_splitter.split_documents(pages)
    print(f"loaded {len(docs)} docs.")
    db = FAISS.from_documents(docs, embeddings)
    if os.path.exists("bot_data/faiss_index"):
        shutil.rmtree("bot_data/faiss_index")
        print("Deleted existing vector store")
    db.save_local("bot_data/faiss_index")
    print("Saved vector store")

if __name__== '__main__':
    # Open the JSON file
    with open('bot_data/links.json', 'r') as file:
        data = json.load(file)

    # Read the array into the links variable
    links = data['links']

    # Print the links to verify
    #load_web(links)