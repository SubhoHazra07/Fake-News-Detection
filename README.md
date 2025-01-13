<div align="center">
<strong><h1>Fake News Detection</h1><strong>
</div>

<p align="center">
  <img src="https://github.com/user-attachments/assets/503516c9-32f9-43d7-ae02-e72a32365e32" alt="Sample Image" width="850">
</p>

This project focuses on detecting fake news using various machine learning algorithms. The goal is to build models that classify news articles as either "Fake News" or "Not A Fake News" based on their textual content. The dataset used for training and testing consists of labeled fake and true news articles.

## Features

- **Preprocessing**: 
  - **Text cleaning**: Removes noise such as special characters, numbers, and irrelevant text to simplify the data.
  - **Tokenization**: Breaks the text into individual words, making it easier for algorithms to analyze.
  - **Lemmatization**: Converts words to their base forms (e.g., "running" to "run") to standardize the text and reduce redundancy.
  - **Removal of stopwords**: Eliminates common words (e.g., "the", "and") that do not add value to the analysis.
  - **Removal of punctuation, URLs, HTML tags, emojis, and frequent/rare words**: Further reduces noise, ensuring the model focuses on meaningful text.

- **Models Implemented**:
  - **Logistic Regression**: A simple, effective algorithm for binary classification problems.
  - **Decision Tree Classifier**: Provides interpretable decision rules and handles non-linear relationships well.
  - **Gradient Boosting Classifier**: Combines multiple weak learners to create a strong predictive model.
  - **Random Forest Classifier**: Uses ensemble learning to improve accuracy and reduce overfitting.

- **Manual Testing**: Allows users to test specific news articles against all trained models to check predictions.

- **Model Persistence**: Saves trained models and vectorizer using Joblib, making it easy to reuse them without retraining.

## Dataset

The dataset includes:
- **Fake News**: Contained in `Fake.csv`.
- **True News**: Contained in `True.csv`.

Both datasets are merged, shuffled, and processed for training and testing. A `class` column is added to label fake news as `0` and true news as `1`.

- **Why this structure?**: Labeling and merging data ensures consistent input for the machine learning pipeline, while shuffling helps reduce bias during training.

## Requirements

Install the required Python packages using:
```bash
pip install -r requirements.txt
```

### Dependencies
- **Python 3.8+**: Ensures compatibility with the libraries used.
- **Numpy**: For numerical computations.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: To visualize model performance.
- **Scikit-learn**: Provides tools for preprocessing, modeling, and evaluation.
- **NLTK**: For natural language processing tasks such as tokenization and stopword removal.
- **SpaCy**: For efficient lemmatization and advanced NLP tasks.
- **Joblib**: For saving and loading trained models efficiently.

## Preprocessing Steps

The following text preprocessing functions are applied:
1. **Convert text to lowercase**: Standardizes text to prevent case-sensitive mismatches.
2. **Remove punctuation**: Reduces noise by eliminating unnecessary symbols.
3. **Remove stopwords**: Focuses on meaningful words by discarding common, irrelevant terms.
4. **Remove frequent and rare words**: Prevents bias from overly common words and reduces noise from very rare words.
5. **Lemmatize words**: Ensures consistency by converting words to their root forms.
6. **Remove emojis, URLs, and HTML tags**: Cleans data by eliminating non-textual elements.

- **Why preprocessing?**: These steps refine raw data, enhancing model performance by providing clean, structured input.

## Workflow

![Fake News Detection](https://github.com/user-attachments/assets/dc48ce9f-1531-4662-9a8a-aab141eb8164)


1. **Data Preparation**:
   - Load datasets (`Fake.csv`, `True.csv`).
   - Combine, shuffle, and label the data.
   - Drop irrelevant columns (`title`, `subject`, `date`).

   - **Why drop irrelevant columns?**: These columns do not contribute to the text analysis and may introduce noise or bias.

2. **Preprocessing**:
   - Apply the `wordopt()` function to clean and preprocess the text.

   - **Why preprocess text?**: Cleaned text improves the reliability of feature extraction and model predictions.

3. **Train-Test Split**:
   - Split the data into training and testing sets using an 80-20 ratio.

   - **Why split data?**: Separating training and testing data prevents overfitting and provides an unbiased evaluation of model performance.

4. **Feature Extraction**:
   - Use `TfidfVectorizer` to convert text data into numerical features.

   - **Why TF-IDF?**: It captures the importance of words relative to a document and the entire dataset, enhancing feature representation.

5. **Model Training**:
   - Train the following models:
     - Logistic Regression
     - Decision Tree Classifier
     - Gradient Boosting Classifier
     - Random Forest Classifier

   - **Why multiple models?**: Comparing diverse algorithms helps identify the best-performing model for the task.

6. **Evaluation**:
   - Measure accuracy, precision, recall, and F1-score.
   - Generate confusion matrices for each model.

   - **Why evaluate models?**: These metrics provide a comprehensive understanding of model performance, ensuring reliable predictions.

7. **Manual Testing**:
   - Test user-provided news articles with trained models.

   - **Why manual testing?**: Allows real-time validation of the model's predictions on unseen data.

8. **Model Saving**:
   - Save models and vectorizer for future use using `Joblib`.

   - **Why save models?**: Reduces computational cost by reusing trained models instead of retraining from scratch.

## Usage

### Training
Run the main script to preprocess data, train models, and save the trained models:
```bash
python main.py
```

### Manual Testing

![Prediction](https://github.com/user-attachments/assets/d15821b8-d2cf-4312-8b74-a7e2eaeb85f0)


Test a custom news article by providing it as input to the `manual_testing()` function in the script:
```python
news = "Your news article here."
manual_testing(news)
```

### Saved Models
Trained models and vectorizer are saved as:
- `LogicticRegression_model.pkl`
- `DecisionTree_model.pkl`
- `GradientBoosting_model.pkl`
- `RandomForest_model.pkl`
- `Vectorizer.pkl`

These files can be loaded later for predictions.

- **Why save vectorizer?**: Ensures the same feature extraction process is applied to new data.

## Example

### Manual Testing Output
```text
LR Prediction: Not A Fake News 
DT Prediction: Fake News 
GBC Prediction: Not A Fake News 
RFC Prediction: Not A Fake News
```

## Results

| Model                  | Training Accuracy | Testing Accuracy |
|------------------------|-------------------|------------------|
| Logistic Regression    | High              | High             |
| Decision Tree Classifier | High              | Moderate         |
| Gradient Boosting Classifier | High              | High             |
| Random Forest Classifier | High              | High             |

- **Why accuracy metrics?**: They indicate the reliability of the model in distinguishing between fake and true news.

## Repository Structure

```
.
├── Fake.csv
├── True.csv
├── main.py
├── nltk_utils.py
├── requirements.txt
├── LogicticRegression_model.pkl
├── DecisionTree_model.pkl
├── GradientBoosting_model.pkl
├── RandomForest_model.pkl
├── Vectorizer.pkl
└── README.md
```

- **Why organize files?**: A structured repository improves readability and simplifies project navigation.

## Acknowledgements

- **Dataset**: Publicly available datasets of fake and true news articles.
- **Libraries**: Scikit-learn, NLTK, SpaCy, and Joblib.

- **Why acknowledgements?**: Credits the resources and tools that contributed to the project.

## Author

- **Subho Hazra** (GitHub: [SubhoHazra07](https://github.com/SubhoHazra07))
