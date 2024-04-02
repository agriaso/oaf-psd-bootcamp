from update_local_data import update_local_data
import pandas as pd

def test_update_local_data():
    input_csv = "scraped_data4.csv"
    output_csv = "scraped_data4_cleaned.csv"
    print("original file length: ", len(pd.read_csv(input_csv)))
    print("Testing update_local_data")
    update_local_data(input_csv, output_csv)
    print("new file length: ", len(pd.read_csv(output_csv)))
    assert len(pd.read_csv(output_csv)) <= len(pd.read_csv(input_csv))

if __name__ == "__main__":
    test_update_local_data()
    print("update_local_data passed")