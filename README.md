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

### Extra (after sorting desc) 
![image](https://user-images.githubusercontent.com/26707584/128879166-4b7e7739-0d4d-419d-8d23-c31eb2b245b6.png)

---
---
# Assignment 2

## Requirements

-   Make a alphabetic list from all locations from the orders.csv.
    
-   Group by “location” with target “Holland” 
    
-   Count how many times Holland was the target from that location
    
-   Code is executed from Pig View
    
## Expected output
Adriatic Sea, Holland, 6
Albania, Holland, 5
...

## Solution 

1. Import orders.csv data file
2. Create a basic script that will LOAD and DUMP the whole dataset. Execute with Tez as well as MapReduce to see which one has a faster execution time, Tez is almost 3x as fast. Still takes 2 minutes to execute, therefore I created a snippet of the dataset (1.3m rows to 200k rows). 
3. FILTER our dataset on "Holland"
4. GROUP by location and target -> returns a bag with tuples containing each 
5. We now need to FLATTEN our data, and COUNT 1 for each tuple we find inside our group.
6. At last we want to order it alphabetically, using the ORDER command. 
7. DUMP our results. 

### Extra

## Output


`("Adriatic Sea","Holland",1)
("Aegean Sea","Holland",5)
("Albania","Holland",1)
("Armenia","Holland",1)
("Baltic Sea","Holland",326)
("Barents Sea","Holland",38)
("Belgium","Holland",35134)
("Berlin","Holland",1282)
("Black Sea","Holland",3)
("Bohemia","Holland",5)
("Brest","Holland",32)
("Budapest","Holland",1)
("Bulgaria","Holland",2)
("Burgundy","Holland",1153)
...`



