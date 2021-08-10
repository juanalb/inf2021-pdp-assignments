# inf2021-pdp-assignments
A collection of assignments for the course Parallel Distributed Programming, part of the minor Big Data at Inholland.


# Assignment 1

We want to count the number of ratings given for each movie from the ml-100k data file, we want to achieve this by using Hadoop's MapReduce. The code should be able to execute on the basic HDFS we made in the first two lectures of Parallel Distributed Programming. The code should be executed using python, to easily test this locally without running it on a cluster, we'll use mjrob. 


## Solution 

1. Create a python file called count_ratings.py which while execute our code. 
2. We'll create a function to only map the data into key/value pairs that we'll need to achieve our goal. This function would be called map(), returning the k/v pair for each movie/with a value of 1. Since each row in our dataset is a movie rating, we can use the value of 1.  
3. We'll need to create a reducer, returning the sum of the value for each key(movie).
4. Execute the file locally to test that everything works, we can use Ambari Hive with SQL syntax to confirm this since our knowledge in this space is minimal.
5. We'll execute this in HDFS.

### Extra

6. Sort the movies by their numbers of ratings


## Commands 

### Testing it locally
`python count_ratings.py u.data`

### Using HDFS
`python count_ratings.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar u.data`


## Output
![image](https://user-images.githubusercontent.com/26707584/128789927-5cb0a1ce-f8e5-4aca-952a-e73470c696b6.png)
![image](https://user-images.githubusercontent.com/26707584/128790291-1d082bf9-7c01-4e23-832c-db2b947b29e8.png)

### Extra (after sorting asc) 
![image](https://user-images.githubusercontent.com/26707584/128879166-4b7e7739-0d4d-419d-8d23-c31eb2b245b6.png)





