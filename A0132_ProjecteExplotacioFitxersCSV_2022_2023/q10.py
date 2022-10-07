# Imports
import utils
import pprint

# -----------------------------------------------------------------------------
# Q10. Mean of H index by region
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def q10():
    # Get clean entries
    raw_entries:   list[dict] = utils.read_csv_file("A0132_ProjecteExplotacioFitxersCSV_2022_2023/scimago-medicine.csv")
    clean_entries: list[dict] = utils.clean_entries(raw_entries)

    # Get list of regions
    region_set:  set[str]  = {entry["Region"] for entry in clean_entries}
    region_list: list[str] = sorted(region_set)

    # Calculate H-index average for each region
    h_index_avg_list: list[float] = [utils.get_h_index_avg('Region', region, clean_entries) for region in region_list]

    # Create ranking
    country_ranking: dict[str, float] = dict(zip(region_list, h_index_avg_list))

    # Sort ranking
    sorted_region_ranking: list[tuple[str, float]] = utils.sort_ranking(country_ranking)

    # Print ranking
    pprint.pp(sorted_region_ranking)
    

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q10()
# -----------------------------------------------------------------------------
