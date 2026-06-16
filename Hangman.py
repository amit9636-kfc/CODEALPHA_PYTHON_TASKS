import random

def hangman():
    # 1. Word list
    words = ["python", "coding", "computer", "challenge", "program"]
    target_word = random.choice(words)
    guessed_letters = []
    attempts = 6
    
    print("--- Hangman Game Shuru! ---")

    # 2. Main game loop
    while attempts > 0:
        # Display word progress
        display_word = ""
        for letter in target_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"\nWord: {display_word}")
        print(f"Bache hue attempts: {attempts}")
        
        if "_" not in display_word:
            print("Badhai ho! Aap jeet gaye!")
            break
            
        # 3. User input
        guess = input("Ek letter guess karein: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Kripya sirf ek valid letter daalein.")
            continue
            
        if guess in guessed_letters:
            print("Ye letter aap pehle hi guess kar chuke hain.")
            continue
            
        guessed_letters.append(guess)
        
        # 4. Logic check
        if guess in target_word:
            print("Sahi guess hai!")
        else:
            attempts -= 1
            print("Galat guess!")
            
    if attempts == 0:
        print(f"\nGame Over! Sahi word tha: {target_word}")

# Game chalayein
hangman()