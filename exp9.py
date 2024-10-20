import numpy as np
from fractions import Fraction

def display_format(my_vector, my_decimal):
    return np.round((my_vector).astype(float), decimals=my_decimal)

my_dp = Fraction(1, 3)  # Define the equal probability

# Adjacency matrix (links between pages)
Mat = np.matrix([[Fraction(1, 3), Fraction(1, 2), 0],          # Page A links to Page B and C
                 [Fraction(1, 3), 0, Fraction(1, 2)],  # Page B links to Page A and C
                 [Fraction(1, 3), Fraction(1, 2), Fraction(1, 2)]]) # Page C links to A, B, and itself

# Matrix of equal probabilities for teleportation (stochastic jump)
Ex = np.zeros((3, 3))
Ex[:] = my_dp  # Each element has a value of 1/3 (equal probability of moving to any page)

beta = 0.7  # Damping factor (70% follows links, 30% random jump)

# Transition matrix combining both the teleportation and link-following behavior
Al = beta * Mat + ((1 - beta) * Ex)

# Initial rank vector (equal probability for all 3 pages)
r = np.matrix([my_dp, my_dp, my_dp])
r = np.transpose(r)

previous_r = r

# Iterate until convergence or up to 4 iterations
for i in range(1, 4):
    r = Al * r  # Update the rank vector
    print(f"Iteration {i}:")
    print(display_format(r, 3))

    # Check if the rank vector has converged (difference is negligible)
    if (previous_r == r).all():
        print("Converged!")
        break

    previous_r = r  # Update for the next iteration

# Final result
print("\nFinal PageRank Vector:\n", display_format(r, 3))
print("Sum of ranks:", np.sum(r))

# Find the highest rank page
highest_rank_index = np.argmax(r)  # Index of the page with the highest rank
highest_rank_value = r[highest_rank_index, 0]  # Get the highest rank value

# Map index to page names
pages = ['Page A', 'Page B', 'Page C']  # Corresponding page names
highest_page = pages[highest_rank_index]  # Name of the highest rank page

print(f"The highest rank page is: {highest_page} with a rank of {highest_rank_value:.3f}")
