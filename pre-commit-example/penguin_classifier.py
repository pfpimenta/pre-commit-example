from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from sklearn import metrics
from some_functions import impute_data, drop_missing_records
from sklearn.ensemble import RandomForestClassifier

# Loading the Penguins Dataset from Seaborn
df = sns.load_dataset('penguins')

# treat missing data
df = impute_data(df)
df = drop_missing_records(df)

# Mapping the sex variable to binary values
df['sex int'] = df['sex'].map({'Male': 0, 'Female': 1})

# One-hot Encoding the Island Feature
one_hot = OneHotEncoder()
encoded = one_hot.fit_transform(df[['island']])
df[one_hot.categories_[0]] = encoded.toarray()

# Dropping Unnecessary Columns
df = df.drop(columns=['island', 'sex'])

print(df.head())

# Splitting the data
X = df.iloc[:, 1:]
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=100)

# instantiate classifier
forest = RandomForestClassifier(n_estimators=100, random_state=100)

# Fitting a model and making predictions
forest.fit(X_train,y_train)
predictions = forest.predict(X_test)

# Evaluating the model
print("Accuracy:",metrics.accuracy_score(y_test, predictions))
