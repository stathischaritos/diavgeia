QUERIES = {
    "expensesPerSigner" : {
        "query": {
            "filtered": {
                "query": {
                    "match_all": {}
                }
            }
        },
        "aggs": {
            "sponsors": {
                "terms": {
                    "size":100,
                    "order" : {
                        "expenses" : "desc"
                    },
                    "field": "extraFieldValues.sponsor.sponsorAFMName.name"
                },
                "aggs": {
                    "expenses": {
                        "sum": {
                            "field": "extraFieldValues.sponsor.expenseAmount.amount"
                        }
                    },
                    "top_sponsor_hits": {
                        "top_hits": {
                            "sort": [
                                {
                                    "submissionTimestamp": {
                                        "order": "desc"
                                    }
                                }
                            ],
                            "_source": {
                                "include": [
                                    "subject",
                                    "documentUrl",
                                    "url",
                                    "extraFieldValues"
                                ]
                            },
                            "size" : 10
                        }
                    }
                }
            },
            "expense_stats" : { "stats" : { "field" : "extraFieldValues.sponsor.expenseAmount.amount" } }
        }
    },
    "getOldestEntry": {
        "query": {
            "match_all": {}
        },
        "sort": [
            {
                "submissionTimestamp": "asc"
            }
        ]
    }
}