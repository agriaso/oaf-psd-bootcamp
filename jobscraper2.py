import csv
import requests
from bs4 import BeautifulSoup
import re

def split_job_info(string):
    '''
    Formats string into a dictionary with the following job listing data

    Args:
    string (str): A string containing job listing information

    Returns:
    dict: A dictionary containing the following keys:
        - Department: The department name
        - Ref Number: The reference number
        - Appt Type: The appointment type
        - Job Class: The job class
        - Job Title: The job title
    '''
    date_removed = re.sub(r'Apply\sby:\s[A-Za-z]+\s\d{2},\s\d{4}\s*', '', string)
    date_removed = date_removed.replace(" ", "")
    split_data = date_removed.split('|')
    split_data[0] = "".join(filter(lambda x: x.isalpha(), split_data[0]))
    
    if re.match(r'(Brandnew)', split_data[0]):
        split_data[0] = re.sub(r'(Brandnew)', '',
                         split_data[0], count=1)
    else:
        split_data[0] = re.sub(r'(Recentlyupdated)', '',
                         split_data[0], count=1)
        split_data[0] = re.sub(r'(d)', '',
                         split_data[0], count=1)
    
    department = re.sub(r'(ays|days|Applynowclosestoday|Applyby||Oneapplicationmanyopportunities|Oneapplicationmanyopportunities)', '',
                         split_data[0])

    # Extract job details using regex patterns
    details = {}

    regex_patterns = {
    'Appt_Job_JobTitle': r"(.\w+)(\d{4})-(.\w+)"
    }

    matches = re.findall(regex_patterns['Appt_Job_JobTitle'], split_data[2])

    details["Department"] = department
    details["Ref Number"] = split_data[1].strip()
    details["Appt Type"] = matches[0][0]
    details["Job Class"] = matches[0][1]
    details["Job Title"] = matches[0][2]
    
    return details

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
                'Paragraphs': "  ".join(paragraph_texts),
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

#implements split job info
def scrape_job_data2(url):
    job_data = []

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        job_divs = soup.find_all('div', class_='row listJob')

        for div in job_divs:
            # Extracting link href
            link = div.find('a', itemprop='url')['href']

            # Extracting text from <p> tags
            paragraphs = div.find_all('p')
            paragraph_texts = [paragraph.text.strip() for paragraph in paragraphs]
            joined_paragraphs = "".join(paragraph_texts)

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

            # Process paragraphs and extract job details
            formatted_p = {}
            formatted_p.update(split_job_info(joined_paragraphs))

            # Combining all data into a single row
            row_data = {
                'Department': formatted_p.get('Department', ''),
                'Ref Number': formatted_p.get('Ref Number', ''),
                'Appt Type': formatted_p.get('Appt Type', ''),
                'Job Class': formatted_p.get('Job Class', ''),
                'Job Title': formatted_p.get('Job Title', ''),
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
        fieldnames = ['Paragraphs', 'Meta_Identifier', 'Meta_DirectApply', 
                      'Meta_HiringOrganization', 'Meta_DatePosted', 'Meta_Description', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if file is empty, if yes, write headers
        csvfile.seek(0, 2)
        if csvfile.tell() == 0:
            writer.writeheader()

        for row in data:
            writer.writerow(row)

#different fields expected
def write_to_csv2(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
        'Department',
        'Ref Number',
        'Appt Type',
        'Job Class',
        'Job Title',
        'Meta_Identifier',
        'Meta_DirectApply',
        'Meta_HiringOrganization',
        'Meta_DatePosted',
        'Meta_Description',
        'Link'
        ]
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
        scraped_data = scrape_job_data2(offset_url)
        write_to_csv2(scraped_data, 'scraped_data2.csv')
    
