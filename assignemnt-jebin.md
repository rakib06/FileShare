


To solve the task, we need to apply TF-IDF (Term Frequency-Inverse Document Frequency) vectorization on the text data, then train and evaluate multiple machine learning algorithms such as ID3, C4.5, CART, Logistic Regression (LR), Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Multinomial Naive Bayes (MNB), Bernoulli Naive Bayes (BNB), Gaussian Naive Bayes (FNB), Random Forest (RF), Gradient Boosting (GB), and XGBoost. For each model, we need to evaluate the following:

1. Confusion Matrix
2. Classification Report
3. ROC Curve
4. Precision-Recall Curve

### Steps to Implement

1. **Data Preprocessing**:
   - Load the data from the Excel file.
   - Clean the text data if necessary (e.g., remove stop words, special characters, etc.).
   - Encode the labels (`Pray`, `Emergency Relief`, `Grateful`) into numerical values.

2. **Feature Extraction**:
   - Apply TF-IDF Vectorizer to convert the text data into feature vectors.

3. **Model Training and Evaluation**:
   - Split the dataset into training and testing sets.
   - Train each algorithm using the training data.
   - Evaluate each model using the testing data:
     - Compute the confusion matrix, classification report, and ROC/precision-recall curves.

4. **Visualization**:
   - Plot the ROC curves and Precision-Recall curves for each algorithm.

### Example Code Using Python (scikit-learn, XGBoost, matplotlib, etc.)

Below is an outline of how you would approach this problem using Python:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from sklearn.tree import DecisionTreeClassifier

# Load your Excel file
df = pd.read_excel("your_file.xlsx")

# Sample data structure (based on your input):
# df.columns = ["Text", "Label"]

# Encode labels
label_encoder = LabelEncoder()
df['Label'] = label_encoder.fit_transform(df['Label'])

# Text preprocessing
X = df['Text']
y = df['Label']

# Apply TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X_tfidf = vectorizer.fit_transform(X)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.3, random_state=42)

# Define models to evaluate
models = {
    "ID3": DecisionTreeClassifier(criterion='entropy'),
    "C4.5": DecisionTreeClassifier(criterion='entropy'),  # C4.5 is essentially ID3 with enhancements
    "CART": DecisionTreeClassifier(criterion='gini'),
    "Logistic Regression": LogisticRegression(),
    "SVM": SVC(probability=True),
    "KNN": KNeighborsClassifier(),
    "MultinomialNB": MultinomialNB(),
    "BernoulliNB": BernoulliNB(),
    "GaussianNB": GaussianNB(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "XGBoost": xgb.XGBClassifier(eval_metric='logloss')
}

# Loop through models, train, and evaluate
for model_name, model in models.items():
    print(f"Training and evaluating {model_name}...")

    # Train the model
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]  # For ROC curve

    # Confusion Matrix
    print(f"Confusion Matrix for {model_name}:")
    print(confusion_matrix(y_test, y_pred))

    # Classification Report
    print(f"Classification Report for {model_name}:")
    print(classification_report(y_test, y_pred))

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(10, 6))
    plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve for {model_name}')
    plt.legend(loc='lower right')
    plt.show()

    # Precision-Recall Curve
    precision, recall, _ = precision_recall_curve(y_test, y_prob)
    plt.figure(figsize=(10, 6))
    plt.plot(recall, precision, color='green', lw=2)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(f'Precision-Recall Curve for {model_name}')
    plt.show()

```

### Explanation:

1. **TF-IDF Vectorizer**: The `TfidfVectorizer` is used to convert the textual data into numerical format that machine learning algorithms can process. The `stop_words='english'` argument removes common English stop words.

2. **Label Encoding**: We encode the text labels (`Pray`, `Emergency Relief`, `Grateful`) into numerical values using `LabelEncoder` from scikit-learn.

3. **Model Definitions**: We define all the models that need to be evaluated. Some models like ID3 and C4.5 are approximated by using Decision Trees (`DecisionTreeClassifier`), while others are directly available in scikit-learn (e.g., SVM, KNN).

4. **Model Training and Evaluation**: For each model, the following steps are performed:
   - The model is trained on the training set.
   - Predictions are made on the test set.
   - The confusion matrix and classification report are printed.
   - ROC and Precision-Recall curves are plotted.

5. **ROC Curve and Precision-Recall Curve**: These curves provide insights into the model's performance at various thresholds. The `roc_curve` and `precision_recall_curve` functions from scikit-learn are used for plotting these curves.

### Evaluation Metrics:
- **Confusion Matrix**: Shows the counts of actual vs predicted class labels.
- **Classification Report**: Includes precision, recall, F1-score, and support for each class.
- **ROC Curve**: Helps evaluate how well the model distinguishes between classes. The area under the curve (AUC) provides a single measure of performance.
- **Precision-Recall Curve**: Specifically useful in imbalanced classification problems.

### Libraries Required:
- `pandas`
- `scikit-learn`
- `xgboost`
- `matplotlib`

### Final Output:
After running the code, you will get:
1. Confusion matrices for each algorithm.
2. Classification reports for each algorithm.
3. ROC curves and Precision-Recall curves for each algorithm.

This will help you compare the performance of all the algorithms and choose the best one for your task.

If you have any specific questions or need further clarification, feel free to ask!
