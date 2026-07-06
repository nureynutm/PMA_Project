
import pandas as pd

def test_dataset_load():
    df = pd.read_csv("ai_student_impact_dataset.csv")
    assert df.shape[0] > 0

def test_no_missing_values():
    df = pd.read_csv("ai_student_impact_dataset.csv")
    assert df.isnull().sum().sum() == 0
