# -*- coding: utf-8 -*-
# Copyright (C) 2018.02.09 kyung seok jeong <humanist96@koscom.co.kr>

from natto import MeCab
import pandas as pd
import collections
import re

def run_ma(text, nBest=1):
    """
    Return the dataframe of all Information of morpheme analyzer.
    - input : string, {nbest number}
    - output : dataframe
    """
    options=r'-F%m,%f[0],%f[1],%f[2],%f[3],%f[4],%f[5],%f[6],%f[7]\n'
    options+=" -N"+str(nBest)
    
    _me=MeCab(options)
    
    _df = pd.DataFrame(None, columns=['surface', 'tag', 'meaning_class', 'final_consonant', 
                                     'reading', 'type', 'first_tag', 'final_tag','expression'])

    i=0
    for term_str in str(_me.parse(text)).split('\n'):
        term_list = re.split(',', term_str)
        if len(term_list) < 2:
            continue
        _df.loc[i]=term_list   
        i+=1
    return _me, _df


def get_all_morph(df):
    """
    Returns all morphemes and Part-of-Speech.
    - input : dataframe
    - output : string
    """
    ret=''
    for index, row in df.iterrows():      
        if row['type'] == 'Inflect' or row['type'] == 'Compound':
            tag=row['expression']
            ret+=tag.replace('+',' ').replace("/*", '')+" "
        else:
            tag=row['tag']
            ret+=row['surface']+"/"+tag+" "        
    ret=ret.rstrip()
    ret=ret+"\n"
    
    return(ret)


def get_noun_morph(df, option='N'):
    """
    Returns noun morphemes and Part-of-Speech.
    - input : dataframe, {option : compound noun decomposition flag, default : N}
    - output : string
    """
    _noun_type = ['NNG', 'NNP']
    ret=''
    
    for index, row in df.iterrows():
        if row['tag'] in _noun_type:
            if row['type'] == 'Compound' and option != 'N':
                tag=row['expression']
                ret+=tag.replace('+',' ').replace("/*", '')+" "
            else:
                ret+=row['surface']+"/"+row['tag']+" " 
    ret=ret.rstrip()
    ret=ret+"\n"
    
    return(ret)

def get_noun_term_freq(df, option='N'):
    """
    Returns noun morphemes and freqeuncy
    - input : dataframe, {option : compound noun decomposition flag, default : N}
    - output : list of tuples(morpheme, frequency)
    """
    _noun_type = ['NNG', 'NNP']
    _terms = []
    
    for index, row in df.iterrows():
        if row['tag'] in _noun_type:
            if row['type'] == 'Compound' and option != 'N':
                tag=row['expression']
                _terms.extend(re.split(' ', tag.replace('+',' ').replace("/*", '')))
            else:
                _terms.append(row['surface'])
                
    return sorted(collections.Counter(_terms).items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
	ret=''
	me, df=run_ma("대한민국 형태소분석기는 한글 이 잘 쪼개질까?")
	print(" -- morpheme analzyer info --")
	print(me)
	print(" -- all info of morpheme analzyer  --")
	print(df)
	print(" -- all morphemes and POS --")
	ret=get_all_morph(df)
	print(ret)
	print(" -- noun morphemes and POS --")
	ret=get_noun_morph(df)
	print(ret)
	print(" -- noun morphemes and freq --")
	print(get_noun_term_freq(df))
