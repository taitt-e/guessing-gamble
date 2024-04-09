import argparse
import time

def dynamicProgrammingFind(minRange, maxRange, target):
    print("Finding: " + str(target))
    tempInt = minRange
    breakBool = True
    operator = 2
    guess_count = 0
    ##Find a smaller subrange to begin iterating on via dynamic division
    while (breakBool):
        if(tempInt == target):
            return tempInt,guess_count
        guess_count+=1
        if(target > (maxRange//operator)):
            operator-=1
            tempInt = maxRange//operator
            break
        else:
            operator+=1
    if(tempInt == target):
        return tempInt,guess_count
    
    ##Further close the gap via dynamic multiplication with loops
    ##Not properly iterating here, I believe its a logic error - TE
    operator = 1
    while(breakBool):
        for x in range(operator):
            guess_count+=1
            if(tempInt+(operator*x) > target):
                tempInt = tempInt+(operator*(x-1))
                breakBool = False
        operator+=1
    if(tempInt == target):
        return tempInt,guess_count
    
    ##Close the gap even more with dynamic addition
    ##Not properly iterating here, I believe its a logic error - TE
    operator = 1
    breakBool = True
    while(breakBool):
            for x in range(operator):
                guess_count+=1
                if(tempInt+(operator+x) > target):
                    tempInt += (operator+x)
                    breakBool = False
                    break

            operator+=1
    
    ##Finally close the gap with subtraction
    while(tempInt != target):
        guess_count+=1
        tempInt-=1
    
    return tempInt, guess_count

def main(min_range, max_range, target, jackpot):
    start_time = time.perf_counter()  # Start time in microseconds
    guess, guess_count = dynamicProgrammingFind(min_range, max_range, target)
    end_time = time.perf_counter()  # End time in microseconds
    elapsed_time = (end_time - start_time) * 1_000_000  # Time taken to find the correct value

    with open("DynamicProgrammingResults.txt", "a") as file:
        file.write(f"{min_range} {max_range} {target} {guess_count} {jackpot} {jackpot - guess_count} {elapsed_time:.2f}\n")

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