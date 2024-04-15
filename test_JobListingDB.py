from JobListingDB import JobListingDB

def test_create_table():
    db = JobListingDB('test_job_listings.db')
    db.connect()
    db.create_table()
    db.close()
    assert True

def test_add_job_listings():
    db = JobListingDB('test_job_listings.db')
    db.connect()
    db.create_table()
    job_listings = [
        {
            'Department': 'IT',
            'Ref Number': '123',
            'Appt Type': 'Full-time',
            'Job Class': 'Software Engineer',
            'Job Title': 'Python Developer',
            'Meta_Identifier': '12345',
            'Meta_DirectApply': 'Yes',
            'Meta_HiringOrganization': 'ABC Tech',
            'Meta_DatePosted': '2024-04-02',
            'Meta_Description': 'Join our team as a Python Developer...',
            'Link': 'https://example.com/job/123'
        },
    ]
    db.add_job_listings(job_listings)
    db.close()
    assert True

def test_get_all_job_listings():
    db = JobListingDB('test_job_listings.db')
    db.connect()
    db.create_table()
    db.drop_all_rows()
    job_listings = [
        {
            'Department': 'IT',
            'Ref Number': '123',
            'Appt Type': 'Full-time',
            'Job Class': 'Software Engineer',
            'Job Title': 'Python Developer',
            'Meta_Identifier': '12345',
            'Meta_DirectApply': 'Yes',
            'Meta_HiringOrganization': 'ABC Tech',
            'Meta_DatePosted': '2024-04-02',
            'Meta_Description': 'Join our team as a Python Developer...',
            'Link': 'https://example.com/job/123'
        },
    ]
    db.add_job_listings(job_listings)
    table_size = len(db.get_all_job_listings())
    db.close()
    assert table_size == 1

def test_drop_duplicates():
    db = JobListingDB('test_job_listings.db')
    db.connect()
    db.create_table()
    job_listings = [
        {
            'Department': 'IT',
            'Ref Number': '123',
            'Appt Type': 'Full-time',
            'Job Class': 'Software Engineer',
            'Job Title': 'Python Developer',
            'Meta_Identifier': '12345',
            'Meta_DirectApply': 'Yes',
            'Meta_HiringOrganization': 'ABC Tech',
            'Meta_DatePosted': '2024-04-02',
            'Meta_Description': 'Join our team as a Python Developer...',
            'Link': 'https://example.com/job/123'
        },
        {
            'Department': 'IT',
            'Ref Number': '123',
            'Appt Type': 'Full-time',
            'Job Class': 'Software Engineer',
            'Job Title': 'Python Developer',
            'Meta_Identifier': '12345',
            'Meta_DirectApply': 'Yes',
            'Meta_HiringOrganization': 'ABC Tech',
            'Meta_DatePosted': '2024-04-02',
            'Meta_Description': 'Join our team as a Python Developer...',
            'Link': 'https://example.com/job/123'
        }
    ]
    db.add_job_listings(job_listings)
    original_table_size = len(db.get_all_job_listings())
    db.drop_duplicates()
    table_size_after_drop = len(db.get_all_job_listings())
    db.close()
    assert table_size_after_drop < original_table_size