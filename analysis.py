from pandas import read_csv
from matplotlib import pyplot


FILEPATH = "master.csv"

dataframe = read_csv(FILEPATH)
dataframe.drop(["HDI for year", "country-year", "suicides/100k pop"], axis=1, inplace=True)
dataframe[" gdp_for_year ($) "] = dataframe[" gdp_for_year ($) "].str.replace(",", "").astype(float)

target = dataframe.pop("suicides_no").values
features = dataframe["age"].values

pyplot.bar(features, target)
pyplot.xlabel("Age Group")
pyplot.ylabel("Suicide Rate")
pyplot.show()
