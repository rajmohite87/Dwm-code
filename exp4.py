#1) Data Exploration: Compute Mean, Median, Mode, and Five-Number Summary

import numpy as np
import statistics as stats

# Data for exploration
data = [13, 15, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 35, 35, 35]

# Mean
mean = np.mean(data)
# Median
median = np.median(data)
# Mode
mode = stats.mode(data)

# Five-Number Summary
minimum = np.min(data)
maximum = np.max(data)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

print("Data Exploration:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Minimum: {minimum}")
print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"Maximum: {maximum}")
print(f"Interquartile Range (IQR): {iqr}")

# 2) Data Preprocessing: Smoothing Using Binning Data: [8, 16, 9, 15, 21, 21, 24, 30, 26, 27, 30, 34]
# a. Bin Mean:

# Data for Binning
data = [8, 16, 9, 15, 21, 21, 24, 30, 26, 27, 30, 34]

# Create bins (equal-width binning, with 3 bins)
# bins = [data[i:i+4] for i in range(0, len(data), 4)]
bins = []
for i in range (0, len(data), 4):
    bins.append(data[i:i+4])
print(f"Bins:{bins}")
# Calculate the mean of each bin
# Bin Mean
# bin_mean = [int(np.mean(bin)) for bin in bins]
bin_mean = []
for bin in bins:
    bin_mean.append(int(np.mean(bin)))
print(f"Bin Mean:{bin_mean}")

# Replace values in each bin by the mean of that bin
bin_mean_result = []
for bin, mean in zip(bins, bin_mean):
    bin_mean_result.extend([mean] * len(bin))


print("\nBinning by Mean:")
print(bin_mean_result)


# b) Bin Boundaries:

# Bin Boundaries
bin_boundary_result = []
for bin in bins:
    min_boundary = min(bin)
    max_boundary = max(bin)
    boundary_bin = [min_boundary if abs(x - min_boundary) < abs(x - max_boundary) else max_boundary for x in bin]
    bin_boundary_result.extend(boundary_bin)

print("\nBinning by Boundaries:")
print(bin_boundary_result)

# c) 
# Bin Median
bin_median = [int(np.median(bin)) for bin in bins]

# Replace values in each bin by the median of that bin
bin_median_result = []
for bin, median in zip(bins, bin_median):
    bin_median_result.extend([median] * len(bin))

print("\nBinning by Median:")
print(bin_median_result)

