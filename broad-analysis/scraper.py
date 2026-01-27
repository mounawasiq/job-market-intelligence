"""
Job Market Intelligence - Day 4 (Revised)
Analyze job titles, companies, and salary trends
"""

import pandas as pd
from datetime import datetime
from collections import Counter
import re

print("\n" + "="*70)
print("JOB MARKET INTELLIGENCE - DAY 4: ANALYZE JOB MARKET")
print("="*70)

# ============================================
# LOAD CSV
# ============================================

print("\n[1/5] Loading job data...")
print("-" * 70)

csv_file = "job_postings_20260127_202057.csv"

try:
    df = pd.read_csv(csv_file)
    print(f"✓ Loaded {len(df)} jobs")
except FileNotFoundError:
    print(f"✗ File not found: {csv_file}")
    exit()

# ============================================
# ANALYZE JOB TITLES
# ============================================

print("\n[2/5] Analyzing job titles...")
print("-" * 70)

# Extract job level from title
def get_job_level(title):
    """Determine seniority level from title"""
    title_lower = title.lower()
    if 'senior' in title_lower or 'principal' in title_lower or 'lead' in title_lower:
        return 'Senior'
    elif 'junior' in title_lower or 'entry' in title_lower or 'graduate' in title_lower:
        return 'Junior'
    elif 'manager' in title_lower or 'head' in title_lower:
        return 'Management'
    else:
        return 'Mid-Level'

df['job_level'] = df['title'].apply(get_job_level)

# Count job levels
job_levels = df['job_level'].value_counts()
print(f"\nJob levels found:")
for level, count in job_levels.items():
    pct = (count / len(df)) * 100
    print(f"  {level:15s} - {count:2d} jobs ({pct:5.1f}%)")

# ============================================
# ANALYZE COMPANIES
# ============================================

print("\n[3/5] Analyzing top companies hiring...")
print("-" * 70)

# Count jobs by company
company_counts = df['company'].value_counts().head(15)
print(f"\nTop 15 companies hiring data analysts:")
for idx, (company, count) in enumerate(company_counts.items(), 1):
    print(f"  {idx:2d}. {company:30s} - {count:2d} jobs")

# ============================================
# ANALYZE SALARY DATA
# ============================================

print("\n[4/5] Analyzing salary information...")
print("-" * 70)

# Extract salary ranges where available
salaries_available = df[df['salary'] != 'Not listed']
print(f"\nSalary data available for {len(salaries_available)}/{len(df)} jobs ({len(salaries_available)/len(df)*100:.1f}%)")

if len(salaries_available) > 0:
    print(f"\nSample salaries found:")
    for idx in range(min(10, len(salaries_available))):
        title = salaries_available.iloc[idx]['title']
        salary = salaries_available.iloc[idx]['salary']
        print(f"  {title[:40]:40s} - {salary}")
else:
    print("  (No salary data in this dataset)")

# ============================================
# ANALYZE JOB SOURCES
# ============================================

print("\n[5/5] Analyzing data sources...")
print("-" * 70)

source_counts = df['source'].value_counts()
print(f"\nJobs by source:")
for source, count in source_counts.items():
    pct = (count / len(df)) * 100
    bar = "█" * int(count/2)
    print(f"  {source:15s} - {count:2d} jobs ({pct:5.1f}%) {bar}")

# ============================================
# SAVE ANALYSIS
# ============================================

print("\n" + "="*70)
print("SAVING ANALYSIS RESULTS")
print("="*70)

# Save with job level added
analysis_filename = f"jobs_analyzed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
df.to_csv(analysis_filename, index=False)
print(f"\n✓ Saved analyzed data to: {analysis_filename}")

# ============================================
# FINAL INSIGHTS
# ============================================

print("\n" + "="*70)
print("✓✓✓ KEY INSIGHTS FROM DATA ANALYST JOB MARKET ✓✓✓")
print("="*70)

print(f"\n📊 1. JOB MARKET OVERVIEW:")
print(f"   Total jobs analyzed: {len(df)}")
print(f"   Data sources: {len(source_counts)} (Indeed, LinkedIn, Glassdoor)")
print(f"   Companies hiring: {df['company'].nunique()}")

print(f"\n💼 2. SENIORITY DISTRIBUTION:")
top_level = job_levels.index[0]
top_level_count = job_levels.iloc[0]
print(f"   Most common: {top_level} ({top_level_count} jobs, {top_level_count/len(df)*100:.1f}%)")
print(f"   This means: {['Most jobs are mid-level positions', 'Most jobs are entry-level', 'Most jobs are senior positions', 'Most jobs are management'][['Mid-Level', 'Junior', 'Senior', 'Management'].index(top_level)]}")

print(f"\n🏢 3. HIRING HOTSPOTS:")
print(f"   Top hiring company: {company_counts.index[0]} ({company_counts.iloc[0]} jobs)")
print(f"   Market concentration: Top 5 companies have {company_counts.head(5).sum()}/{len(df)} jobs ({company_counts.head(5).sum()/len(df)*100:.1f}%)")

print(f"\n💰 4. SALARY DATA:")
if len(salaries_available) > 0:
    print(f"   {len(salaries_available)}/{len(df)} jobs list salary information")
    print(f"   (Data sites vary in salary transparency)")
else:
    print(f"   Limited salary data in this dataset")

print(f"\n🌐 5. MARKET DISTRIBUTION:")
for source, count in source_counts.items():
    pct = (count / len(df)) * 100
    print(f"   {source:15s}: {count:2d} jobs ({pct:5.1f}%)")

print(f"\n✅ 6. NEXT STEPS:")
print(f"   → Day 5: Create visualizations of these insights")
print(f"   → Generate charts showing job levels, companies, salary ranges")
print(f"   → Build portfolio narrative: 'What data analysts need'")

print("\n" + "="*70)
print(f"✓ Analysis complete!")
print("="*70 + "\n")