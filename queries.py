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
                    "field": "extraFieldValues.sponsor.sponsorAFMName.name"
                },
                "aggs": {
                    "expenses": {
                        "sum": {
                            "field": "extraFieldValues.sponsor.expenseAmount.amount"
                        }
                    }
                }
            }
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