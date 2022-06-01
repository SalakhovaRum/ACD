def knapsack(cap, values, weights): #У нас есть 2 массива; В одном содержатся значения веса всех предметов (weights),
    # а в другом — их стоимость (values). Также нам дан рюкзак ограниченной вместимости (cap)
    items = []
    for i in range(len(values)):
        itemInfo = {
            'vpw': values[i] / weights[i],
            'weight': weights[i]
        }
        if len(items) == 0:
            items.append(itemInfo)
        else:
            k = 0
            while k < len(items) and items[k]['vpw'] > itemInfo['vpw']:
                k += 1
            items.insert(k, itemInfo)
    total = 0
    cap_left = cap
    for item in items:
        if cap_left - item['weight'] >= 0:
            total += item['weight'] * item['vpw']
            cap_left -= item['weight']
        elif cap_left > 0:
            total += item['vpw'] * cap_left
            cap_left = 0
    return total

cap = 60
values = [60, 100, 120]
weights = [20, 50, 30]
print(knapsack(cap, values, weights))