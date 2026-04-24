import pytest
from kmer_counter import extract_kmers, count_kmers


def test_extract_kmers_basic():
    """Test standard k-mer extraction."""
    result = extract_kmers("ATGT", 2)
    assert result == [("AT", "G"), ("TG", "T")]


def test_extract_kmers_short_sequence():
    """Sequence shorter than k should return empty list."""
    assert extract_kmers("A", 2) == []


def test_count_kmers_single_sequence():
    """Test counting on a single sequence."""
    result = count_kmers(["ATGT"], 2)

    assert result["AT"]["total"] == 1
    assert result["AT"]["next"]["G"] == 1


def test_count_kmers_multiple_sequences():
    """Test aggregation across multiple sequences."""
    result = count_kmers(["ATG", "ATG"], 2)

    assert result["AT"]["total"] == 2
    assert result["AT"]["next"]["G"] == 2


def test_multiple_next_characters():
    """Test k-mer followed by different nucleotides."""
    result = count_kmers(["ATGA", "ATGG"], 2)

    assert result["TG"]["total"] == 2
    assert result["TG"]["next"]["A"] == 1
    assert result["TG"]["next"]["G"] == 1


def test_empty_input():
    """Empty sequence list should return empty dict."""
    assert count_kmers([], 2) == {}


def test_k_equal_sequence_length():
    """No k-mers if sequence length equals k."""
    assert count_kmers(["AT"], 2) == {}
