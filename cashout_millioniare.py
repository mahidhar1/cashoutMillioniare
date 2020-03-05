# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:01:50 2020

@author: Mahidhar
"""

# -*- coding: utf-8 -*-
"""
 --------------- RUN THE REPL IN A NEW WINDOW ------------ 
 
"""

import sys
#import numpy as np
import random
import time

MIN_CASHOUT = 1000000
Bets = {
        "x2": { 
                'description': {"LO": "0 - 299" , "HI": "700 - 999"}
              },
       "x5": { 
               'description': {"LO" : "0 - 199",  "HI": "800 - 999" }
             },
       "x10": {
               'description': {"LO" : "0 - 99", "HI": "900 - 999"}
              }
        }


def game_instructions():
    print("You make cautious decision on staking your tickets on bets")
    time.sleep(1)
    print("You have three choices for making bets. Stake your tickets wisely to win.")
    time.sleep(1)
    print("x2 doubles yours tickets, x5 increases your stakes five times, x10 gives a chance to make your tickets at stake ten fold!")
    time.sleep(1)
    print("Each ticket cost $1000. But you just pay $10 for each ticket and buy 100 tickets to start the game.")
    time.sleep(1)
    print("That costs just $10 x 100 = $1000.")
    time.sleep(1)
    print("However, once the game starts you cannot exit the game unless you have made at_least 1000 tickets or a cash of a million $%d" %MIN_CASHOUT)
    time.sleep(1)
    print("More tickets you won through stakes the more money you make.")
    time.sleep(1)
    start_game = input("Would you like to pay $1000 to start the game.[y]/n: ")
    return start_game
    

class Game(object):
    def __init__(self):
        self.tickets = 100
        self.cash = self.tickets* 1000
        self.won_x2 = 0
        self.won_x5 = 0
        self.won_x10 = 0
        #self.tickets_won = 0
        self.won = {"x2": self.won_x2, "x5": self.won_x5, "x10": self.won_x10}
        self.status = {"Tickets": self.tickets, "Cash": self.cash, "Won": sum(self.won.values()) }
       
    def roll(self):
        #num_x2 = random.choice([random.randint(0, 299), random.randint(700, 999)])
        #num_x5 = random.choice([random.randint(0, 199), random.randint(800, 999)])
        #num_x10 = random.choice([random.randint(0, 99), random.randint(900, 999)])
        #print(num_x2, num_x5, num_x10)
        num_x2 = random.randint(0, 1000)
        num_x5 =  random.randint(0, 1000)
        num_x10 = random.randint(0, 1000)
        n0, n1, n2 = 0, 0, 0
        print("")
        for iter1 in range(1, 1000):
            n0 = {True: n0, False: iter1}[iter1>=num_x2]
            n1 = {True: n1, False: iter1}[iter1>=num_x5]
            n2 = {True: n2, False: iter1}[iter1>=num_x10]
            time.sleep(0.01)
            n0, n1, n2 = str(n0).center(40, " "), str(n1).center(40, " "), str(n2).center(40, " ")
            print('\r|%s|%s|%s|'%(n0, n1, n2), end=" ")
            #sys.stdout.write( '\r|%s|%s|%s|'%(n0, n1, n2) )
            #sys.stdout.flush()
        print("")
        return n0, n1, n2
        
        
    def current_status(self):
        print(''.join(["|"] + [k.center(40, " ") + '|' for k in self.status.keys()]))
        print(''.join(["|"] + [str(v).center(40, " ") + '|' for v in self.status.values()]))
        
    def update_status(self):
        self.status['Tickets'] = self.tickets
        self.status['Cash'] = self.cash
        self.status['Won'] = sum(self.won.values())
     
    def hi_or_lo(self):
        print("")
        print("How would you like to place your bets: ")
        inp1 = list()
        for k in Bets.keys():
            print("Type HI/LO for %s" %k)
            inp1.append( input("> ").upper() )
    
        return inp1    
        
    def how_many_tickets(self):
        print("")
        print("How many tickets: ")
        inp2 = list()
        for k in Bets.keys():
            print("At stake for %s" %k)
            inp2.append( input("> ") )
            
        return inp2
    
    def welcome_message(self):
        print("Welcome to the CASHOUT game.")
        skip_instructions = input('Skip Instructions [y]/n: ')
        if skip_instructions == 'n':
            start_game = game_instructions()
        else:
            start_game = input("You have to buy 100 tickets for $10 each to start the game. Would you like pay $1000 to start [y]/n: ")
        
        if start_game == 'y':

             for i in range(501):
                 sys.stdout.write(   ("\r Loading ... [%d]%%" %(100*i/500) ).center(120, " ")   )
                 sys.stdout.flush()
                 time.sleep(0.005)

             print("")
             self.start()
        elif start_game == 'n':
            print("")
            print("Relax! you are not paying actual money from your credit card. ")
            time.sleep(1)
            start_game1 = input("Would you like to start. [y]/n: ")
            if start_game1 == 'y':

                 for i in range(501):
                     sys.stdout.write(   ("\r Loading ... [%d]%%" %(100*i/500) ).center(120, " ")   )
                     sys.stdout.flush()
                     time.sleep(0.005)

                 print("")
                 self.start()
            else: 
                print("Goodbye... Come back again to try.")
        
     
    def start(self):
        
        while self.tickets > 10:
            self.current_status()
            print("\n"*2)
            print(''.join(['|'] + ['Tickets at Stake'.center(40, " ") + '|' for k in Bets.keys()]))
            print(''.join(['|'] + [k.center(40, " ") + '|' for k in Bets.keys()]))
            print(''.join(['|'] + [(Bets[k]['description']['LO'].ljust(15, " ") + Bets[k]['description']['HI'].rjust(15, " ")).center(40, " ") + '|' for k in Bets.keys()]))
            print(''.join(['|'] + [('LO'.ljust(15, " ") + 'HI'.rjust(15, " ")).center(40, " ") + "|" for k in Bets.keys()]))
            #print([(Bets[k]['description']['LO'] + '\t' + Bets[k]['description']['HI']).center(40, " ") for k in Bets.keys()])
            print("\n"*2)
            
            while True:
                try: 
                    inp1 = self.hi_or_lo()
                    if (inp1[0] not in ['HI', 'LO'])  or (inp1[1] not in ['HI', 'LO']) or (inp1[2] not in ['HI', 'LO']):
                        raise TypeError   
                    else: 
                        break
                except: 
                    print("Invalid Input !!! Please type HI or LO for each bet")
                    
            
            
            while True:
                try:
                   inp2 = self.how_many_tickets() 
                   inp2 = [int(s) for s in inp2]
                   try: 
                       if inp2[0] + inp2[1] + inp2[2] > self.tickets:
                           raise TypeError
                       else: 
                           break
                   except:
                       print("You only have %d tickets" %self.tickets)            
                except: 
                    print("Invalid Input !!! Please type integer values for the number of tickets")
            
            print("\n")
            print(''.join(['|'] + [k.center(40, " ") + '|' for k in Bets.keys()]))
            print(   ''.join( ["|"] + [('Tickets at Stake: '+ str(iter1)).center(40, " ") + "|" for iter1 in inp2] )   )
            print(   ''.join( ["|"] + [('Your bet: '+ str(iter1)).center(40, " ") + "|" for iter1 in inp1] )   )
            print(''.join(['|'] + [(Bets[k]['description']['LO'].ljust(15, " ") + Bets[k]['description']['HI'].rjust(15, " ")).center(40, " ") + '|' for k in Bets.keys()]))
            print(''.join(['|'] + [('LO'.ljust(15, " ") + 'HI'.rjust(15, " ")).center(40, " ") + "|" for k in Bets.keys()]))
            self.tickets = self.tickets - inp2[0] - inp2[1] - inp2[2]
            print("\n")
            print(("tickets left: %d" %self.tickets).center(120, " ")) 
            
            n0, n1, n2 = self.roll()
            #print(n0, n1, n2)
            roll_x2 = int(n0) in {'LO': range(0, 300), "HI": range(700, 1000)}[inp1[0]] 
            roll_x5 = int(n1) in {'LO': range(0, 200), "HI": range(800, 1000)}[inp1[1]] 
            roll_x10 = int(n2) in {'LO': range(0, 100), "HI": range(900, 1000)}[inp1[2]] 
            
            self.won_x2 = {True: inp2[0]*2, False: 0}[roll_x2]
            self.won_x5 = {True: inp2[1]*5, False: 0}[roll_x5]
            self.won_x10 = {True: inp2[2]*10, False: 0}[roll_x10]
            self.won.update({'x2': self.won_x2 , 'x5': self.won_x5 , 'x10': self.won_x10})
            
            
            w1 = "Won :" + str({True: inp2[0], False: 0}[roll_x2]) + 'x2'
            w2 = "Won :" + str({True: inp2[1], False: 0}[roll_x5]) + 'x5'
            w3 = "Won :" + str({True: inp2[2], False: 0}[roll_x10]) + 'x10'
            
            print( ''.join( ['|'] + [w.center(40, " ") + '|' for w in [w1, w2, w3] ]  )  )
            
            print("")
            
            self.tickets = self.tickets + sum(self.won.values())
            self.cash = self.tickets * 1000
            print( ("Tickets won: %d + %d + %d = %d" %(self.won['x2'], self.won['x5'], self.won['x10'], sum(self.won.values())) ).center(120, " ") )
            print( ("Tickets now: %d" %self.tickets).center(120, " ") )
            print( ("Cash : %d" %self.cash).center(120, " ") )
            self.update_status()
            print("")
            
            if self.tickets > 10: 
                y_or_n = input("Would you like to continue: [y/n]: ")
                if y_or_n == 'N' or y_or_n == 'n':
                    if self.cash > 1000*1000:
                        print( ("Cashout : %d" %self.cash).center(120, " ") )
                        print( ("Congratulation!").center(120, " ") )
                        print( ("You made money! Play again to make more").center(120, " ") )
                        break
                    else:
                        print("\n"*2)
                        print( ("You cannot exit with this cash of %d and %d number of tickets" %(self.cash, self.tickets)).center(120, " ") )
                        time.sleep(1)
                        print( ("!!! You have to make a million to exit !!!").center(120, " ") )
                        time.sleep(0.5)
                        print( ("Minimum CASHOUT: %d" %MIN_CASHOUT).center(120, " ") )
                        time.sleep(1)
                        print( ("You need to have atleast 1000 tickets to exit").center(120, " ") )
                        time.sleep(1)
                        print("\n"*2)

                        for i in range(501):
                             sys.stdout.write(   ("\r Reloading ... [%d]%%" %(100*i/500) ).center(120, " ")   )
                             sys.stdout.flush()
                             time.sleep(0.005)

                        print("")
                        print("")
                        continue
                else: 
                    continue
        
            else: 
                print( ("Exiting game...Insuffienct balance: Minimum Tickets should be 10").center(120, " ") )
                print( ("Play again to become a millionare!").center(120, " ") )
                print("\n"*5)
                break
        
                
            
            
            
       
        
        
if __name__ == '__main__':
    game = Game()
    game.welcome_message()
    
    
    
    
    
    
    
    
    
    
#==============================================================================
#                    if type(inp2[0]) != int or type(inp2[0]) != int or type(inp2[0]) != int:
#                        raise ValueError
#==============================================================================





#sys.stdout.write("Download progress: %d%%   \r" % (i) )
        #sys.stdout.flush()
        

#==============================================================================
#         while True:
#             instruction = input('> ')
# 
#             try:
#                 self.follow(instruction)
#             except RuntimeError as err:
#                 print(err)
#==============================================================================


