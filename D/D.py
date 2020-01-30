# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D\D_input.txt', 'r', encoding="utf-8")
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
N, W = [int(item) for item in input().split()]
item = [[int(item) for item in input().split()] for _ in range(N)]

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for w in range(W+1):
        if 0 <= w - item[i][0]:
            dp[i+1][w] = max(dp[i][w], dp[i][w - item[i][0]] + item[i][1])
        else:
            dp[i+1][w] = dp[i][w]
print(dp[N][W])
