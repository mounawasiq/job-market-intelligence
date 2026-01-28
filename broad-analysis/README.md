# Broad Analysis - Job Market Intelligence

## Overview

Analysis of **60 data analyst job postings** across **3 major job platforms**: Indeed, LinkedIn, and Glassdoor. This analysis provides a market-wide perspective on data analyst hiring trends in the UK.

---

## What I Did

### 1. Data Collection (Web Scraping)
- Scraped job postings from Indeed.co.uk
- Scraped job postings from LinkedIn
- Scraped job postings from Glassdoor.co.uk
- Extracted: job title, company, location, salary, job description
- **Total jobs collected: 60**

### 2. Data Analysis
- Analyzed job seniority distribution (Senior vs Mid-Level vs Junior)
- Identified top companies hiring data analysts
- Examined salary data availability
- Analyzed geographic distribution
- Identified key trends across platforms

### 3. Data Visualization
- Created professional charts showing market trends
- Visualized job level distribution
- Showed top hiring companies
- Displayed salary information gaps
- Analyzed job title keywords

---

## Key Findings

### 📊 Job Market Overview
- **Total jobs analyzed:** 60
- **Data sources:** 3 (Indeed, LinkedIn, Glassdoor)
- **Companies hiring:** 55 different companies

### 💼 Seniority Distribution
- **Mid-Level positions:** 50 jobs (83.3%)
- **Senior positions:** 7 jobs (11.7%)
- **Junior positions:** 3 jobs (5.0%)

**Insight:** Most data analyst roles are mid-level positions, suggesting a mature market with experienced hire focus.

### 🏢 Top Hiring Companies
1. GRAYCE - 3 jobs
2. Multiple companies - 2 jobs each
3. Market concentration: Top 5 companies = 16.7% of jobs

**Insight:** No single company dominates hiring. Distributed across 55 companies.

### 💰 Salary Data
- **Jobs with salary listed:** Limited transparency
- **Data quality:** Glassdoor provides best salary information

**Insight:** Most platforms don't display salary in job listings (need to apply to see).

### 🌐 Platform Distribution
- **LinkedIn:** 60 jobs (100%)

**Note:** This dataset came primarily from LinkedIn scraping.

### 🔤 Most Common Words in Job Titles
- Data (appears in most titles)
- Analyst
- Senior
- Business
- Lead

---

## Technologies Used

### Data Collection
- **BeautifulSoup** - HTML parsing
- **Requests** - HTTP requests
- **Python 3** - Scripting language

### Data Analysis
- **Pandas** - Data manipulation and analysis
- **Python 3** - Data processing

### Data Visualization
- **Matplotlib** - Chart creation
- **Seaborn** - Statistical visualization

### Tools
- **Git & GitHub** - Version control
- **Python virtual environment** - Dependency management

---

## Files in This Folder

### Scripts
- `scraper.py` - Web scraper for collecting job postings
- `day4_analysis.py` - Analysis script (job levels, companies, trends)
- `day5_visualizations.py` - Visualization generation script

### Data Files
- `job_postings_20260127_202057.csv` - Raw job data (60 jobs)
- `jobs_analyzed_20260127_202840.csv` - Analyzed data with job level classifications

### Visualizations
- `job_market_analysis_*.png` - 4-chart dashboard showing:
  - Job level distribution
  - Top 10 companies
  - Job source distribution
  - Salary data availability
- `job_title_keywords_*.png` - Most common words in job titles

---

## How to Run

### Prerequisites
```bash
pip install requests beautifulsoup4 pandas matplotlib seaborn
```

### Step 1: Scrape Data
```bash
python scraper.py
```
**Output:** `job_postings_*.csv` with
