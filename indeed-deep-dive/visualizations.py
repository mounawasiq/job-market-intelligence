"""
Job Market Intelligence - LinkedIn Visualization & Analysis
Analyzes LinkedIn job data and creates professional visualizations
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from collections import Counter
import re

print("\n" + "="*70)
print("JOB MARKET INTELLIGENCE - LINKEDIN ANALYSIS & VISUALIZATION")
print("="*70)

# ============================================
# LOAD CSV
# ============================================

print("\n[1/5] Loading job data...")
print("-" * 70)

csv_file = "job_postings_20260128_072356.csv"  # CHANGE THIS TO YOUR CSV FILENAME

try:
    df = pd.read_csv(csv_file)
    print(f"✓ Loaded {len(df)} jobs")
except FileNotFoundError:
    print(f"✗ File not found: {csv_file}")
    exit()

# ============================================
# ANALYZE JOB TITLES - ADD JOB LEVEL
# ============================================

print("\n[2/5] Analyzing job titles...")
print("-" * 70)

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
    print(f"  {level:15s} - {count:3d} jobs ({pct:5.1f}%)")

# ============================================
# ANALYZE COMPANIES
# ============================================

print("\n[3/5] Analyzing top companies...")
print("-" * 70)

company_counts = df['company'].value_counts().head(15)
print(f"\nTop 15 companies hiring:")
for idx, (company, count) in enumerate(company_counts.items(), 1):
    pct = (count / len(df)) * 100
    print(f"  {idx:2d}. {company:30s} - {count:3d} jobs ({pct:5.1f}%)")

# ============================================
# CREATE VISUALIZATIONS
# ============================================

print("\n[4/5] Creating visualizations...")
print("-" * 70)

sns.set_style("whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('LinkedIn Job Market Analysis - 240 Jobs', fontsize=16, fontweight='bold')

# Chart 1: Job Level Distribution
job_levels = df['job_level'].value_counts()
colors_levels = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
axes[0, 0].bar(job_levels.index, job_levels.values, color=colors_levels[:len(job_levels)])
axes[0, 0].set_title('Job Level Distribution', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Number of Jobs')
axes[0, 0].set_xlabel('Job Level')

for i, v in enumerate(job_levels.values):
    axes[0, 0].text(i, v + 1, str(v), ha='center', fontweight='bold')

# Chart 2: Top 10 Companies
top_10_companies = df['company'].value_counts().head(10)
axes[0, 1].barh(range(len(top_10_companies)), top_10_companies.values, color='#45B7D1')
axes[0, 1].set_yticks(range(len(top_10_companies)))
axes[0, 1].set_yticklabels(top_10_companies.index)
axes[0, 1].set_title('Top 10 Companies Hiring', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Number of Job Postings')
axes[0, 1].invert_yaxis()

for i, v in enumerate(top_10_companies.values):
    axes[0, 1].text(v + 0.2, i, str(v), va='center', fontweight='bold')

# Chart 3: Source Distribution (if multiple sources)
source_counts = df['source'].value_counts()
colors_sources = ['#FF6B6B', '#4ECDC4', '#45B7D1']
axes[1, 0].pie(source_counts.values, 
               labels=source_counts.index, 
               autopct='%1.1f%%',
               colors=colors_sources[:len(source_counts)],
               startangle=90)
axes[1, 0].set_title('Jobs by Source', fontsize=12, fontweight='bold')

# Chart 4: Job Level by Source
source_level = pd.crosstab(df['source'], df['job_level'])
source_level.plot(kind='bar', ax=axes[1, 1], color=colors_levels[:len(job_levels)])
axes[1, 1].set_title('Job Level Distribution by Source', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Number of Jobs')
axes[1, 1].set_xlabel('Source')
axes[1, 1].legend(title='Job Level')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()

# Save visualization
viz_filename = f"linkedin_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
plt.savefig(viz_filename, dpi=300, bbox_inches='tight')
print(f"\n✓ Saved visualization to: {viz_filename}")

# ============================================
# SAVE ANALYZED DATA
# ============================================

print("\n[5/5] Saving analyzed data...")
print("-" * 70)

analyzed_filename = f"linkedin_analyzed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
df.to_csv(analyzed_filename, index=False)
print(f"✓ Saved analyzed data to: {analyzed_filename}")

# ============================================
# FINAL INSIGHTS
# ============================================

print("\n" + "="*70)
print("✓✓✓ KEY INSIGHTS - LINKEDIN DEEP DIVE ✓✓✓")
print("="*70)

print(f"\n📊 1. MARKET OVERVIEW:")
print(f"   Total jobs analyzed: {len(df)}")
print(f"   Data sources: {len(source_counts)} ({', '.join(source_counts.index)})")
print(f"   Companies hiring: {df['company'].nunique()}")

print(f"\n💼 2. SENIORITY DISTRIBUTION:")
top_level = job_levels.index[0]
top_level_count = job_levels.iloc[0]
print(f"   Most common: {top_level} ({top_level_count} jobs, {top_level_count/len(df)*100:.1f}%)")
level_mapping = {
    'Mid-Level': 'Most jobs are mid-level positions',
    'Junior': 'Most jobs are entry-level',
    'Senior': 'Most jobs are senior positions',
    'Management': 'Most jobs are management positions'
}
print(f"   Insight: {level_mapping.get(top_level, 'Mixed distribution')}")

print(f"\n🏢 3. HIRING HOTSPOTS:")
print(f"   Top company: {company_counts.index[0]} ({company_counts.iloc[0]} jobs)")
top_5_total = company_counts.head(5).sum()
print(f"   Top 5 companies have {top_5_total}/{len(df)} jobs ({top_5_total/len(df)*100:.1f}%)")

print(f"\n🌐 4. SOURCE BREAKDOWN:")
for source, count in source_counts.items():
    pct = (count / len(df)) * 100
    print(f"   {source:15s}: {count:3d} jobs ({pct:5.1f}%)")

print(f"\n✅ 5. NEXT STEPS:")
print(f"   → Review visualizations")
print(f"   → Create README documentation")
print(f"   → Push to GitHub")

print("\n" + "="*70)
print(f"✓ Analysis complete!")
print("="*70 + "\n")