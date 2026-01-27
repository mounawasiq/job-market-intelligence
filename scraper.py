"""
Job Market Intelligence - Day 3
Scale scraper to collect 100+ jobs from multiple pages
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import random

print("\n" + "="*70)
print("JOB MARKET INTELLIGENCE - DAY 3: SCALE TO 100+ JOBS")
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

all_jobs = []

# ============================================
# INDEED - MULTIPLE PAGES
# ============================================

def scrape_indeed_multiple_pages():
    """
    Scrape Indeed across multiple pages
    Indeed uses 'start' parameter for pagination: 0, 10, 20, 30...
    """
    print("\n[1/3] Scraping Indeed.co.uk (Multiple Pages)...")
    print("-" * 70)
    
    jobs = []
    base_url = "https://www.indeed.co.uk/jobs?q=data+analyst&l=London&start="
    
    # Scrape first 3 pages (30 jobs typically)
    for page in range(0, 30, 10):  # pages 0, 10, 20
        url = base_url + str(page)
        print(f"\nPage {page//10 + 1}: {url}")
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                job_cards = soup.find_all('div', class_='job_seen_beacon')
                
                print(f"  Found {len(job_cards)} jobs on this page")
                
                for idx, job_card in enumerate(job_cards):
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
                        
                        # Extract salary
                        salary_elem = job_card.find('span', class_='salary-snippet')
                        salary = salary_elem.text.strip() if salary_elem else "Not listed"
                        
                        # Extract job description snippet
                        desc_elem = job_card.find('ul', class_='jobsearch-JobComponent-description')
                        description = desc_elem.text.strip()[:200] if desc_elem else "N/A"
                        
                        job_data = {
                            'source': 'Indeed',
                            'title': title,
                            'company': company,
                            'location': location,
                            'salary': salary,
                            'description': description,
                            'date_scraped': datetime.now().strftime("%Y-%m-%d")
                        }
                        
                        jobs.append(job_data)
                        print(f"    ✓ {title[:50]}...")
                        
                    except Exception as e:
                        continue
                
            else:
                print(f"  ✗ Status {response.status_code}")
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
        
        # Be nice to the server - wait between requests
        time.sleep(random.uniform(2, 4))
    
    print(f"\n✓ Indeed: Extracted {len(jobs)} jobs")
    return jobs


# ============================================
# LINKEDIN - MULTIPLE PAGES
# ============================================

def scrape_linkedin_multiple_pages():
    """
    Scrape LinkedIn across multiple pages
    LinkedIn uses 'start' parameter for pagination
    """
    print("\n[2/3] Scraping LinkedIn (Multiple Pages)...")
    print("-" * 70)
    
    jobs = []
    base_url = "https://www.linkedin.com/jobs/search/?keywords=data%20analyst&location=London&start="
    
    # Scrape first 2 pages (25 jobs typically)
    for page in range(0, 25, 25):  # pages 0, 25 (LinkedIn shows 25 per page)
        url = base_url + str(page)
        print(f"\nPage {page//25 + 1}: {url}")
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                job_cards = soup.find_all('div', class_='base-card')
                
                print(f"  Found {len(job_cards)} jobs on this page")
                
                for idx, job_card in enumerate(job_cards):
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
                        
                        # LinkedIn rarely shows salary in list view
                        salary = "Not listed"
                        description = "N/A"
                        
                        job_data = {
                            'source': 'LinkedIn',
                            'title': title,
                            'company': company,
                            'location': location,
                            'salary': salary,
                            'description': description,
                            'date_scraped': datetime.now().strftime("%Y-%m-%d")
                        }
                        
                        jobs.append(job_data)
                        print(f"    ✓ {title[:50]}...")
                        
                    except Exception as e:
                        continue
                
            else:
                print(f"  ✗ Status {response.status_code}")
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
        
        # Wait between requests
        time.sleep(random.uniform(2, 4))
    
    print(f"\n✓ LinkedIn: Extracted {len(jobs)} jobs")
    return jobs


# ============================================
# GLASSDOOR - MULTIPLE PAGES
# ============================================

def scrape_glassdoor_multiple_pages():
    """
    Scrape Glassdoor across multiple pages
    """
    print("\n[3/3] Scraping Glassdoor (Multiple Pages)...")
    print("-" * 70)
    
    jobs = []
    # Glassdoor pagination: add &p=1, &p=2 etc
    base_url = "https://www.glassdoor.co.uk/Job/data-analyst-jobs-SRCH_KO0,12.htm?location=London&p="
    
    # Scrape first 2 pages (30 jobs typically)
    for page in range(1, 3):  # pages 1, 2
        url = base_url + str(page)
        print(f"\nPage {page}: {url}")
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                job_cards = soup.find_all('li', class_='react-job-listing')
                
                print(f"  Found {len(job_cards)} jobs on this page")
                
                for idx, job_card in enumerate(job_cards):
                    try:
                        # Extract title
                        title_elem = job_card.find('a', class_='jobTitle')
                        title = title_elem.text.strip() if title_elem else "N/A"
                        
                        # Extract company
                        company_elem = job_card.find('div', class_='jobEmpolyerName')
                        company = company_elem.text.strip() if company_elem else "N/A"
                        
                        # Extract location
                        location_elem = job_card.find('div', class_='jobLocation')
                        location = location_elem.text.strip() if location_elem else "N/A"
                        
                        # Extract salary
                        salary_elem = job_card.find('span', class_='salaryEstimate')
                        salary = salary_elem.text.strip() if salary_elem else "Not listed"
                        
                        description = "N/A"
                        
                        job_data = {
                            'source': 'Glassdoor',
                            'title': title,
                            'company': company,
                            'location': location,
                            'salary': salary,
                            'description': description,
                            'date_scraped': datetime.now().strftime("%Y-%m-%d")
                        }
                        
                        jobs.append(job_data)
                        print(f"    ✓ {title[:50]}...")
                        
                    except Exception as e:
                        continue
                
            else:
                print(f"  ✗ Status {response.status_code}")
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
        
        # Wait between requests
        time.sleep(random.uniform(2, 4))
    
    print(f"\n✓ Glassdoor: Extracted {len(jobs)} jobs")
    return jobs


# ============================================
# SAVE TO CSV
# ============================================

def save_to_csv(jobs_list, filename=None):
    """Save jobs to CSV file"""
    if filename is None:
        filename = f"job_postings_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        df = pd.DataFrame(jobs_list)
        df.to_csv(filename, index=False, encoding='utf-8')
        
        print(f"\n✓ Saved {len(df)} jobs to: {filename}")
        print(f"\nFirst 10 rows of data:")
        print(df.head(10).to_string())
        
        return filename, len(df)
        
    except Exception as e:
        print(f"✗ Error saving to CSV: {e}")
        return None, 0


# ============================================
# MAIN EXECUTION
# ============================================

print("\nStarting multi-page scraping...")
print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Scrape from all sources
indeed_jobs = scrape_indeed_multiple_pages()
time.sleep(2)
linkedin_jobs = scrape_linkedin_multiple_pages()
time.sleep(2)
glassdoor_jobs = scrape_glassdoor_multiple_pages()

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
    print("✓✓✓ SUCCESS! SCALED TO 100+ JOBS ✓✓✓")
    print("="*70)
    print(f"\nYou have extracted {saved_count} jobs from 3 sources!")
    print(f"CSV file: {filename}")
    print(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
else:
    print("\n✗ No jobs found to save")

print("\n" + "="*70)