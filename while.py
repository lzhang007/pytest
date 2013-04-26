#!/usr/bin/python
#Filename:while.py

number=50
guess=int(raw_input("type a integer:"))
while guess != number:
    print 'error'
    guess=int(raw_input("type a integer:"))
print 'good'

