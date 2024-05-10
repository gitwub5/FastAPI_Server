KHUTHON 2024
=============
서비스명: HOWGREEN
-------------
<img src="https://github.com/gitwub5/FastAPI_Server/assets/132264450/93828431-a71e-4758-9ba5-b6f4b47faa23" width="450px" height="300px"></img><br/>

![KakaoTalk_Photo_2024-05-11-05-06-34-2](https://github.com/gitwub5/FastAPI_Server/assets/132264450/93828431-a71e-4758-9ba5-b6f4b47faa23)
![KakaoTalk_Photo_2024-05-11-05-10-29](https://github.com/gitwub5/FastAPI_Server/assets/132264450/69c032ea-43ec-4a6a-9efb-93523820608e)

### 서비스 설명: 그린워싱 방법이 교모해져가는 사회에서 녹색 소비, 즉 친환경 소비를 지향하는 소비자를 위한 정보 전달 어플리케이션
### 아키텍쳐: Flutter(Frontend) - FastAPI(Backend) - SQlite(Database)
Frontend: URL "[https://github.com/cherrie-k/khuthon](https://github.com/cherrie-k/khuthon)"    
Backend: URL "[https://github.com/cherrie-k/khuthon](https://github.com/gitwub5/FastAPI_Server)"
### 문제정의: 그린워싱으로 인해 소비자들이 친환경 제품에 대한 의구심 증가 
### 친환경 마케팅 과정에서의 모호한 표현들: 
**친환경성을 표현하는 키워드가 한 번 이상 포함**되어 있으나 **구체적인 근거가 명시되지 않은** 경우
  - ‘친환경성을 표현하는 키워드'의 예 : ‘친환경', ‘플라스틱제로', ‘천연', ‘식물성', ‘자연유래성분', ‘자연을 담은', ‘무독성', ‘무해' 등
  - ‘구체적인 근거’의 예 : 성분 및 원료 출처, 공정과정, 인증마크 등
  - 기타 : 자연물 이미지가 포함되어 환경친화적인 느낌을 연상시키지만 구체적인 근거가 명시되지 않은 경우 포함

* * *
## FastAPI Server
> 1. /app: 애플리케이션의 주요 코드를 포함합니다.
> 2. /api: API 엔드포인트를 정의합니다. /router 폴더를 사용할 수 있습니다.
> 3. /core: 애플리케이션 설정과 같은 핵심 구성요소를 포함합니다.
>>models: dto를 설정 및 관리합니다.
>>schemas: Pydantic을 사용하여 요청과 응답 스키마를 정의합니다.
>>database: SQlite Database를 설정합니다.
> 4. /service: 서비스와 AI 관련 코드를 포함합니다. 모델 로드, 로직 실행 등의 기능을 정의합니다.
> 5. main.py: FastAPI 애플리케이션을 생성하고 구성하는 메인 파일입니다.
> 6. /tests: 단위 테스트 및 통합 테스트를 위한 폴더입니다.
> 7. requirements.txt: 프로젝트 의존성을 명시합니다.
> 8. .env: 환경 변수를 저장합니다.
