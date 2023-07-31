from pandas import read_csv, DataFrame
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer

FILEPATH = "master.csv"

dataframe = read_csv(FILEPATH)

dataframe.drop(["HDI for year", "country-year", "suicides/100k pop"], axis=1, inplace=True)

def encode_column(dataset: DataFrame, column_index: int, column_name: str) -> None:
    """
    Encodes categorical columns with numeric values
    """
    # Extract unique values from the specified column
    column_values = dataset[dataset.columns[column_index]].unique()

    # Creating a mapping of unique values to numeric indices
    column_mapping = {}
    for index, _ in enumerate(column_values):
        column_mapping[column_values[index]] = index

    dataset[column_name] = dataset[column_name].map(column_mapping)

# Encoding categorical columns with numeric values
encode_column(dataframe, 0, "country")
encode_column(dataframe, 1, "year")
encode_column(dataframe, 2, "sex")
encode_column(dataframe, 3, "age")
encode_column(dataframe, 7, "gdp_per_capita ($)")
encode_column(dataframe, 8, "generation")

dataframe[" gdp_for_year ($) "] = dataframe[" gdp_for_year ($) "].str.replace(",", "").astype(float)

target = dataframe.pop("suicides_no").values

data = dataframe.values.astype(float)

# Creating a ColumnTransformer to apply different preprocessing steps to different columns
transformer = ColumnTransformer(
    [
        # One-hot encoding categorical columns
        ("Encoder", OneHotEncoder(sparse_output=False), [0, 1, 2, 3, 6, 7]),
        ("Scaler", MinMaxScaler(), [4, 5]),  # Scaling numerical columns
    ],
)

transformed_data = transformer.fit_transform(data)

print(DataFrame(transformed_data))
