# DaskPython

Dask is a flexible library for parallel computing in Python. Dask is composed of two parts: ... “Big Data” collections like parallel arrays, dataframes, and lists that extend common interfaces like NumPy, Pandas, or Python iterators to larger-than-memory or distributed environments.

Dask is an open-source project that allows developers to build their software in coordination with scikit-learn, pandas, and NumPy. It is a very versatile tool that works with a wide array of workloads. This tool includes two important parts; dynamic task scheduling and big data collections.

If your task is simple or fast enough, single-threaded normal Pandas may well be faster. For slow tasks operating on large amounts of data, you should definitely try Dask out. As you can see, it may only require very minimal changes to your existing Pandas code to get faster code with lower memory use.

When data doesn’t fit in memory, you can use chunking: loading and then processing it in chunks, so that only a subset of the data needs to be in memory at any given time. But while chunking saves memory, it doesn’t address the other problem with large amounts of data: computation can also become a bottleneck.

# Using Dask to emulate Pandas
The way Dask works involves two steps:

First, you setup a computation, internally represented as a graph of operations.
Then, you actually run the computation on that graph.
When Dask emulates the Pandas API, it doesn’t actually calculate anything; instead, it’s remembering what operations you want to do as part of the first step above. Only once you run compute() does the actual work happen.



The naive read-all-the-data Pandas code and the Dask code are quite similar. So how do they compare on memory usage and runtime, and to the original version which used chunks but wasn’t multi-threaded?

# Peak memory use	Wallclock time	CPU time

Pandas (chunked)	26 MiB	5.9 seconds	6.1 seconds
Pandas (naive)	334 MiB	6.7 seconds	6.9 seconds
Dask	88 MiB	3.9 seconds	6.5 seconds

