from JobListingDB import JobListingDB
from jobscraper2 import scrape_job_data2
from jobscraper2 import split_job_info

# Example usage:
if __name__ == "__main__":
    db = JobListingDB('job_listings.db')
    db.connect()
    db.create_table()

    """url = 'https://careers.sf.gov/'
    num_pages = 15  # Adjust the number of pages as needed


    for page_num in range(0, num_pages + 1):
        offset_url = f'{url}?offset={page_num * 15}'
        scraped_data = scrape_job_data2(offset_url)
        db.add_job_listings(scraped_data)
    """
    print("Table size:", len(db.get_all_job_listings()))
    db.drop_duplicates()
    print("Complete")
    print("Table size after drop:", len(db.get_all_job_listings()))
    db.close()
