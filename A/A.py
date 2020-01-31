# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\A\A_input.txt', 'r', encoding="utf-8")
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

N = int(input())
hight_list = np.array([int(item) for item in input().split()])

dp = np.full(N, hight_list.sum(), dtype='int64')
dp[0] = 0
dp[1] = abs(hight_list[1] - hight_list[0])

for i in range(2, N):
    cost1 = abs(hight_list[i-1] - hight_list[i])
    cost2 = abs(hight_list[i-2] - hight_list[i])
    dp[i] = min(dp[i-1] + cost1, dp[i-2] + cost2)
    # print(dp)

print(np.max(dp))
    