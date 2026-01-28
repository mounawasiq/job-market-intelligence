
# LinkedIn Deep Dive Analysis

## Overview
Detailed analysis of **240 LinkedIn job postings** for data analyst roles in London.

## Note on Data Source
Initially attempted to scrape Glassdoor and Indeed directly, but both platforms 
implement anti-scraping measures (HTTP 403 blocking). 

**Solution:** Used LinkedIn as primary data source for this deep dive analysis, 
which was successfully scraped and provides robust job market insights.

## What This Shows
- Extended job dataset (240 jobs vs 60 in broad-analysis)
- LinkedIn-specific hiring patterns
- Deeper seniority distribution analysis
- Company hiring concentration
- Job market trends and insights

## Data Collection
- Source: LinkedIn job postings
- Location: London, UK
- Role: Data Analyst
- Total jobs: 240
- Date: January 28, 2026

## Files
- `scraper_linkedin.py` - Web scraper for LinkedIn
- `visualize_linkedin.py` - Analysis and visualization
- `job_postings_*.csv` - Raw job data
- `linkedin_analyzed_*.csv` - Analyzed data with job levels
- `linkedin_analysis_*.png` - Professional visualizations

## Key Findings
- 83%+ of jobs are mid-level positions
- Top companies vary but market is distributed
- Strong demand for data analyst roles across sectors

## Technologies
- Python, BeautifulSoup, Pandas
- Matplotlib, Seaborn for visualization
- Web scraping, data analysis

## Status
✓ Complete