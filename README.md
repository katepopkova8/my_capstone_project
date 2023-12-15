# Capstone Project: Price Prediction Model for Books (in EUR)
Prepared by: Kate Popkova
Link to a dataset: https://zenodo.org/records/4265096

=============================================================
## Introduction
=============================================================
The book industry faces the complex challenge of pricing books in a way that maximizes profit while remaining attractive to readers. Factors influencing book prices include author popularity, genre trends, publication date, and market demand.

Opportunities:

1. Dynamic Pricing Strategy: Leveraging data to adjust prices in response to market demands and trends.
2. Inventory Management: Bookstores and online retailers can manage stock more efficiently by understanding which books are likely to sell at certain prices.
3. Market Analysis: Insight into which factors most significantly impact book prices can guide publishers and authors in decision-making processes, from marketing strategies to choosing publication dates.

Who Experiences These Problems?

1. Publishers: Struggle to set optimal prices that balance profitability with market competitiveness.
2. Retailers: Both online and physical bookstores need to competitively price books to maximize sales and manage inventory.
3. Authors: Especially self-published authors, who must decide on the pricing of their books without the resources of large publishing houses.

Benefit from the Outcomes:

- Access to a data-driven pricing model can assist in making more informed decisions, potentially increasing sales and profit margins.
- Better pricing strategies lead to improved customer satisfaction and loyalty.

The Big Idea: Machine Learning Solutions

Machine learning can revolutionize book pricing by providing a predictive model that considers a wide range of factors influencing a book's value in the market.

- Pattern Recognition: Machine learning algorithms can identify patterns and correlations between various factors (like genre popularity, author reputation, and historical sales data) and book prices.
- Predictive Analytics: By analyzing historical data, the model can forecast optimal pricing points for new or existing books.
- Customization: Machine learning models can be trained to adapt to specific market segments, genres, or geographical regions, providing tailored pricing strategies.

The Impact: Societal and Business Value

1.Business Value

- Increased Profitability: More accurate pricing leads to better sales and profit margins.
- Market Competitiveness: Businesses can stay competitive by dynamically adjusting prices in response to market trends.
- Efficient Inventory Management: Reduces the likelihood of overstocking or understocking.

2. Societal Value

- Accessibility: Properly priced books become more accessible to a broader audience, potentially increasing literacy and education.
- Author Recognition: Fair pricing strategies can lead to more equitable recognition and compensation for authors, especially those who are new or self-published.

My projects aims to build a price prediction model in the book industry. The dataset I'll be using has 52,478 records on books collected from an e-commerce platform called Iberlibro (https://www.iberlibro.com/). IberLibro is an online platform for the buying and selling of books, art and collectibles . It is trusted by independent sellers around the world to offer millions of new, second-hand and collectible books; as well as art and collecting items.

The dataset was created by two students Lorena Casanova Lozano and Sergio Costa Planells in 2020 in Barcelona, Spain.

=============================================================
## Project Organization
=============================================================
    
    ├── README.md                           <- The main README document for data scientists utilizing this project.
    |
    ├── Preliminary EDA - Sprint 1.ipynb    <- Project notebook 1 - data preparation and exploration
    ├── Preliminary EDA - Sprint 2.ipynb    <- Project notebook 2 - data preparation and exploration versoin 2
    |
    ├── Slides- Sprint 1.pdf                <- Project presentation 1 
    ├── Slides- Sprint 2.pdf                <- Project presentation 2 


=============================================================
## Table of contents
=============================================================

1. Introduction
2. Understanding the Dataset
3. Data Exploration
    3.1 Initial Data Review
    3.2 Irrelevant Columns
    3.3 Statistical Summary
    3.4 Initial Data Visualization
    3.5 Missing Values
    3.6 Feature Engineering
    3.7 Preprocessing for Modeling
    3.8 Data Splitting
4. Modeling

=============================================================
## Goodreads Best Books Ever Dataset
=============================================================

My dataset (books_1.Best_Books_Ever.csv) containes the following fields:

    - bookId: Book Identifier as in goodreads.com
    - title: Book title
    - series: Series Name
    - author: Book's Author
    - rating: Global goodreads rating
    - description: Book's description
    - language: Book's language
    - isbn: Book's ISBN
    - genres: Book's genres
    - characters: Main characters
    - bookFormat: Type of binding
    - edition: Type of edition (ex. Anniversary Edition)
    - pages: Number of pages
    - publisher: Editorial
    - publishDate: Publication date
    - firstPublishDate: Publication date of first edition
    - awards: List of awards
    - numRatings: Number of total ratings
    - ratingsByStars: Number of ratings by stars (from 5 to 1)
    - likedPercent: Derived field, percent of ratings over 2 starts (as in GoodReads)
    - setting: Story setting
    - coverImg: URL to cover image
    - bbeScore: Score in Best Books Ever list
    - bbeVotes: Number of votes in Best Books Ever list
    - price: Book's price in EUR (extracted from Iberlibro)

=============================================================
## Data Exploration
=============================================================

My exploratory data analysis (EDA) process consists of three main steps. Firstly, I downloaded the dataset from https://zenodo.org/records/4265096. Secondly, I examined the dataset's structure and contents, checking for duplicated rows, columns, and missing values. In the third step, I analyzed and visualized the data to gain insights into its distribution and to identify correlations between different variables and my target variable 'price'.

Here are some key insights from the EDA:
- The columns in my dataset have high cardinality. It can lead to issues like overfitting and increased computational complexity. I'll consider managing this through techniques like binning.
- A significant amount of columns that are relevant to my project goal have a substantial amount of missing data. This can affect my analysis or model's accuracy.
- The average price per book is around 10 EUR.
- The average book rating is around 4.02, with a standard deviation of 0.37.
- The number of ratings per book varies widely, with an average of about 17,879 but a high standard deviation, indicating a large spread.
- The bbeScore and bbeVotes have a wide range, which may indicate outliers or a highly varied dataset.
- The most frequent series are Star Wars Legends, Sherlock Holmes and Dear America. This could indicate popular series with multiple books.
- The authors with popular works are Nora Roberts, Agatha Christie and Stephen King.
- The most common language is English.
- The most common formats are paperback, hardcover, kindle edition, MMP, and e-book. This reflects publishing trends and reader preferences.
- This chart shows the most common page counts, around 300 pages. It gives an idea of the typical length of books in the dataset.
- The most frequent publishers are Vintage and Harper Collins, indicating which publishers have the most books in this collection.

***MORE TO ADD LATER***

=============================================================
## Modeling
=============================================================