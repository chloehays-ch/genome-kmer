# Genome K-mer Analyzer
## Chloe Hays

## Overview

This project analyzes DNA sequence fragments by extracting **k-mers** (substrings of length k) and tracking:
- The total frequency of each k-mer
- The frequency of each character that immediately follows each k-mer

This is a simplified model of steps used in genome assembly workflows.

## Project Structure

```text
project/
│
├── corrected_kmer_analyzer.py   # Main program
├── tests/
│   └── test_kmer_counter.py     # Pytest test suite
├── sample_data/
│   ├── sample_sequences.txt
│   └── invalid_sequences.txt
└── README.md
---

## AI Use Statement
Portions of this project were developed with assistance from ChatGPT for:

- debugging logic errors in k-mer counting
- designing pytest test cases
- improving code structure and readability
- writing documentation

All final code was reviewed, tested, and modified by myself. 
