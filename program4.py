import csv
import os

# Function to read the CSV file
def read_csv(filename):
    try:
        with open(filename, 'r', newline='') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

# Function to parse the CSV data into separate lists
def parse_csv(csv_data):
    countryNames = []
    countryCodes = []
    
    for line in csv_data:
        parts = line.strip().split(',')
        if len(parts) == 2:
            countryNames.append(parts[0])
            countryCodes.append(parts[1])
    
    return countryNames, countryCodes

# Function to print the data as specified
def print_data(countryNames, countryCodes):
    for name, code in zip(countryNames, countryCodes):
        print(name)
        print(code)
        print("- - - - -")

def main():
    # Create a folder called program4
    folder_name = "program4"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # Download the CSV file
    csv_url = "https://raw.githubusercontent.com/datasets/country-list/master/data.csv"
    csv_filename = os.path.join(folder_name, "data.csv")

    try:
        import urllib.request
        urllib.request.urlretrieve(csv_url, csv_filename)
        print("CSV file downloaded successfully.")
    except Exception as e:
        print(f"Error downloading the CSV file: {e}")

    # Read the CSV file
    csv_data = read_csv(csv_filename)

    if csv_data:
        # Parse the CSV data
        countryNames, countryCodes = parse_csv(csv_data)

        # Print the data
        print_data(countryNames, countryCodes)

if __name__ == "__main__":
    main()
