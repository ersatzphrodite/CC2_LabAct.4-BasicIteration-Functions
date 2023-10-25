def find_pairs_with_sum_zero(numbers):
    #   `find_pairs_with_sum_zero(numbers)` function takes list of numbers and returns list of pairs whose sum is zero.
    pairs = set()  # Uses a set to store unique pairs.
    seen = set()   # Uses a set to store unique numbers already seen.

    for num in numbers:
        complement = -num
    # Calculates the complement by multiplying the value of num by -1.
        if complement in seen:
            # Sort the pair to ensure uniqueness
            pair = tuple(sorted((num, complement)))  # Creates a new tuple where the numbers are in sorted order.
            pairs.add(pair)  # Adds the sorted tuple to the pairs set.

        seen.add(num)   # Adds the current `num` to the `seen` set.

    return list(pairs)  # Converts the set of unique pairs found into a list before returning it.


def get_user_input(max_input=7):
    #  `get_user_input(max_input=7)` function sets the maximum number of inputs to 7.
    numbers = []
    for i in range(max_input):  # Sets up a loop that iterates i from 0 to max_input.
        num = input(f"✔ Enter an integer (or press Enter to finish): ")

        if not num:
            break  # Exits the loop if the user presses `Enter` without entering a number.
        try:
            num = int(num)  # Converts the input to an integer.
            if num not in numbers:  # Checks if num is not already in the set.
                numbers.append(num)  # Stores input into a list.
        except ValueError:
            print("Invalid input. Please enter a valid number or press Enter to finish input.")
        #   Displays an error message if user enters something that is not an integer.
        if len(numbers) >= max_input:   # Enforces a limit on the number of inputs a user can provide.
            print("You've reached the maximum number of inputs (7).")
            break

    return numbers


def main():
    while True:  # Starts an infinite loop.
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

        print("▩▩▩▩▩▩▩▩▩▩▩▩▩ DO YOU WANT TO ENTER MORE NUMBERS? ▩▩▩▩▩▩▩▩▩▩▩▩▩▩")
        while True:
            response = input("(yes/no): ").strip().lower()
            """   `strip()` is used to remove extra spaces or unwanted characters in users response;
                  `lower()` is used to convert the user's input to lowercase,
                   whether the user enters "YES," "Yes," "yes," or "no," "NO," "No," or "no".
            """
            if response == "no":
                return  # Exits the program if the response is "no".
            elif response == "yes":
                break  # Exits the response loop and continue entering numbers.
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
    #   Ensures that the main function that contains existing code is executed when the script is run.
