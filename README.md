# RAW XIC Export

This repository contains a Python script to extract Extracted Ion Chromatograms (XICs) from Thermo Fisher Scientific RAW mass spectrometry files. The script leverages the **ThermoRawFileParser** to access and convert RAW data for subsequent XIC extraction based on specified m/z values.

## Features

- **XIC Extraction**: Extracts chromatographic data for specified m/z values with a user-defined tolerance.
- **Docker Compatibility**: Runs with Docker for cross-platform use, or locally on compatible systems.
- **User-Defined Ions**: Specify a list of m/z values for targeted ion extraction.
- **Output Options**: Generates outputs for downstream analysis.

## Requirements

- Python 3.x
- [Docker](https://www.docker.com/)
- [pandas](https://pandas.pydata.org/)
- [pyrawr](https://pypi.org/project/pyrawr/)

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/wilhan-nunes/raw-xic-export.git
    cd raw-xic-export
    ```

2. **Install Dependencies**:

    ```bash
    pip install pandas pyrawr
    ```

3. **ThermoRawFileParser**:

   Download and install ThermoRawFileParser or use the Docker version specified in the script.

## Usage

1. **Specify Ions and Tolerance**:

   In `raw_parser.py`, specify the ions of interest in `ion_list` with m/z values and tolerance settings.

   ```python
   ion_list = ['164.107', '178.1226', '192.0689', '192.1383', '206.1539']
   ```

2. **Execute the Script**:

   Run the script to extract ions from RAW files in the specified directory.

   ```bash
   python raw_parser.py
   ```

3. **Docker Execution**:

   Ensure Docker is installed and running. Adjust Docker image paths in the script if needed. If running on windows/linux, please refer to the [pyrawr documentation](https://pyrawr.readthedocs.io/en/latest/api.html) for more details.


