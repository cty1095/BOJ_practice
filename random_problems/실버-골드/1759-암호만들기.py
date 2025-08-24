import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

L , C = map(int,input().split())

candi = list(input().split())
candi.sort()
# print(candi)

def backtrcking(current_idx,depth,tmp):
    if depth == L:
        vowels= 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        cnt_vowel = 0
        cnt_consonant = 0
        for letter in tmp:
            if letter in vowels:
                cnt_vowel += 1
            elif letter in consonants:
                cnt_consonant += 1
        if cnt_vowel >= 1 and cnt_consonant >=2:
            print(''.join(tmp))
        return
    if current_idx == C:
        return
    
    #-------------------------------
    tmp.append(candi[current_idx])
    backtrcking(current_idx+1,depth+1,tmp)
    tmp.pop()
    backtrcking(current_idx+1,depth,tmp)

backtrcking(0,0,[])