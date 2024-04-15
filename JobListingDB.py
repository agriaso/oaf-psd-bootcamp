import sqlite3

class JobListingDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS JobListing (
                                Department TEXT,
                                RefNumber TEXT,
                                ApptType TEXT,
                                JobClass TEXT,
                                JobTitle TEXT,
                                MetaIdentifier TEXT,
                                MetaDirectApply TEXT,
                                MetaHiringOrganization TEXT,
                                MetaDatePosted TEXT,
                                MetaDescription TEXT,
                                Link TEXT
                                )''')
        self.connection.commit()

    def add_job_listings(self, job_listings):
        for job in job_listings:
            self.cursor.execute('''INSERT INTO JobListing (
                                    Department,
                                    RefNumber,
                                    ApptType,
                                    JobClass,
                                    JobTitle,
                                    MetaIdentifier,
                                    MetaDirectApply,
                                    MetaHiringOrganization,
                                    MetaDatePosted,
                                    MetaDescription,
                                    Link
                                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                    (
                                    job['Department'],
                                    job['Ref Number'],
                                    job['Appt Type'],
                                    job['Job Class'],
                                    job['Job Title'],
                                    job['Meta_Identifier'],
                                    job['Meta_DirectApply'],
                                    job['Meta_HiringOrganization'],
                                    job['Meta_DatePosted'],
                                    job['Meta_Description'],
                                    job['Link']
                                    ))
        self.connection.commit()

    def get_all_job_listings(self):
        self.cursor.execute("SELECT * FROM JobListing")
        rows = self.cursor.fetchall()
        return rows
    
    def drop_duplicates(self):
        self.cursor.execute('''DELETE FROM JobListing WHERE rowid NOT IN
                            (SELECT MIN(rowid) FROM JobListing GROUP BY Department, RefNumber)''')
        self.connection.commit()

    def drop_all_rows(self):
        self.cursor.execute("DELETE FROM JobListing")
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()

