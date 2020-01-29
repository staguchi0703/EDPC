# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\template\input.txt', 'r', encoding="utf-8")
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
N = int(input())
hight_list = [int(item) for item in input().split()]


dp = [0 for i in range(N+1)]
dp[0] = hight_list[0] 

def rec(i):
    if dp[i] != 0:
        return dp[i]

    jump1 = abs(dp[i+2] - dp[i])
    jump2 = abs(dp[i+1] - dp[i])

    if jump1 > jump2:
        dp[i+2] = rec(i) + jump2
        return dp[i+2]
    else:
        dp[i+1] = rec(i) + jump1
        return dp[i+1]

print(rec(N))
    

    

