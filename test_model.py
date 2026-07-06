import pandas as pd

def test_load():
    df = pd.read_csv("ai_student_impact_dataset.csv")
    assert df.shape[0] > 0

def test_missing():
    df = pd.read_csv("ai_student_impact_dataset.csv")
    assert df.isnull().sum().sum() == 0
