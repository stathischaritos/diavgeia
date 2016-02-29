Diavgeia
========

This is python script to scrape the Greek OpenGov API that contains all published decisions of the greek government. The API contains decisions and reports about all (hopefully) government expenses, so it should be interesting to gain insights. 

The data is downloaded and saved in ElasticSearch for an initial view. The script  is able to resume from where it was if it crashes. More fault tolerance can be added in the future.