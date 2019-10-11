#text="The BTS also known as the Bangtan Boys, is a seven-member South Korean boy band formed by Big Hit Entertainment in 2013. The name became a backronym for Beyond the Scene in July 2017. The band won several New Artist of the Year awards for the track No More Dream and gained prominence with their subsequent albums Dark & Wild (2014), The Most Beautiful Moment in Life, Part 2 (2015) and The Most Beautiful Moment in Life: Young Forever (2016). The latter two entered the U.S. Billboard 200, and The Most Beautiful Moment in Life: Young Forever won the Album of the Year award at the 2016 Melon Music Awards.Read more on Brainly.in - https://brainly.in/question/8042024#readmore "
from bs4 import BeautifulSoup
import re as r
import requests
from nltk.tokenize import word_tokenize
url="https://www.myntra.com/"
res = requests.get(url)  #to get the data
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
output = ''
blacklist = [
'[document]',
'noscript',
'header',
'html',
'meta',
'head',
'input',
'script', # there may be more elements you don't want, such as "style", etc.
    ]
for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)
#punct='''::/\@#$^&*()_,+-={}.;'''
    b=r.sub("\W"," ",output)
    b=b.lower()
"--------------------------------------------------------------"    
from nltk.corpus import stopwords #sopword for grammer
sw=set(stopwords.words('english'))
filtered=[]
word1=word_tokenize(b)
for i in word1:
    if i not in sw:
        filtered.append(i)
f=str(filtered)
c=r.sub("\W"," ",filtered) #W is used to remove spaces and punctuation
"--------------------------------------------------------------"
from nltk.probability import FreqDist
fr=FreqDist(filtered)
fr.plot(10)
"--------------------------------------------------------------"
from wordcloud import WordCloud
import matplotlib.pyplot as plt
ac=WordCloud()
ac.generate(c)
plt.imshow(ac)
"--------------------------------------------------------------"