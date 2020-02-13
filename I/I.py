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

dp = np.zeros((N+1, N+1), dtype='float')


dp[0, :] = 1
dp[:, 0] = 1

#掛けるで操作する
#

print(dp[0])

# for i in range(N):
    
#     dp[i+1] = dp[i] * p1_list
#     dp[i+1] =


    

