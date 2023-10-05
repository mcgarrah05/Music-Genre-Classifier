# Project Log Book
Music Genre Classification  
Aubrey McGarrah

## 9/28/23
Decide what components of a song (or *fields*, as MSD calls them) that will be looked for the experiment(?) at by using the Million Song Database [Example Track Description](http://millionsongdataset.com/pages/example-track-description/). It shows what function will be used to get that component of a song from the song file.  
  
For my project, I am only concerned about the following fields:
- song name and artist name
- artist location
- danceability
- energy
- key and key confidence
- loudness
- tempo
- time signature and time signature confidence
- year
  
![thumbs up emoji](thumbs-up.png)
  
That is how to start this project.

## 10/3/23
Besides just making a music genre classifier, it would be beneficial (and potentially fun) to analyze the data in the Million Song Dataset subset, looking for relationships between song fields.  

For example, here is a graph that shows the relationship between the tempo of a song and the year the song was released:

<img src="tempo-over-years.png" width="600" height="300">

There doesn't seem to be a significant trend or relationship between the tempo and release year based on the graph.  

**Note: I am using the MSD subset (at least at this point). The MSD subset is a random selection of 10,000 songs (1% of the entire dataset, 1.8 GB) from the entire dataset (280 GB), so because the song files were selected at random, it may affect analytical results, graphs, etc.**  

Here are some questions I may answer:
- How does the tempo affect the genre of a song?
- How does the key signature affect the genre of a song?
- What’s the correlation between the key signature and tempo, if there is one?
- Is danceability and energy related and how?