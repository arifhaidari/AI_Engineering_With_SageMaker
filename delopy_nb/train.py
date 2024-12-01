import argparse
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

def train_model():
     # Load and preprocess data
     df = pd.read_csv('/opt/ml/input/data/train/newsCorpora.csv', sep='\t', header=None, names=[
          'ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'
     ])
     df.drop_duplicates(subset=['TITLE'], inplace=True)
     df.dropna(subset=['TITLE', 'CATEGORY'], inplace=True)
     
     # Prepare training and testing sets
     train_df, test_df = train_test_split(df.sample(frac=0.05, random_state=42), test_size=0.4, random_state=42)

     tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
     X_train = tfidf.fit_transform(train_df['TITLE'])
     y_train = LabelEncoder().fit_transform(train_df['CATEGORY'])

     # Train model
     model = MultinomialNB()
     model.fit(X_train, y_train)

     # Save model and vectorizer
     joblib.dump(model, '/opt/ml/model/model.pkl')
     joblib.dump(tfidf, '/opt/ml/model/tfidf_vectorizer.pkl')

if __name__ == "__main__":
     train_model()
