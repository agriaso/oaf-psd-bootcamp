from jobscraper2 import scrape_job_data

def test_scrape_job_data():
    url = 'https://careers.sf.gov/'
    scraped_data = scrape_job_data(url)
    assert len(scraped_data) > 0
