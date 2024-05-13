HOW GREEN?
=============
KHUTHON 2024 - 우수상 수상 🏆
-------------
<br>

## 🍀 프로젝트 개요
**해커톤 주제:** 
- 환경과 소프트웨어: 지속가능한 지구와 인간사회를 위한 ESG 관점의 고찰

**아이디어 제안:**
- **How Green? 당신이 사용하는 제품은 얼마나 Green 한가요?**
- 환경에 대한 관심이 증가함에 따라 **그린워싱(Greenwashing)** 방법이 교묘해져가는 사회에서 녹색 소비, 즉 친환경 소비를 지향하는 소비자를 위한 정보 전달 어플리케이션.

**개발 기간:**
- 2024.05.10 ~ 2024.05.11

<br>

## 💻 연계 프론트엔드 레포지토리
- "[https://github.com/cherrie-k/Khuthon_HowGreen](https://github.com/cherrie-k/Khuthon_HowGreen)"

<br>

## ❓ 문제 정의
사회에 만연한 **그린워싱**으로 인해 소비자들이 친환경 제품들에 대한 의구심 증가와 투명한 제품·기업 정보에 대한 수요 증가


> **그린워싱이란?**
> "Green" + White"washing"
> 친환경적이지 않음에도 친환경적인 제품인 것처럼 포장해 홍보하는 위장 환경주위.
<br>

**그린워싱의 발생 배경**
1. 그린 마케팅을 통해 매출과 이윤을 올리고자 함
2. ESG 경영의 중요성으로 인해 겉으로만 친환경인 척 포장함
3. 친환경 제품, 브랜드를 강조하지만 실제로 환경을 위한 노력은 하지 않음

**그린워싱의 문제와 실태**
- 경기도민의 67%는 제품을 선택할 때 기업의 친환경 활동 여부를 고려함 [[출처](https://www.yna.co.kr/view/AKR20230105041000061)]
- 인스타그램 계정을 운영하는 기업 중 그린워싱 게시물을 한 건이라도 업로드한 기업의 비율은 41%에 달함 [[출처](https://www.greenpeace.org/korea/press/27748/presslease-greenwashing-report-2023/)]

- **가치있는 소비를 지향하는 소비자들의 신뢰를 떨어뜨림**


**그린워싱의 예시**

친환경 마케팅 과정에서의 모호한 표현들: 
- **친환경성을 표현하는 키워드가 한 번 이상 포함**되어 있으나 **구체적인 근거가 명시되지 않은** 경우
  - ‘친환경성을 표현하는 키워드'의 예 : ‘친환경', ‘플라스틱제로', ‘천연', ‘식물성', ‘자연유래성분', ‘자연을 담은', ‘무독성', ‘무해' 등
  - ‘구체적인 근거’의 예 : 성분 및 원료 출처, 공정과정, 인증마크 등
  - 기타 : 자연물 이미지가 포함되어 환경친화적인 느낌을 연상시키지만 구체적인 근거가 명시되지 않은 경우 포함

<br>

## 🌳 문제 해결 (프로젝트 기능)
소비자들에게 제품과 관련된 투명한 친환경 정보를 제공함으로서 **녹색 소비**에 도움을 줌.


1️⃣   상품 검색
   - 상품, 기업 정보 입력
     
2️⃣   입력 정보를 토대로 기업 정보 크롤링
   - 공공기관, 이커머스, 온라인 뉴스에서 정보 수집
     
3️⃣   내부 알고리즘과 AI를 통한 기업 정보 분석

4️⃣   상품, 기업 정보 반환
   - 상품의 친환경 인증 여부, 기업의 ESG 경영 지표 반환
   - 기업 관련 기사를 요약하여 링크와 함께 제공
   - 상품 상세 페이지 내 정보를 요약하여 제공
     
5️⃣   상품 리스트 적재와 검색
   - 이미 검색된 상품들은 데이터베이스에 저장되어 앱에 기록되고, 언제든 다시 불러올 수 있음
     
6️⃣   쉽고 빠른 친환경 정보 제공을 통해 소비자의 녹색 소비 도움



<br>

## 🛠️ 프로젝트 아키텍쳐
<p align="center">
<img src="https://github.com/cherrie-k/Khuthon_HowGreen/assets/80851202/0eb99764-1b0f-4725-97e5-10e5dd477a1b" width=82%>
</p>

<br>

## 📸 프로젝트 화면
**🔹 메인 화면** - 상품 검색, 이전 검색 상품 조회
<br>
<p align="center">
<img src="https://github.com/gitwub5/FastAPI_Server/assets/132264450/d4359e20-06b0-4e1a-8792-debeb3e390ee" width="235px" height="543px"></img>
&nbsp;
<img src="https://github.com/gitwub5/FastAPI_Server/assets/132264450/ab74b02f-f647-4691-95db-818fd00b4b8c" width="235px" height="543px"></img>
</p>

**🔹 로딩 화면** - 데이터 처리 중 로딩 인디케이터와 esg 관련 정보 표시
<br>
<p align="center">
<img src="https://github.com/gitwub5/FastAPI_Server/assets/132264450/8d278dff-a85b-494e-9d41-f22a66d5b778" width="235px" height="543px"></img>
&nbsp;
<img src="https://github.com/gitwub5/FastAPI_Server/assets/132264450/0cada277-56b1-40ca-b0be-59d3beecb1e3" width="235px" height="543px"></img>
</p>

**🔹 결과 화면 1** - 상품 분석 결과에 따라 화면 표시
<br>
<p align="center">
<img src="https://github.com/gitwub5/FastAPI_Server/assets/132264450/7bba687a-6f43-4e6a-86af-fb57abd27055" width="235px" height="543px"></img>
&nbsp;
<img src="https://github.com/gitwub5/FastAPI_Server/assets/132264450/c5d0913e-9c09-44c9-b389-16c6eb8c6966" width="235px" height="543px"></img>
</p>

**🔹 결과 화면 2** - 분석한 제품의 정보와 관련 기사 제시
<br>
<p align="center">
<img src="https://github.com/gitwub5/FastAPI_Server/assets/132264450/fdd487ec-3a16-414b-b2a8-0e242ccd11f8" width="235px" height="543px"></img>
&nbsp;
<img src="https://github.com/gitwub5/FastAPI_Server/assets/132264450/f946cefd-e498-4852-9714-8e7a44c4c55e" width="235px" height="543px"></img>
</p>

</br>


## FastAPI Server
> 1. /app: 애플리케이션의 주요 코드를 포함합니다.
> 2. /api: API 엔드포인트를 정의합니다. /router 폴더를 사용할 수 있습니다.
> 3. /core: 애플리케이션 설정과 같은 핵심 구성요소를 포함합니다.
>> models: dto를 설정 및 관리합니다.   
>> schemas: Pydantic을 사용하여 요청과 응답 스키마를 정의합니다.   
>> database: SQlite Database를 설정합니다.   
> 4. /service: 서비스와 AI 관련 코드를 포함합니다. 모델 로드, 로직 실행 등의 기능을 정의합니다.
> 5. main.py: FastAPI 애플리케이션을 생성하고 구성하는 메인 파일입니다.
> 6. /tests: 단위 테스트 및 통합 테스트를 위한 폴더입니다.
> 7. requirements.txt: 프로젝트 의존성을 명시합니다.
> 8. .env: 환경 변수를 저장합니다.


## 🫂 프로젝트 참여
<p align="center">
  
|<img src="https://avatars.githubusercontent.com/u/80851202?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/132264450?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/52268188?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/52253037?v=4" width="150" height="150"/>|
|:-:|:-:|:-:|:-:|
|Cherrie Kim [FE]<br/>[@cherrie-k](https://github.com/cherrie-k)|GeonWoo Shin [BE, AI]<br/>[@gitwub5](https://github.com/gitwub5)|Sunwu Park [BE, AI]<br/>[@sunwupark](https://github.com/sunwupark)|Seungheon Han [BE]<br/>[@seungheon123](https://github.com/seungheon123)|

</p>
