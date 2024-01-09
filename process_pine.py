import os
from dotenv import load_dotenv
import pinecone
from langchain_community.vectorstores.pinecone import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms.openai import OpenAI
from langchain.chains.question_answering import load_qa_chain

# 환경 변수 로드
load_dotenv()

# Pinecone 및 OpenAI 초기화
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
PINECONE_INSTANCE_NAME = os.environ.get('PINECONE_INSTANCE_NAME')
PINECONE_NAMESPACE = os.environ.get('PINECONE_NAMESPACE')

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_API_ENV
)

# OpenAI Embeddings 초기화
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
index_name = PINECONE_INSTANCE_NAME
namespace = PINECONE_NAMESPACE

# 이메일 조각화 및 Pinecone DB에 임베딩
def chunk_and_embed(emails):
    for email in emails:
        # 이메일을 조각화
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        email_chunks = text_splitter.split_text(email["Body"])
        for i in range(len(email_chunks)):
            email_chunks[i] += f" From: {email['From']} Date: {email['Date']} Subject: {email['Subject']}"

        # Pinecone DB에 임베딩
        for chunk in email_chunks:
            print("Chunk", chunk)
        Pinecone.from_texts(email_chunks, embeddings, index_name=index_name, namespace=namespace)

llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")

def semantic_search(query):
    llm_query = f"{query} You are given a list of emails and a query that appears before this sentence. Please return the subject and date for the email that best matches this query and provide additional information about this email if the query asks for additional information.Also, please output the returned content in Markdown format."
    doc_search = Pinecone.from_existing_index(index_name, embeddings, namespace=namespace)
    # 의미론적 검색
    docs = doc_search.similarity_search(query)
    # 첫 번째 문서 출력
    print(docs[0].page_content)
    # llm 보조 응답 수집
    response = chain.run(input_documents=docs, question=llm_query)
    return response
