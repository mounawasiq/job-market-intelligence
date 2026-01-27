"""
Job Market Intelligence - Fixed Web Scraper
Using Better Headers + Fallback Sites
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

print("\n" + "="*60)
print("JOB MARKET INTELLIGENCE - WEB SCRAPER (ENHANCED)")
print("="*60)

# Better headers that work better
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

jobs_found = []

# ============================================
# TRY INDEED WITH BETTER HEADERS
# ============================================

print("\n[1/3] Trying Indeed.co.uk (with better headers)...")
print("-" * 60)

url_indeed = "https://www.indeed.co.uk/jobs?q=data+analyst&l=London"

try:
    response = requests.get(url_indeed, headers=HEADERS, timeout=10)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        jobs = soup.find_all('div', class_='job_seen_beacon')
        
        if len(jobs) > 0:
            print(f"✓ Indeed working! Found {len(jobs)} jobs")
            jobs_found.append(('Indeed', len(jobs)))
        else:
            print(f"✗ Indeed returned 200 but no jobs found (might need different selectors)")
    else:
        print(f"✗ Indeed blocked us (Status {response.status_code})")
        
except Exception as e:
    print(f"✗ Error with Indeed: {e}")

time.sleep(2)  # Wait between requests

# ============================================
# TRY LINKEDIN JOBS
# ============================================

print("\n[2/3] Trying LinkedIn Jobs...")
print("-" * 60)

url_linkedin = "https://www.linkedin.com/jobs/search/?keywords=data%20analyst&location=London"

try:
    response = requests.get(url_linkedin, headers=HEADERS, timeout=10)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        jobs = soup.find_all('div', class_='base-card')
        
        if len(jobs) > 0:
            print(f"✓ LinkedIn working! Found {len(jobs)} jobs")
            jobs_found.append(('LinkedIn', len(jobs)))
        else:
            print(f"✗ LinkedIn returned 200 but no jobs found")
    else:
        print(f"✗ LinkedIn blocked us (Status {response.status_code})")
        
except Exception as e:
    print(f"✗ Error with LinkedIn: {e}")

time.sleep(2)

# ============================================
# TRY GLASSDOOR
# ============================================

print("\n[3/3] Trying Glassdoor...")
print("-" * 60)

url_glassdoor = "https://www.glassdoor.co.uk/Job/data-analyst-jobs-SRCH_KO0,12.htm?location=London"

try:
    response = requests.get(url_glassdoor, headers=HEADERS, timeout=10)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        jobs = soup.find_all('li', class_='react-job-listing')
        
        if len(jobs) > 0:
            print(f"✓ Glassdoor working! Found {len(jobs)} jobs")
            jobs_found.append(('Glassdoor', len(jobs)))
        else:
            print(f"✗ Glassdoor returned 200 but no jobs found")
    else:
        print(f"✗ Glassdoor blocked us (Status {response.status_code})")
        
except Exception as e:
    print(f"✗ Error with Glassdoor: {e}")

# ============================================
# RESULTS
# ============================================

print("\n" + "="*60)
print("RESULTS SUMMARY")
print("="*60)

if jobs_found:
    total = sum([count for _, count in jobs_found])
    print(f"\n✓ SUCCESS! Found jobs from:")
    for source, count in jobs_found:
        print(f"  • {source}: {count} jobs")
    print(f"\n✓ TOTAL: {total} jobs found")
    print("\n✓✓✓ SCRAPER IS WORKING! ✓✓✓")
else:
    print(f"\n✗ No jobs found yet")
    print("\nThis is normal! Job sites block scrapers.")
    print("\nNext steps:")
    print("  1. Try adding delays between requests")
    print("  2. Use Selenium for JavaScript-heavy sites")
    print("  3. Or use Scrapy framework")
    print("  4. Or use APIs instead (Rapid API, etc.)")
    print("\n→ Continue to Day 2 plan: Use Selenium instead")

print("\n" + "="*60)