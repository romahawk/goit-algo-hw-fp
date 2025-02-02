import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        dice_sum = roll_dice()
        sums_count[dice_sum] += 1
        
    probabilities = {sum_: count / num_rolls for sum_, count in sums_count.items()}
    
    return probabilities

def plot_probabilities(probabilities, title):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Сума')
    plt.ylabel('Імовірність')
    plt.title(title)
    plt.xticks(sums)
    plt.grid(True)
    plt.show()

# Симуляція з великою кількістю кидків кубиків
num_rolls = 100000
monte_carlo_probabilities = monte_carlo_simulation(num_rolls)

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Побудова графіків
plot_probabilities(monte_carlo_probabilities, 'Ймовірності за методом Монте-Карло')
plot_probabilities(analytical_probabilities, 'Аналітичні ймовірності')

# Порівняння результатів
print("Ймовірності за методом Монте-Карло:")
for sum_, prob in monte_carlo_probabilities.items():
    print(f"Сума {sum_}: {prob:.4f}")

print("\nАналітичні ймовірності:")
for sum_, prob in analytical_probabilities.items():
    print(f"Сума {sum_}: {prob:.4f}")
