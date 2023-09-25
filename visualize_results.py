### Show Average ###########################################

import matplotlib.pyplot as plt
import numpy as np

# Data
languages = ["Python", "C++", "Rust"]
problems = ["contains-duplicate", "valid-anagram", "two-sum", "valid-palindrome", "best-time-to-buy-and-sell-stock", "valid-parentheses", "binary-search", "reverse-linked-list", "invert-binary-tree", "maximum-depth-of-binary-tree"]
time_ms = {
    "Python": [430, 51, 53, 50, 904, 15, 219, 45, 40, 50],
    "C++": [96, 4, 15, 4, 95, 0, 0, 7, 0, 8],
    "Rust": [18, 1, 2, 2, 9, 0, 64, 1, 0, 1],
}
memory_mb = {
    "Python": [29.2, 16.7, 17.7, 17.2, 27.2, 13.4, 17.8, 17.8, 16.2, 18.5],
    "C++": [51.4, 7.3, 10.9, 7.3, 93.6, 6.4, 2.1, 8.2, 10.1, 19.3],
    "Rust": [3.7, 2.1, 2.3, 2.8, 2.9, 1.9, 27.4, 2.4, 2, 2.5],
}

# Specify colors
colors = {
    "Python": "yellow",
    "C++": "blue",
    "Rust": "orange",
}

# Compute average time and memory for each language
avg_time_ms = [np.mean(time_ms[lang]) for lang in languages]
avg_memory_mb = [np.mean(memory_mb[lang]) for lang in languages]

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Average Time (ms) bar chart
ax1.bar(languages, avg_time_ms, width=0.4, color=[colors[lang] for lang in languages], alpha=0.7)
ax1.set_ylabel("Average Time (ms)")
ax1.set_title("Average Performance: Time (ms)")

# Average Memory (MB) bar chart
ax2.bar(languages, avg_memory_mb, width=0.4, color=[colors[lang] for lang in languages], alpha=0.7)
ax2.set_ylabel("Average Memory (MB)")
ax2.set_title("Average Performance: Memory (MB)")

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()

### Show Individual ###

# import matplotlib.pyplot as plt
# import numpy as np

# # Define the data
# languages = ["Python", "C++", "Rust"]
# problems = ["contains-duplicate", "valid-anagram", "two-sum", "valid-palindrome", "best-time-to-buy-and-sell-stock", "valid-parentheses", "binary-search", "reverse-linked-list", "invert-binary-tree", "maximum-depth-of-binary-tree"]
# time_ms = {
#     "Python": [430, 51, 53, 50, 904, 15, 219, 45, 40, 50],
#     "C++": [96, 4, 15, 4, 95, 0, 0, 7, 0, 8],
#     "Rust": [18, 1, 2, 2, 9, 0, 64, 1, 0, 1],
# }
# memory_mb = {
#     "Python": [29.2, 16.7, 17.7, 17.2, 27.2, 13.4, 17.8, 17.8, 16.2, 18.5],
#     "C++": [51.4, 7.3, 10.9, 7.3, 93.6, 6.4, 2.1, 8.2, 10.1, 19.3],
#     "Rust": [3.7, 2.1, 2.3, 2.8, 2.9, 1.9, 27.4, 2.4, 2, 2.5],
# }

# # Create subplots for time and memory
# fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# # Time metrics
# axs[0].bar(np.arange(len(problems)), time_ms["Python"], width=0.2, label="Python", align="center")
# axs[0].bar(np.arange(len(problems)) - 0.2, time_ms["C++"], width=0.2, label="C++", align="center")
# axs[0].bar(np.arange(len(problems)) + 0.2, time_ms["Rust"], width=0.2, label="Rust", align="center")
# axs[0].set_title("Time (ms)")
# axs[0].set_xticks(np.arange(len(problems)))
# axs[0].set_xticklabels(problems, rotation=90)
# axs[0].legend()

# # Memory metrics
# axs[1].bar(np.arange(len(problems)), memory_mb["Python"], width=0.2, label="Python", align="center")
# axs[1].bar(np.arange(len(problems)) - 0.2, memory_mb["C++"], width=0.2, label="C++", align="center")
# axs[1].bar(np.arange(len(problems)) + 0.2, memory_mb["Rust"], width=0.2, label="Rust", align="center")
# axs[1].set_title("Memory (MB)")
# axs[1].set_xticks(np.arange(len(problems)))
# axs[1].set_xticklabels(problems, rotation=90)
# axs[1].legend()

# plt.tight_layout()
# plt.show()


