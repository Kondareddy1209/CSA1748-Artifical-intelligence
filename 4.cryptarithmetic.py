from itertools import permutations

def get_user_input():
    """Get the cryptarithmetic problem from the user."""
    print("Enter the cryptarithmetic problem:")
    
    # Get the components of the problem
    first_term = input("First term : ").strip()
    second_term = input("Second term : ").strip()
    result = input("Result ").strip()

    # Combine all letters
    all_letters = set(first_term + second_term + result)
    
    if len(all_letters) > 10:
        raise ValueError("More than 10 unique letters, which is not possible with digits 0-9.")
    
    return first_term, second_term, result, all_letters

def solve_cryptarithmetic(first_term, second_term, result, all_letters):
    """Solve the cryptarithmetic problem using brute force."""
    digits = '0123456789'

    # Generate all possible permutations of the digits for the letters
    for perm in permutations(digits, len(all_letters)):
        # Map each letter to a digit
        letter_to_digit = dict(zip(all_letters, perm))
        
        # Form the numbers based on the current mapping
        first_number = int(''.join(letter_to_digit[c] for c in first_term))
        second_number = int(''.join(letter_to_digit[c] for c in second_term))
        result_number = int(''.join(letter_to_digit[c] for c in result))

        # Check if the current mapping satisfies the equation
        if first_number + second_number == result_number:
            return letter_to_digit

    return None

def main():
    try:
        first_term, second_term, result, all_letters = get_user_input()
        solution = solve_cryptarithmetic(first_term, second_term, result, all_letters)
        if solution:
            print("Solution found:")
            for letter, digit in solution.items():
                print(f"{letter} = {digit}")
        else:
            print("No solution found.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
