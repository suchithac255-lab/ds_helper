import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import pandas as pd

def visualize(df):
    for column in df.columns:
        data = df[column]
        plt.figure(figsize=(8, 4))
        if data.dtype == 'object':
            if data.apply(lambda x: isinstance(x, str)).mean() > 0.8 and data.str.split().apply(len).mean() > 1:
                text = ' '.join(data.dropna().astype(str))
                wordcloud = WordCloud(background_color='white').generate(text)
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                plt.title(f'Word Cloud: {column}')
            else:
                sns.countplot(y=column, data=df, order=data.value_counts().index)
                plt.title(f'Count Plot: {column}')
        elif data.dtype in ['int64', 'float64']:
            if data.nunique() < 10:
                sns.boxplot(x=column, data=df)
                plt.title(f'Box Plot: {column}')
            else:
                sns.histplot(data, kde=True)
                plt.title(f'Histogram: {column}')
        plt.tight_layout()
        plt.show()

df = pd.DataFrame(data)
visualize(df)
