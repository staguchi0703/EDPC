# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\C\C_input.txt', 'r', encoding="utf-8")
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
    N = int(input())
    act = np.array([[int(item) for item in input().split()] for _ in range(N)])

    dp = np.zeros((2, 3), dtype='int64')
    zero_diag = np.ones((3, 3), dtype='int64') - np.eye(3, dtype='int64')
    print(zero_diag)
    for i in range(0,N):
        act_array = np.array([[act[i]]*3])*zero_diag
        dp[i%2 ^ 1] = #計算の方法を考えるこ
        # print(dp)
    print(np.max(dp))

main()


