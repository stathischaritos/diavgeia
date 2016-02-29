Diavgeia
========
This is a python script to scrape the Greek OpenGov API that contains all published decisions of the greek government. The API contains decisions and reports about all (hopefully) government expenses, so it should be interesting to gain insights about public spending. 

The data is downloaded and saved in ElasticSearch for an initial abalysis. The script is able to resume from where it was if it crashed. More fault tolerance can be added in the future.


How to run:
-----------
For now it is best to run the script using "forever" to keep it running through crashes.

    
    npm install -g forever 

    forever start -c python main.py


Why is this interesting:
------------------------
Open data is one step towards transparency in government, but the huge amounts of data availlable make it possible for many cases of unusual public spending to go unnoticed as it is burried inside millions of public spending decisions.

