# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Calculate the best math results
best_math_schools = schools[schools['average_math'] >= 0.8 * 800][['school_name', 'average_math']]
best_math_schools = best_math_schools.sort_values(by='average_math', ascending=False)
print(best_math_schools)

# Calculate the total SAT score
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
# Get the top 10 performing schools based on the combined SAT scores
top_10_schools = schools[['school_name', 'total_SAT']].sort_values(by='total_SAT', ascending=False).head(10)
print(top_10_schools)

# Calculate the standard deviation of the combined SAT score for each borough
borough_stats = schools.groupby('borough').agg(
    num_schools=('school_name', 'size'),
    average_SAT=('total_SAT', 'mean'),
    std_SAT=('total_SAT', 'std')
).reset_index()

# Find the borough with the largest standard deviation in the combined SAT score
largest_std_dev = borough_stats[borough_stats['std_SAT'] == borough_stats['std_SAT'].max()]
largest_std_dev = largest_std_dev.round({'average_SAT': 2, 'std_SAT': 2})
print(largest_std_dev)
