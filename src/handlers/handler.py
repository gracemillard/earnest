from processor.processor import FileProcessor
from common.filter_params import FilterParams
import pandas as pd
import json


def main(file):
    if not file:
        raise ValueError("Empty, cannot proceed")

    json_config_path="resources/filters.json"
    processor = FileProcessor()
    processor.process_files(file,json_config_path)



if __name__ == "__main__":
    file=pd.read_csv("resources/bank_enriched_addresses.csv")
    main(file)

    print("processinng complete")
