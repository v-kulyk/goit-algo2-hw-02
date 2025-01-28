from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}
    
    def helper(l):
        if l == 0:
            return (0, [])
        if l in memo:
            return memo[l]
        max_profit = 0
        best_cuts = []
        for j in range(1, l + 1):
            if j > len(prices):
                current_price = 0
            else:
                current_price = prices[j-1]
            profit, cuts = helper(l - j)
            total = current_price + profit
            if total > max_profit:
                max_profit = total
                best_cuts = [j] + cuts
        memo[l] = (max_profit, best_cuts)
        return (max_profit, best_cuts)
    
    max_profit, cuts = helper(length)
    number_of_cuts = len(cuts) - 1 if cuts else 0
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": number_of_cuts
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    n = length
    dp = [0] * (n + 1)
    cuts = [[] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        max_val = -1
        best_cut = []
        for j in range(1, i + 1):
            if j > len(prices):
                current_price = 0
            else:
                current_price = prices[j-1]
            remaining = i - j
            current_val = current_price + dp[remaining]
            if current_val > max_val:
                max_val = current_val
                best_cut = [j] + cuts[remaining]
            elif current_val == max_val:
                new_cut = [j] + cuts[remaining]
                if len(new_cut) > len(best_cut):
                    best_cut = new_cut
        dp[i] = max_val
        cuts[i] = best_cut
    
    number_of_cuts = len(cuts[n]) - 1 if cuts[n] else 0
    return {
        "max_profit": dp[n],
        "cuts": cuts[n],
        "number_of_cuts": number_of_cuts
    }

def run_tests():
    test_cases = [
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

if __name__ == "__main__":
    run_tests()