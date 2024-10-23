class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word + '( '+self.meaning+')'
flash=[]
print("Welcome to flash application")

while(True):
 word=input("Enter the word:")
 meaning=input("Enyter the meaning of the word: ")

 flash.append(flashcards(word,meaning))
 option=int(input("Enter 1 to end or 0 to add more information: "))

 if (option):
    break
print("\n Your flashcard:")
for i in flash:
   print(">",i)
