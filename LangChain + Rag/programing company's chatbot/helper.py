from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS #pip install faiss-cpu
import pickle
from langchain.chains import LLMChain, SimpleSequentialChain,RetrievalQAWithSourcesChain,RetrievalQA
from langchain_community.document_loaders import CSVLoader
import os
from langchain.prompts import PromptTemplate


load_dotenv()
# Fix the typo in your ChatGoogleGenerativeAI initialization:
llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-pro',
    temperature=0.7
)


embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def create_vecctor_db():
    file_path = "vector_index2.pkl"
    loader = CSVLoader(file_path='codebasics_faqs.csv', source_column='prompt')
    data = loader.load()
    vectorindex = FAISS.from_documents(embedding=embeddings, documents=data)
    vectorindex.save_local(file_path)

def get_qa_chain(query):
    file_path = "vector_index2.pkl"
    vectordb = FAISS.load_local(
        file_path,
        embeddings,
        allow_dangerous_deserialization=True  # Explicitly enable
    )
    retriever = vectordb.as_retriever()
    template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    chain=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
    )
    return chain({"query": query})

