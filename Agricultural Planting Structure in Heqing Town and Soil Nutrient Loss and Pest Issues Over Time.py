# Copyright (c) 2025 Kang Kai
# Date: March 17, 2025
# 
# Project: Agricultural Planting Structure in Heqing Town and Soil Nutrient Loss and Pest Issues Over Time
# Chart IV-c
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

categories = ['Rice', 'Vegetables', 'Other Crops']
planting_area = [77, 15, 8]

years = np.arange(2018, 2024)
nutrient_loss = np.array([26, 29, 31, 35, 34, 33])
pest_issues = np.array([17, 18, 21, 27, 33, 35])

trend_nutrient = np.polyfit(years, nutrient_loss, 1)
trend_pest = np.polyfit(years, pest_issues, 1)

trend_nutrient_line = np.poly1d(trend_nutrient)(years)
trend_pest_line = np.poly1d(trend_pest)(years)

sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 12, 'axes.labelsize': 14, 'axes.titlesize': 16})

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))
fig.subplots_adjust(hspace=0.6) 

bar_colors = ['#66b3ff', '#99ff99', '#ffcc99']
bars = ax1.bar(categories, planting_area, color=bar_colors, edgecolor='black', hatch=['/', 'x', '\\'], width=0.6)

ax1.set_title('Agricultural Planting Structure', fontsize=18, pad=20, fontweight='bold')
ax1.set_ylabel('Percentage of Total Cultivated Area (%)', fontsize=14)
ax1.set_ylim(0, 100)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

for bar, value in zip(bars, planting_area):
    ax1.text(bar.get_x() + bar.get_width()/2, value + 2, f'{value}%', ha='center', va='bottom', fontsize=14, fontweight='bold')

ax2.plot(years, nutrient_loss, marker='o', markersize=8, linestyle='-', color='#ff6666', label='Soil Nutrient Loss (%)', linewidth=2)
ax2.plot(years, pest_issues, marker='s', markersize=8, linestyle='-', color='#6666ff', label='Pest Issue Severity (%)', linewidth=2)

error_range = np.array([2] * len(years))
ax2.errorbar(years, nutrient_loss, yerr=error_range, fmt='o', color='#ff6666', capsize=5, alpha=0.5)
ax2.errorbar(years, pest_issues, yerr=error_range, fmt='s', color='#6666ff', capsize=5, alpha=0.5)

ax2.plot(years, trend_nutrient_line, linestyle='dashed', color='#ff3333', linewidth=1.5, alpha=0.8, label='Nutrient Loss Trend')
ax2.plot(years, trend_pest_line, linestyle='dashed', color='#3333ff', linewidth=1.5, alpha=0.8, label='Pest Issue Trend')

ax2.set_title('Soil Nutrient Loss and Pest Issues Over Time', fontsize=18, pad=20, fontweight='bold')
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Percentage (%)', fontsize=14)
ax2.set_ylim(0, 50)
ax2.grid(True, linestyle='--', alpha=0.7)

for x, y in zip(years, nutrient_loss):
    ax2.text(x, y + 1.5, f'{y}%', ha='center', fontsize=12, fontweight='bold', color='#ff6666')
for x, y in zip(years, pest_issues):
    ax2.text(x, y + 1.5, f'{y}%', ha='center', fontsize=12, fontweight='bold', color='#6666ff')

ax2.legend(loc='upper left', fontsize=13)

plt.tight_layout()
plt.show()
