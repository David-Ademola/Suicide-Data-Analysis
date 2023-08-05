# Machine Learning for Suicide Data Analysis

## Introduction:
The "Machine Learning for Suicide Data Analysis" project aims to explore and analyze suicide-related data from a global dataset. The dataset contains various socio-economic and demographic attributes, such as country, year, sex, age group, GDP per capita, and generation, and the corresponding number of suicides. The goal of the project is to preprocess the data, prepare it for machine learning, and use machine learning techniques to gain insights into factors that may influence suicide rates.

## Data Preprocessing:
The project begins by loading the dataset using the pandas library and removing unnecessary columns that are not relevant for the analysis.
Categorical columns such as "country," "year," "sex," "age," "gdp_per_capita ($)," and "generation" are encoded with numeric values using a custom function, encode_column. This ensures that the categorical data can be used in machine learning algorithms effectively.
The "gdp_for_year ($)" column is cleaned by removing commas and converting the values to float to facilitate numerical operations.

## Data Transformation:
The target variable, "suicides_no," is extracted from the DataFrame and stored separately as the "target" variable in a NumPy array.
The remaining features are converted into a 2D NumPy array and cast to float to prepare the data for machine learning.

## Feature Engineering and Preprocessing:
The data contains categorical variables, which need to be one-hot encoded to be suitable for machine learning models. The OneHotEncoder from scikit-learn is used to transform these columns.
Numerical features, "population" and " gdp_for_year ($) ", are scaled using the MinMaxScaler to ensure that they are on the same scale as the one-hot encoded categorical features.

## Visualization and Analysis:
The processed data is now ready for visualization. Using the matplotlib software a bar chart of the age groups and suicide rates was created allowing me to easily see which age groups had the highest suicide rates.
![image](https://github.com/David-Ademola/Suicide-Data-Analysis/assets/131247654/6bd0ee0e-e040-411a-8c68-58d517410ec0)

## Conclusion:
The "Machine Learning for Suicide Data Analysis" project demonstrates essential data preprocessing steps required before applying machine learning algorithms to analyze suicide-related data. By encoding categorical features and scaling numerical ones, the data is made suitable for various machine learning models. The preprocessed dataset provides a foundation for further exploratory data analysis and modeling to gain insights into the factors affecting suicide rates worldwide.
