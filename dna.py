import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Error - need 2 arguments")
        sys.exit(1)

    # Read database file into a variable
    with open(sys.argv[1]) as file:
        database = csv.DictReader(file)
        database_dictionary = list(database)
        # storing headers from file to loop them later
        database_header = database.fieldnames[1:]

    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as dna_file:
        dna_sequence = dna_file.read()

    # Find longest match of each STR in DNA sequence
    result = {}
    for sequence in database_header:
        result[sequence] = longest_match(dna_sequence, sequence)

    # Check database for matching profiles
    matched_suspect = None
    # looping every suspect in DB
    for suspect in database_dictionary:
        # setting initial matched_all_sequences to True so when you inner loop finds 1 not matching sequence it can and stop, set it to false and stop there
        matched_all_sequences = True
        for sequence_matched in result:
            if result[sequence_matched] != int(suspect[sequence_matched]):
                matched_all_sequences = False
                break
        # if all sequences are matching the matched_all_sequences will not be changed and then it will store current suspect name
        if matched_all_sequences:
            matched_suspect = suspect["name"]
    # if there is  matched_suspect - print his name, else "No match"
    if matched_suspect:
        print(matched_suspect)
    else:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
