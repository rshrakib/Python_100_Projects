import pandas as pd

def auto_data_entry(data, file_path):
    try:

        try:
            existing_data = pd.read_csv(file_path)

        except FileNotFoundError:
            existing_data = pd.DataFrame()


        new_data = pd.DataFrame(data)
        combined_data = pd.concat([existing_data,new_data], ignore_index=True)
        combined_data.to_csv(file_path, index = False)
        print("Data Entry successful!!!")

    except Exception as e:
        print(f"an error occurred: {e}")

data_to_enter = [
    {'name': "Rakib", 'age': 30, 'city': "Bogura"},
    {'name': "Riyad", 'age': 20, 'city': "Dhaka"},
    {'name': "Arif", 'age': 10, 'city': "Rangpur"}
]

csv_file_path = 'data.csv'
auto_data_entry(data_to_enter, csv_file_path)