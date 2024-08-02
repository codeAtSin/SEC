# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 23:14:05 2019

@author: BeastUnleashed
"""
##from __future__ import print_function

def hello():
    print("Hello there!")
    text = "X-DSPAM-Confidence:    0.8475"
    spos=text.find(':')
    #epos=text.find('5')
    print(float(text[spos+1:].strip()))
    lst = list()
    #for line in fh:
    words=text.split()
    for word in words:
        if word not in lst:
            lst.append(word)
    print(lst)
    carry=format(6, 'b')
    print(carry[0])

    # call the program
hello()