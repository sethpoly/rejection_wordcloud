import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

import service_account as acc

# Retrieve data from google sheets API
data = acc.Spreadsheet('Applications', 'Rejections').sheet

# Create df from data
rows = data.get_all_records()
df = pd.DataFrame(rows)

# First 50 rejection emails
text = " ".join(email for email in df.Email[1:50])
print(f'There are {len(text)} words in the combination of all the rejection emails.')

# Apply stopwords
STOPWORDS = ["Boston MA", "MA Excellent", "MA", "MA Possible", "NY", "New York", "email", "sjpolyniak", "Boston", "to", "we", "and", "the", "will", "have" "of","this", "Match Posted", "Senior"]

# Create mask from any PNG img
mask = np.array(Image.open("assets/mask.jpg"))

# Create & generate wordcloud image
wordcloud = WordCloud(stopwords=STOPWORDS, mode='RGBA', mask=mask, max_words=300, background_color="white").generate(text)

# create coloring from image
image_colors = ImageColorGenerator(mask)

# Display generated image
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis("off")
plt.show()
