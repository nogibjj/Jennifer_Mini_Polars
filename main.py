import polars as pl
import matplotlib.pyplot as plt

# Load job applicant csv file into dataframe
job_applicants_df = pl.read_csv("Job_Applicants_by_Gender_and_Ethnicity.csv")


# Generate a summary of statistics
def stats_overview(job_applicants_df):
    summary_stats = job_applicants_df.select(
        [
            "Apps Received",
            "Black",
            "Hispanic",
            "Asian",
            "Caucasian",
            "American Indian/ Alaskan Native",
            "Filipino",
            "Unknown_Ethnicity",
        ]
    ).describe()
    print(summary_stats)
    return stats_overview


# Generate a table showing the total number of applicants by ethnicity
def total_and_eth_value(job_applicants_df):
    total_and_eth = job_applicants_df.select(
        [
            pl.sum("Apps Received").alias("Apps Received"),
            pl.sum("Black").alias("Black"),
            pl.sum("Hispanic").alias("Hispanic"),
            pl.sum("Asian").alias("Asian"),
            pl.sum("Caucasian").alias("Caucasian"),
            pl.sum("American Indian/ Alaskan Native").alias(
                "American Indian/ Alaskan Native"
            ),
            pl.sum("Filipino").alias("Filipino"),
            pl.sum("Unknown_Ethnicity").alias("Unknown_Ethnicity"),
        ]
    )

    # Add a row name for the total row
    total_and_eth = total_and_eth.with_columns(pl.lit("total").alias("statistic"))
    total_by_value = total_and_eth.select(
        ["statistic"] + [col for col in total_and_eth.columns if col != "statistic"]
    )
    print(total_by_value)
    return total_by_value


# calculate total number of applicants by ethinicity, for plotting
def ethnicity_total():
    ethnicity_total = job_applicants_df[
        [
            "Black",
            "Hispanic",
            "Asian",
            "Caucasian",
            "American Indian/ Alaskan Native",
            "Filipino",
            "Unknown_Ethnicity",
        ]
    ].sum()
    return ethnicity_total


# visualize the total number of applicants by ethnicity
def eth_chart():
    eth_and_total = ethnicity_total()
    eth_and_total = eth_and_total.to_pandas()
    eth_and_total.plot(kind="bar", stacked=False, title="Number of Applicants")
    plt.figure(figsize=(16, 6))
    plt.xlabel("Ethnicity")
    plt.ylabel("Number of Applicants")
    plt.show()
    return eth_chart


if __name__ == "__main__":
    stats_overview(job_applicants_df)
    total_and_eth_value(job_applicants_df)
    ethnicity_total()
    eth_chart()
