# word_guesser_
A classic word-guessing game implemented in Python that challenges players to reveal a hidden programming language by guessing letters one at a time.   

🎮 Features
* Random Word Selection: Chooses from 9 popular programming languages
* Visual Word Display: Shows correctly guessed letters and blanks for unknowns
* Attempt Tracking: Limited to 10 incorrect guesses
* Case-Insensitive Input: Converts all guesses to lowercase for consistency
* Win/Loss Conditions: Clear victory and defeat messages
* Real-time Feedback: Instant feedback on correct/incorrect guesses

🛠️ How It Works
*  The program randomly selects a word from the word bank
*  Players guess one letter at a time
* Correct guesses reveal the letter's position(s) in the word
* Incorrect guesses reduce remaining attempts
* Game ends when:
* Player guesses all letters (win)
* Player runs out of attempts (loss)

💻 Code Structure
* Random Selection: Uses random.choice() for word selection
* List Comprehension: Creates the initial hidden word display
* String Manipulation: Uses join() for clean word display
* Loop Logic: while loop controls game flow with exit conditions

📋 Example Gameplay 

    Current word: _ _ _ _ _ _

    Guess a letter: p
    Great guess!

    Current word: p _ _ _ _ _

    Guess a letter: x
    Wrong guess! Attempts left: 9

🎯 Learning Outcomes
* This project demonstrates:
* Basic Python syntax and control structures
* String and list manipulation
* Random module usage
* User input handling
* Conditional logic implementation
