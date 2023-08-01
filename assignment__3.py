#1 QUESTION
def sort_odd_even(numbers):
    odd_nos = []
    even_nos =[]
    for num in numbers:
        if num%2!=0:
            odd_nos.append(num)
        else:
            even_nos.append(num)
    odd_nos.sort()
    even_nos.sort()
    return odd_nos+even_nos
numbers_list = [5, 0, 4, 9, 3, 1, 6, 7]
sorted_list=sort_odd_even(numbers_list)
print(sorted_list)


#2 QUESTION
list = [12,24,35,24,88,120,155]
list= [i for i in list if i!=24]
print(list)


#3 QUESTION
odd_nos  = [1,3,5,7,11,13,17]
square_nos = []
for num in odd_nos:
    square_nos.append(num**2)
print(square_nos)


#4 QUESTION
def even_integers(arr):
    even = sum(1 for num in arr if num % 2 == 0)
    return even
array = [1, 2, 3, 4, 5, 6, 7, 8,12,13,24,25,67,88,23,89,92]
result = even_integers(array)
print("The number of even number is:",result)


#5 QUESTION
def filter_words(word):
    return len(word) >= 4
words_list = ["cat", "goat", "car", "bicycle", "home", "balcony"]
filtered_words = list(filter(filter_words, words_list))
print("words that are shorter than 4 letters from a list of words:\n",filtered_words)


#6 QUESTION
fahrenheit_temperatures = [98, 65, 73, 107, 92]
celsius_temperatures = [(temp - 32) * 5/9 for temp in fahrenheit_temperatures]
print(celsius_temperatures)


#7 QUESTION
fahrenheit_temperatures = [65, 76, 68, 98, 106]
celsius_temperatures = list(map(lambda temp: (temp - 32) * 5/9, fahrenheit_temperatures))
print("Celsius Temperatures:", celsius_temperatures)


#8 QUESTION
keys = ["maths", "science", "English", "Social"]
values = [89, 70, 85, 92]
list_dictionary = dict(zip(keys, values))
print(list_dictionary)


#9 QUESTION
import random

def get_player_choice():
    player_choice = input("Enter your choice (Rock, Paper, or Scissors): ")
    while player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter 'Rock', 'Paper', or 'Scissors'.")
        player_choice = input("Enter your choice (Rock, Paper, or Scissors): ")
    return player_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        return "Player"
    else:
        return "Computer"

def main():
    player_score = 0
    computer_score = 0

    for round in range(1, 11):
        print(f"\nRound {round}:")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"Computer chooses: {computer_choice.capitalize()}")
        winner = determine_winner(player_choice, computer_choice)

        if winner == "Player":
            player_score += 1
            print("You win this round!")
        elif winner == "Computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

    print("\nGame Over!")
    print(f"Player's Points: {player_score}")
    print(f"Computer's Points: {computer_score}")

    if player_score > computer_score:
        print("Congratulations! You win the game!")
    elif computer_score > player_score:
        print("Computer wins the game!")
    else:
        print("It's a tie. No overall winner.")
if True:
    main()


#10 QUESTION
inp = input("Enter comma-separated numbers: ")
nos_list = inp.split(',')
nos_tuple = tuple(nos_list)
print(nos_list)
print(nos_tuple)


#11 QUESTION
inp = input("Enter comma-separated sequence of words: ")
words_list = inp.split(',')
sorted_words_list = sorted(words_list)
sorted_seq = ",".join(sorted_words_list)
print(sorted_seq)


#12 QUESTION
def is_divisible_by_5(binary):
    decimal = int(binary, 2)
    return decimal % 5 == 0
input_sequence = input("Enter a sequence of comma-separated 4-digit binary numbers: ")
output_sequence = ",".join(binary for binary in input_sequence.split(',') if is_divisible_by_5(binary))
print(output_sequence)

