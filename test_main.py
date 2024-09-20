"""
Test goes here

"""

from main import total_applicants, total_female_applicant, total_male_applicant

import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
Data = {
    "Apps Received": [100, 200, 150],
    "Female": [40, 80, 70],
    "Male": [60, 110, 80],
}

sample_df = pd.DataFrame(Data)


# Function tests
def test_total_applicants():
    assert total_applicants(sample_df) == 450
    print("total_applicants test passed!")


def test_female_applicants():
    assert total_female_applicant(sample_df) == 190
    print("total_female_applicants test passed!")


def test_male_applicants():
    assert total_male_applicant(sample_df) == 250
    print("total_male_applicants test passed!")


if __name__ == "__main__":
    test_total_applicants()
    test_female_applicants()
    test_male_applicants()
    print("All tests passed!")
