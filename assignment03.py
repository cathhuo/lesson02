# -*- encoding:utf-8 -*-

"""
1."梯度下降"中,什么是梯度,什么是下降?
2.与以前的方法比,第三梯度下降法的优点是什么?
3.用几个简单的词描述,什么是机器学习
"""
from collections import defaultdict

from functools import wraps




if __name__ == "__main__":
    original_price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 35]
    price = defaultdict(int)
    for i, p in enumerate(original_price):
        price[i + 1] = p


    def memo(f):
        already_computed = {}
        def _wrap(n):
            if n in already_computed:
                return already_computed[n]
            else:
                already_computed[n]=f(n)
                return already_computed[n]
        return _wrap

    @memo
    def r(n):
        return max(
            [price[n]] + [r(i) + r(n - i) for i in range(1, n)]
        )
    print(r(89))














