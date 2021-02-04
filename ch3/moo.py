#!/usr/bin/python3
import fire

def greet(people="KD"):
    print(f"{people} is good at b-ball")

def moo(ani="COW"):
    print(f"{ani} can MOOOOOO")
    
if __name__ == '__main__':
    fire.Fire()