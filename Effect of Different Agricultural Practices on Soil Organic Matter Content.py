# Copyright (c) 2025 Kang Kai
# Date: March 17, 2025
#
# Project: Effect of Different Agricultural Practices on Soil Organic Matter Content
# Chart IV-a, b
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

treatments = ['No Fertilizer', 'Chemical Fertilizer', 'Organic Fertilizer', 'Integrated Fertilizer']
soil_organic_matter = [1.2, 1.5, 2.1, 2.4]

plt.figure(figsize=(10, 6))
bars = plt.bar(treatments, soil_organic_matter, color=['gray', 'blue', 'green', 'purple'])

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.1f}", ha='center', va='bottom', fontsize=12)

plt.xlabel('Treatment')
plt.ylabel('Soil Organic Matter (%)')
plt.title('Effect of Different Agricultural Practices on Soil Organic Matter Content')
plt.ylim(0, 3)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
