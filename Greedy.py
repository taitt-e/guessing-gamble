import argparse
import time

def egyptian_fraction_find(min_range, max_range, target_number, jackpot, guess_count=0):
    # Check if the jackpot is in the middle
    middle_divisor = (min_range + max_range) // 2
    
    ##guess_count += 1

    if jackpot == middle_divisor:
        return jackpot, guess_count
    elif jackpot < middle_divisor:
        # Check if the jackpot is on the low end
        find_int = middle_divisor - 1
        for i in range(find_int, 0, -1):
            guess_count += 1
            if i < jackpot:
                find_int = i
                break
        ##for i in range(find_int, jackpot + 1):
        ##    guess_count += 1
        ##    if i == jackpot:
        ##        return jackpot, guess_count
        # Recursive call for lower subrange
        return egyptian_fraction_find(min_range, middle_divisor - 1, target_number, jackpot, guess_count)
    else:
        # Check if the jackpot is on the high end
        find_int = middle_divisor
        for i in range(find_int, 0, -1):
            guess_count += 1
            if i < jackpot:
                find_int = i
                break
        ##for i in range(middle_divisor, max_range + 1):
        ##    guess_count += 1
        ##    if i == jackpot:
        ##        return jackpot, guess_count
        # Recursive call for upper subrange
        return egyptian_fraction_find(middle_divisor + 1, max_range, target_number, jackpot, guess_count)

def main(min_range, max_range, target_number, jackpot):
    start_time = time.perf_counter()  # Start time in microseconds
    guess, guess_count = egyptian_fraction_find(min_range, max_range, target_number, jackpot)
    end_time = time.perf_counter()  # End time in microseconds
    elapsed_time = (end_time - start_time) * 1_000_000  # Time taken to find the correct value

    with open("GreedyResults.txt", "a") as file:
        file.write(f"{min_range} {max_range} {target_number} {guess_count} {jackpot} {jackpot - guess_count} {elapsed_time:.2f}\n")

    if guess is not None:
        print("Jackpot won! Target number is:", guess)
        print("Number of guesses:", guess_count)
        print("Time taken (microseconds): {:.2f}".format(elapsed_time))
    else:
        print("Target number not found in this subrange.")

def read_arguments_from_file(filename):
    with open(filename, "r") as file:
        for line in file:
            arguments = line.strip().split()
            if len(arguments) == 4:
                min_range, max_range, target_number, jackpot = map(int, arguments)
                main(min_range, max_range, target_number, jackpot)
            else:
                print("Invalid input format:", line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Greedy guessing game")
    parser.add_argument("filename", type=str, help="File containing arguments")
    args = parser.parse_args()

    read_arguments_from_file(args.filename)
