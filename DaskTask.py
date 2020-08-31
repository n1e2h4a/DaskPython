
import dask.dataframe as dd

# Load the data with Dask instead of Pandas.
df = dd.read_csv(
    "newdask.csv",
    blocksize=16 * 1024 * 1024, # 16MB chunks
    usecols=["Name",
             "Technology"],
)

# Setup the calculation graph; unlike Pandas code,

def get_counts(df):
    tech = df.groupby("Technology")
    name = tech["Name"]
    return name.value_counts()
result = get_counts(df)

# Actually run the computation, using 2 threads:
result = result.compute(num_workers=2)

# Sort using normal Pandas DataFrame, since Dask's
# Pandas emulation doesn't implement this method:
result.sort_values(ascending=False, inplace=True)

print(result)

