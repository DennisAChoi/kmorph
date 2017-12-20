from natto import MeCab


# _morpheme_type = ['NNG', 'NNP', 'NNB']
_morpheme_type = ['NNG', 'NNP']
_escape_pattern = ['\n', '^ROW_END^\n']
_nm = MeCab()

def parse_sentence(text):
    global _nm
    global _morpheme_type

    words = []
    for term_info in str(_nm.parse(text)).split('\n'):
        _term_info = term_info.split('\t')
        if len(_term_info) < 2:
            continue
        surface = _term_info[0]
        analysis = _term_info[1].split(',')
        if analysis[0] in _morpheme_type:
            # print(surface, analysis[0])
            words.append(surface)
    return words


def generate_corpus(data_path):
    global _escape_pattern

    corpus = []
    fp = open(data_path, 'r')
    for line in fp.readlines():
        if line not in _escape_pattern:
            words = parse_sentence(line)
            corpus.append(words)
            # print(words)
    return corpus


corpus = generate_corpus('./sample.txt')
for word in corpus:
	print(word)
