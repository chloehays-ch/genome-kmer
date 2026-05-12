import os
import tempfile

from corrected_kmer_analyzer import (
    validate_sequence,
    update_kmer_count,
    count_kmers_with_context,
    merge_kmer_data,
    write_results_to_file
)


def test_validate_sequence_valid():
    """
    Test that a valid DNA sequence is accepted.

    A valid sequence contains only A, T, C, G and is
    at least length k.
    """
    assert validate_sequence("ATCG", 2) is True


def test_validate_sequence_too_short():
    """
    Test that sequences shorter than k are rejected.
    """
    assert validate_sequence("AT", 3) is False


def test_validate_sequence_invalid_character():
    """
    Test that sequences containing invalid characters
    (non A/T/C/G) are rejected.
    """
    assert validate_sequence("ATXG", 2) is False


def test_validate_sequence_numbers():
    """
    Test that sequences containing numeric characters
    are rejected.
    """
    assert validate_sequence("AT12", 2) is False


def test_validate_sequence_lowercase():
    """
    Test that lowercase sequences are correctly handled.

    The function should convert lowercase input to uppercase
    before validation.
    """
    assert validate_sequence("atcg", 2) is True


def test_update_kmer_count_new_entry():
    """
    Test adding a completely new k-mer to an empty dictionary.

    The function should initialize count and next character data.
    """
    data = {}

    update_kmer_count(data, "AT", "C")

    assert data["AT"]["count"] == 1
    assert data["AT"]["next_chars"]["C"] == 1


def test_update_kmer_count_existing_entry():
    """
    Test updating an existing k-mer entry.

    Counts should increment correctly for both k-mer and next char.
    """
    data = {
        "AT": {
            "count": 1,
            "next_chars": {"C": 1}
        }
    }

    update_kmer_count(data, "AT", "C")

    assert data["AT"]["count"] == 2
    assert data["AT"]["next_chars"]["C"] == 2


def test_count_kmers_with_context():
    """
    Test counting k-mers and their following characters in a sequence.

    Verifies that both k-mer counts and next-character tracking work.
    """
    result = count_kmers_with_context("ATCG", 2)

    assert result["AT"]["count"] == 1
    assert result["AT"]["next_chars"]["C"] == 1

    assert result["TC"]["count"] == 1
    assert result["TC"]["next_chars"]["G"] == 1


def test_count_kmers_empty_result():
    """
    Test that sequences too short to produce a next character
    return an empty result dictionary.
    """
    result = count_kmers_with_context("AT", 2)

    assert result == {}


def test_merge_kmer_data():
    """
    Test merging two k-mer dictionaries together.

    Ensures counts and next-character frequencies combine correctly.
    """
    master = {
        "AT": {
            "count": 1,
            "next_chars": {"C": 1}
        }
    }

    new = {
        "AT": {
            "count": 2,
            "next_chars": {"C": 1, "G": 1}
        }
    }

    merge_kmer_data(master, new)

    assert master["AT"]["count"] == 3
    assert master["AT"]["next_chars"]["C"] == 2
    assert master["AT"]["next_chars"]["G"] == 1


def test_merge_new_kmer():
    """
    Test merging a dictionary containing a completely new k-mer.

    The k-mer should be added correctly to the master dictionary.
    """
    master = {}

    new = {
        "CG": {
            "count": 1,
            "next_chars": {"A": 1}
        }
    }

    merge_kmer_data(master, new)

    assert master["CG"]["count"] == 1
    assert master["CG"]["next_chars"]["A"] == 1


def test_write_results_to_file():
    """
    Test writing k-mer results to an output file.

    Verifies that the output format is correctly written.
    """
    data = {
        "AT": {
            "count": 2,
            "next_chars": {
                "C": 1,
                "G": 1
            }
        }
    }

    # Create temporary file for testing output
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    write_results_to_file(data, filename)

    # Read file content back
    with open(filename, "r") as f:
        content = f.read()

    # Clean up temporary file
    os.remove(filename)

    # Check expected output appears in file
    assert "AT 2 C:1 G:1" in content
