from langchain.agents import tool
import json

election_result = {}

# Load the JSON files into memory
with open("llm/tools/2019-presidential.json", "r", encoding="utf-8") as file_2019:
    election_result["2019"] = json.load(file_2019)

with open("llm/tools/2024-presidential.json", "r", encoding="utf-8") as file_2024:
    election_result["2024"] = json.load(file_2024)

@tool
def get_district_result(year: str, district: str) -> dict:
    """Returns the district results of the presidential election"""

    if year in ["2015", "2010", "2005", "1999", "1994", "1988", "1982"]:
        return f"The presidential election results for the {district} district in {year} are currently unavailable."
    elif year in election_result:
        return election_result[year]
    else:
        return "There was no presidential election held in 2020."


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