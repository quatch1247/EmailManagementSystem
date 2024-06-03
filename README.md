<img width="1076" alt="스크린샷 2024-01-09 오후 3 19 08" src="https://github.com/mathminds-sd/pinecone-gmail/assets/80108373/b7ac2053-2b02-4761-a051-6b67090e0a60">
<img width="1078" alt="스크린샷 2024-01-09 오후 3 20 08" src="https://github.com/mathminds-sd/pinecone-gmail/assets/80108373/ce0afe9f-bc07-4862-8cb2-7166adf6e8ad">
<img width="1031" alt="스크린샷 2024-01-09 오후 3 43 17" src="https://github.com/mathminds-sd/pinecone-gmail/assets/80108373/4d04a126-6634-4966-ba48-8b43953ef841">

# Streamlit과 Pinecone을 사용한 이메일 저장 및 추출 예제

이 프로젝트는 Streamlit과 Pinecone을 사용하여 Google 이메일을 인증, 추출, 임베딩하고, 이를 기반으로 의미론적 검색을 수행하는 간단한 예제입니다.

## 시작하기

### 1. 가상 환경 설정

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env` 파일을 편집하고 Google JSON 파일을 추가합니다.

### 3. 애플리케이션 실행

```bash
streamlit run main.py
```

- **main.py**: 메인 애플리케이션 파일로, Streamlit을 사용하여 이메일을 인증하고 추출하며, Pinecone에 임베딩하고 검색하는 기능을 포함하고 있습니다.
- **process_gmail.py**: Google 이메일을 인증하고 추출하는 기능을 포함하고 있습니다.
- **process_pine.py**: 추출한 이메일을 Pinecone에 임베딩하고, 의미론적 검색을 수행하는 기능을 포함하고 있습니다.
- **.env**: 환경 변수를 저장하는 파일로, Google API 인증에 필요한 정보를 포함하고 있습니다.
- **requirements.txt**: 프로젝트에 필요한 Python 패키지 목록을 포함하고 있습니다.

## 추가 정보

- **Streamlit**: Python을 사용한 데이터 애플리케이션을 빠르게 구축할 수 있는 오픈 소스 프레임워크입니다.
- **Pinecone**: 고성능 벡터 검색 인덱스 서비스를 제공하는 플랫폼으로, 대규모 데이터에서 의미론적 검색을 수행할 수 있습니다.
