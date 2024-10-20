import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the dimensions
locations = ['Chicago', 'New York', 'Toronto', 'Vancouver']
countries = ['USA', 'USA', 'Canada', 'Canada']  # Mapping for locations to countries
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
items = ['Mobile', 'Modem', 'Phone', 'Security']

# Create a 3D array to represent the data cube with integer sales numbers
# Random sales data for the sake of example
sales_cube = np.random.randint(100, 500, size=(len(locations), len(quarters), len(items)))

# Function to visualize 2D heatmaps
def visualize_2d_heatmap(data, x_labels, y_labels, title, annotate=False):
    plt.figure(figsize=(10, 6))
    sns.heatmap(data, annot=annotate, fmt="d", cmap="YlGnBu", cbar_kws={'label': 'Sales'})
    plt.xticks(ticks=np.arange(len(x_labels)) + 0.5, labels=x_labels, rotation=45)
    plt.yticks(ticks=np.arange(len(y_labels)) + 0.5, labels=y_labels, rotation=0)
    plt.title(title)
    plt.xlabel('Items')
    plt.ylabel('Locations')
    plt.show()

# Initial Cube Visualization (All Quarters)
print("Initial Data Cube Visualization (All Quarters):")
visualize_2d_heatmap(sales_cube.sum(axis=1).astype(int), items, locations, title="Sales Data - All Quarters", annotate=True)

# Roll-Up: Aggregating from cities to countries
# Aggregate by countries (USA and Canada)
unique_countries = list(set(countries))
rollup_cube = np.zeros((len(unique_countries), len(items)))

for loc_index, location in enumerate(locations):
    country_index = unique_countries.index(countries[loc_index])
    rollup_cube[country_index] += sales_cube[loc_index].sum(axis=0)

# Convert rollup_cube to integers
rollup_cube = rollup_cube.astype(int)

# Visualize Cube after Roll-Up (Countries vs. Items for All Quarters)
print("\nData Cube after Roll-Up (Countries vs. Items for All Quarters):")
visualize_2d_heatmap(rollup_cube.astype(int), items, unique_countries, title="Sales Data after Roll-Up - All Quarters", annotate=True)

# Drill-Down: Changing time from quarters to months
# Let's assume each quarter consists of 3 months
sales_months_cube = np.zeros((len(locations), len(months), len(items)))

# Fill the data based on quarters to months
for loc_index in range(len(locations)):
    for quarter_index in range(len(quarters)):
        for month_index in range(3):  # Each quarter has 3 months
            sales_months_cube[loc_index, quarter_index * 3 + month_index] = sales_cube[loc_index, quarter_index]

# Now we will drill down, removing the quarters and visualizing with months
# Aggregate monthly sales for each location and item
drill_down_cube = sales_months_cube.sum(axis=0).astype(int)  # Sum over the locations for each month

# Visualize Cube after Drill-Down (All Months)
print("\nData Cube after Drill-Down (All Months):")
visualize_2d_heatmap(drill_down_cube, items, months, title="Sales Data after Drill-Down - All Months", annotate=True)

# Slice: Cutting down the time dimension for all Q1
slice_op = sales_cube[:, 0, :]  # Slice for Q1 only (index 0 for Q1)

# Visualize Cube after Slice (for Q1 only)
print("\nData Cube after Slice (Q1 only):")
visualize_2d_heatmap(slice_op.astype(int), items, locations, title="Sales Data after Slice - Q1", annotate=True)

# Dice: Selecting criteria (Location = Toronto or Vancouver, Time = Q1 or Q2, Item = Mobile or Modem)
dice_locations_indices = [2, 3]  # Toronto and Vancouver
dice_quarters_indices = [0, 1]    # Q1 and Q2
dice_items_indices = [0, 1]        # Mobile and Modem

# Create the resulting cube after dice operation
dice_op = sales_cube[np.ix_(dice_locations_indices, dice_quarters_indices, dice_items_indices)]

# Visualize Cube after Dice
# We will visualize the sum across the quarter dimension for simplicity.
dice_visualization = dice_op.sum(axis=1).astype(int)  # Summing over the quarter dimension

# Now visualize the filtered data after dice operation
print("\nData Cube after Dice (Toronto & Vancouver, Q1 & Q2, Mobile & Modem):")
visualize_2d_heatmap(dice_visualization.astype(int), ['Mobile', 'Modem'], ['Toronto', 'Vancouver'], title="Sales Data after Dice (Filtered Data)", annotate=True)
