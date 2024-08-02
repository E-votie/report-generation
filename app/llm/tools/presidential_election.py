from langchain.agents import tool

@tool
def get_district_result(year: str, district: str) -> dict:
    """Returns the district results of the presidential election"""
    res = {
        "district": district,
        "year": year,
        "valid_votes": 1369177,
        "rejected_votes": 15333,
        "total_polled": 1383510,
        "candidate_results": [
           {"candidate_name": "Gotabaya Rajapaksa", "Votes_Received": 727713},
           {"candidate_name": "Sajith Premadasa", "Votes_Received": 559921},
           {"candidate_name": "Anura Kumara Dissanayaka", "Votes_Received": 53803},
           {"candidate_name": " Mahesh Senanayake", "Votes_Received": 10335},
        ]
    }

    return res


@tool
def get_all_island_result(year: str) -> dict:
    """Returns the all island results of the presidential election and winner"""
    res = {
        "year": year,
        "valid_votes": 13252499,
        "rejected_votes": 135452,
        "total_polled": 13387951,
        "winner": "Gotabaya Rajapaksa",
        "candidate_results": [
           {"candidate_name": "Gotabaya Rajapaksa", "Votes_Received": 6924255},
           {"candidate_name": "Sajith Premadasa", "Votes_Received": 5564239},
           {"candidate_name": "Anura Kumara Dissanayaka", "Votes_Received": 418553},
           {"candidate_name": " Mahesh Senanayake", "Votes_Received": 49655},
        ]
    }

    return res