import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def visualize(df):
    for col in df.columns:
        print(f"\nVisualizing column: {col}")
        if pd.api.types.is_numeric_dtype(df[col]):
            plt.figure(figsize=(12, 4))
            plt.subplot(1, 3, 1)
            sns.histplot(df[col].dropna(), kde=True)
            plt.title(f'Histogram of {col}')
            plt.subplot(1, 3, 2)
            sns.boxplot(x=df[col].dropna())
            plt.title(f'Boxplot of {col}')
            plt.subplot(1, 3, 3)
            if df.shape[0] <= 2000:
                sns.scatterplot(x=range(len(df[col])), y=df[col])
                plt.title(f'Scatter of {col}')
            plt.tight_layout()
            plt.show()
        elif pd.api.types.is_categorical_dtype(df[col]) or df[col].dtype == object:
            if df[col].nunique() < 20:
                plt.figure(figsize=(6, 4))
                sns.countplot(x=df[col])
                plt.title(f'Countplot of {col}')
                plt.xticks(rotation=45)
                plt.show()
        if df[col].dtype == object and df[col].str.len().mean() > 20:
            text_data = " ".join(df[col].dropna().astype(str))
            if text_data.strip():
                wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text_data)
                plt.figure(figsize=(8, 4))
                plt.imshow(wordcloud, interpolation="bilinear")
                plt.axis("off")
                plt.title(f'WordCloud of {col}')
                plt.show()
    df = pd.DataFrame({
        "Age": [22, 25, 30, 28, 40, 35, 22],
        "Gender": ["Male", "Female", "Female", "Male", "Male", "Female", "Male"],
        "Comments": ["Good", "Excellent service", "Bad experience", "Okay", "Loved it", "Could be better", "Nice"]
    })
    visualize(df)