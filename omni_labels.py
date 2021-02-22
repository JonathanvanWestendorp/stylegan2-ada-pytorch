import numpy as np
import pandas as pd
import json

def convert_to_float(x):
    try:
        return float(x)
    except:
        return -1

def main():
    labels = []
    omniart = pd.read_csv("./omniart/omniart_v3_datadump.csv", chunksize=10000)
    for chunk in omniart:
        chunk = chunk.fillna(0)
        chunk["century"][chunk["century"].apply(lambda x: convert_to_float(x)) < 0] = 0
        for _, row in chunk.iterrows():
            labels.append((str(row["omni_id"])+".jpg", int(float(row["century"]))))

    with open("dataset.json", "w") as outfile:
        json.dump({'labels': labels}, outfile)

if __name__ == "__main__":
    main()