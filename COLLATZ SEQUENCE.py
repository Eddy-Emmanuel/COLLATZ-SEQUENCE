def collatz_sequence(n):
    """
    The Collatz sequence, also called the 3n + 1 
    problem, is the simplest impossible math 
    problem. (But don’t worry, the program 
    itself is easy enough for beginners.) From a 
    starting number, n, follow three rules to get the next 
    number in the sequence:
    1. If n is even, the next number n is n // 2.
    2. If n is odd, the next number n is n * 3 + 1.
    3. If n is 1, stop. Otherwise, repeat.
    It is generally thought, but so far not mathematically proven, that 
    every starting number eventually terminates at 1. More information 
    about the Collatz sequence can be found at https://en.wikipedia.org/wiki/
    Collatz_conjecture.
    """

    col_seq = [str(n)]
    while True:
        if n == 1:
            return ", ".join(col_seq)
        else:
            n = n // 2 if (n % 2) == 0 else n*3 + 1
        col_seq.append(str(n))    
        

def main():

    while True:
        user_input = input("Enter a starting number (greater than 0) or QUIT:")
        
        if user_input == "quit":
            return 
        
        try:
            user_input = int(user_input)
            if user_input < 0:
                print("Enter a number greater than 0.")
            else:
                print(collatz_sequence(user_input))
        except:
            raise("Value Error...")
    
if __name__ == "__main__":
    main()
    
