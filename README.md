# YouTube Data API Project
***

This is an exploratory data analysis project where I utilize [YouTube's Data API v3](https://developers-dot-devsite-v2-prod.appspot.com/youtube) to curate my own datasets describing a subset of roughly 80 channels, over 4000 of their videos, and over 100,000 comments. The purpose of this project is to obtain insights into the current state of the platform, and identify trends in video lengths, video titles, upload timelines, and more. 

I have also set up a local data pipeline, including scripts for automating the following:
- querying the API
- retrieving/parsing and validating the resulting data
- preliminary preprocessing/cleaning (normalization, data type conversions, NLP, etc.)

Given that I have more or less automated to the process of data retrieval and cleaning, I plan on adding to this project in the future to focus on different samples of YouTube channels.


## Process Outline
|Step|Task|Description|
|--|--|--|
|1|Data Querying|Specify desired fields for retrieval, query API for desired info|
|2|JSON Parsing/Data Validation|Parse the raw data returned, perform perliminary validation checks, save as csv|
|3|Preprocessing|Prepare data for analysis by removing any null entries using normalization techniques, dtype conversions, and NLP on text fields. Which operations are performed are specified by a few input parameters, then save result in csv format|
|4|Analysis|Using the prepared and cleaned data for data visualization and statistical analyses|


## Data Selection Criteria
The process for selecting YouTube channels was done manually, through a mix of suggestions from chatGPT, channels I am familiar with, or notable figures on the platform (either currently or historically). My goal was to compile a dataset that includes at least one or more creators from a wide range of genres, including but not limited to:

- News
- Sports
- Gaming
- Music
- Lifestyle/vlog
- Animation/Art
- Commentary/video essay
- Documentary
- Beauty
- ASMR
- Comedy
- Entertainment
- Television/network

The channels selected all fit the following criteria:
- \> 1,000,000 subscribers
- primarily English-speaking or their audience is primarily English-speaking

