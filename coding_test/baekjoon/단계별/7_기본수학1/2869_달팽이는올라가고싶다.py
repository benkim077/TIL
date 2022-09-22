from math import ceil
import sys
sys.stdin = open('input.txt')

A, B, V = map(int, input().split())

print(ceil((V - B) / (A - B)))