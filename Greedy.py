import argparse
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

    with open("EgyptianFractionResults.txt", "a") as file:
        file.write(f"{numerator} {denominator} {target} {len(fraction_representation)} {jackpot} {jackpot - len(fraction_representation)} {guess_count} {elapsed_time:.2f}\n")

    if(guessLimitBool):
        ##appendguessLimit(guess, upperBound)

    ##Was previously Guess
    ##if fraction_representation is not None:
        if(guessLimitBool):
            appendSuccess()
        else:
            ##print("Jackpot won! Target number is:", guess)
            print("Number of guesses:", guess_count)
            print("Time taken (microseconds): {:.2f}".format(elapsed_time))
        ##appendTime("{:.2f}\n".format(elapsed_time))
        ##appendMax(str(upperBound) + "\n")
        ##appendGuesses(str(guess_count) + "\n")

def appendSuccess():
    f = open("MaxGuesses.txt", "a")
    f.write(str(1) + "\n")
    f.close()

def appendguessLimit(guesses, maxRange):
    maxGuesses = maxRange // 2
    if(guesses == maxGuesses):
        f = open("MaxGuesses.txt", "a")
        f.write(str(0) + "\n")
        guesses = 0
        f.close()

def appendTime(time):
    f = open("DynamicProgrammingTimes.txt", "a")
    f.write(time)
    f.close

def appendMax(max):
    f = open("DynamicProgrammingMaxes.txt", "a")
    f.write(max)
    f.close

def appendGuesses(guessCount):
    f = open("DynamicProgrammingGuesses.txt", "a")
    f.write(guessCount)
    f.close

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Egyptian fraction guessing game")
    parser.add_argument("numerator", type=int, help="Numerator of the fraction")
    parser.add_argument("denominator", type=int, help="Denominator of the fraction")
    parser.add_argument("target", type=int, help="Target number of unit fractions")
    parser.add_argument("jackpot", type=int, help="Jackpot number of unit fractions")
    args = parser.parse_args()

    main(args.numerator, args.denominator, args.target, args.jackpot)
