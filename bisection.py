import argparse
import time

def Bisection(target, low, high, guess_count=0):
    if low <= high:
        guess_count += 1
        mid = (low + high) // 2
        if mid == target:
            return mid, guess_count  # Found the target and the number of guesses
        elif mid < target:
            return Bisection(target, mid + 1, high, guess_count)  # Search in the right half
        else:
            return Bisection(target, low, mid - 1, guess_count)  # Search in the left half
    else:
        return -1, guess_count  # Target not found within the given range

def main(lowerBound, upperBound, target, jackpot):
    guessLimitBool = True
    start_time = time.perf_counter()  # Start time in microseconds
    guess, guess_count = Bisection(target, lowerBound, upperBound)
    end_time = time.perf_counter()  # End time in microseconds
    elapsed_time = (end_time - start_time) * 1_000_000  # Time taken to find the correct value

    ##with open("BisectionResults.txt", "a") as file:
    ##    file.write(f"{lowerBound} {upperBound} {target} {guess_count} {jackpot} {jackpot - guess_count} {elapsed_time:.2f}\n")

    if(guessLimitBool):
        appendguessLimit(guess, upperBound)

    if guess is not None:
        if(guessLimitBool):
            appendSuccess()
        else:
            print("Jackpot won! Target number is:", guess)
            print("Number of guesses:", guess_count)
            print("Time taken (microseconds): {:.2f}".format(elapsed_time))
            appendTime("{:.2f}\n".format(elapsed_time))
            appendMax(str(upperBound) + "\n")
            appendGuesses(str(guess_count) + "\n")

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

def read_arguments_from_file(filename):
    with open(filename, "r") as file:
        for line in file:
            arguments = line.strip().split()
            if len(arguments) == 4:
                lowerBound, upperBound, target, jackpot = map(int, arguments)
                main(lowerBound, upperBound, target, jackpot)
            else:
                print("Invalid input format:", line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guessing game")
    parser.add_argument("filename", type=str, help="File containing arguments")
    args = parser.parse_args()

    read_arguments_from_file(args.filename)
