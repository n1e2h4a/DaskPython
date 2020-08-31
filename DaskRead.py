import dask.dataframe as dd


print("Read locally...")
df = dd.read_csv(
    "./log_data.csv",
)
print(df)
print(df.compute())
print(len(df))


print("\nRead on HDFS...")
df = dd.read_csv("hdfs://localhost:54310/user/newtask/log_data.csv")
print(df)  # Columns are correctly read by npartitions=0
print(df.compute())  # Empty
print(len(df))  # Error
