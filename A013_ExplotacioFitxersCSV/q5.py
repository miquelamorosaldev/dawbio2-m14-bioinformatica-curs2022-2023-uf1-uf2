# Imports
import utils
import pprint

# -----------------------------------------------------------------------------
# Q5. Ranking of countries according to H index
# -----------------------------------------------------------------------------

# The utils module has a generic version
# -----------------------------------------------------------------------------
def get_h_index_avg(country: str, clean_entries: list[dict]) -> float:
    "Returns the H-Index average of all entries of the given country"

    # Get all entries of that country
    country_entries: list[dict] = [entry for entry in clean_entries if entry['Country'] == country]

    # Get all H-Indexes of that country
    h_index_list: list[int] = [entry['H index'] for entry in country_entries]

    # Calculate H-Index average
    h_index_avg: float = sum(h_index_list) / len(h_index_list)

    return h_index_avg

# -----------------------------------------------------------------------------
def q5():
    # Get clean entries
    raw_entries:   list[dict] = utils.read_csv_file("scimago-medicine.csv")
    clean_entries: list[dict] = utils.clean_entries(raw_entries)

    # Get list of countries
    country_set:  set[str]  = {entry["Country"] for entry in clean_entries}
    country_list: list[str] = sorted(country_set)

    # Calculate H-index average for each country
    h_index_avg_list: list[float] = [get_h_index_avg(country, clean_entries) for country in country_list]

    # Create ranking
    country_ranking: dict[str, float] = dict(zip(country_list, h_index_avg_list))

    # Sort ranking
    sorted_country_ranking: list[tuple[str, float]] = utils.sort_ranking(country_ranking)

    # Print top 40
    pprint.pp(sorted_country_ranking[0:40])

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q5()
# -----------------------------------------------------------------------------
