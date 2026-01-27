"""
Job Market Intelligence - Day 5
Create professional visualizations of insights
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

print("\n" + "="*70)
print("JOB MARKET INTELLIGENCE - DAY 5: CREATE VISUALIZATIONS")
print("="*70)

# ============================================
# LOAD ANALYZED DATA
# ============================================

print("\n[1/4] Loading analyzed data...")
print("-" * 70)

csv_file = "jobs_analyzed_20260127_202840.csv"  # Change to YOUR analyzed CSV

try:
    df = pd.read_csv(csv_file)
    print(f"✓ Loaded {len(df)} jobs")
except FileNotFoundError:
    print(f"✗ File not found: {csv_file}")
    exit()

# ============================================
# SET UP VISUALIZATION STYLE
# ============================================

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 10

# Create figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Data Analyst Job Market Analysis - 60 Jobs', fontsize=16, fontweight='bold')

# ============================================
# CHART 1: JOB LEVEL DISTRIBUTION
# ============================================

print("\n[2/4] Creating Chart 1: Job Level Distribution...")

job_levels = df['job_level'].value_counts()
colors_levels = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
axes[0, 0].bar(job_levels.index, job_levels.values, color=colors_levels[:len(job_levels)])
axes[0, 0].set_title('Job Level Distribution', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Number of Jobs')
axes[0, 0].set_xlabel('Job Level')

# Add value labels on bars
for i, v in enumerate(job_levels.values):
    axes[0, 0].text(i, v + 0.5, str(v), ha='center', fontweight='bold')

# ============================================
# CHART 2: TOP 10 COMPANIES
# ============================================

print("[3/4] Creating Chart 2: Top Companies...")

top_companies = df['company'].value_counts().head(10)
axes[0, 1].barh(range(len(top_companies)), top_companies.values, color='#45B7D1')
axes[0, 1].set_yticks(range(len(top_companies)))
axes[0, 1].set_yticklabels(top_companies.index)
axes[0, 1].set_title('Top 10 Companies Hiring Data Analysts', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Number of Job Postings')
axes[0, 1].invert_yaxis()

# Add value labels
for i, v in enumerate(top_companies.values):
    axes[0, 1].text(v + 0.05, i, str(v), va='center', fontweight='bold')

# ============================================
# CHART 3: JOB LEVEL BY SOURCE
# ============================================

print("[4/4] Creating Chart 3: Source Distribution...")

source_counts = df['source'].value_counts()
colors_sources = ['#FF6B6B', '#4ECDC4', '#45B7D1']
axes[1, 0].pie(source_counts.values, 
               labels=source_counts.index, 
               autopct='%1.1f%%',
               colors=colors_sources[:len(source_counts)],
               startangle=90)
axes[1, 0].set_title('Jobs by Source', fontsize=12, fontweight='bold')

# ============================================
# CHART 4: SALARY DATA AVAILABILITY
# ============================================

print("Creating Chart 4: Salary Information...")

# Count salary availability
salaries_available = len(df[df['salary'] != 'Not listed'])
salaries_unavailable = len(df[df['salary'] == 'Not listed'])

salary_data = [salaries_available, salaries_unavailable]
salary_labels = ['Salary Listed', 'Salary Not Listed']
colors_salary = ['#2ECC71', '#E74C3C']

axes[1, 1].bar(salary_labels, salary_data, color=colors_salary)
axes[1, 1].set_title('Salary Data Availability', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Number of Jobs')

# Add percentage labels
total_jobs = salaries_available + salaries_unavailable
for i, v in enumerate(salary_data):
    pct = (v / total_jobs) * 100
    axes[1, 1].text(i, v + 1, f'{v}\n({pct:.1f}%)', ha='center', fontweight='bold')

# ============================================
# SAVE VISUALIZATION
# ============================================

plt.tight_layout()

visualization_file = f"job_market_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
plt.savefig(visualization_file, dpi=300, bbox_inches='tight')

print("\n" + "="*70)
print("✓ VISUALIZATION CREATED")
print("="*70)
print(f"\n✓ Saved to: {visualization_file}")
print(f"✓ High quality (300 DPI) - ready for portfolio")

# ============================================
# CREATE ADDITIONAL DETAILED CHARTS
# ============================================

print("\n[BONUS] Creating additional detailed charts...")

# Chart 5: Job Title Keywords
fig2, ax = plt.subplots(figsize=(12, 6))

# Extract keywords from titles
title_words = []
for title in df['title']:
    words = str(title).lower().split()
    title_words.extend(words)

# Count common words
from collections import Counter
word_counts = Counter(title_words)

# Filter for meaningful words
stop_words = {'and', 'or', 'the', 'a', 'of', 'in', 'to', 'with', 'for', 'is', 'an', '-'}
meaningful_words = {w: c for w, c in word_counts.items() if w not in stop_words and len(w) > 3}

# Get top 15 words
top_words = sorted(meaningful_words.items(), key=lambda x: x[1], reverse=True)[:15]
words, counts = zip(*top_words)

ax.barh(words, counts, color='#9B59B6')
ax.set_title('Most Common Words in Job Titles', fontsize=14, fontweight='bold')
ax.set_xlabel('Frequency')
ax.invert_yaxis()

for i, v in enumerate(counts):
    ax.text(v + 0.1, i, str(v), va='center', fontweight='bold')

plt.tight_layout()
keywords_file = f"job_title_keywords_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
plt.savefig(keywords_file, dpi=300, bbox_inches='tight')

print(f"✓ Saved keywords chart to: {keywords_file}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "="*70)
print("✓✓✓ WEEK 1 COMPLETE! ✓✓✓")
print("="*70)

print("\nYou have created:")
print(f"  ✓ {visualization_file}")
print(f"    - Job level distribution")
print(f"    - Top 10 companies hiring")
print(f"    - Source distribution (Indeed, LinkedIn, Glassdoor)")
print(f"    - Salary data availability")
print(f"\n  ✓ {keywords_file}")
print(f"    - Most common words in job titles")

print("\n" + "="*70)
print("WEEK 1 DELIVERABLES SUMMARY")
print("="*70)

print(f"\n📊 Project 1: Job Market Intelligence - COMPLETE")
print(f"\n✓ Code:")
print(f"  - scraper.py (web scraping)")
print(f"  - day4_analysis.py (market analysis)")
print(f"  - day5_visualizations.py (charts)")

print(f"\n✓ Data Files:")
print(f"  - job_postings_20260127_202057.csv (60 jobs)")
print(f"  - jobs_analyzed_20260127_202840.csv (analyzed)")

print(f"\n✓ Visualizations:")
print(f"  - job_market_analysis_*.png (4-chart dashboard)")
print(f"  - job_title_keywords_*.png (keyword analysis)")

print(f"\n✓ GitHub:")
print(f"  - All code pushed to: github.com/mounawasiq/job-market-intelligence")

print(f"\n📈 KEY INSIGHTS:")
print(f"  - 60 jobs analyzed")
print(f"  - 83% are mid-level positions")
print(f"  - 55 different companies hiring")
print(f"  - Most common role: 'Data Analyst'")
print(f"  - LinkedIn: primary job source")

print("\n" + "="*70)
print("READY FOR WEEK 2!")
print("="*70)

print("\nNext: Project 2 - Real Charity Data Analysis")
print("  - SQL queries")
print("  - Real organizational data")
print("  - Reference letter from organization")
print("\n✓ You've earned your rest. Great work!")
print("\n" + "="*70 + "\n")