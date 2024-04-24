# oaf-psd-bootcamp
This code was written for the Open Avenues Professional Python Software Development Bootcamp by Brian Adam.

Jobscraper
------
This repo scrapes data from the job posting website careers.sf.gov used by the City and County of San Francisco.

How does it work?
------
The jobscraper file contains two key functions:

- scrape_job_data
- split_job_info

scrape_job_data takes a target url and scrapes predefined HTML objects with beautiful soup. The scraped data is returned as a dictionary object.

It has two configurations:
- one returns all scraped <p> elements as a single string
- the other returns all scraped <p> elements broken up and processed via split_job_info

The essential part of split_job_info is a regex removing text like "Apply today," "Closes soon," and "Brand new."

What do we do with the data?
------
The data returned from jobscraper can be written to a local csv file or a SQL database.

Another file provides code analyzing an input data frame to generate high level observations, e.g. what is the most common job class, which department has the most openings, etc.

Where does the data go?
------
All the job postings are presented on a website.

This website features all job postings with additional information in a table.

It includes additional filters not available in the original website, like:
- filter by salary
- filter by years of experience
- filter by degree required

How can the website be expanded?
------
- The website can be expanded by adding integration with LinkedIn.
- Users can then filter jobs based on their resume data from Linkedin automatically.
- Generative AI like OpenAI's Completion API call could be used to summarize job descriptions or key qualifications.
 

