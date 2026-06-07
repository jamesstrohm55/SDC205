import pandas as pd                    # import pandas for DataFrames and MultiIndex
import numpy as np                     # import numpy to generate the grade values
import matplotlib.pyplot as plt        # import matplotlib's pyplot for the bar graph


def main():
    print("Student ID: jamstr4441")

    # Step 2: store a roster of 10 students in an array (list)
    students = ["Ana", "Bruno", "Carla", "Diego", "Elena",
                "Felipe", "Gabriela", "Hugo", "Isabela", "Joao"]

    # Step 3: build a MultiIndex pairing each student with each subject.
    # product() creates every student+subject combination (10 students x 2 subjects = 20 rows).
    subjects = ["Math", "Science"]
    index = pd.MultiIndex.from_product([students, subjects], names=["Student", "Subject"])

    # Step 4: create a DataFrame of grades, one grade per student per subject.
    # 20 random grades between 60 and 100 are generated to fill the 20 index rows.
    grades = np.random.randint(60, 101, size=20)
    df = pd.DataFrame(grades, index=index, columns=["Grade"])

    # Step 5: display the full DataFrame to the console.
    print(df)

    # Step 6: group by the Subject index level and calculate the mean grade for each subject.
    subject_means = df.groupby(level="Subject").mean()
    print(subject_means)

    # Step 7: display a vertical bar graph of the average grade per subject.
    subject_means.plot(kind="bar", legend=False, color="g")
    plt.title("jamstr4441 Average Grade by Subject")  # chart title with student ID
    plt.xlabel("Subject")                              # x-axis label
    plt.ylabel("Average Grade")                        # y-axis label
    plt.xticks(rotation=0)                             # keep subject labels upright
    plt.tight_layout()                                 # prevent labels getting cut off
    plt.show()                                         # render the graph


main()   # run the program