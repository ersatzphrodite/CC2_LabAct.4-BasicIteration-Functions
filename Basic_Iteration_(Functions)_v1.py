def find_pairs_with_sum_zero(numbers):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 0:
                pairs.append((numbers[i], numbers[j]))  # Used pairs.append to store pairs in a list.
    return pairs
#   `find_pairs_with_sum_zero(numbers)` function takes list of numbers and returns list of pairs whose sum is zero.

def get_user_input(max_input=7):
    numbers = []
    for i in range(max_input):
        num = input(f"✔ Enter an integer (or press Enter to finish): ")

        if not num:
            break  # Exit the loop if the user presses `Enter` without entering a number.
        try:
            num = int(num)  # Convert the input to an integer.
            if num not in numbers:  # Checks if num is not already in the set.
                numbers.append(num)  # Stores input into a list.
            else:
                print("You've already entered that number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number or press Enter to finish input.")

        if len(numbers) >= max_input:
            print("You've reached the maximum number of inputs (7).")
            break

    return numbers
  #  `get_user_input(max_input=7)` function sets the maximum number of inputs to 7.

def main():
    print("▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩ INPUT UP TO 7 NUMBERS: ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩")
    numbers = get_user_input()
    print("▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩")

    print("Numbers =", numbers)
    print("Which pair/s of numbers have the sum of zero?")

    pairs = find_pairs_with_sum_zero(numbers)

    if len(pairs) == 1:
        print("✔ The pair", pairs[0], "has a sum of zero.")  # Checks if there's exactly one pair in the pairs list.
    elif pairs:
        print("✔ The pairs", pairs, "have a sum of zero.")  # Checks if there are multiple pairs.
    else:
        print("✔ No existing pair has a sum of zero.")  # Executes if pairs list = False (empty).

    print("▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩")


if __name__ == "__main__":  # Ensures that the main function is executed when the script is run as the main program.
    main()
    #   The main function contains existing code for processing, and output.
