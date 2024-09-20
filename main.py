import pandas as pd
import matplotlib.pyplot as plt

# Load job applicant csv file into dataframe
job_applicants_df = pd.read_csv("Job_Applicants_by_Gender_and_Ethnicity.csv")


# Calculate total number of applicants
def total_applicants(df):
    total_apps = df["Apps Received"].sum()
    print(f"Total applicants: {total_apps}")
    return total_apps


# calculate total number of applicants by gender
def total_female_applicant(df):
    total_female_applicants = df["Female"].sum()
    print(f"Total female applicants: {total_female_applicants}")
    return total_female_applicants


def total_male_applicant(df):
    total_male_applicants = df["Male"].sum()
    print(f"Total male applicants: {total_male_applicants}")
    return total_male_applicants


gender_total = job_applicants_df[["Female", "Male"]].sum()


# Generate a summary of statistics
# List key indicators, including mean, median, standar deviation
def stats_overview():
    summary_stats = job_applicants_df[["Apps Received", "Female", "Male"]].describe()
    summary_stats.loc["median"] = job_applicants_df[
        ["Apps Received", "Female", "Male"]
    ].median()
    summary_stats.loc["total"] = job_applicants_df[
        ["Apps Received", "Female", "Male"]
    ].sum()
    summary_stats = summary_stats.round(2)
    print(summary_stats)
    return summary_stats


# Data visualization: Gender chart
def gender_chart():
    plt.figure(figsize=(10, 6))
    plt.bar(gender_total.index, gender_total.values)
    plt.title("Number of Applicants by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Number of Applicants")
    plt.show()


if __name__ == "__main__":
    stats_overview()
    total_applicants(job_applicants_df)
    total_female_applicant(job_applicants_df)
    total_male_applicant(job_applicants_df)
    gender_chart()
