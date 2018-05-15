# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/workspace/my_bigdata/kmorph/src/kma");
import kma_api as a

if __name__ == '__main__':
    
    ret=''

    me, df=a.run_ma("코스콤(Koscom)은 증권 및 파생상품 시장과 증권회사를 비롯한 금융업계의 각종 전산 인프라를 효율적으로 구축하고 운용하는 전산전문회사로 금융위원회의 관리감독을 받는 증권유관기관이다. 1977년 9월 한국증권전산(주)로 창립되어 2005년 5월 (주)코스콤으로 회사명을 변경하였다. 서울특별시 영등포구 여의나루로 76(여의도동 33)에 위치하고 있다.", "./stopword.txt", 2)
    print(" -- morpheme analzyer info --")
    print(me)
    print(" -- all info of morpheme analzyer  --")
    print(df)
    print(" -- all morphemes and POS --")
    ret=a.get_all_morph(df)
    print(ret)
    print(" -- noun morphemes and POS --")
    ret=a.get_noun_morph(df)
    print(ret)
    print(" -- noun morphemes and freq --")
    ret=a.get_noun_term_freq(df)
    print(ret)
