import pandas as pd
from app import app
import os


def retrieve_limits(color_type):
    df = pd.read_csv(os.path.join(app.config["STATIC_FOLDER"], f"lower_limit_{color_type}.csv"))
    lower_data = {"x": list(df.input), "y": list(df.output), "type": "scatter", "name": "LOWER_LIMIT_{}".format(color_type.upper())}
    df = pd.read_csv(os.path.join(app.config["STATIC_FOLDER"], f"upper_limit_{color_type}.csv"))
    upper_data = {"x": list(df.input), "y": list(df.output), "type": "scatter", "name": "UPPER_LIMIT_{}".format(color_type.upper())}
    return lower_data, upper_data
