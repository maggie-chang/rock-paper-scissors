import random
import ipywidgets

#number_of_rounds = input("How many rounds do you want to play")
#rock = 1
#paper = 2
#scissors = 3
#computer_choice = random.randint(rock, paper, scissors)

def get_computer_choice():
  options = ["rock", "paper", "scissors"]
  comp_options = random.choice(options)
  return comp_options

def is_only_letters(user_opt):
  for letter in user_opt:
      if (
          letter
          not in "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
      ):
          return False
  return True

def introduction():
  print("""
  Welcome to Rock Paper Scissors!!!
You'll be playing against a robot; enter either rock, paper, or scissors. Good luck!
  """)

def play_game():
  while True:

    rounds = input("how many rounds would you like? enter a #: ")
    rounds = int(rounds)
    round_counter = 1
    com_score = 0
    user_score = 0


    while round_counter <= rounds:

      com_choice = get_computer_choice()
      print("-----------------------")
      guess = input("pick: rock, paper, or scissors: ").strip().lower()

      if not is_only_letters(guess):
        print("please enter only letters (a-z).")
        continue

      if not guess == "rock" "paper" "scissors":
        print("please enter either rock, paper, or scissors")

      if com_choice == guess:
        print("---------")
        print(f"i pick {com_choice}")
        print("tie")
        round_counter += 1
      elif com_choice == 'paper' and guess == 'rock':
        print("---------")
        print(f"i pick {com_choice}")
        print("you lost")
        round_counter += 1
        com_score += 1
      elif com_choice == 'scissors' and guess == 'paper':
        print("---------")
        print(f"i pick {com_choice}")
        print("you lost")
        round_counter += 1
        com_score += 1
      elif com_choice == 'rock' and guess == 'scissors':
        print("---------")
        print(f"i pick {com_choice}")
        print("you lost")
        round_counter += 1
        com_score += 1
      elif com_choice == 'rock' and guess == 'paper':
        print("---------")
        print(f"i pick {com_choice}")
        print("you win")
        round_counter += 1
        user_score += 1
      elif com_choice == 'paper' and guess == 'scissors':
        print("---------")
        print(f"i pick {com_choice}")
        print("you win")
        round_counter += 1
        user_score += 1
      elif com_choice == 'scissors' and guess == 'rock':
        print("---------")
        print(f"i pick {com_choice}")
        print("you win")
        round_counter += 1
        user_score += 1

    print(f"your score is {user_score}, and my score is {com_score}!")
    break


introduction()
while True:
  play_game()
  print("do yo want to play again? yes/no")
  if not input().lower().startswith("y"):
    print("play again soon!")
    break
