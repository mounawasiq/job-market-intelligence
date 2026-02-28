# Job Market Intelligence

**Web scraping job postings and analyzing skill demand

A comprehensive data analysis project examining the UK data analyst job market across multiple platforms. This portfolio demonstrates web scraping, data analysis, visualization, and market research skills.

---

## 📋 Project Overview

Comprehensive analysis of data analyst job market in the UK by collecting and analyzing job postings from major hiring platforms.

**Duration:** Week 1 of portfolio (January 2026)  
**Status:** ✓ Broad Analysis Complete | ✓ LinkedIn Deep Dive Complete | Project 1 FINISHED

---

## 🎯 What This Project Shows

### Skills Demonstrated
- ✓ Web Scraping - Collecting real data from multiple websites
- ✓ Data Analysis - Extracting insights from raw job data
- ✓ Data Visualization - Creating professional charts and reports
- ✓ Python Programming - Writing production-quality scripts
- ✓ Git & GitHub - Version control and code management
- ✓ Problem Solving - Adapting to different data sources and blocking

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
│   ├── scraper.py                    # Web scraper (LinkedIn)
│   ├── visualizations.py             # Chart generation
│   ├── job_postings_*.csv            # Raw job data (60 jobs)
│   ├── jobs_analyzed_*.csv           # Analyzed data
│   ├── job_market_analysis_*.png     # Dashboard (4 charts)
│   ├── job_title_keywords_*.png      # Keyword analysis
│   └── README.md                     # Detailed documentation
│
├── indeed-deep-dive/
│   ├── scraper_linkedin.py           # LinkedIn scraper (240 jobs)
│   ├── visualizations.py             # Visualization script
│   ├── job_postings_*.csv            # LinkedIn jobs data
│   ├── linkedin_analyzed_*.csv       # Analyzed data
│   ├── linkedin_analysis_*.png       # Charts
│   └── README.md                     # Deep dive documentation
│
└── README.md                         # This file
```

---

## 📊 Current Findings

### Market Overview
- **60 jobs** analyzed in broad analysis (3 platforms: Indeed, LinkedIn, Glassdoor)
- **240 jobs** analyzed in LinkedIn deep dive
- **55+ companies** actively hiring for data analyst roles
- **83% mid-level positions** (most opportunities are mid-career)
- **Limited salary transparency** (most jobs don't list salary)

### Key Insights

**Seniority Distribution:**
- Mid-Level: 50 jobs (83.3%)
- Senior: 7 jobs (11.7%)
- Junior: 3 jobs (5.0%)

**Top Hiring Companies:**
- GRAYCE: 3 jobs
- Diverse hiring across 55+ companies (no single dominant employer)

**Platform Insights:**
- Indeed: Blocked by anti-scraping measures (HTTP 403)
- LinkedIn: Successful - 240 jobs extracted
- Glassdoor: Blocked by anti-scraping measures (HTTP 403)

**Salary Data:**
- Limited transparency across platforms
- Glassdoor has best salary information (when accessible)

---

## 🔍 Two-Part Analysis

### Part 1: Broad Analysis (✓ COMPLETE)
**60 jobs across 3 platforms**
- Multi-source job scraping
- Market-wide overview
- General trend identification
- See: [Broad Analysis README](./broad-analysis/README.md)

### Part 2: LinkedIn Deep Dive (✓ COMPLETE)
**240 jobs from LinkedIn**
- Extended LinkedIn dataset
- Platform-specific hiring patterns
- Company distribution analysis
- Seniority trends
- See: [LinkedIn Deep Dive README](./indeed-deep-dive/README.md)

**Note on Glassdoor:** Attempted scraping but faced anti-scraping measures (HTTP 403 blocking). Focused on LinkedIn deep dive analysis instead, providing comprehensive data for comparative insights.

---

## 🚀 How to Use This Project

### View the Analysis

1. **Broad Analysis:**
   - Check [broad-analysis/README.md](./broad-analysis/README.md) for detailed findings
   - View visualizations in `broad-analysis/*.png`
   - Examine raw data in CSV files

2. **LinkedIn Deep Dive:**
   - Check [indeed-deep-dive/README.md](./indeed-deep-dive/README.md) for insights
   - View visualizations in `indeed-deep-dive/*.png`
   - Examine analyzed data in `linkedin_analyzed_*.csv`

3. **Data Files:**
   - `job_postings_*.csv` - Raw scraped data
   - `*_analyzed_*.csv` - Data with analysis
   - Open in Excel, Python, or any CSV viewer

4. **Visualizations:**
   - `*_analysis_*.png` - Professional dashboards
   - `*_keywords_*.png` - Keyword frequency analysis

### Run the Analysis Yourself

```bash
# Prerequisites
pip install requests beautifulsoup4 pandas matplotlib seaborn

# Broad Analysis
# Step 1: Scrape data
python broad-analysis/scraper.py

# Step 2: Create visualizations
python broad-analysis/visualizations.py

# LinkedIn Deep Dive
# Step 1: Scrape data
python indeed-deep-dive/scraper_linkedin.py

# Step 2: Create visualizations
python indeed-deep-dive/visualizations.py
```

---

## 💡 Key Takeaways for Job Seekers

### For Data Analysts
1. **Mid-level is the market** - Most opportunities are for experienced analysts
2. **Competition is distributed** - No single company dominates; apply broadly
3. **Check multiple platforms** - Each platform shows different opportunities
4. **Salary varies widely** - Research thoroughly before applying

### For Career Planning
1. **Build 2-3 years experience** - Mid-level positions value proven track record
2. **Network across companies** - Jobs spread across 55+ companies
3. **Skills to emphasize** - SQL, Python, Excel, Tableau (based on job titles)

---

## 🛠️ Technologies Used

### Data Collection
- BeautifulSoup - Parse HTML and extract job data
- Requests - Fetch web pages
- Python 3 - Scripting and automation

### Data Analysis
- Pandas - Data manipulation and transformation
- Collections - Counter for frequency analysis

### Data Visualization
- Matplotlib - Chart creation
- Seaborn - Statistical visualizations

### Development
- Git - Version control
- GitHub - Repository hosting
- Python virtual environment - Dependency management

---

## 📈 Project Progression

**Week 1 Status:**
- ✓ Broad analysis: Complete (60 jobs)
- ✓ LinkedIn deep dive: Complete (240 jobs)
- ✓ Project 1: FINISHED

**Technical Challenges Overcome:**
- Adapted to Indeed's anti-scraping measures
- Successfully pivoted to LinkedIn for comprehensive analysis
- Built robust error handling for different website structures

---

## 📝 Data Quality Notes

- **Job Count:** 60 jobs in broad analysis + 240 jobs in deep dive
- **Primary Platform:** LinkedIn (successful scraping)
- **Attempted Platforms:** Indeed, Glassdoor (blocked by anti-scraping)
- **Location:** UK-focused
- **Date Collected:** January 27-28, 2026
- **Salary Data:** Limited (requires deeper scraping or individual applications)
- **Updates:** Can be refreshed weekly for trend tracking

---

## 🎓 Learning Outcomes

By completing this project, I demonstrated:

- ✓ Web scraping from real websites
- ✓ Handling multiple data sources
- ✓ Cleaning and analyzing raw data
- ✓ Creating professional visualizations
- ✓ Documenting findings clearly
- ✓ Version control with Git
- ✓ Problem-solving (adapting when sites block scrapers)
- ✓ Real-world data challenges and solutions

---

## 👤 Author
Mounawasiq

## 📅 Date Created
January 27, 2026

## ✅ Status
**Project 1: COMPLETE** ✓

---

## 📞 Questions?

For detailed analysis findings:
- See [broad-analysis/README.md](./broad-analysis/README.md)
- See [indeed-deep-dive/README.md](./indeed-deep-dive/README.md)
