import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pytz

def analyze_job_data(df):
    # Load the data

    # Get current date in UTC timezone
    utc_now = datetime.datetime.now(datetime.UTC)

    # Convert to a specific timezone (for example, 'America/New_York')
    desired_timezone = pytz.timezone('America/Los_Angeles')
    today_timezone_aware = utc_now.replace(tzinfo=pytz.utc).astimezone(desired_timezone)


    df["Meta_DatePosted"] = pd.to_datetime(df["Meta_DatePosted"])
    df['Listing_Duration'] = pd.to_datetime(today_timezone_aware) - df['Meta_DatePosted']
    avg_listing_time,median_listing_time = df['Listing_Duration'].mean(),df['Listing_Duration'].median()
    by_department = df.groupby('Department').count()
    by_job_class = df.groupby('Job Class').count()
    by_type = df.groupby('Appt Type').count()
    top_5_jobs = df['Job Title'].value_counts().head(5)
    top_5_depts = df['Department'].value_counts().head(5)

    print(f"Average listing time: {avg_listing_time}")
    print(f"Median listing time: {median_listing_time}")    
    print(f"Jobs by department: {by_department}")
    print(f"Jobs by job class: {by_job_class}")
    print(f"Jobs by type: {by_type}")
    print(f"Top 5 jobs: {top_5_jobs}")
    print(f"Top 5 departments: {top_5_depts}")