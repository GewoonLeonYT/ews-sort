#!/usr/bin/env python3
import decimal

import numpy
import pandas


algorithms = ("heapsort", "radixsort")
list_types = ("random", "sorted", "reverse_sorted", "unique", "similar")

for algorithm in algorithms:
    data = pandas.read_csv(f"./log/result_{algorithm}_100x1000000_noinput.csv", sep=";", dtype={"Time": str})
    data["Time"] = data["Time"].apply(decimal.Decimal)
    with open(f"./log/times_{algorithm}.csv", "w") as file:
            file.write("List type;Average Time;Fastest time;Slowest time;Standard deviation\n")
    for list_type in list_types:
        times = numpy.array(data.loc[data["List type"] == list_type]["Time"])
        avg_time = sum(times) / decimal.Decimal(len(times))
        fastest = min(times)
        slowest = max(times)
        standard_deviation = numpy.std(times, ddof=1)
        with open(f"./log/times_{algorithm}.csv", "a") as file:
            file.write(f"{list_type};{avg_time};{fastest};{slowest};{standard_deviation}\n")
        