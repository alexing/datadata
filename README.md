# Data, data
## A statistical analysis and exploration on Jorge Drexler's music and lyrics.

### by [Alex Ingberg](https://www.linkedin.com/in/alexingberg/)



Data, data is a homage to the great Uruguayan musician and songwriter [Jorge Drexler](https://www.youtube.com/watch?v=aU9gzRy2dQc).


Pulling data using both the Genius API and the Spotify API I've been able to analyze Jorge's music and get some insights and visualizations on his creative process and his songs in general; both from the lyrics side and the musical theory side.

Wordcount, lexical and lyrical density, sentiment analysis and analysis of musical components like tempo, time signature and key are all taken into account. Also, in the end, [gloom_index](https://www.rcharlie.com/post/fitter-happier/) is used combining both lyrics and music.

## To check the analysis, go [here](drexler_data_exploration.ipynb).

## To see the article published in Towards Data Science, go [here](https://towardsdatascience.com/data-data-1fedfac91c79)
## To check it's spanish translation, go [here](https://medium.com/@alexing/data-data-b82201ec1cf4)

### To check how i built the database, go [here](drexler_dataset_builder.ipynb).



Some cool samples from the visualizations:

![NRC emotions through the years](img/emotions_through_time.jpg?raw=true "NRC emotions through the years")
![Tempo by albums](img/tempo_by_albums.jpg?raw=true "Tempo by albums")
![Usage of keys](img/keys.jpg?raw=true "Usage of keys")
![Top 10 songs with more words](img/top_songs_more_words.jpg?raw=true "Top 10 songs with more words")
![Wordcloud](img/wordcloud.jpg?raw=true "Wordcloud")
![Lyrical density vs lexical density](img/lyrical_density_v_lexical_density.jpg?raw=true "Lyrical density vs lexical density")
![Correlation in negative NRC emotions](img/correlation_in_emotions.jpg?raw=true "Correlation in negative NRC emotions")

This whole project has been created using [Python 3](https://www.python.org/downloads/), [Jupyter Notebook](http://jupyter.org/) and a little bit of [PyCharm](https://www.jetbrains.com/pycharm/).

I created the databases with [pandas](https://pandas.pydata.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Spotipy](https://spotipy.readthedocs.io/en/latest/) (an amazing Python wrapper for the Web Spotify API), and the [Genius API](https://genius.com/developers) and [Web Spotify API](https://developer.spotify.com/documentation/web-api/).

To work on the analysis the tools I used were [pandas](https://pandas.pydata.org/), [NumPy](http://www.numpy.org/), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/), [scikit-learn](http://scikit-learn.org/), [SciPy](https://www.scipy.org/), [Natural Language Toolkit](https://www.nltk.org/), [wordcloud](https://github.com/amueller/word_cloud) and [py-lex](https://github.com/dropofwill/py-lex). 


## To check the analysis, go [here](drexler_data_exploration.ipynb).

### To check how i built the database, go [here](drexler_dataset_builder.ipynb).



### References:

[1] [Text analysis in Pandas with some TF-IDF (again)](http://sigdelta.com/blog/text-analysis-in-pandas/) by Jakub Nowacki

[2] [ Everything in Its Right Place: Visualization and Content Analysis of Radiohead Lyrics](http://www.everydayanalytics.ca/2013/06/radiohead-lyrics-data-visualization-and-content-analysis.html) by Myles Harrison

[3] [Data Visualization and Analysis of Taylor Swift’s Song Lyrics](https://www.promptcloud.com/blog/data-visualization-text-mining-taylor-swift-song-lyrics) by [Preetish Panda](https://www.promptcloud.com/author/preetish-panda/)

[4] [fitteR happieR](https://www.rcharlie.com/post/fitter-happier/) by [Rcharlie](https://www.rcharlie.com/post/fitter-happier/)

[5] [Quantifying Sufjan Stevens with the Genius API and NLTK](http://www.jw.pe/blog/post/quantifying-sufjan-stevens-with-the-genius-api-and-nltk/) by Jonathan Evans
