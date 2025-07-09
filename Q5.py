import random
def generate():
    return [random.randint(100, 150) for _ in range(100)]
def mean(num):
    total = 0
    for num in num:
        total += num
    return total / length(num)
def median(num):
    num.sort()
    n = length(num)
    if n % 2 == 1:
        return num[n // 2]
    else:
        return (num[n // 2 - 1] + num[n // 2]) / 2
def mode(num):
    frequency = {}
    for num in num:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_freq = max(frequency.values())
    mode = [num for num, freq in frequency.items() if freq == max_freq]
    return mode
num_random = int(input("Enter the number of random numbers to generate"))
rand_numb = [random.randint(100, 150) for _ in range(num_random)]
mean_val = mean(rand_numb)
median_val = median(rand_numb)
mode_val = mode(rand_numb)
print(f"Mean: {mean_val}, Median: {median_val}, Mode: {mode_val}")