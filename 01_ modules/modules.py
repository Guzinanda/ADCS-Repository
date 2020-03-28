'''
@ TITLE:    modules.py
@ DATE:     25-03-2020
@ AUTHOR:   Fernanda Guzman Gomez
@ PROBLEM:  Exercise 08
'''

import math

sample1 = [11, 11, 14, 17, 25, 28, 43, 43]
''' Sample (data) to test: Sample Mean, Standard Deviation and Median '''
sample2 = [11, 14, 25, 28, 43, 17, 11]
''' Sample (data) to test: Sample Mean, Standard Deviation and Median '''


''' Sample Mean '''
def sample_mean(sample):
    total_sum = 0
    sample_quantities = 0
    for i in sample:
        total_sum = total_sum + i
        sample_quantities = sample_quantities + 1
    prom = total_sum / sample_quantities
    return prom


''' Standard Deviation ''' 
def sample_standard_deviation(samples):
    div = 0
    for i in samples:
        div = div + math.pow((i - sample_mean(samples)), 2)
    divisor = len(samples) - 1
    med = div / divisor
    return med


''' Median ''' 
def median(samples):
    samples.sort()
    if len(samples) % 2 == 0:
        sum_sample = samples[len(samples) // 2] + samples[len(samples) // 2 - 1]
        med_even = sum_sample / 2
        return med_even
    else:
        med_odd = samples[len(samples) // 2]
        return med_odd


''' N-Percentile ''' 
def n_percentile(given_sample, given_n):
    given_sample.sort()
    below_n = 0
    for i in given_sample:
        if given_n <= i:
            continue
        else:
            below_n = below_n + 1
    percentile_n = (below_n / len(given_sample)) * 100
    return percentile_n


''' N-Quartile ''' 
def n_quartile(given_sample, given_n):
    given_sample.sort()
    percentage_q = n_percentile(given_sample, given_n)
    if percentage_q <= 25:
        return "Quartile Q1"
    elif (percentage_q > 25) and (percentage_q <= 50):
        return "Quartile -Q2"
    elif (percentage_q > 50) and (percentage_q <= 75):
        return "Quartile +Q2"
    else:
        return "Quartile Q3"


if __name__ == "__main__":

    print("\n")
    print("////////////////////////////////////////////////")
    print("SAMPLE NOº 1")
    print(f"Original Sample: {sample1}")
    print(f"Sorted Sample: {sorted(sample1)}")
    print(f"Mean: {sample_mean(sample1)}")
    print(f"Standard Deviation: {sample_standard_deviation(sample1)}")
    print(f"Median: {median(sample1)}")
    print(f"Percentile: {n_percentile(sample1, 11)}")
    print(f"Quartile: {n_quartile(sample1, 11)}")

    print("\n")
    print("////////////////////////////////////////////////")
    print("SAMPLE NOº 2")
    print(f"Original Sample: {sample1}")
    print(f"Sorted Sample: {sorted(sample1)}")
    print(f"Mean: {sample_mean(sample1)}")
    print(f"Standard Deviation: {sample_standard_deviation(sample1)}")
    print(f"Median: {median(sample1)}")
    print(f"Percentile: {n_percentile(sample1, 17)}")
    print(f"Quartile: {n_quartile(sample1, 17)}")

    print("\n")
    print("////////////////////////////////////////////////")
    print("SAMPLE NOº 3")
    print(f"Original Sample: {sample2}")
    print(f"Sorted Sample: {sorted(sample2)}")
    print(f"Mean: {sample_mean(sample2)}")
    print(f"Standard Deviation: {sample_standard_deviation(sample2)}")
    print(f"Median: {median(sample2)}")
    print(f"Percentile: {n_percentile(sample2, 28)}")
    print(f"Quartile: {n_quartile(sample2, 28)}")


    print("\n")
    print("////////////////////////////////////////////////")
    print("SAMPLE NOº 4")
    print(f"Original Sample: {sample2}")
    print(f"Sorted Sample: {sorted(sample2)}")
    print(f"Mean: {sample_mean(sample2)}")
    print(f"Standard Deviation: {sample_standard_deviation(sample2)}")
    print(f"Median: {median(sample2)}")
    print(f"Percentile: {n_percentile(sample2, 43)}")
    print(f"Quartile: {n_quartile(sample2, 43)}")
