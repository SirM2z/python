# -*- coding: utf-8 -*-

from sys import exit
from random import randint
from leftroom import lroom
from rightroom import rroom

class Game():
    def __init__(self):
        self.died=[
                   "you died here,please restar.",
                   "I believe you can win next time."
                   ]
        self.success=["You win!Congratulation---*-*"]
        self.start="firstroom"
        self.roomnum=0
        
    def died(self):
        """when you died,it will be run"""
        print self.died
        exit(1)
        
    def play(self):
        next=self.start
        
        while True:
            print "\n-------------"
            room=getattr(self, next)
            next=room()
            
    def firstroom(self):
        print "Now you are in a room"
        print "There are two doors in the room"
        print "You should choose one"
        print "For example leftroom or rightroom"
        print "You will face differents things because of your differents choose"
        
        action=raw_input(">")
            
        if action=="leftroom":
            leftgame=lroom()
            return leftgame.l_play()
        elif action=="rightroom":
            rightgame=rroom()
            return rightgame.r_play()
            return""
        else:
            return "died"
        
    def lsuccess(self):
        self.roomnum+=1
        if self.roomnum==2:
            print self.success
        else:
            return "firstroom"
    def rsuccess(self):
        self.roomnum+=1
        if self.roomnum==2:
            print self.success
            exit(1)
        else:
            return "firstroom"
my_game=Game()
my_game.play()
            
    
