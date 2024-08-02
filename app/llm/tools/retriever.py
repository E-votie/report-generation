from langchain_community.vectorstores import FAISS
from llm.embeddings import get_embedding
from langchain.tools.retriever import create_retriever_tool

embedding = get_embedding()
vector = FAISS.load_local("../bot_data/faiss_index", embedding, allow_dangerous_deserialization=True)
retriever = vector.as_retriever(search_kwargs={'k': 4})

retriever_tool = create_retriever_tool(
    retriever,
    "election_search",
    "Search for information about election, election commission and QnA. For any questions about election, you must use this tool!",
)