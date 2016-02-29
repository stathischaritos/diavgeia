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






