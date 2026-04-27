from collections import defaultdict


def extract_kmers(sequence, k):
    """
    Generate all k-mers from a sequence along with their following character.

    A k-mer is a substring of length `k`. For each k-mer in the input sequence,
    this function pairs it with the character that immediately follows it.

    Parameters:
        sequence (str): Input sequence (e.g., DNA, RNA, or text).
        k (int): Length of each k-mer.

    Returns:
        list[tuple[str, str]]: A list of (kmer, next_char) tuples.

    Example:
        extract_kmers("ATCG", 2) -> [("AT", "C"), ("TC", "G")]
    """
    result = []

    # Stop at len(sequence) - k to avoid going out of bounds
    for i in range(len(sequence) - k):
        # Extract substring of length k
        kmer = sequence[i:i + k]

        # Character immediately following the k-mer
        next_char = sequence[i + k]

        result.append((kmer, next_char))

    return result


def count_kmers(sequences, k):
    """
    Count occurrences of k-mers and the distribution of following characters.

    For each sequence, this function:
    - Normalizes it (strips whitespace and converts to uppercase)
    - Extracts k-mers and their next characters
    - Tracks:
        1. Total occurrences of each k-mer
        2. Frequency of each possible next character after that k-mer

    Parameters:
        sequences (iterable[str]): Collection of input sequences.
        k (int): Length of k-mers.

    Returns:
        dict: A dictionary of the form:
            {
                kmer: {
                    "total": int,
                    "next": {
                        char: int,
                        ...
                    }
                },
                ...
            }

    Example:
        count_kmers(["ATCG"], 2) ->
        {
            "AT": {"total": 1, "next": {"C": 1}},
            "TC": {"total": 1, "next": {"G": 1}}
        }
    """
    # Each k-mer maps to:
    #   - total count
    #   - dictionary of next-character counts
    counts = defaultdict(lambda: {"total": 0, "next": defaultdict(int)})

    for seq in sequences:
        # Normalize sequence (important for consistency)
        seq = seq.strip().upper()

        # Skip sequences too short to form any k-mer + next character
        if len(seq) <= k:
            continue

        # Update counts using extracted k-mers
        for kmer, next_char in extract_kmers(seq, k):
            counts[kmer]["total"] += 1
            counts[kmer]["next"][next_char] += 1

    # Convert defaultdict to regular dict for cleaner output / serialization
    return dict(counts)
