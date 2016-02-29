Diavgeia
========

This is python script to scrape the Greek OpenGov API that contains all published decisions of the greek government. The API contains decisions and reports about all (hopefully) government expenses, so it should be interesting to gain insights. 

The data is downloaded and saved in ElasticSearch for an initial view. The script  is able to resume from where it was if it crashes. More fault tolerance can be added in the future.


Why is this interesting:
------------------------
Open data is one step towards transparency in government, but the huge amounts of data availlable make it possible for many cases of unusual public spending to go unnoticed as it is burried inside millions of public spending decisions.