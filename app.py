import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load('gbm_model.pkl')

# Streamlit app layout
st.title('Book Price Prediction')

# Creating input fields for the features
edition_binary = st.selectbox('Edition Binary', options=[0, 1])
series_binary = st.selectbox('Series Binary', options=[0, 1])
category_Horror_Gothic = st.selectbox('Category Horror & Gothic', options=[0, 1])
category_Graphic_Novels_Comics = st.selectbox('Category Graphic Novels & Comics', options=[0, 1])
category_Religious_Spiritual = st.selectbox('Category Religious & Spiritual', options=[0, 1])
category_Special_Interest_Others = st.selectbox('Category Special Interest & Others', options=[0, 1])
category_Mystery_Thriller = st.selectbox('Category Mystery & Thriller', options=[0, 1])
category_Romance = st.selectbox('Category Romance', options=[0, 1])
category_Fantasy_Science_Fiction = st.selectbox('Category Fantasy & Science Fiction', options=[0, 1])
category_History_Cultural = st.selectbox('Category History & Cultural', options=[0, 1])
category_Young_Adult_Children = st.selectbox('Category Young Adult & Children', options=[0, 1])
category_Non_Fiction = st.selectbox('Category Non Fiction', options=[0, 1])
category_Literature_Classics = st.selectbox('Category Literature Classics', options=[0, 1])
category_Other = st.selectbox('Category Other', options=[0, 1])
category_Cultural_Ethnic = st.selectbox('Category Cultural & Ethnic', options=[0, 1])
format_Paperback = st.selectbox('Format Paperback', options=[0, 1])
format_Hardcover = st.selectbox('Format Hardcover', options=[0, 1])
format_Mass_Market_Paperback = st.selectbox('Format Mass Market Paperback', options=[0, 1])
format_Kindle_Edition = st.selectbox('Format Kindle Edition', options=[0, 1])
format_ebook = st.selectbox('Format eBook', options=[0, 1])
format_Audio_CD = st.selectbox('Format Audio CD', options=[0, 1])
format_Unknown_Binding = st.selectbox('Format Unknown Binding', options=[0, 1])
format_Trade_Paperback = st.selectbox('Format Trade Paperback', options=[0, 1])
format_Audiobook = st.selectbox('Format Audiobook', options=[0, 1])
format_Board_Book = st.selectbox('Format Board Book', options=[0, 1])
format_Other = st.selectbox('Format Other', options=[0, 1])
publisher_Vintage = st.selectbox('Publisher Vintage', options=[0, 1])
publisher_HarperCollins = st.selectbox('Publisher HarperCollins', options=[0, 1])
publisher_Penguin_Books = st.selectbox('Publisher Penguin Books', options=[0, 1])
publisher_Ballantine_Books = st.selectbox('Publisher Ballantine Books', options=[0, 1])
publisher_Bantam = st.selectbox('Publisher Bantam', options=[0, 1])
publisher_Pocket_Books = st.selectbox('Publisher Pocket Books', options=[0, 1])
publisher_Avon = st.selectbox('Publisher Avon', options=[0, 1])
publisher_Penguin_Classics = st.selectbox('Publisher Penguin Classics', options=[0, 1])
publisher_Del_Rey = st.selectbox('Publisher Del Rey', options=[0, 1])
publisher_Tor_Books = st.selectbox('Publisher Tor Books', options=[0, 1])
publisher_Other = st.selectbox('Publisher Other', options=[0, 1])
pages_short = st.selectbox('Pages Short', options=[0, 1])
pages_medium = st.selectbox('Pages Medium', options=[0, 1])
pages_long = st.selectbox('Pages Long', options=[0, 1])

# Button to make predictions
if st.button('Predict Price'):
    input_data = {
        'edition_binary': edition_binary,
        'series_binary': series_binary,
        'Category Horror & Gothic': category_Horror_Gothic,
        'Category Graphic Novels & Comics': category_Graphic_Novels_Comics,
        'Category Religious & Spiritual': category_Religious_Spiritual,
        'Category Special Interest & Others': category_Special_Interest_Others,
        'Category Mystery & Thriller': category_Mystery_Thriller,
        'Category Romance': category_Romance,
        'Category Fantasy & Science Fiction': category_Fantasy_Science_Fiction,
        'Category History & Cultural': category_History_Cultural,
        'Category Young Adult & Children': category_Young_Adult_Children,
        'Category Non Fiction': category_Non_Fiction,
        'Category Literature Classics': category_Literature_Classics,
        'Category Other': category_Other,
        'Category Cultural & Ethnic': category_Cultural_Ethnic,
        'Format Paperback': format_Paperback,
        'Format Hardcover': format_Hardcover,
        'Format Mass Market Paperback': format_Mass_Market_Paperback,
        'Format Kindle Edition': format_Kindle_Edition,
        'Format eBook': format_ebook,
        'Format Audio CD': format_Audio_CD,
        'Format Unknown Binding': format_Unknown_Binding,
        'Format Trade Paperback': format_Trade_Paperback,
        'Format Audiobook': format_Audiobook,
        'Format Board Book': format_Board_Book,
        'Format Other': format_Other,
        'Publisher Vintage': publisher_Vintage,
        'Publisher HarperCollins': publisher_HarperCollins,
        'Publisher Penguin Books': publisher_Penguin_Books,
        'Publisher Ballantine Books': publisher_Ballantine_Books,
        'Publisher Bantam': publisher_Bantam,
        'Publisher Pocket Books': publisher_Pocket_Books,
        'Publisher Avon': publisher_Avon,
        'Publisher Penguin Classics': publisher_Penguin_Classics,
        'Publisher Del Rey': publisher_Del_Rey,
        'Publisher Tor Books': publisher_Tor_Books,
        'Publisher Other': publisher_Other,
        'Pages Short': pages_short,
        'Pages Medium': pages_medium,
        'Pages Long':pages_long 
    }
    
    input_df = pd.DataFrame([input_data])
    predicted_price = model.predict(input_df)
    st.write(f'Predicted Price of the Book: ${predicted_price[0]:.2f}')
