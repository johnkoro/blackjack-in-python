import random
import itertools
import Tkinter
cards=[i for i in range(1,11)]
suit=["C","S","H","D"]
figures=["J","Q","K"]
cards=cards+figures
DECK=itertools.product(cards,suit) 
DECK=list(DECK)

DECK=[]
for i in suit:
        for j in cards:
                DECK.append([i,j])
random.shuffle(DECK)
def get_card_value(c):
        if c[1] in figures:
                return 10
        else:
                return c[1]
                
def sum_cards(LST):
        score=0
        for c in LST:
                score+=get_card_value(c)
        return score
def print_hand(l):
        txt=""
        for c in l:
                txt+=str(c[0])+str(c[1])+","
        txt=txt[:-1]
        return txt
score = 5000
print "Your score is: ", score
while (score>0):
 user_hand=[]
 comp_hand=[]
 for i in range(2):
        user_hand+=[DECK.pop()]
        comp_hand+=[DECK.pop()]
 print "your hand: ",print_hand(user_hand)
 user_score=sum_cards(user_hand)
 cards2draw=raw_input("Do you want to draw? Press Y to continue and N for no ")
 while (cards2draw=="Y"):
  user_hand+=[DECK.pop()]
  user_score=sum_cards(user_hand)
  print "your hand: ",print_hand(user_hand),user_score
  cards2draw=raw_input("Do you want to draw? Press Y to continue and N for no ")
 print "your hand: ",print_hand(user_hand),user_score
 if (user_score<=21):
  comp_score=sum_cards(comp_hand)
  while (comp_score<=16):
     comp_hand+=[DECK.pop()]
     comp_score=sum_cards(comp_hand)
  if (user_score==11):
                if (comp_score==21):
                        print "You Lose!!", "CPU's score: ", comp_score
                else: 
                                        print "You Win!!", "CPU's score: ", comp_score
                                        score=score+500
                score=score-500
  else :
                if (comp_score<=21) and (user_score<=21):
                     if (comp_score>=user_score):
                        print "You Lose!!", "CPU's score: ", comp_score
                        score=score-500
                     else : 
                                            print "You Win!!", "CPU's score: ", comp_score 
                                            score=score+500 
                else : 
                                      print "You Win!!", "CPU's score: ", comp_score
                                      score=score+500
 else :
         print "You Lose!!", "CPU's score: ", user_score
         score=score-500

 print "Your score: ", score
 DECK=DECK+user_hand+comp_hand
 random.shuffle(DECK)
 if (score<=0):
     from Tkinter import *
     msg = Message(text="GAME OVER!!")
     msg.config(bg='red', font=('times', 16, 'italic'))
     msg.pack()
     mainloop()
 
 
        
