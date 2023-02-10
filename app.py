import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model3.joblib")
labels = model.labels_
df = pd.read_csv('products.csv')
vectorizer = joblib.load("vec.joblib")

cluster_0 = []
cluster_1= []
cluster_2=[]
cluster_3=[]
cluster_4=[]
cluster_5=[]
cluster_6=[]

for i in range(0, len(labels)):
  if labels[i] == 0:
    cluster_0.append([df['Url'][i],df['Description'][i]])
  elif labels[i] == 1:
    cluster_1.append([df['Url'][i],df['Description'][i]])
  elif labels[i] == 2:
    cluster_2.append([df['Url'][i],df['Description'][i]])
  elif labels[i] == 3:
    cluster_3.append([df['Url'][i],df['Description'][i]])
  elif labels[i] == 4:
    cluster_4.append([df['Url'][i],df['Description'][i]])
  elif labels[i] == 5:
    cluster_5.append([df['Url'][i],df['Description'][i]])
  else:
    cluster_6.append([df['Url'][i],df['Description'][i]])


st.title('Image Clustering')

st.write('A collection of product images scraped from Kasha Rwanda New Arrivals page(https://kasha.rw/product-category/new-arrivals/) and clustered using Agglomerative Clustering into 7 different clusters according to the similarity of their descriptions')


st.header('Cluster 0')

for i in cluster_0:
  col1, col2 = st.columns([1,3])
  col1.image(i[0],width=100)
  col2.write(i[1])

st.header('Cluster 1')

for i in cluster_1:
  col3, col4 = st.columns([1,3])
  col3.image(i[0],width=100)
  col4.write(i[1])

st.header('Cluster 2')

for i in cluster_2:
  col5, col6 = st.columns([1,3])
  col5.image(i[0],width=100)
  col6.write(i[1])

st.header('Cluster 3')

for i in cluster_3:
  col7, col8 = st.columns([1,3])
  col7.image(i[0],width=100)
  col8.write(i[1])

st.header('Cluster 4')

for i in cluster_4:
  col9, col10 = st.columns([1,3])
  col9.image(i[0],width=100)
  col10.write(i[1])

st.header('Cluster 5')

for i in cluster_5:
  col11, col12 = st.columns([1,3])
  col11.image(i[0],width=100)
  col12.write(i[1])

st.header('Cluster 6')

for i in cluster_6:
  col13, col14 = st.columns([1,3])
  col13.image(i[0],width=100)
  col14.write(i[1])