import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Step 1: Define the data points
data_points = np.array([
    [0.4, 0.53],  # D1
    [0.22, 0.38], # D2
    [0.35, 0.32], # D3
    [0.26, 0.19], # D4
    [0.08, 0.41], # D5
    [0.45, 0.30]  # D6
])

# Step 2: Perform Agglomerative Hierarchical Clustering using Single Linkage
Z = linkage(data_points, method='single')

# Step 3: Plot the Dendrogram
plt.figure(figsize=(10, 6))
dendrogram(Z, labels=[f'D{i+1}' for i in range(len(data_points))])
plt.title('Dendrogram - Agglomerative Hierarchical Clustering (Single Linkage)')
plt.xlabel('Data Points')
plt.ylabel('Euclidean Distance')
plt.grid()
plt.show()
