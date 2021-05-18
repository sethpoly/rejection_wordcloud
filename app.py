import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

import service_account as acc

data = acc.Spreadsheet('Applications', 'Rejections').sheet
