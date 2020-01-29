# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\B\B_input.txt', 'r', encoding="utf-8")
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
N, K = [int(item) for item in input().split()]
h =[0] + [int(item) for item in input().split()]

dp = [0 for _ in range(N+1)]

for i in range(2, N+1):
    for k in range(1, K+1):
        if i - k >= 1:
            if dp[i] != 0:
                dp[i] = min(dp[i-k] + abs(h[i] - h[i-k]), dp[i])
            else:
                dp[i] = dp[i-k] + abs(h[i] - h[i-k])
print(dp[N])
