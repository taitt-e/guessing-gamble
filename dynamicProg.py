import argparse
import time
import math

def dynamicProgrammingFind(maxRange, target):
    print("Finding: " + str(target))
    numerator = 1
    denominator = 2
    breakBool = True
    guess_count = 0
    ##Find the answer via dynamic division
    while (breakBool):
        guess_count+=1
        tempInt = numerator/denominator
        tempInt *= maxRange
        if(math.floor(tempInt) == target):
            tempInt = math.floor(tempInt)
            break
        if(math.ceil(tempInt) == target):
            tempInt = math.ceil(tempInt)
            break
        if(tempInt == target):
            break
        if(target > tempInt):
            numerator += 1
        denominator += 1

    return tempInt, guess_count

def main(min_range, max_range, target, jackpot):
    start_time = time.perf_counter()  # Start time in microseconds
    guess, guess_count = dynamicProgrammingFind(max_range, target)
    end_time = time.perf_counter()  # End time in microseconds
    elapsed_time = (end_time - start_time) * 1_000_000  # Time taken to find the correct value

    with open("DynamicProgrammingResults.txt", "a") as file:
        file.write(f"{min_range} {max_range} {target} {guess_count} {jackpot} {jackpot - guess_count} {elapsed_time:.2f}\n")

    if guess is not None:
        print("Jackpot won! Target number is:", guess)
        print("Number of guesses:", guess_count)
        print("Time taken (microseconds): {:.2f}".format(elapsed_time))
        appendTime("{:.2f}\n".format(elapsed_time))
    else:
        print("Target number not found in this subrange.")

def appendTime(time):
    f = open("DynamicProgrammingTimes", "a")
    f.write(time)
    f.close

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
    parser = argparse.ArgumentParser(description="Dynamic Programming guessing game")
    parser.add_argument("filename", type=str, help="File containing arguments")
    args = parser.parse_args()

    read_arguments_from_file(args.filename)