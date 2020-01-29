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
N = int(input())
hight_list = [int(item) for item in input().split()]


dp = [0 for i in range(N+1)]

dp[1] = abs(hight_list[1] - hight_list[0])

for i in range(2, N):
    jump1 = abs(hight_list[i] - hight_list[i-1])
    jump2 = abs(hight_list[i] - hight_list[i-2])

    dp[i] = min(dp[i-1] + jump1, dp[i-2] + jump2)


print(dp[N-1])
    