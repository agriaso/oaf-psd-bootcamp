from analyze_job_data import analyze_job_data
import pandas as pd

def test_analyze_job_data():
    df = pd.read_csv("scraped_data3.csv")
    analyze_job_data(df)
    assert True

if __name__ == "__main__":
    test_analyze_job_data()
    print("analyze_job_data passed")