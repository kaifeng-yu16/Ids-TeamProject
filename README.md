# A Micro-service Based on AutoML to Predict Risk of Heart Disease

[![CI with Github Actions](https://github.com/kaifeng-yu16/Ids-TeamProject/actions/workflows/main.yml/badge.svg)](https://github.com/kaifeng-yu16/Ids-TeamProject/actions/workflows/main.yml)

![Code Build](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiYmVTRXA1alJyVkRXcGRHdkk1KzAxTlZaVjhESG91M3p0bnZWSmxmNmxjNmY3c1pZTzRNUGJPRlJVUG0wTXZlZmdCcVNLd1hLMExORS9LL3d3U3ptUHMwPSIsIml2UGFyYW1ldGVyU3BlYyI6ImQ4YTNoVkFmVUt1eU9RN1EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

Website: https://igih3eivbr.us-east-1.awsapprunner.com

The application was containerized using Docker! The Docker image could be easily built by running
```shell
docker build -t .
```

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

## Result
Users will be first pointed to the main page as follows.

<img width="530" alt="main" src="https://user-images.githubusercontent.com/89489224/164993039-5a97ed49-5564-45b6-9408-1a8eaf944ddb.png">

By clicking "Heartattack Prediction", the page will jump to the precition page as below. Auto-filling was adopted in this page. Users will only need to enter "BMI" and "Sleep Time". Other entries could also be modified if the users want to.

<img width="575" alt="prediction" src="https://user-images.githubusercontent.com/89489224/164993102-94acf814-76c4-48c8-aa7c-83a05d6edfe8.png">

By clicking "predict", the result will show up.

<img width="525" alt="res" src="https://user-images.githubusercontent.com/89489224/164993181-9b2b7b35-eebe-4e9b-b2b6-4a7ed417741f.png">

## Load Test
Due to the resource contrain, the load test was performed on local machine. Five hundreds users were simulated at a spawn rate of 5 users spawned/second. As shown below, the failure rate remained 0 while testing. As the requests went up, the response time was in a resonable range though there was a peak during the process. In most of the time, the median response time was below 300ms.


![number_of_users_1650826137](https://user-images.githubusercontent.com/89489224/164993337-a4436f97-6852-48d0-b33c-3d7de1763140.png)

![response_times_(ms)_1650826137](https://user-images.githubusercontent.com/89489224/164993346-eca5a74a-9628-481a-8e45-85876c9920ad.png)


![total_requests_per_second_1650826137](https://user-images.githubusercontent.com/89489224/164993349-a936897e-85f9-4b3e-a6b1-f10b980bfe93.png)
