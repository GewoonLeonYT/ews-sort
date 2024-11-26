#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy
import pandas

list_types = ("random", "sorted", "reverse_sorted", "unique", "similar")
# list_types = ("random",)

plt.style.use('seaborn-v0_8-paper')

file = "./log/result_radixsort_100x1000000_noinput.csv"
data = pandas.read_csv(file, sep=";")
for list_type in list_types:
    times = numpy.array(data.loc[data["List type"] == list_type]["Time"])
    fig, ax = plt.subplots(1, 1)

    ax.hist(times, bins=100)
    ax.set_xlabel("Tijd (s)")
    ax.set_ylabel("Aantal voorvallen")
    ax.set_title(f"Radixsort - {list_type}")
    
    # print(plt.style.available)
    plt.savefig(f"./log/figuur_radixsort_{list_type}.svg")
