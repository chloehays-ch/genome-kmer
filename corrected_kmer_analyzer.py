import sys


def validate_sequence(sequence, k):
    """
    Validate that a sequence is usable for k-mer analysis.

    A valid sequence:
    - Must be at least length k
    - Must contain only valid nucleotide characters:
      A, T, C, G

    Parameters
    ----------
    sequence : str
        DNA sequence to validate.
    k : int
        Length of the k-mer.

    Returns
    -------
    bool
        True if the sequence is valid, False otherwise.
    """

    # Convert sequence to uppercase for consistency
    sequence = sequence.upper()

    # Sequence must be at least length k
    if len(sequence) < k:
        return False

    # Valid nucleotide characters
    valid_nucleotides = {"A", "T", "C", "G"}

    # Check every character in the sequence
    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            return False

    return True


def update_kmer_count(kmer_data, kmer, next_char):
    """
    Update k-mer frequency data.

    Stores:
    - Total frequency of each k-mer
    - Frequency of the character that follows each k-mer

    Parameters
    ----------
    kmer_data : dict
        Dictionary containing k-mer statistics.
    kmer : str
        Current k-mer.
    next_char : str
        Character immediately following the k-mer.

    Returns
    -------
    dict
        Updated k-mer dictionary.
    """

    # Create entry if k-mer has not been seen before
    if kmer not in kmer_data:
        kmer_data[kmer] = {
            "count": 0,
            "next_chars": {}
        }

    # Increment total k-mer count
    kmer_data[kmer]["count"] += 1

    # Initialize next character count if needed
    if next_char not in kmer_data[kmer]["next_chars"]:
        kmer_data[kmer]["next_chars"][next_char] = 0

    # Increment next character frequency
    kmer_data[kmer]["next_chars"][next_char] += 1

    return kmer_data


def count_kmers_with_context(sequence, k):
    """
    Count all k-mers and their following characters in a sequence.

    Parameters
    ----------
    sequence : str
        DNA sequence to analyze.
    k : int
        Length of the k-mer.

    Returns
    -------
    dict
        Dictionary containing k-mer frequencies and context counts.
    """

    # Store all k-mer information
    kmer_data = {}

    # Convert sequence to uppercase
    sequence = sequence.upper()

    # Iterate through sequence
    for i in range(len(sequence) - k):

        # Extract current k-mer
        kmer = sequence[i:i + k]

        # Character immediately following the k-mer
        next_char = sequence[i + k]

        # Update counts
        update_kmer_count(kmer_data, kmer, next_char)

    return kmer_data


def merge_kmer_data(master_data, new_data):
    """
    Merge k-mer statistics from one dictionary into another.

    Parameters
    ----------
    master_data : dict
        Main dictionary storing all k-mer data.
    new_data : dict
        Dictionary containing newly calculated k-mer data.

    Returns
    -------
    dict
        Updated master dictionary.
    """

    for kmer in new_data:

        # Create new k-mer entry if needed
        if kmer not in master_data:
            master_data[kmer] = {
                "count": 0,
                "next_chars": {}
            }

        # Add total counts
        master_data[kmer]["count"] += new_data[kmer]["count"]

        # Add next character frequencies
        for char in new_data[kmer]["next_chars"]:

            if char not in master_data[kmer]["next_chars"]:
                master_data[kmer]["next_chars"][char] = 0

            master_data[kmer]["next_chars"][char] += (
                new_data[kmer]["next_chars"][char]
            )

    return master_data


def write_results_to_file(kmer_data, output_filename):
    """
    Write k-mer statistics to an output file.

    Output format:
    kmer total_count next_char:frequency ...

    Example:
    AT 3 C:2 G:1

    Parameters
    ----------
    kmer_data : dict
        Dictionary containing k-mer statistics.
    output_filename : str
        Name of output file.
    """

    # Sort k-mers alphabetically for readable output
    sorted_kmers = sorted(kmer_data.keys())

    with open(output_filename, "w") as f:

        for kmer in sorted_kmers:

            total_count = kmer_data[kmer]["count"]
            next_chars = kmer_data[kmer]["next_chars"]

            # Sort next characters alphabetically
            next_char_str = " ".join(
                f"{char}:{freq}"
                for char, freq in sorted(next_chars.items())
            )

            # Write formatted output line
            f.write(f"{kmer} {total_count} {next_char_str}\n")


def main():
    """
    Main program execution.

    Reads sequence data from a file, counts k-mers and
    following characters, then writes results to an output file.
    """

    # Check correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python kmer_counter.py <sequence_file> <k> <output_file>")
        sys.exit(1)

    sequence_file = sys.argv[1]

    # Validate k value
    try:
        k = int(sys.argv[2])

        if k <= 0:
            raise ValueError

    except ValueError:
        print("Error: k must be a positive integer.")
        sys.exit(1)

    output_file = sys.argv[3]

    print(f"Reading sequences from {sequence_file}...")

    # Master dictionary storing all sequence results
    all_kmer_data = {}

    try:
        with open(sequence_file, "r") as f:

            for line_number, sequence in enumerate(f, start=1):

                # Remove whitespace/newline characters
                sequence = sequence.strip()

                # Skip empty lines
                if not sequence:
                    continue

                # Validate sequence
                if not validate_sequence(sequence, k):
                    print(
                        f"Warning: Skipping invalid sequence "
                        f"on line {line_number}"
                    )
                    continue

                # Count k-mers for current sequence
                sequence_kmer_data = count_kmers_with_context(sequence, k)

                # Merge into master dictionary
                merge_kmer_data(all_kmer_data, sequence_kmer_data)

        # Write final results
        write_results_to_file(all_kmer_data, output_file)

        print(f"Results written to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{sequence_file}' not found.")
        sys.exit(1)


if __name__ == "__main__":
    main()
            
       
