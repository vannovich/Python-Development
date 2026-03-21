import random
# Greetings
print(f"Welcome to hangman".upper())

print()
words = [
    "apple", "banana", "orange", "grapes", "mangoes",
    "peach", "cherry", "lemon", "melon", "berry",
    "table", "chair", "couch", "shelf", "floor",
    "house", "window", "doorway", "ceiling", "garden",
    "computer", "laptop", "keyboard", "monitor", "printer",
    "screen", "router", "server", "memory", "storage",
    "animal", "tiger", "zebra", "horse", "panda",
    "eagle", "shark", "whale", "snake", "lizard",
    "river", "ocean", "mountain", "valley", "desert",
    "forest", "island", "beach", "jungle", "canyon",
    "happy", "angry", "excited", "nervous", "joyful",
    "calmly", "brave", "proud", "eager", "silly",
    "music", "guitar", "piano", "violin", "drums",
    "trumpet", "flute", "singer", "artist", "melody",
    "light", "darkness", "shadow", "bright", "glowing",
    "energy", "power", "charge", "voltage", "current",
    "travel", "journey", "ticket", "flight", "luggage",
    "hotel", "resort", "tourist", "voyage", "cruise",
    "school", "college", "university", "teacher", "student",
    "lesson", "course", "degree", "diploma", "campus"
]

chosen_word = random.choice(words)

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

lives = 10
    
end_of_game = False
while not end_of_game:
    guess = input("Guessa letter: ").lower()
    for position in range(len(chosen_word) - 1):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter 
       
            
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")
        
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You Win")
            