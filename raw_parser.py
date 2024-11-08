import pandas as pd
from pyrawr import ThermoRawFileParser
import os

# Path to the folder containing the raw files
raw_files_path = '/Users/wilhan/Downloads/'
output_path = '/Users/wilhan/PycharmProjects/Raw_parser'
# Filter only raw files
raw_files = [file for file in os.listdir(raw_files_path) if file.endswith('.raw')]

# For execution with docker you need it to be installed on your computer
# you can also install the thermorawfileparser locally if you are using windows or linux
trfp = ThermoRawFileParser(
    executable="thermorawfileparser",
    docker_image="quay.io/biocontainers/thermorawfileparser:1.3.3--ha8f3691_1",
)

# Add the ions you want to extract as a list of strings
ion_list = ['164.107', '178.1226', '192.0689', '192.1383', '206.1539']

for file in raw_files:
    file_path = os.path.join(raw_files_path, file)

    # list of dictionaries specifying the m/z for the ions to extract
    query_list = [{"mz": float(i), "tolerance": 5, "tolerance_unit": "ppm"} for i in ion_list]
    ion_chromatogram = trfp.xic(file_path, query_list)
    for i in range(len(ion_chromatogram['Content'])):
        data = ion_chromatogram['Content'][i]

        meta_data = data.pop('Meta')  # remove the "Meta" key to create a dataframe
        df = pd.DataFrame(data)
        # export TSV
        df.to_csv(os.path.join(output_path, f"{file}_{ion_list[i]}.tsv"), sep='\t')
