# A Micro-service Based on AutoML to Predict Risk of Heart Disease

[![CI with Github Actions](https://github.com/kaifeng-yu16/Ids-TeamProject/actions/workflows/main.yml/badge.svg)](https://github.com/kaifeng-yu16/Ids-TeamProject/actions/workflows/main.yml)

![Code Build](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiYmVTRXA1alJyVkRXcGRHdkk1KzAxTlZaVjhESG91M3p0bnZWSmxmNmxjNmY3c1pZTzRNUGJPRlJVUG0wTXZlZmdCcVNLd1hLMExORS9LL3d3U3ptUHMwPSIsIml2UGFyYW1ldGVyU3BlYyI6ImQ4YTNoVkFmVUt1eU9RN1EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

Website: https://igih3eivbr.us-east-1.awsapprunner.com

## Introduction
According to CDC, “[h]eart disease is the leading cause of death in the United States.” [1] And there are many risk factors like high blood pressure, obesity, etc.[2] So, it may be meaningful to have a micro-service based on a machine learning model to tell the potential risk of having heart disease.

[1] Centers for Disease Control and Prevention. Underlying Cause of Death, 1999–2018. CDC WONDER Online Database. Atlanta, GA: Centers for Disease Control and Prevention; 2018. Accessed March 12, 2020.

[2] “About Heart Disease,” Sept. 27, 2021. Accessed on: April 24, 2022. [Online]. Available: https://www.cdc.gov/heartdisease/about.htm

## Data
From Kaggle: https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease

<img width="285" alt="numbers" src="https://user-images.githubusercontent.com/89489224/164992469-62d37abd-c4ff-40a1-ba92-ae3fca2911c5.png">

## Workflow
After data wrangling, AutoML was performed using Azure Databricks. The optimal machine learning model was selected. Then, the frontend was built using HTML. AWS Cloud9 developing environment was used. Next, AWS CodeBuild was used to compile and containerize the application into a Docker image. The image was pushed into Amazon Elastic Container Registry. Finally, the micro-service was deployed and served out using Amazon AppRunner.

<img width="913" alt="workflow" src="https://user-images.githubusercontent.com/89489224/164992887-3ba91391-a230-41b6-889a-cec904ec1b47.png">
