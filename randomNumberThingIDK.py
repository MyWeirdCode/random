#I am a beginner
import random

var = input("pick a number: ")
var2 = input("pick a number again: ")

def hello():
    print(random.randrange(int(var), int(var2)))
    
hello()