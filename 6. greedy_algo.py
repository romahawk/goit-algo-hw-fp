def greedy_algorithm(items, budget):
    # Сортування елементів за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    chosen_items = []

    for item, details in sorted_items:
        if budget >= details['cost']:
            budget -= details['cost']
            total_calories += details['calories']
            chosen_items.append(item)

    return chosen_items, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
chosen_items, total_calories = greedy_algorithm(items, budget)
print("Обрані страви:", chosen_items)
print("Загальна кількість калорій:", total_calories)


def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[item]['cost'] for item in item_names]
    calories = [items[item]['calories'] for item in item_names]

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    chosen_items = []

    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(item_names[i - 1])
            w -= costs[i - 1]

    chosen_items.reverse()
    return chosen_items, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
chosen_items, total_calories = dynamic_programming(items, budget)
print("Обрані страви:", chosen_items)
print("Загальна кількість калорій:", total_calories)
