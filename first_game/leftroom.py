# -*- coding: utf-8 -*-

from random import randint

class lroom():
    def __init__(self):
        self.booshand=["two","five","ten"]
    
    def l_play(self):
        print "Now you must play a game with Boss"
        print "I believe you have been played"
        print "The name of game is ---Rock Paper Scissors---"
        print "You can choose two-rock or paper-five or scissors"
        
        while True:
            print "The boos has been choose,please---"
            bossaction=self.booshand[randint(0,len(self.booshand)-1)]
            action=raw_input(">")
            if action=="two":
                if bossaction=="two":
                    print "This draw,please restart---0.0"
                elif bossaction=="five":
                    print "Congratulation!,you win!---"
                    return "lsuccess"
                else:
                    print "Unfortunately,You lose!---0.0"
            elif action=="five":
                if bossaction=="five":
                    print "This draw,please restart---0.0"
                elif bossaction=="ten":
                    print "Congratulation!,you win!---"
                    return "lsuccess"
                else:
                    print "Unfortunately,You lose!---0.0"
            else:
                if bossaction=="ten":
                    print "This draw,please restart---0.0"
                elif bossaction=="two":
                    print "Congratulation!,you win!---"
                    return "lsuccess"
                else:
                    print "Unfortunately,You lose!---0.0"