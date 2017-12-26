# KMORPH(한국어 형태소 분석기 개발) #

### 프로젝트 개요
* 목적 
    * 본 프로젝트는 mecab 과 mecab_ko_dic 을 base 로 한국어 텍스트 문서 분석 및 기계학습에 용이한 기능을 제공하는 품사분석기를 개발제공
* 기능 명세
    * 데이터 분석 / 기계학습의 형태소분석기 필요한 기능 지원
    * 주요 오픈소스 데이터 솔루션( Tensorflow / Pandas / Elasticstack / Apache Spark ... )의 플러그인 제공


### 라이센스 정보 
* [Apache 2.0 라이센스](https://olis.or.kr/license/Detailselect.do?lId=1002)를 준수합니다.


### Mecab 분석
* 장점
    * mecab 성능 품질 측면에서 검증이 되어 있음( 카카오토픽, LG )
    * 안정적으로 한국어 사전이 갱신되고 있음
* 단점
    * 지정한 형태소를 뽑아내는 기능이 없음
    * 원형(활용형)을 반환기능이 없음
    * Panda 포맷의 DataFrame 포맷으로 반환기능이 없음
    * 동의어 / 유의어 / 언어번역 형태로 제공하는 기능이 있음


### 셋업 가이드(ubuntu 기준)
* Python 3.5 이상 설치( [miniconda](https://conda.io/miniconda.html) 추천 )
* gcc 7.20 설치( sudo apt install gcc )
* automake1.11 설치( sudo apt install automake1.11 )
* natto-py 설치( pip install natto-py )
* skleran 설치( pip install sklearn )
* mecab-0.996 설치
    * cd mecab-0.006
    * $./configure
    * $ make
    * $ sudo make install
* mecab-ko-dic 설치
* 은전한닢 프로젝트에서 제공하는 [mecab_ko_dic](https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/) 을 다운로드
    * $ tar zxvf mecab-ko-dic-x.x.x-xxxxxxxx.tar.gz
    * $ cd mecab-ko-dic-x.x.x-xxxxxxxx
    * $ cd ./configure
    * $ make
    * $ sudo make install
* /usr/local/etc/mecabrc 을 편집하여 아래와 같이 수정
    * dicdir=/usr/local/lib/mecab/dic/mecab-ko-dic
* mecab 한글 분석 테스트
    * $ mecab
        ```
        한글이 제대로 분해가 되나?
        한글	NNG,*,T,한글,*,*,*,*
        이	JKS,*,F,이,*,*,*,*
        제대로	MAG,성분부사/양태부사,F,제대로,*,*,*,*
        분해	NNG,*,F,분해,*,*,*,*
        가	JKS,*,F,가,*,*,*,*
        되	VV,*,F,되,*,*,*,*
        나	EF,*,F,나,*,*,*,*
        ?	SF,*,*,*,*,*,*,*
        EOS
        ```
* Jupuyter Notebook(*.ipynb) 파일 실행방법
    * $ cd sample
    * $ jupyter notebook
    * 브라우저로 접속하여 테스트
* [은전한닢(mecab_ko) 품사표](https://docs.google.com/spreadsheets/d/1-9blXKjtjeKZqsf4NzHeYJCrr49-nXeRF6D80udfcwY/edit#gid=589544265)

