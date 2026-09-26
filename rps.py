
import random
choice = input()
comp = ["rock", "paper", "scissors"]
if choice == "rock":
  ran = random.choice(comp)
  print(ran)
if choice == "scissors":
  ran = random.choice(comp)
  print(ran)
if choice == "paper":
  ran = random.choice(comp)
  print(ran)

if choice == "rock" and ran == "rock":
  print("Tie.")
if choice == "paper" and ran == "paper":
  print("Tie.")
if choice == "scissors" and ran == "scissors":
  print("Tie.")
if choice == "rock" and ran == "paper":
  print("Computer won.")
if choice == "rock" and ran == "scissors":
  print("You Won!")
if choice == "paper" and ran == "rock":
  print("You won.")
if choice == "paper" and ran == "scissors":
  print("Computer won.")
if choice == "scissors" and ran == "paper":
  print("You Won!")
if choice == "scissors" and ran == "rock":
  print("Computer won.")
