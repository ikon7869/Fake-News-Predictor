# Fake-News-Predictor

This project focuses on building a fake news prediction model using machine learning techniques. The goal is to determine whether a news article is genuine or fake based on its content and various features.

Dataset
The dataset for this project was obtained from Kaggle and consists of approximately 72,000 news articles. It contains labeled data, where each article is categorized as either real or fake news.
https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification

Exploratory Data Analysis (EDA)
In the initial phase of the project, we conducted Exploratory Data Analysis to gain insights into the dataset. This included:

Data Visualization: We used various plotting libraries like Matplotlib and Seaborn to visualize data distributions, word frequencies, and other patterns in the dataset.

Data Statistics: We calculated basic statistics such as mean, median, and standard deviation to understand data characteristics.

Data Preprocessing
Data preprocessing is a crucial step in any natural language processing (NLP) project. Here's what we did:

Text Cleaning: We removed special characters, punctuation, and unnecessary whitespaces from the text data.

Stemming: We applied the Porter Stemming algorithm to reduce words to their root form, helping to reduce feature dimensions and improve model performance.

Text Vectorization
Text data needs to be converted into numerical form for machine learning models. We experimented with two common techniques:

TF-IDF Vectorization: This technique converts text data into a sparse matrix of TF-IDF features. However, we observed that this increased complexity and resulted in high-dimensional vectors.

Count Vectorization: Count Vectorization, on the other hand, provided better results. It converts text data into a sparse matrix of word counts, simplifying the feature space.

Model Selection
We compared the performance of two machine learning algorithms:

Naive Bayes: A classic choice for text classification tasks.

Random Forest: We found that Random Forest performed better in terms of prediction accuracy.

Prediction Pipeline
To make predictions on new data, we built a prediction pipeline. This pipeline includes text preprocessing, vectorization, and model prediction steps. Clients can use this pipeline to classify news articles as real or fake.

Conclusion
This project demonstrates the process of building a fake news prediction model using machine learning. By leveraging data analysis, text preprocessing, vectorization techniques, and model selection, we were able to develop an accurate prediction system.
