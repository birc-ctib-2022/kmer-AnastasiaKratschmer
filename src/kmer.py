"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']
    """
    kmers=[]
    for i in range(0, len(x)-k+1):
        kmerr=x[i:i+k]
        kmers.append(kmerr)
    return kmers



def unique_kmers(x: str, k: int) -> list[str]:
    """
    >>> unique_kmers('abcd', 2)
    ['ab', 'bc', 'cd']
    """
    kmers=[]
    for i in range(0, len(x)-k+1):
        kmerr=x[i:i+k]
        if kmerr not in kmers:
            kmers.append(kmerr)
    return kmers


def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    >>> count_kmers('abcd', 4)
    {'abcd': 1}
    """
    kmer_count={}
    kmers=[]
    for i in range(0, len(x)-k+1):
        kmerr=x[i:i+k]
        kmers.append(kmerr)
    for kmerr in kmers:
        if kmerr in kmer_count:
            kmer_count[kmerr]+=1
        else:
            kmer_count[kmerr]=1
    return kmer_count