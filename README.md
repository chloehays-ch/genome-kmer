# Genome K-mer Analyzer
## Chloe Hays
## Overview

This project analyzes DNA sequence fragments by extracting **k-mers** (substrings of length k) and calculating:

- Total frequency of each k-mer
- Frequency of each nucleotide that follows each k-mer

This is a simplified model of early steps in genome assembly.

---

## Project Structure


project/
│
├── corrected_kmer_analyzer.py # Main program
├── tests/
│ └── test_kmer_counter.py # Pytest test suite
├── sample_data/
│ ├── sample_sequences.txt
│ └── invalid_sequences.txt
└── README.md


---

## How to Run the Program

### Command format:

```bash id="k1p9wx"
python corrected_kmer_analyzer.py <input_file> <k> <output_file>
Example:
python corrected_kmer_analyzer.py sample_data/sample_sequences.txt 2 results.txt
Example Input

sample_data/sample_sequences.txt

ATCGAT
ATCGTT
GGATCA
Example Output

results.txt

AT 3 C:2 G:1
CG 2 A:1 T:1
GA 1 T:1
TC 2 G:2
CA 1 T:1
What the Output Means

Each line follows this format:

kmer total_count next_char:frequency
Example:
AT 3 C:2 G:1

Means:

"AT" appears 3 times total
It is followed by:
"C" two times
"G" one time

## Running Tests

Install pytest:
pip install pytest
Run tests:
pytest

## Test Coverage

The test suite verifies:

- Sequence validation
- valid DNA sequences
- invalid characters
- numeric input
- lowercase handling
- length constraints
- K-mer logic
- correct counting
- updating existing entries
- merging multiple sequences
- Output validation
- correct file formatting
- correct aggregation across sequences
- Design Notes
- All sequences are converted to uppercase
- Uses dictionary-based counting for efficiency
- Modular functions for testability
- Final results are aggregated before writing output


## AI Use Statement

Portions of this project were developed with assistance from ChatGPT for:

debugging k-mer counting logic
designing pytest test cases
improving code structure and readability
resolving Git and Markdown formatting issues

All final code was reviewed, tested, and modified by the author.
