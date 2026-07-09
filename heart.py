import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn  as sns
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier



df=pd.read_csv("heart.csv")
print(df)

'''EDA and CLEANING'''
print(df.describe())
print(df.columns)
print(df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())

print(df['HeartDisease'].value_counts().plot(kind='bar')) # perfectly distrubted
plt.show()

def plotting(var,num):
    plt.subplot(2,2,num)
    sns.histplot(df[var],kde=True)
plotting('Age',1)
plotting('RestingBP',2)
plotting('Cholesterol',3)
plotting('MaxHR',4)
plt.tight_layout()
plt.show()

#BY seeing the data in graphs we came to know that RestingBP can't be zero and Cholesterol also which means that someone make the null data into 0
print(df['Cholesterol'].value_counts())
ch_mean=df.loc[df['Cholesterol']!=0,'Cholesterol'].mean()
print(ch_mean)
df['Cholesterol']=df['Cholesterol'].replace(0,ch_mean)
print(df['Cholesterol'].value_counts())
resting_bp_mean = df.loc[df['RestingBP'] != 0, 'RestingBP'].mean()
df['RestingBP'] = df['RestingBP'].replace(0, resting_bp_mean)
df['RestingBP'] = df['RestingBP'].round(2)


# Categorical Analysis
sns.countplot(x='Sex', hue='HeartDisease', data=df)
plt.show()

sns.countplot(x='ChestPainType', hue='HeartDisease', data=df)
plt.show()

sns.countplot(x='FastingBS', hue='HeartDisease', data=df)
plt.show()

# Boxplot
sns.boxplot(x='HeartDisease', y='Cholesterol', data=df)
plt.show()

# Violin Plot
sns.violinplot(x='HeartDisease', y='Age', data=df)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

# One-Hot Encoding
df_encode = pd.get_dummies(df, drop_first=True)

# Convert Boolean Columns to Integer
df_encode = df_encode.astype(int)

# Feature Scaling
numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']

scaler = StandardScaler()
df_encode[numerical_cols] = scaler.fit_transform(
    df_encode[numerical_cols]
)

print(df_encode.head())

"ML Part"
X = df_encode.drop('HeartDisease', axis=1)
y = df_encode['HeartDisease']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
scaler=StandardScaler()
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model_logr = LogisticRegression()
model_NB = GaussianNB()
model_logr.fit(X_train_scaled, y_train)
model_NB.fit(X_train_scaled, y_train)
y_pred_logr = model_logr.predict(X_test_scaled)
y_pred_NB = model_NB.predict(X_test_scaled)
accuracy_logr = accuracy_score(y_test, y_pred_logr)
accuracy_NB = accuracy_score(y_test, y_pred_NB)
print("Logistic Regression Accuracy:", accuracy_logr)
print("Naive Bayes Accuracy:", accuracy_NB)

"we can see the logistic regression and Naive Bayes are giving the same accuracy with or without "
"the scaling but the other models are not giving the same accuracy with or without "
"scaling so we need to scale the data for all the models"

"Scaled data use karo toh aacha hai but na use karo toh dikkat hai "

models={
    "Logistic Regression": LogisticRegression(),
    "Naive Bayes": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(),
    "SVM": SVC(kernel='rbf', probability=True),
    "K-Nearest Neighbors": KNeighborsClassifier()
}
results=[]
for name,model in models.items():
    model.fit(X_train_scaled,y_train)
    y_pred_model=model.predict(X_test_scaled)
    acc=accuracy_score(y_test,y_pred_model)
    f1=f1_score(y_test,y_pred_model)
    results.append({
        "Model":name,
        "Accuracy":round(acc,4),
        "F1 Score":round(f1,4),
    })
  
print(results)



import joblib
joblib.dump(models['K-Nearest Neighbors'], 'knn_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(X.columns.tolist(), 'columns.pkl')
