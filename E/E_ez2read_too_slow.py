# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\E\E_input.txt', 'r', encoding="utf-8")
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

N, W = [int(item) for item in input().split()]
item = np.array([[int(item) for item in input().split()] for _ in range(N)])


dp = np.full((N+1, 10**5 + 1), 10**12+1)
dp[0][0] = 0

for i in range(N):
    for j in range(10**5 + 1):
        w, v = item[i]
        if j >= v:
            dp[i+1][j] = min(dp[i][j], dp[i][j - v] + w)
        else:
            dp[i+1][j] = dp[i][j]

print(np.where(dp[N] <= W)[0][-1])

