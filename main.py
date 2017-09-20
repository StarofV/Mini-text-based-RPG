#Some RPG game, made by (DogeSec™), enjoy :D.. In devolpment updated 9/20/17

from time import sleep

name = input("Enter your name\n")

def menu():
  print(f"Welcome to 1 minute RPG, glad to see you here, {name}.")
  
  print('''
[1]-Move on
[2]-Exit game
[3]-Credits
        ''')
  
  user_choice = input()
  if user_choice == '1':
    roads()
  elif user_choice == '2': #exit game if chosen
    exit(2) #exit without erros
  elif user_choice == '3':
    creds()

def roads(): #Road scene
  road_choice = input("there are 2 roads infront of you, which one will you choose? L/R")
  
  if road_choice.lower() in ('r'): # checking if user choice "R"
    right_road()
  
  elif road_choice.lower() in ('l'):
    print("You made it into level 2")
    left_road()
    
def Game_Over():
  print("You lost, you will be returning to menu in 5 seconds")
  sleep(5)
  menu()
  
def creds():
  print("By DogeSec™, and others to come?...")
  menu()
  
def left_road():
  welcome = input("Welcome to the next level, move on? Y/N\n")
  if welcome.lower() in ('y'):
    print("This is the end to the mini RPG (not even an RPG, lol)")
    sleep(2)
    creds()
  else: 
    print("Bye")
    sleep(3)
    creds()
    exit()
def right_road(): #The right road choice 
  print("Game Over\n") 
  Game_Over()
