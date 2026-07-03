# Tech Stack Recommender System

## Project Description

This project builds a recommendation system that maps a user's skills and interests to suitable technology roles and career paths.

The system accepts user skills as input and applies TF-IDF and Cosine Similarity techniques to identify and rank the most relevant career recommendations.

## Features

* Accepts user skill inputs
* Converts skills into vectors using TF-IDF
* Calculates similarity using Cosine Similarity
* Recommends top matching career paths
* Displays ranking scores

## Technologies Used

* Python
* Pandas
* Scikit-Learn

## Dataset Used

Custom dataset (`raw_skills.csv`) containing:

* DevOps
* Cloud Engineer
* Data Scientist
* Backend Developer
* Frontend Developer
* AI Engineer
* Cloud Architect
* System Administrator
* Cyber Security Analyst

## Project Structure

Tech-Stack-Recommender/

├── raw_skills.csv
├── tech_recommender.py
└── README.md

## Installation

Install required packages:

pip install pandas scikit-learn

## Run Project

python tech_recommender.py

## Sample Input

Python
Cloud
Automation

## Sample Output

1. DevOps
2. Cloud Architect
3. Cloud Engineer

## Concepts Used

* Recommendation Systems
* TF-IDF Vectorization
* Cosine Similarity
* Pattern Matching
* User Preference Analysis

## Author

Hajarabee Shaik


