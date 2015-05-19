# -*- coding: utf-8 -*-

class rroom():
    def __init__(self):
        self.question={
                      "first":1,
                      "second":3,
                      "third":5
                      }
    
    def r_play(self):
        print "Now you should choose some numbers"
        while True:
            print "first:1 or 2"
            print self.question["first"]
            action=raw_input(">")
            if int(action)==self.question["first"]:
                print "Congratulation!,you win!---"
                break
            else:
                print "Unfortunately,You lose!---0.0"
        while True:
            print "second:3 or 4"
            action=raw_input(">")
            if int(action)==self.question["second"]:
                print "Congratulation!,you win!---"
                break
            else:
                print "Unfortunately,You lose!---0.0"
        while True:
            print "third:5 or 6"
            action=raw_input(">")
            if int(action)==self.question["third"]:
                print "Congratulation!,you win!---"
                return "rsuccess"
            else:
                print "Unfortunately,You lose!---0.0"