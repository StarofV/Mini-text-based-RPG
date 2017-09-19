#Some RPG game, made by (DogeSec™), enjoy :D 

name = input("Enter your name\n")

def menu():
  print(f"Welcome to 1 minute RPG, glad to see you here, {name}.")
  
  print('''
[1]-Move on
[2]-Exit game
[3]-Credits
        ''')
  
  user_choice = input()
  if user_choice == '1': #continue into the story
    roads()
  elif user_choice == '2': #exit game if chosen
    exit(2) #exit without erros
  elif user_choice == '3':
    creds()

def roads(): #Road scene
  road_choice = input("there are 2 roads infront of you, which one will you choose? L/R")
  if road_choice.lower() in ('r'): # checking if user choice "R"
    right_road()

def creds():
  print("By DogeSec™, and others to come") 
  menu()


def right_road(): #The right road choice 
  print("You lost") #In devolpment, will be changed 

menu()
