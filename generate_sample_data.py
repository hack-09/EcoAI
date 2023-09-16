import csv
import random

num_additional_rows = 1000  

headers = ['Date', 'Air Quality', 'Water Pollution', 'Deforestation']

# Create sample data
sample_data = [
    ['2023-01-01', 50, 25, 0.1],
    ['2023-01-02', 55, 30, 0.2]
]


for _ in range(num_additional_rows):
    date = f'2023-01-0{_ + 3}'  
    
    air_quality = random.uniform(40, 70)
    water_pollution = random.uniform(20, 35)
    deforestation = random.uniform(0.05, 0.3)
    
    sample_data.append([date, air_quality, water_pollution, deforestation])

# Write data to CSV file
with open('environmental_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  
    writer.writerows(sample_data)

print(f'Sample data with {num_additional_rows} additional rows generated and saved to environmental_data.csv.')
