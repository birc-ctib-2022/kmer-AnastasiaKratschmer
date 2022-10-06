# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from kmer import(kmer, unique_kmers,count_kmers)

def test_kmer():
    assert kmer('agtagtcg', 3)==['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

def test_unique_kmers():
    assert unique_kmers('abcd', 2)==['ab', 'bc', 'cd']

def test_count_kmers():
    count_kmers('abcd', 4)=={'abcd': 1}
