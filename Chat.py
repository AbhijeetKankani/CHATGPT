import os
import sys

import constants
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.indexes import VectorstoreIndexCreator

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = sys.argv[1]

# loader = TextLoader('data.txt')
loader = DirectoryLoader("data/")
# loader = DirectoryLoader("data/", glob="*.txt")
# loader = DirectoryLoader("data/", glob="*.txt|*.pdf")

index = VectorstoreIndexCreator().from_loaders([loader])


print(index.query(query, llm=ChatOpenAI()))
