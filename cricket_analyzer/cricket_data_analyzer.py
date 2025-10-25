import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("players_stats.csv")

print("\n--- Cricket Player Stats ---")
print(df.head())

# Top batsmen by average
top_batsmen = df.sort_values(by="Average", ascending=False).head(3)
print("\n🏏 Top 3 Batsmen by Average:")
print(top_batsmen[["Player", "Average"]])

# Top bowlers by wickets
top_bowlers = df.sort_values(by="Wickets", ascending=False).head(3)
print("\n🎯 Top 3 Bowlers by Wickets:")
print(top_bowlers[["Player", "Wickets"]])

# Plot 1: Runs comparison
plt.figure(figsize=(8, 5))
plt.bar(df["Player"], df["Runs"], color='green')
plt.title("Total Runs by Players")
plt.xlabel("Players")
plt.ylabel("Runs Scored")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Plot 2: Wickets comparison
plt.figure(figsize=(8, 5))
plt.bar(df["Player"], df["Wickets"], color='blue')
plt.title("Total Wickets by Players")
plt.xlabel("Players")
plt.ylabel("Wickets Taken")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

