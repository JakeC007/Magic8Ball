import random
def main():
  #ascii art
  ball_img = "  ._---_. \n /   _   \ \n |  (8)  | \n \   ^   / \n  '-...-'"
  evil_img = "      ,  ,  , , ,\n     <(__)> | | |\n     | \/ | \_|_/ \n     \^  ^/   | \n     /\--/\  / \n    /  \/  \/ |"
  print("Welcome to the Magic 8 Ball." )
  print(ball_img)
  number = random.randint(1, 8)
  print("Your number is %d" %(number))
  if number == 6:
    print(evil_img)

main()
