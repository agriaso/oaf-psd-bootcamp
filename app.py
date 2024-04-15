from flask import Flask, render_template
from JobListingDB import JobListingDB
from jobscraper2 import scrape_job_data2

app = Flask(__name__)
db = JobListingDB('job_listings.db')

# Function to scrape job data and add it to the database
def scrape_and_add_job_data(url, num_pages):
    db.connect()
    db.create_table()

    for page_num in range(num_pages + 1):
        offset_url = f'{url}?offset={page_num * 15}'
        scraped_data = scrape_job_data2(offset_url)
        db.add_job_listings(scraped_data)

    db.close()

# Define a Flask route to display the job listings
@app.route('/')
def display_job_listings():
    db.connect()
    job_listings = db.get_all_job_listings()
    fieldnames = [
    'Department',
    'Ref Number',
    'Appt Type',
    'Job Class',
    'Job Title',
    'Meta Identifier',
    'Meta Direct Apply',
    'Meta Hiring Organization',
    'Meta Date Posted',
    'Meta Description',
    'Link'
    ]

    # Convert tuples to dictionaries
    rows_dicts = [dict(zip(fieldnames, row)) for row in job_listings]
    db.close()
    return render_template('job_listings.html', job_listings=rows_dicts)

if __name__ == "__main__":
    app.run(debug=True)
