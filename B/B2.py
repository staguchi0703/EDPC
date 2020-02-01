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
import sys
input = sys.stdin.readline
import numpy as np

def main():
    N, K = [int(item) for item in input().split()]
    h =np.array([int(item) for item in input().split()])
    dp = np.full(N+K, 10**10+1, dtype='int64')
    dp[0] = 0

    for i in range(1, N):
        max1 = min(N, i+K)
        cost = abs(h[i:max1] - h[i-1])
        dp[i:max1] = np.minimum(dp[i:max1], dp[i-1] + cost)

    print(dp[N-1])

main()
