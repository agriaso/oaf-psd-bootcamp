from jobscraper2 import split_job_info
import csv

def test_split_job_info():
    cleaned_strings = []

    with open("target_strings.csv", "r") as file:
        next(file)
        for row in file:
            cleaned_strings.append(split_job_info(row))

    assert len(cleaned_strings[0])==5
    assert cleaned_strings[0]["Department"] == "PublicHealth"
    assert cleaned_strings[0]["Ref Number"] == "REF39347N"
    assert cleaned_strings[0]["Appt Type"] == "PermanentExempt"
    assert cleaned_strings[0]["Job Class"] == "9910"
    assert cleaned_strings[0]["Job Title"] == "PublicServiceTrainee"