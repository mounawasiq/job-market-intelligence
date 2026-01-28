# Job Market Intelligence

**Web scraping job postings and analyzing skill demand using NLP**

A comprehensive data analysis project examining the UK data analyst job market across multiple platforms. This portfolio demonstrates web scraping, data analysis, visualization, and market research skills.

---

## 📋 Project Overview

Comprehensive analysis of **data analyst job market** in the UK by collecting and analyzing job postings from major hiring platforms (Indeed, LinkedIn, Glassdoor).

**Duration:** Week 1 of portfolio (January 2026)  
**Status:** ✓ Broad Analysis Complete | ○ Indeed Deep Dive | ○ Glassdoor Deep Dive

---

## 🎯 What This Project Shows

### Skills Demonstrated
- ✓ **Web Scraping** - Collecting real data from multiple websites
- ✓ **Data Analysis** - Extracting insights from raw job data
- ✓ **Data Visualization** - Creating professional charts and reports
- ✓ **Python Programming** - Writing production-quality scripts
- ✓ **Git & GitHub** - Version control and code management
- ✓ **Problem Solving** - Adapting to different data sources

### Technical Skills
- Python 3
- BeautifulSoup (HTML parsing)
- Requests (HTTP requests)
- Pandas (Data manipulation)
- Matplotlib & Seaborn (Visualization)
- Git

---

## 📁 Project Structure

```
job-market-intelligence/
│
├── broad-analysis/
│   ├── scraper.py                          # Web scraper (3 platforms)
│   ├── day5_visualizations.py              # Chart generation
│   ├── job_postings_*.csv                  # Raw job data (60 jobs)
│   ├── jobs_analyzed_*.csv                 # Analyzed data
│   ├── job_market_analysis_*.png           # Dashboard (4 charts)
│   ├── job_title_keywords_*.png            # Keyword analysis
│   └── README.md                           # Detailed documentation
│
├── indeed-deep-dive/
│   ├── scraper_indeed.py                   # Indeed-only scraper (Coming)
│   ├── analysis_indeed.py                  # Indeed analysis (Coming)
│   ├── visualizations_indeed.py            # Indeed charts (Coming)
│   ├── indeed_jobs_*.csv                   # Indeed data (Coming)
│   ├── *.png                               # Visualizations (Coming)
│   └── README.md                           # Indeed analysis docs (Coming)
│
├── glassdoor-deep-dive/
│   ├── scraper_glassdoor.py                # Glassdoor-only scraper (Coming)
│   ├── analysis_glassdoor.py               # Glassdoor analysis (Coming)
│   ├── visualizations_glassdoor.py         # Glassdoor charts (Coming)
│   ├── glassdoor_jobs_*.csv                # Glassdoor data (Coming)
│   ├── *.png                               # Visualizations (Coming)
│   └── README.md                           # Glassdoor analysis docs (Coming)
│
└── README.md                               # This file
```

---

## 📊 Current Findings (Broad Analysis)

### Market Overview
- **60 jobs analyzed** across 3 platforms
- **55 companies** actively hiring for data analyst roles
- **83% mid-level positions** (most opportunities are mid-career)
- **Limited salary transparency** (most jobs don't list salary)

### Key Insights
1. **Seniority Distribution:**
   - Mid-Level: 50 jobs (83.3%)
   - Senior: 7 jobs (11.7%)
   - Junior: 3 jobs (5.0%)

2. **Top Hiring Companies:**
   - GRAYCE: 3 jobs
   - Diverse hiring across 55 companies (no single dominant employer)

3. **Platform Comparison:**
   - Primary data from LinkedIn
   - Indeed and Glassdoor provide complementary perspectives

4. **Salary Data:**
   - Jobs with salary info: Limited
   - Glassdoor provides best salary transparency

---

## 🔍 Three-Part Analysis

### Part 1: Broad Analysis (✓ COMPLETE)
**60 jobs across 3 platforms**
- Multi-source job scraping
- Market-wide overview
- General trend identification
- See: [Broad Analysis README](./broad-analysis/README.md)

### Part 2: Indeed Deep Dive (○ IN PROGRESS)
**100+ jobs from Indeed**
- Indeed-specific hiring patterns
- Company distribution on Indeed
- Seniority trends specific to Indeed
- Coming soon...

### Part 3: Glassdoor Deep Dive (○ PLANNED)
**100+ jobs from Glassdoor**
- Glassdoor salary analysis (best data source)
- Company ratings correlation
- Salary ranges by role
- Coming soon...

---

## 🚀 How to Use This Project

### View the Analysis
1. **Broad Analysis:** 
   - Check [broad-analysis/README.md](./broad-analysis/README.md) for detailed findings
   - View visualizations in `broad-analysis/*.png`
   - Examine raw data in CSV files

2. **Data Files:**
   - `job_postings_*.csv` - Raw scraped data
   - `jobs_analyzed_*.csv` - Data with analysis
   - Open in Excel, Python, or any CSV viewer

3. **Visualizations:**
   - `job_market_analysis_*.png` - 4-chart dashboard
   - `job_title_keywords_*.png` - Keyword frequency

### Run the Analysis Yourself
```bash
# Prerequisites
pip install requests beautifulsoup4 pandas matplotlib seaborn

# Step 1: Scrape data
python broad-analysis/scraper.py

# Step 2: Create visualizations and analysis
python broad-analysis/day5_visualizations.py
```

---

## 💡 Key Takeaways for Job Seekers

### For Data Analysts
1. **Mid-level is the market** - Most opportunities are for experienced analysts
2. **Competition is distributed** - No single company dominates; apply broadly
3. **Check multiple platforms** - Each platform shows different opportunities
4. **Salary varies widely** - Check Glassdoor for salary insights

### For Career Planning
1. **Build 2-3 years experience** - Mid-level positions value proven track record
2. **Network across companies** - Jobs spread across 55+ companies
3. **Skills to emphasize** - SQL, Python, Excel, Tableau (based on job titles)

---

## 🛠️ Technologies Used

### Data Collection
- **BeautifulSoup** - Parse HTML and extract job data
- **Requests** - Fetch web pages
- **Python 3** - Scripting and automation

### Data Analysis
- **Pandas** - Data manipulation and transformation
- **NumPy** - Numerical computations
- **Collections** - Counter for frequency analysis

### Data Visualization
- **Matplotlib** - Chart creation
- **Seaborn** - Statistical visualizations

### Development
- **Git** - Version control
- **GitHub** - Repository hosting
- **Python virtual environment** - Dependency management

---

## 📈 Project Progression

**Week 1 Status:**
- ✓ Week 1 complete: Broad analysis delivered
- ○ Indeed deep dive: 50% planned
- ○ Glassdoor deep dive: Planned for next week

**Timeline:**
- ✓ Days 1-5: Broad analysis (60 jobs, 3 platforms)
- ○ Next 3-4 days: Indeed deep dive (100+ jobs)
- ○ Following days: Glassdoor deep dive (100+ jobs)

---

## 📝 Data Quality Notes

- **Job Count:** 60 jobs in broad analysis (representative sample)
- **Platforms:** Indeed, LinkedIn, Glassdoor
- **Location:** UK-focused
- **Date:** Data collected January 27, 2026
- **Salary Data:** Limited (requires deeper scraping or individual applications)
- **Updates:** Can be refreshed weekly for trend tracking

---

## 🎓 Learning Outcomes

🎓 Learning Outcomes
By completing this project, I demonstrated:

✓ Web scraping from real websites
✓ Handling multiple data sources
✓ Cleaning and analyzing raw data
✓ Creating professional visualizations
✓ Documenting findings clearly
✓ Version control with Git
✓ Problem-solving (adapting when sites block scrapers)

---

## 🔗 Related Portfolio Projects

This is **Project 1** of a 5-project data analyst portfolio:

1. **Job Market Intelligence** (Current)
2. Charity Impact Analysis (Week 3)
3. Property Price Forecasting (Week 6)
4. University ROI Analysis (Week 9-10)
5. Streaming Wars Full-Stack App (Week 11-12)

---

## 👤 Author
**Mounawasiq**

## 📅 Date Created
January 27, 2026

## ✅ Status
**Week 1: Broad Analysis - COMPLETE**

---

## 📞 Questions?

For detailed analysis findings, see [broad-analysis/README.md](./broad-analysis/README.md)

For upcoming deep dives, check back for Indeed and Glassdoor sub-project documentation.
