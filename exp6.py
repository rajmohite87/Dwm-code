import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 4: Hardcoded dataset with more data points
# Example data points (more diverse)
X = np.array([
    [1.0, 2.0],
    [1.5, 1.8],
    [5.0, 8.0],
    [8.0, 8.0],
    [1.0, 0.6],
    [9.0, 11.0],
    [8.0, 2.0],
    [10.0, 2.0],
    [9.0, 3.0],
    [1.2, 1.9],
    [5.5, 7.0],
    [7.5, 5.5],
    [2.0, 4.0],
    [6.5, 6.5],
    [2.5, 1.5],
    [3.0, 4.0],
    [4.5, 9.0],
    [8.5, 8.5],
    [0.5, 1.0],
    [11.0, 8.0]
])

# Parameters
n_clusters = 2  # Set the number of clusters

# Apply K-means clustering using scikit-learn
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Step 5: Visualize the results
plt.figure(figsize=(10, 6))
colors = ['r', 'g', 'b', 'y']  # Colors for clusters

# Plot each cluster
for i in range(n_clusters):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], s=100, c=colors[i], label=f'Cluster {i + 1}')

# Plot centroids
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='black', marker='X', label='Centroids')
plt.title('K-means Clustering (using scikit-learn)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid()
plt.show()
