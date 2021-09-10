from itemlist import *
import random
import time

class Bmagic:


    def select(self):    # allows user to choose an object in the room

        print('**Welcome to the BLACK MAGIC game!**')
        print("PLAYER 1")
        self = input('Please choose an object in the room:  ')
        print(), time.sleep(1),print(), time.sleep(1),print(),print(),print(),print(),print(),print(),print(),print(),print()
        print('I now want to welcome our Black Magic Guru....'),print(),print(),print(),print(),print(),print()
        time.sleep(2)
        return self


    def appendlist(self,l): # this will take the user input (self.n) and add it to the item list(l)
        self.n =[game1.select(),'x']
        l.append(self.n) # adds the users input to the end of the item list
        return l

    def checklist(self,l):
        for i in range(len(l)-1):
            if l[i][0] == l[len(l)-1][0]:
                l.pop(i)
                break
            else:
                pass
        return l


    def guess(self,l): #pick a random item from the list, ask "is this the item?". if the player says "no", revise list then try again.
        self.comguess = random.randint(0,len(l)-2)
        print('Oh Black Magic Guru! Is this the item Player 1 thought of?:  ', l[self.comguess][0])
        self.ans = input('(y/n) ')
        time.sleep(2)
        if self.ans == 'y':
            time.sleep(3)
            print('CORRECT!!')
            print('And that is how it\'s done!')
        else:
            time.sleep(1)
            x=0
            bguess = self.comguess
            game1.isblack(l,bguess)
            if x ==0:
                global magwords
                print()
                time.sleep(.5)
                print(wrong[random.randint(0, len(wrong) - 1)])
                print(), print(), print(), print(), print(), print()
                time.sleep(3)
                print(magwords[random.randint(0,len(magwords)-1)])
                print(),print(),print(),print(),print()



                time.sleep(1)
                game1.revlist(l,bguess)
                pass
        pass

    def revlist(self,l,bguess):
        l.pop(bguess)
        game1.guess(items)


        pass

    def isblack(self,l,bguess):
        global wrong
        if l[bguess][1] == 'black':
            print()
            time.sleep(.5)
            print(wrong[random.randint(0, len(wrong) - 1)])
            print(), print(), print(), print(), print(), print()
            time.sleep(3)
            print(magwords[random.randint(0, len(magwords) - 1)])
            print(), print(), print(), print(), print()
            print('Oh Black Magic Guru! Is this the item Player 1 thought of?:  ', l[-1][0])
            x = input('(y/n) ')
            if x != 'y':
                print('The Spirits are telling me there is a liar in our midst...')
                print('Re-run the game and play again, if you\'re feeling truthful..')
                exit()
            else:
                print('And that is how Black Magic is done!'),print()
                print('Restart program to play again!')
                exit()
        else:pass

game1 = Bmagic()
game1.appendlist(items)
game1.checklist(items)
game1.guess(items)

y=1