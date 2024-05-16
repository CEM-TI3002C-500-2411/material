from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib

df = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
df = df.dropna(subset=["Critic_Score", "Rating"])

# Predecir el Critic_Score a partir de NA_Sales,EU_Sales,JP_Sales,Other_Sales
X = df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]]
Y = df["Critic_Score"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

gnb = GaussianNB()
gnb.fit(X_train, Y_train)
gnb_predictions = gnb.predict(X_test)
print(f"Accuracy score: {accuracy_score(Y_test, gnb_predictions)}")
joblib.dump(gnb, "modelo_gaussiano.joblib")
print("Modelo Gaussiano guardado...")

# Predecir el Rating a partir de Platform, Genre, Publisher, Developer
X = df[["Platform", "Genre", "Publisher", "Developer"]]
Y = df["Rating"]
X = pd.get_dummies(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

mnb = MultinomialNB()
mnb.fit(X_train, Y_train)
mnb_predictions = mnb.predict(X_test)
print(f"Accuracy score: {accuracy_score(Y_test, mnb_predictions)}")
mnb_prediction_probability = mnb.predict_proba(X_test.head(1))[0]
print(f"Classes: {mnb.classes_}")
print(f"Probabilities: {mnb_prediction_probability}")
mnb_prediction = mnb.predict(X_test.head(1))[0]
print(f"Class prediction: {mnb_prediction}")
joblib.dump(mnb, "modelo_multimodal.joblib")
print("Modelo Multimodal guardado...")