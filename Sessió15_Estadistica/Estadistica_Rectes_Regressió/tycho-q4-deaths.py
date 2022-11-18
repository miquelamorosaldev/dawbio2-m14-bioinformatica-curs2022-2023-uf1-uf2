# Imports
import pandas  as pd

# -----------------------------------------------------------------------------
# Student name: Marc Coca Moreno
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: get_tuberculosis_deaths()
# -----------------------------------------------------------------------------
# 
# - You are given the fixed Tycho dataset.
# - Write a function to answer this question:
#   - Plot the deaths caused by tuberculosis in these states: New York, California
#   - and Texas in year 1897.
# 
# - Entry parameters:
#   - The dataframe with all entries.
#   - 
# - Return parameters:
#   - Return a dataframe.
#   - The dataframe must have the following columns in the same order:
#     week, NY_deaths, CA_deaths, IL_deaths
#   - The week column must start from 1 and end in 52.
# 
# - Hint:
#   - The easiest way to group the data is create a dataframe with the epi_week and num_deaths
#   - of each state and then create a new dataframe.
#   - Check the q4_diseases_example.pdf to see how should look the resulting plot.
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - Run pytest to make sure you succeeded.
# -----------------------------------------------------------------------------


# - Write your solution here.
# - This function must be pure. Remember to delete your print() calls when done.
# ------------------------------------------------------------------------------------
def get_state_disease_mask(disease: str, state: list[str]):
    
    return (entries.loc[ : ,'disease'] == disease) & (entries.loc[ : ,'state']).isin(state)


def get_tuberculosis_deaths(entries: pd.DataFrame) -> pd.DataFrame:
    
    # Another HINT. Filter records with disease TUBERCULOSIS in NY.
    #tuberculosis_NY_mask = get_state_disease_mask('TUBERCULOSIS',['NY',"CA","TX"])
    diseases: pd.DataFrame = (entries)
    
    diseases_mask = get_state_disease_mask('TUBERCULOSIS',['NY',"CA","TX"])
    
    diseases = diseases[diseases_mask]
    diseases["week"] = diseases["epi_week"].astype(str).str.slice(4,6).astype(int)
    diseases = diseases[["week","state","num_deaths"]]
    diseases = diseases.groupby(["week","state"]).agg({"num_deaths":"sum"}).reset_index()
    diseases = pd.pivot_table(diseases,index="week",columns="state",values="num_deaths", fill_value=0).reset_index()

    return diseases


# Main
# ------------------------------------------------------------------------------------
if __name__ == "__main__":

    entries:    pd.DataFrame = pd.read_csv("data/tycho-fixed22.csv", sep=",")
    # Filter records by year.
    entries = entries.query('year == 1897')
    diseases:   pd.DataFrame = get_tuberculosis_deaths(entries)

    diseases.set_index('week', drop=True) \
        .plot(kind='line', title='Tuberculosis deaths in 1897')  \
        .get_figure().savefig("output/diseases2.pdf")
    print(diseases)

# -----------------------------------------------------------------------------