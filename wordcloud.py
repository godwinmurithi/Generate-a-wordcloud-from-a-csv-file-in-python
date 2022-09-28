 # Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS



    # Importing Dataset
df = pd.read_csv("tweetsdata0.tsv", sep="	")

#Creating the text variable
text = " ".join(cat for cat in df.text)

#We can generate the wordcloud in the following manner.
# Generate word cloud
word_cloud = WordCloud(
    width=3000,
    height=2000,
    random_state=1,
    background_color="black",
    colormap="Pastel1",
    collocations=False,
    stopwords=STOPWORDS,
    ).generate(text)


# Display the generated Word Cloud
plt.imshow(word_cloud)
plt.axis("off")
plt.show()
