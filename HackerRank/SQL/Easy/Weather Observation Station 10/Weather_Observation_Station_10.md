# Question

Query the list of *CITY* names from **STATION** that *do not end* with vowels. Your result cannot contain duplicates.

**Input Format**

The **STATION** table is described as follows:

![Untitled](../../../../image/HackerRank/Weather_Observation_Station_10/image.jpg)

where *LAT_N* is the northern latitude and *LONG_W* is the western longitude.

# Answer

```sql
SELECT DISTINCT
    city
FROM station
WHERE city regexp '([^aeiou])$'
AND LAT_N > 0
AND LONG_W > 0;
```