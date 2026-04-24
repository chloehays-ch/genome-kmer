from collections import defaultdict


def extract_kmers(sequence, k):
    """
    Return k-mers and the next character after each k-mer.
    """
    result = []

    for i in range(len(sequence) - k):
        kmer = sequence[i:i + k]
        next_char = sequence[i + k]
        result.append((kmer, next_char))

    return result


def count_kmers(sequences, k):
    """
    Count k-mer frequencies and next-character frequencies.
    """
    counts = defaultdict(lambda: {"total": 0, "next": defaultdict(int)})

    for seq in sequences:
        seq = seq.strip().upper()

        if len(seq) <= k:
            continue

        for kmer, next_char in extract_kmers(seq, k):
            counts[kmer]["total"] += 1
            counts[kmer]["next"][next_char] += 1

    return dict(counts)
