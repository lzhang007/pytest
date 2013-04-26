#!/usr/bin/python
#Filename:ifstat.py

number=23
guess=raw_input("type a integer:")
if guess == number:
    print'great,you guess it'
elif guess > number:
    print'no,it little lower than number'
else:
    print'no,it little big than number'
print'done'
