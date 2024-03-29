import csv
import requests
from bs4 import BeautifulSoup
import re

def scrape_job_data(url):
    response = requests.get(url)
    job_data = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        job_divs = soup.find_all('div', class_='row listJob')

        for div in job_divs:
            # Extracting link href
            link = div.find('a', itemprop='url')['href']

            # Extracting text from <p> tags
            paragraphs = div.find_all('p')
            paragraph_texts = [paragraph.text.strip() for paragraph in paragraphs]

            # Extracting content from <meta> tags
            meta_tags = div.find_all('meta')
            meta_data = {
                'identifier': '',
                'directApply': '',
                'hiringOrganization': '',
                'datePosted': '',
                'description': ''
            }
            for meta_tag in meta_tags:
                itemprop = meta_tag.get('itemprop', '')
                content = meta_tag.get('content', '').strip()
                if itemprop in meta_data:
                    meta_data[itemprop] = content

            # Combining all data into a single row
            row_data = {
                'Paragraphs': ' '.join(paragraph_texts),
                'Meta_Identifier': meta_data['identifier'],
                'Meta_DirectApply': meta_data['directApply'],
                'Meta_HiringOrganization': meta_data['hiringOrganization'],
                'Meta_DatePosted': meta_data['datePosted'],
                'Meta_Description': meta_data['description'],
                'Link': link
            }
            job_data.append(row_data)
    else:
        print("Failed to retrieve the page")

    return job_data

def write_to_csv(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Paragraphs', 'Meta_Identifier', 'Meta_DirectApply', 'Meta_HiringOrganization', 'Meta_DatePosted', 'Meta_Description', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if file is empty, if yes, write headers
        csvfile.seek(0, 2)
        if csvfile.tell() == 0:
            writer.writeheader()

        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    url = 'https://careers.sf.gov/'
    num_pages = 15  # Adjust the number of pages as needed

    for page_num in range(0, num_pages + 1):
        offset_url = f'{url}?offset={page_num * 15}'
        scraped_data = scrape_job_data(offset_url)
        write_to_csv(scraped_data, 'scraped_data.csv')
    
