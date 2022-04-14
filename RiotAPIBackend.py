import requests

# Riot Development API Key that needs to be refreshed daily
riot_api_key = "?api_key=RGAPI-31d68dd1-a577-4499-bfca-b63190e2b21e"

# Usage of this API in this program creates a dictionary where a champion can be found by its id
champions_dict = {}
champions_list_url = "http://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json"
champions_list_response = requests.get(champions_list_url)
champions_list_data = champions_list_response = champions_list_response.json()["data"]
for champ_name, champ_data in champions_list_data.items():
    champions_dict[int(champ_data["key"])] = champ_name


# This function creates the challenger leaderboard
def get_challenger_leaderboard():
    league_leaderboard_url = "https://na1.api.riotgames.com/lol/league/v4/" \
                                     "challengerleagues/by-queue/RANKED_SOLO_5x5" + riot_api_key
    league_leaderboard_response = requests.get(league_leaderboard_url)
    league_leaderboard_raw_data = league_leaderboard_response.json()
    league_leaderboard_sorted = sorted(league_leaderboard_raw_data["entries"], key=lambda x: -x["leaguePoints"])[:10]

    player_data = {}
    for player in league_leaderboard_sorted:
        most_played_champions_url = "https://na1.api.riotgames.com/lol/champion-mastery/" \
                                    "v4/champion-masteries/by-summoner/"
        summoner_id = player["summonerId"]
        summoner_name = player["summonerName"]
        total_wins = player["wins"]
        total_losses = player["losses"]
        summoner_lp = player["leaguePoints"]

        most_played_champions_response = requests.get(most_played_champions_url + summoner_id + riot_api_key)
        most_played_champion_id = most_played_champions_response.json()[0]["championId"]
        player_data[summoner_name] = {"most_played": champions_dict[most_played_champion_id],
                                      "wins": total_wins, "losses": total_losses,
                                      "league_points": summoner_lp}
    return player_data


