# δ₂（2次構造差）を計算する
#
# 入力:
#   before: 1次元の数値列（τより前の群）
#   after : 1次元の数値列（τ以後の群）
# 出力:
#   float（δ₂ = |var(before) - var(after)|）
#
# 制約:
#   中心化は2群まとめて全体平均で行う（事例3と同一）
#   分散は標本分散（ddof=1）
#   この関数は τ も prefix も知らない（分割済みの群を受け取るだけ）

import numpy as np

def delta2(x_before, x_after):
    # 中心化（全体平均）
    mu = np.concatenate([x_before, x_after]).mean()
    x_before_c = x_before - mu
    x_after_c = x_after - mu

    # 標本分散（ddof=1）: SSE / (n-1)
    var_before = (x_before_c @ x_before_c) / (len(x_before_c) - 1)
    var_after = (x_after_c @ x_after_c) / (len(x_after_c) - 1)

    return abs(var_before - var_after)

