# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\F\F_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
import sys
input = sys.stdin.readline
import numpy as np

s = input()
t = input()

num_s = len(s)
num_t = len(t)

dp = np.zeros((num_s + 1, num_t + 1), dtype='int64')


for i in range(num_s):
    for j in range(num_t):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j], dp[i][j+1])
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j])
    print(dp[i])

print(np.max(dp))