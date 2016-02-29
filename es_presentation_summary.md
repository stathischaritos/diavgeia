ElasticSearch Presentation Summary
==================================
ElasticSearch is a relatively new open source tool that provides state of the art search capabilities and a big collection of aggregation tools for data analysis. ES is based on Lucene which is the most popular search engine among academics in Information Retrieval research. ES however, as opposed to Lucene, is very easy to setup, has automatic clustering capabilities and provides a range of search algorithms to use out of the box. 

I have used ES during my previous job to index and search over millions of documents of very high variety. Being a NoSQL framework, ES can handle very complex nested documents and provides full text search over all fields. To get the most out of it you need to provide a well designed mapping, but the default indexing capabilities are strong enough for simple text search.

Text search is usualy taken for granted or overlooked, which leads to really bad examples of search engines (ex. wikipedia, typical forum and domain specific search boxes), but with a very small amount of work ES can provide very good document rankings, autocompletion and spell check.

Beyond Search
=============
ElasticSearch comes with a great collection of usefull aggregation algorithms that can be used to gain insights from the data. From simple things like "most popular terms" to date histograms and nested aggregations, ES can quickly provide you with some basic statistics and interesting transformations. You can see it as a middle step between simple search and more complex machine learning methods.

Use Case
========
My passion for open data in combination with the famously deteriorated economic situation of my home coutry, has drawn my interest to "diavgeia", the public API where all government expenses are supposedly uploaded in a strive for more transparency and accountability. 

Unfortunately, the API is slow, has very limited search capabilities, and offers no aggregation options. The uploading started in 2010 and already there are around 20M documents containing details about government expenses. Even though the data is open, it is really easy for unusual expenses to be ignored.

One example is the case of a Greek doctor who, in the middle of the greek crisis, at a point when the National Health System was short of even the most basic medical materials, was transfered to work in Switcherland receiving an additional 10K euro salary per month. The decision, although not illegal, was discovered last month by a greek newspaper and brough into question - once again - the often unreasonable management of the state's finances. The document was discovered through the open API, but who can tell how many other cases of unwarranted public spending can be brough to light if the data is more systematicaly explored.

Experiment
==========
I decided to scrape the data from the "diavgeia" api and dump it in a local ES instance, to get an initial view of the data and see how I can make its exploration easier than the already provided API. The biggest batch of data per response is 500 documents, so I have to poll the API repeatedly using their paging functionality and custom date range queries, to start from the present and go backwards in time until all the data is downloaded. I added some fault tolerance and resuming capability to the script as it needed to run for more than 12 hours to get the whole dataset. I then used some simple aggregations to check the quality of the provided information. I started the exploration by grouping all expenses by the grantee tax code and summing their respective expense amounts. A list can be seen in the slides.

Results
=======
Although most of the aggregated expenses make sense, there seem to be a few significant errors that were probably made during the data entry process.

    - For some expense entries, instead of the expense amount, the grantee tax code was used, resulting in very misleading aggregated results

    - For many of the expenses there are very few explanations given, which leads me to believe that these decisions would be very hard to use for NLP. A lot of unexplained reference codes are present in these documents which means they could be enriched with relations from this or some other government data source which I haven't found yet.









