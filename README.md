# Data, data
## A statistical analysis and exploration on Jorge Drexler's music and lyrics.

### Alex Ingberg

Data, data is a homage to the great Uruguayan musician and songwriter [Jorge Drexler](https://www.youtube.com/watch?v=aU9gzRy2dQc).
Pulling data using both the Genius API and the Spotify API I've been able to analyze Jorge's music and get some insights and visualizations on his creative process and his songs in general; both from the lyrics side and the musical theory side.
Wordcount, lexical and lyrical density, sentiment analysis and analysis of musical components like tempo, time signature and key are all taken into account. Also, in the end, [gloom_index](https://www.rcharlie.com/post/fitter-happier/) is used combining both lyrics and music.

Some cool samples from the visualizations:

![NRC emotions through the years](img/emotions_through_time.jpg?raw=true "NRC emotions through the years")
![Tempo by albums](img/tempo_by_albums.jpg?raw=true "Tempo by albums")
![Usage of keys](img/keys.jpg?raw=true "Usage of keys")
![Top 10 songs with more words](img/top_songs_more_words.jpg?raw=true "Top 10 songs with more words")
![Wordcloud](img/wordcloud.jpg?raw=true "Wordcloud")
![Lyrical density vs lexical density](img/lyrical_density_v_lexical_density.jpg?raw=true "Lyrical density vs lexical density")
![Correlation in negative NRC emotions](img/correlation_in_emotions.jpg?raw=true "Correlation in negative NRC emotions")

MusicMagal is a group recommendation system that recommends n music tracks to a group of m users considering all of the m users preferences into account.
To achieve this we've based our machine learning and deep learning models in Last.Fm data. After computing and when the resulting playlist is output, we create a real playlist using Spotify API's python wrapper: Spotipy.

A typical version of the program's flow is presented in [musicmagal_flow.ipynb](musicmagal_flow.ipynb).

To see our evaluation metrics you can check [musicmagal_evaluation.ipynb](musicmagal_evaluation.ipynb).

Our database exploration is presented in [db_exploration.ipynb](db_exploration.ipynb).

You can read the article going over our model bit by bit in [Hacker Noon](https://hackernoon.com/musicmagal-c93e9dabd01a).



### References:

[1] [Text analysis in Pandas with some TF-IDF (again)](http://sigdelta.com/blog/text-analysis-in-pandas/) by Jakub Nowacki

[2] [ Everything in Its Right Place: Visualization and Content Analysis of Radiohead Lyrics](http://www.everydayanalytics.ca/2013/06/radiohead-lyrics-data-visualization-and-content-analysis.html) by Myles Harrison

[3] [Data Visualization and Analysis of Taylor Swift’s Song Lyrics](https://www.promptcloud.com/blog/data-visualization-text-mining-taylor-swift-song-lyrics) by [Preetish Panda](https://www.promptcloud.com/author/preetish-panda/)

[4] [fitteR happieR](https://www.rcharlie.com/post/fitter-happier/) by [Rcharlie](https://www.rcharlie.com/post/fitter-happier/)

[5] [Quantifying Sufjan Stevens with the Genius API and NLTK](http://www.jw.pe/blog/post/quantifying-sufjan-stevens-with-the-genius-api-and-nltk/) by Jonathan Evans
