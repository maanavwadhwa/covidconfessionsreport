import numpy as np
import csv

#ChatGPT helped me with this JSD function.Thanks ChatGPT!
def jsd(distributions):
    # Create a set of all words in all distributions
    all_words = set()
    for dist in distributions.values():
        all_words.update(dist.keys())

    num_dists = len(distributions)

    eps = 0 
    # Compute the average distribution
    avg_dist = {}
    for word in all_words:
        prob_sum = 0.0
        for dist in distributions.values():
            if word in dist:
                prob_sum += dist[word]
        avg_dist[word] = prob_sum / num_dists

    # Compute the Kullback-Leibler divergence for each distribution
    kl_divs = []
    for dist in distributions.values():
        kl_div = 0.0
        for word, prob in dist.items():
            if word in avg_dist:
                kl_div += (prob + eps) * np.log2((prob + eps) / (avg_dist[word] + eps))
        kl_divs.append(kl_div)

    # Compute the Jensen-Shannon divergence
    jsd = 0.0
    for kl_div in kl_divs:
        jsd += kl_div / num_dists
    # jsd += np.log2(num_dists)
    jsd /= 2.0

    return jsd


monthly_counts_both = {
    1: 10767,
    2: 12645,
    3: 12899,
    4: 15463,
    5: 11512,
    6: 12341,
    7: 11282,
    8: 11379,
    9: 11545,
    10: 10071,
    11: 10554,
    12: 10885
}

monthly_counts_title = {
    1: 3016,
    2: 2951,
    3: 3159,
    4: 2992,
    5: 2942,
    6: 2834,
    7: 2954,
    8: 2944,
    9: 2928,
    10: 3004,
    11: 2746,
    12: 2827
}

monthly_counts_2019_title= {
    1: 3020,
    2: 3103,
    3: 2838,
    4: 2939,
    5: 3291,
    6: 2889,
    7: 2899,
    8: 2898,
    9: 3076,
    10: 2988,
    11: 2798,
    12: 2828
}

monthly_counts_2019_both= {
    1: 11650,
    2: 11081,
    3: 11332,
    4: 11538,
    5: 12527,
    6: 12166,
    7: 11862,
    8: 13620,
    9: 11283,
    10: 10604,
    11: 11917,
    12: 14558
}

amount = 500   #~20% of data
startMonth = 1
which = 'title'

#for 2019
words = dict()
year = 2019
monthly_counts = monthly_counts_2019_title
for month in range(startMonth, 13):
    with open(f"./{month}-{year}_{which}.csv", "r") as csvfile:
        all_lines = csvfile.readlines()[:amount]
        words[month] = [line.strip().split(',') for line in all_lines]
        csvfile.close()

probDistribution = dict()
for start in range(startMonth, 12): #2018, 2019, 2020, 2021
    probDistribution = dict()
    for month in range(start, start+2): #2018-2019, 2019-2020, 2020-2021, 2021-2022
        probDistribution[month] = dict()
        for w in words[month]:
            if len(w) == 2:
                key, value = w[0], w[1]
                probDistribution[month][key] = int(value)/monthly_counts[month]
    print(f'{start}-{start+1}:', jsd(probDistribution))

words = dict()
with open(f"./12-2019_{which}.csv", "r") as csvfile:
    all_lines = csvfile.readlines()[:amount]
    words[12] = [line.strip().split(',') for line in all_lines]
    csvfile.close()

with open(f"./1-2020_{which}.csv", "r") as csvfile:
    all_lines = csvfile.readlines()[:amount]
    words[1] = [line.strip().split(',') for line in all_lines]
    csvfile.close()

#For 12/2019 into 1/2020
probDistribution = dict()
probDistribution[12] = dict()
probDistribution[1] = dict()

for w in words[12]:
    if len(w) == 2:
        key, value = w[0], w[1]
        probDistribution[12][key] = int(value)/monthly_counts_2019_title[12]

for w in words[1]:
    if len(w) == 2:
        key, value = w[0], w[1]
        probDistribution[1][key] = int(value)/monthly_counts_title[1]


print('12-1', jsd(probDistribution))

#For 2020
words = dict()
year = 2020
monthly_counts = monthly_counts_title
for month in range(startMonth, 13):
    with open(f"./{month}-{year}_{which}.csv", "r") as csvfile:
        all_lines = csvfile.readlines()[:amount]
        words[month] = [line.strip().split(',') for line in all_lines]
        csvfile.close()

probDistribution = dict()
for start in range(startMonth, 12): #2018, 2019, 2020, 2021
    probDistribution = dict()
    for month in range(start, start+2): #2018-2019, 2019-2020, 2020-2021, 2021-2022
        probDistribution[month] = dict()
        for w in words[month]:
            if len(w) == 2:
                key, value = w[0], w[1]
                probDistribution[month][key] = int(value)/monthly_counts[month]
    print(f'{start}-{start+1}:', jsd(probDistribution))
