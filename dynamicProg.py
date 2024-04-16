import argparse
import time
import math

def dynamicProgrammingFind(maxRange, target):
    print("Finding: " + str(target))
    numerator = 1
    denominator = 2
    breakBool = True
    guess_count = 0
    modCheck = -1
    ##Find the answer via dynamic division
    while (breakBool):
        ##Skip repeat fractions
        if((((numerator % 2 == 0) and (denominator % 2 == 0)) or ((numerator % 3 == 0) and (denominator % 3 == 0))) and (numerator != 1)):
            if(tempInt > target):
                numerator+=1
            denominator+=1
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
    
        ##print(str(numerator) + " / " + str(denominator))

    return tempInt, guess_count

def main(min_range, max_range, target, jackpot):
    start_time = time.perf_counter()  # Start time in microseconds
    guess, guess_count = dynamicProgrammingFind(max_range, target)
    end_time = time.perf_counter()  # End time in microseconds
    elapsed_time = (end_time - start_time) * 1_000_000  # Time taken to find the correct value

    ##with open("DynamicProgrammingResults.txt", "a") as file:
    ##    file.write(f"{min_range} {max_range} {target} {guess_count} {jackpot} {jackpot - guess_count} {elapsed_time:.2f}\n")

    if guess is not None:
        print("Jackpot won! Target number is:", guess)
        print("Number of guesses:", guess_count)
        print("Time taken (microseconds): {:.2f}".format(elapsed_time))
        appendTime("{:.2f}\n".format(elapsed_time))
        appendMax(str(max_range) + "\n")
        appendGuesses(str(guess_count) + "\n")
    else:
        print("Target number not found in this subrange.")

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
                min_range, max_range, target_number, jackpot = map(int, arguments)
                main(min_range, max_range, target_number, jackpot)
            else:
                print("Invalid input format:", line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dynamic Programming guessing game")
    parser.add_argument("filename", type=str, help="File containing arguments")
    args = parser.parse_args()

    read_arguments_from_file(args.filename)