"""
Job Market Intelligence - Day 2
Extract job details (titles, companies, salaries) and save to CSV
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import csv

print("\n" + "="*70)
print("JOB MARKET INTELLIGENCE - DAY 2: EXTRACT & SAVE DATA")
print("="*70)

# Better headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# Store all jobs here
all_jobs = []

# ============================================
# SCRAPE INDEED AND EXTRACT DETAILS
# ============================================

def scrape_indeed_details():
    """
    Scrape Indeed and extract: title, company, salary, location
    """
    print("\n[1/3] Scraping Indeed.co.uk for job details...")
    print("-" * 70)
    
    url = "https://www.indeed.co.uk/jobs?q=data+analyst&l=London"
    jobs = []
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            job_cards = soup.find_all('div', class_='job_seen_beacon')
            
            print(f"Found {len(job_cards)} job postings on Indeed")
            
            # Extract data from each job
            for idx, job_card in enumerate(job_cards[:20]):  # First 20 for testing
                try:
                    # Extract title
                    title_elem = job_card.find('h2', class_='jobTitle')
                    title = title_elem.text.strip() if title_elem else "N/A"
                    
                    # Extract company
                    company_elem = job_card.find('span', class_='companyName')
                    company = company_elem.text.strip() if company_elem else "N/A"
                    
                    # Extract location
                    location_elem = job_card.find('div', class_='companyLocation')
                    location = location_elem.text.strip() if location_elem else "N/A"
                    
                    # Extract salary (often not available)
                    salary_elem = job_card.find('span', class_='salary-snippet')
                    salary = salary_elem.text.strip() if salary_elem else "Not listed"
                    
                    # Extract job URL
                    link_elem = job_card.find('a', class_='jcs-JobTitle')
                    job_url = "https://www.indeed.co.uk" + link_elem.get('href') if link_elem else "N/A"
                    
                    job_data = {
                        'source': 'Indeed',
                        'title': title,
                        'company': company,
                        'location': location,
                        'salary': salary,
                        'url': job_url,
                        'date_scraped': datetime.now().strftime("%Y-%m-%d")
                    }
                    
                    jobs.append(job_data)
                    print(f"  ✓ Job {idx+1}: {title[:40]}... at {company}")
                    
                except Exception as e:
                    print(f"  ✗ Error extracting job {idx+1}: {e}")
                    continue
            
            print(f"\n✓ Indeed: Successfully extracted {len(jobs)} jobs")
            return jobs
            
        else:
            print(f"✗ Indeed returned status {response.status_code}")
            return []
            
    except Exception as e:
        print(f"✗ Error scraping Indeed: {e}")
        return []

time.sleep(2)

# ============================================
# SCRAPE LINKEDIN AND EXTRACT DETAILS
# ============================================

def scrape_linkedin_details():
    """
    Scrape LinkedIn and extract: title, company, salary, location
    """
    print("\n[2/3] Scraping LinkedIn for job details...")
    print("-" * 70)
    
    url = "https://www.linkedin.com/jobs/search/?keywords=data%20analyst&location=London"
    jobs = []
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            job_cards = soup.find_all('div', class_='base-card')
            
            print(f"Found {len(job_cards)} job postings on LinkedIn")
            
            for idx, job_card in enumerate(job_cards[:20]):
                try:
                    # Extract title
                    title_elem = job_card.find('h3', class_='base-search-card__title')
                    title = title_elem.text.strip() if title_elem else "N/A"
                    
                    # Extract company
                    company_elem = job_card.find('h4', class_='base-search-card__subtitle')
                    company = company_elem.text.strip() if company_elem else "N/A"
                    
                    # Extract location
                    location_elem = job_card.find('span', class_='job-search-card__location')
                    location = location_elem.text.strip() if location_elem else "N/A"
                    
                    # LinkedIn rarely shows salary in preview
                    salary = "Not listed"
                    
                    # Extract URL
                    link_elem = job_card.find('a', class_='base-card__full-link')
                    job_url = link_elem.get('href') if link_elem else "N/A"
                    
                    job_data = {
                        'source': 'LinkedIn',
                        'title': title,
                        'company': company,
                        'location': location,
                        'salary': salary,
                        'url': job_url,
                        'date_scraped': datetime.now().strftime("%Y-%m-%d")
                    }
                    
                    jobs.append(job_data)
                    print(f"  ✓ Job {idx+1}: {title[:40]}... at {company}")
                    
                except Exception as e:
                    print(f"  ✗ Error extracting job {idx+1}: {e}")
                    continue
            
            print(f"\n✓ LinkedIn: Successfully extracted {len(jobs)} jobs")
            return jobs
            
        else:
            print(f"✗ LinkedIn returned status {response.status_code}")
            return []
            
    except Exception as e:
        print(f"✗ Error scraping LinkedIn: {e}")
        return []

time.sleep(2)

# ============================================
# SCRAPE GLASSDOOR AND EXTRACT DETAILS
# ============================================

def scrape_glassdoor_details():
    """
    Scrape Glassdoor and extract: title, company, salary, location
    """
    print("\n[3/3] Scraping Glassdoor for job details...")
    print("-" * 70)
    
    url = "https://www.glassdoor.co.uk/Job/data-analyst-jobs-SRCH_KO0,12.htm?location=London"
    jobs = []
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            job_cards = soup.find_all('li', class_='react-job-listing')
            
            print(f"Found {len(job_cards)} job postings on Glassdoor")
            
            for idx, job_card in enumerate(job_cards[:20]):
                try:
                    # Extract title
                    title_elem = job_card.find('a', class_='jobTitle')
                    title = title_elem.text.strip() if title_elem else "N/A"
                    
                    # Extract company
                    company_elem = job_card.find('div', class_='jobEmpolyerName')
                    company = company_elem.text.strip() if company_elem else "N/A"
                    
                    # Extract location (might be in different element)
                    location_elem = job_card.find('div', class_='jobLocation')
                    location = location_elem.text.strip() if location_elem else "N/A"
                    
                    # Extract salary if available
                    salary_elem = job_card.find('span', class_='salaryEstimate')
                    salary = salary_elem.text.strip() if salary_elem else "Not listed"
                    
                    # Extract URL
                    link_elem = job_card.find('a', class_='jobTitle')
                    job_url = "https://www.glassdoor.co.uk" + link_elem.get('href') if link_elem else "N/A"
                    
                    job_data = {
                        'source': 'Glassdoor',
                        'title': title,
                        'company': company,
                        'location': location,
                        'salary': salary,
                        'url': job_url,
                        'date_scraped': datetime.now().strftime("%Y-%m-%d")
                    }
                    
                    jobs.append(job_data)
                    print(f"  ✓ Job {idx+1}: {title[:40]}... at {company}")
                    
                except Exception as e:
                    print(f"  ✗ Error extracting job {idx+1}: {e}")
                    continue
            
            print(f"\n✓ Glassdoor: Successfully extracted {len(jobs)} jobs")
            return jobs
            
        else:
            print(f"✗ Glassdoor returned status {response.status_code}")
            return []
            
    except Exception as e:
        print(f"✗ Error scraping Glassdoor: {e}")
        return []

# ============================================
# COMBINE AND SAVE TO CSV
# ============================================

def save_to_csv(jobs_list, filename=None):
    """
    Save jobs to CSV file
    """
    if filename is None:
        filename = f"job_postings_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        # Create DataFrame
        df = pd.DataFrame(jobs_list)
        
        # Save to CSV
        df.to_csv(filename, index=False, encoding='utf-8')
        
        print(f"\n✓ Saved {len(df)} jobs to: {filename}")
        print(f"\nFirst 5 rows:")
        print(df.head())
        
        return filename, len(df)
        
    except Exception as e:
        print(f"✗ Error saving to CSV: {e}")
        return None, 0

# ============================================
# MAIN EXECUTION
# ============================================

print("\nStarting scraping process...")

# Scrape from all sources
indeed_jobs = scrape_indeed_details()
linkedin_jobs = scrape_linkedin_details()
glassdoor_jobs = scrape_glassdoor_details()

# Combine all jobs
all_jobs = indeed_jobs + linkedin_jobs + glassdoor_jobs

print("\n" + "="*70)
print("SUMMARY")
print("="*70)
print(f"Indeed jobs: {len(indeed_jobs)}")
print(f"LinkedIn jobs: {len(linkedin_jobs)}")
print(f"Glassdoor jobs: {len(glassdoor_jobs)}")
print(f"TOTAL JOBS: {len(all_jobs)}")

# Save to CSV
if len(all_jobs) > 0:
    filename, saved_count = save_to_csv(all_jobs)
    
    print("\n" + "="*70)
    print("✓✓✓ SUCCESS! DATA SAVED TO CSV ✓✓✓")
    print("="*70)
    print(f"\nYou have extracted {saved_count} jobs!")
    print(f"CSV file: {filename}")
    print("\nNext step: Open the CSV file to verify the data")
    
else:
    print("\n✗ No jobs found to save")
print("\n" + "="*70)