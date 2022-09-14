import random
import enchant
def funct(l1):
    l2=[]
    d=enchant.Dict("en_US")
    i=1
    marks=0
    while i<=5:
        s1=random.choice(l1)
        if(s1 not in l2):
            s2="".join(random.sample(s1,len(s1)))
            l2.append(s1)
            print("Arrange the letters to form a valid word")
            print(s2)
            c=input("enter your answer:")
            if(len(c)==len(s2) and sorted(c)==sorted(s2)):
                if(c==s1 or d.check(c)):
                    print("correct")
                    marks+=1
                    i=i+1
                else:
                    marks-=1
                    i=i+1
                    print("wrong")
            else:
                print("wrong")
                marks-=1
                i=i+1
        else:
            continue
    return marks
                
                
            
        
        
    
    
print("WELCOME TO THE INTERFACE")
print("THIS IS WORD PUZZLE GAME")
print("""In this game user will be give some collection of letters
      in random order and the user have to enter the correct forming
      through that collection of letters,If the is correct then user will
      be marked 1 point else wrong will be printed and user will be given -1
      for point for that word.In each game there will be 5 words which will
      be shown to user one by one and user have to answer""")
a=input("do you want to play the game[y/n]:")
while a:
    if a=='y':
        l=['leg','hello','python','java','pizza','hero','phone','laptop',
           'computer','coaching','time','minute','second','resume']
        random.shuffle(l)
        b=funct(l)
        print("Net Score is",b)
    print("do you want to play again[y/n]")
    e=input()
    if(e=='y'):
        continue
    else:
        break
print("Thanks for playing the game")
        
        
        



