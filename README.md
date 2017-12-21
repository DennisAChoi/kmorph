# KMORPH(한국어 형태소 분석기 개발) #

### 프로젝트 목적 ###
* 본 프로젝트는 mecab 과 mecab_ko_dic 을 베이스로 한국어 텍스트 문서 분석 및 기계학습에 용이한 품사분석기를 개발 제공하고자 합니다.

### 라이센스 정보 
* [Apache 2.0 라이센스](https://olis.or.kr/license/Detailselect.do?lId=1002)를 준수합니다.

### 셋업 가이드(ubuntu 기준) ###
* Python 3.5 이상 설치( [miniconda](https://conda.io/miniconda.html) 추천 )
* gcc 7.20 설치( sudo apt install gcc )
* automake1.11 설치( sudo apt install automake1.11 )
* natto-py 설치( pip install natto-py )
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
* mecab에서 정상적으로 한글 사전을 읽어드리는지 테스트
>
``` aaa 
```
* [은전한닢(mecab_ko) 품사표](https://docs.google.com/spreadsheets/d/1-9blXKjtjeKZqsf4NzHeYJCrr49-nXeRF6D80udfcwY/edit#gid=589544265)

