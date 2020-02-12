# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\H\input.txt', 'r', encoding="utf-8")
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

H, W = [int(item) for item in input().split()]

grid = np.array([[0] + [item for item in input()] for _ in range(H)])

dp = np.zeros((H+1, W+1), dtype='int32')
max_num = 10**9 +7

def main():
    dp[0,1] = 1

    for i in range(H):
        print(np.where(grid[i] != '#', dp[i], 0))
        dp[i+1] = np.where(grid[i] != '#', dp[i], 0)
        np.add.accumulate(dp[i+1], out=dp[i+1])





    print(dp)
    print(dp[H,W])

if __name__ == "__main__":
    main()

