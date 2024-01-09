import streamlit as st
import process_gmail as gmail
from dotenv import load_dotenv
import process_pine

def main():
    # 환경 변수 로드
    load_dotenv()

    # Streamlit 페이지 제목
    st.title("Google 이메일 도우미")

    # 이메일 인증 및 추출
    if st.button("인증 및 추출"):
        credentials = gmail.authenticate()
        emails = gmail.extract_emails(credentials)
        with st.spinner("이메일을 임베딩하는 중입니다..."):
            process_pine.chunk_and_embed(emails)
            # 임베딩 완료 후 성공 메시지 표시
            st.success("모든 이메일의 임베딩이 완료되었습니다.")

    # 응답 변수 초기화
    response = "awaiting response"

    # 쿼리 입력을 위한 검색 바
    search_query = st.text_input("질문을 입력하세요:")
    st.write("검색어:", search_query)

    # 검색 결과 처리 및 표시
    if search_query:
        response = process_pine.semantic_search(search_query)
        with st.expander(f'쿼리: {search_query}', expanded=True):
            # 마크다운 형식의 텍스트를 올바르게 렌더링
            st.markdown(response, unsafe_allow_html=True)

# 스크립트의 시작점
if __name__ == '__main__':
    main()
