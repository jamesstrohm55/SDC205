# SDC205 - Event Manager for a Country Club
# Displays ballroom capacity table, a bar graph of capacities,
# and a pie chart of the attendee demographics.

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # non-interactive backend; figures are saved to PNG files
import matplotlib.pyplot as plt

# --- Print Student ID -------------------------------------------------
# TODO: Replace the value below with your actual Student ID.
student_id = "0000000"
print("Student ID:", student_id)

# --- Data -------------------------------------------------------------
ballrooms = ["Ballroom 1", "Ballroom 2", "Ballroom 3"]
capacities = [25000, 11000, 5000]

demographics = ["Children", "Adults", "Teens"]
demographic_counts = [18000, 13000, 10000]

# --- Print a table of ballroom capacities -----------------------------
capacity_table = pd.DataFrame({
    "Ballroom": ballrooms,
    "Capacity": capacities
})

print("\nBallroom Capacity Table")
print(capacity_table.to_string(index=False))

# --- Bar graph of ballroom capacities ---------------------------------
plt.figure()
plt.bar(ballrooms, capacities, color=["steelblue", "seagreen", "indianred"])
plt.title("Capacity of Each Ballroom")
plt.xlabel("Ballroom")
plt.ylabel("Number of People")
plt.savefig("ballroom_bar_graph.png")
plt.close()
print("\nSaved bar graph to ballroom_bar_graph.png")

# --- Pie chart of attendee demographics -------------------------------
plt.figure()
plt.pie(demographic_counts, labels=demographics, autopct="%1.1f%%",
        colors=["gold", "lightskyblue", "lightcoral"])
plt.title("Attendee Breakdown for the Day")
plt.axis("equal")  # keeps the pie chart circular
plt.savefig("attendee_pie_chart.png")
plt.close()
print("Saved pie chart to attendee_pie_chart.png")
