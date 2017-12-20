from natto import MeCab
import collections

_morpheme_type = ['NNG', 'NNP']
_escape_pattern = ['\n']
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
    return corpus


def get_word_frequency(corpus):
    _words = []
    for words in corpus:
        _words.extend(words)
    return sorted(collections.Counter(_words).items(), key=lambda data: data[1], reverse=True)


def display_list(data_list):
	for data in data_list:
		print(data)


if __name__ == '__main__':
	corpus = generate_corpus('./sample.txt')
	word_frequency = get_word_frequency(corpus)
	print('- corpus info (noun) - ')
	display_list(corpus)
	print('- word frequency best 10 - ')
	display_list(word_frequency[:10])
