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
    start_time = time.perf_counter()  # Start time in microseconds
    guess, guess_count = Bisection(target, lowerBound, upperBound)
    end_time = time.perf_counter()  # End time in microseconds
    elapsed_time = (end_time - start_time) * 1_000_000  # Time taken to find the correct value

    with open("results.txt", "a") as file:
        file.write(f"{lowerBound} {upperBound} {target} {guess_count} {jackpot} {jackpot - guess_count} {elapsed_time:.2f}\n")

    if guess != -1:
        print("Congratulations! You guessed the number:", guess)
        print("Number of guesses:", guess_count)
        print("Time taken (microseconds): {:.2f}".format(elapsed_time))
        if guess == jackpot:
            print("You hit the jackpot!")
    else:
        print("Sorry, the target number was not found within the given range.")

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
