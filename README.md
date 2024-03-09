# Superstore Sales Data Pipeline

## Overview

This repository contains a data pipeline designed for managing and analyzing monthly sales data from the Superstore dataset. The pipeline is incremental, allowing for efficient updates and additions to the dataset.

## Key Components

### Data Extraction and Transformation
- Utilized a Python script for extracting monthly sales data, orchestrating the generation of new CSVs.

### Storage and Partitioning
- Organized CSVs into distinct S3 folders, implementing a partitioning strategy for efficient data management.

### Cataloging with AWS Glue
- Implemented an AWS Glue crawler, automating the cataloging process and seamlessly updating the Data Catalog table to reflect new partitions.

### Querying with Amazon Athena
- Executed direct querying of specific, updated, or added data from CSVs on S3 using Amazon Athena.

### Visualization with Amazon QuickSight
- Integrated with Amazon QuickSight, facilitating the creation of datasets, visualizations, and dashboards for in-depth data analysis.

## Usage

1. **Data Extraction:**
    - Execute the provided Python script for extracting and transforming monthly sales data.

  ![image](https://github.com/Sameer1295/SuperStore-Data-Pipeline-In-AWS/assets/29782669/ddbba754-cda5-4f1c-80da-c163faf6f485)

2. **Storage and Partitioning:**
    - Ensure generated CSVs are stored in separate S3 folders, organized by month.

3. **Cataloging with AWS Glue:**
    - Run the AWS Glue crawler to automate the cataloging process and update the Data Catalog table.

  ![image](https://github.com/Sameer1295/SuperStore-Data-Pipeline-In-AWS/assets/29782669/c64d3d87-c379-4113-9f66-4a8bbb4050f2)

  ![image](https://github.com/Sameer1295/SuperStore-Data-Pipeline-In-AWS/assets/29782669/e3585ec1-6435-4b15-b442-dab08cb396a5)

4. **Querying with Amazon Athena:**
    - Utilize Amazon Athena to run SQL queries on the CSV data stored on S3.

  ![image](https://github.com/Sameer1295/SuperStore-Data-Pipeline-In-AWS/assets/29782669/7e56a924-1b48-4113-bffe-8682d6ef60fb)

5. **Visualization with Amazon QuickSight:**
    - Connect Amazon QuickSight to the Data Catalog table to create insightful visualizations and dashboards.

  ![image](https://github.com/Sameer1295/SuperStore-Data-Pipeline-In-AWS/assets/29782669/6e3e8a3f-5365-4422-806f-28af2a7b42e3)

  ![image](https://github.com/Sameer1295/SuperStore-Data-Pipeline-In-AWS/assets/29782669/9dbfd382-4fab-415c-bb21-e03e8197849f)

