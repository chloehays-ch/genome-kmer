from kmer_counter import extract_kmers, count_kmers


def test_extract_kmers_basic():
    assert extract_kmers("ATGT", 2) == [("AT", "G"), ("TG", "T")]


def test_extract_kmers_short():
    assert extract_kmers("A", 2) == []


def test_count_kmers_single():
    result = count_kmers(["ATGT"], 2)

    assert result["AT"]["total"] == 1
    assert result["AT"]["next"]["G"] == 1


def test_count_kmers_multiple():
    result = count_kmers(["ATG", "ATG"], 2)

    assert result["AT"]["total"] == 2
    assert result["AT"]["next"]["G"] == 2


def test_multiple_next_chars():
    result = count_kmers(["ATGA", "ATGG"], 2)

    assert result["TG"]["total"] == 2
    assert result["TG"]["next"]["A"] == 1
    assert result["TG"]["next"]["G"] == 1


def test_empty_input():
    assert count_kmers([], 2) == {}


def test_k_equal_length():
    assert count_kmers(["AT"], 2) == {}
