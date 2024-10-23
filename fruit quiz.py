import random
class Fruitquiz:
 def __init__(self):
        self.fruits={'apple':'red',
                'orange':'orange',
                'watermelon':'green',
                'banana':'yellow'}
 def quiz(self):

    while(True):
        fruits,colour=random.choice(list(self.fruits.items()))
        print("What is the colour of {}".format(fruits))
        user_answer=input()

        if (user_answer.lower()==colour):
          print("Correct answer")
        else:
          print("wrong answer")
        option=int(input("Enter 0 , if you want to play again otherwise enter 1:"))
print("Welocome to the fruit quiz")
fq=Fruitquiz()
fq.quiz()


