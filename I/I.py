# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\I\input.txt', 'r', encoding="utf-8")
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
import numpy as np

N = int(input())
p0_list = np.array([float(item) for item in input().split()])
p1_list = 1 - p0_list


dp = [[[1.] + [0.0]*N] for _ in range(N+1)] 
dp[0] = [1.] * (N+1)
print(dp)

res = 0.0

#漸化式を考える
for i in range(N):
    for j in range(N):
        dp[i+1][j] = dp[i][j] * p1_list[i]
        dp[i][j+1] = dp[i][j] * p0_list[j] 

print(dp)
print(res)

    

