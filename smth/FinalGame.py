from smth.Game1 import Robot
from smth.Game2 import Human
from smth.Game import CompetitiveGame
from smth.RegistrationCode import Registration
from smth.Sign_InCode import SignIn

a = False
print("Hello player!")
b = int(input("SignIn (Press 1)" + "\n" + "Registration (Press 2)" + "\n"))
while a == False:
    if b == 1:
        login = SignIn(); a = True
    elif b == 2:
        Registration(); login = SignIn(); a = True
    else: print("You can only press 1 or 2 buttons! Try again."); b = int(input("SignIn (Press 1)" + "\n" + "Registration (Press 2)" + "\n"))
a = False
while a == False:
    print("Choose the game type:" + "\n" + "1. You guess the number (Press 1)" + "\n" + "2. Robot guess the number (Press 2)" + "\n" + "3. Competitive (Press 3)")
    gametype = int(input())
    if gametype == 1:
        Human(); a = True
    elif gametype == 2:
        Robot(login); a = True
    elif gametype == 3:
        CompetitiveGame(); a = True
    else: print("You can only press 1, 2 or 3! Try again.")
# reg = open(name, "r")
