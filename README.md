## Genome K-mer Counter ##

This project analyzes DNA sequence fragments and computes:

-The frequency of each k-mer (substrings of length k)
-The frequency of nucleotides - A, T, C, G - following each k-mer

This type of analysis is frequently used in processes such as genome assembly,
sequence comparison, and motif detection 

## Usage ##

Clone the repository:
https://github.com/chloehays-ch/genome-kmer 

Make sure Python 3 is installed 

Run the script from the command line:
python kmer_counter.py input.txt <k> output.txt
Arguments
Argument        Description
input.txt       File containing DNA sequence
<k>             Length of k-mers
output.txt      File where results will be written

## Usage Example ##
Input (input.txt)

ACGTTGCACGTT
Command
python kmer_counter.py input.txt 3 output.txt

Output (output.txt)
ACG: 2 -> T:2
CGT: 2 -> T:2
GTT: 2 -> G:1, (end):1
...

## Logic ##
-Reading the DNA sequence from the input file
-Sliding a window of length k across the sequence
-Counting each k-mer occurrence
-Tracking the nucleotide that follows each k-mer
-Writing results in a structured format

## Status and Tests ##
Work in progress using test-driven development
This project follows test-driven development (TDD).

Run tests with:
pytest
Tests cover:
-Correct k-mer counting
-Accurate nucleotide-following frequencies
-Edge cases and invalid inputs

## AI use statement: ##
I utilized the AI platform ChatGPT for this assignment to:
-design tests necessary to verify suitability of my script
-debug error messages when running pytests
-verify that my script was accurate and had logical implementations
