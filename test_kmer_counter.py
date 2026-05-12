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
    assert validate_sequence("ATCG", 2) is True


def test_validate_sequence_too_short():
    assert validate_sequence("AT", 3) is False


def test_validate_sequence_invalid_character():
    assert validate_sequence("ATXG", 2) is False


def test_validate_sequence_numbers():
    assert validate_sequence("AT12", 2) is False


def test_update_kmer_count_new_entry():
    data = {}

    update_kmer_count(data, "AT", "C")

    assert data["AT"]["count"] == 1
    assert data["AT"]["next_chars"]["C"] == 1


def test_update_kmer_count_existing_entry():
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
    result = count_kmers_with_context("ATCG", 2)

    assert result["AT"]["count"] == 1
    assert result["AT"]["next_chars"]["C"] == 1

    assert result["TC"]["count"] == 1
    assert result["TC"]["next_chars"]["G"] == 1


def test_merge_kmer_data():
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


def test_write_results_to_file():
    data = {
        "AT": {
            "count": 2,
            "next_chars": {
                "C": 1,
                "G": 1
            }
        }
    }

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    write_results_to_file(data, filename)

    with open(filename, "r") as f:
        content = f.read()

    os.remove(filename)

    assert "AT 2 C:1 G:1" in content
