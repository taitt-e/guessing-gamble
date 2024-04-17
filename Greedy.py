import time

def greedy_egyptian_fraction(numerator, denominator, target):
    fractions = []
    original_numerator = numerator  # Store the original numerator for printing
    original_denominator = denominator  # Store the original denominator for printing
    guess_count = 0  # Initialize guess counter
    
    # Adjust the numerator and denominator to represent the fraction provided as input
    if numerator >= denominator:
        fractions.append(numerator // denominator)  # Add the whole part to the fractions
        numerator %= denominator  # Update the numerator
    elif numerator == denominator:
        fractions.append(1)  # Add 1 as a unit fraction
        return fractions, guess_count
    
    while numerator != 0 and len(fractions) < target:
        unit_fraction_denominator = -(-denominator // numerator)  # Ceiling division
        fractions.append(unit_fraction_denominator)
        guess_count += 1  # Increment guess counter
        numerator = numerator * unit_fraction_denominator - denominator
        denominator *= unit_fraction_denominator
        guess_count += 1  # Increment guess counter for the numerator and denominator operations

    # If the loop terminates and there are still unit fractions needed to reach the target,
    # add additional 1s to represent the remaining fraction
    while len(fractions) < target:
        fractions.append(1)
        guess_count += 1  # Increment guess counter for adding 1s

    print('Original fraction:', original_numerator, '/', original_denominator)
    return fractions, guess_count

def main(numerator, denominator, target, jackpot):
    guessLimitBool = False
    start_time = time.perf_counter()  # Start time in microseconds
    fraction_representation, guess_count = greedy_egyptian_fraction(numerator, denominator, target)
    end_time = time.perf_counter()  # End time in microseconds
    elapsed_time = (end_time - start_time) * 1_000_000  # Time taken to find the fraction representation

    # Prepare the result string
    result_str = f"{numerator} {denominator} {target} {len(fraction_representation)} {jackpot} {jackpot - len(fraction_representation)} {guess_count} {elapsed_time:.2f}\n"

    # Write the result string to the result file
    try:
        with open("EgyptianFractionResults.txt", "a") as result_file:
            result_file.write(result_str)
    except Exception as e:
        print("Error writing to EgyptianFractionResults.txt:", e)

    if guessLimitBool:
        appendSuccess()
    #else:
        #appendGuesses(guess_count)
        #appendTime(elapsed_time)

def appendSuccess():
    try:
        with open("EFMaxGuesses.txt", "a") as f:
            f.write("1\n")
    except Exception as e:
        print("Error writing to EFMaxGuesses.txt:", e)

def appendTime(elapsed_time):
    try:
        with open("EFTimes.txt", "a") as f:
            f.write("{:.2f}\n".format(elapsed_time))
    except Exception as e:
        print("Error writing to EFTimes.txt:", e)

def appendGuesses(guess_count):
    try:
        with open("EFGuesses.txt", "a") as f:
            f.write(f"{guess_count}\n")
    except Exception as e:
        print("Error writing to EFGuesses.txt:", e)

def read_arguments_from_file():
    try:
        with open("input.txt", "r") as file:
            for line in file:
                arguments = line.strip().split()
                if len(arguments) == 4:
                    lowerBound, upperBound, target, jackpot = map(int, arguments)
                    main(lowerBound, upperBound, target, jackpot)
                else:
                    print("Invalid input format:", line)
    except Exception as e:
        print("Error reading input.txt:", e)

if __name__ == "__main__":
    read_arguments_from_file()
