# Question

Consider $P_1(a,c)$ and $P_2(b,d)$ to be two points on a 2D plane where $(a,b)$ are the respective minimum and maximum values of *Northern Latitude* (*LAT_N*) and $(c,d)$ are the respective minimum and maximum values of *Western Longitude* (*LONG_W*) in **STATION**.

Query the [Euclidean Distance](https://en.wikipedia.org/wiki/Euclidean_distance) between points $P_1$ and $P_2$ and *format your answer* to display `4` decimal digits.

**Input Format**

The **STATION** table is described as follows:

![Untitled](../../../image/HackerRank/Weather_Observation_Station_19/image.jpg)

where *LAT_N* is the northern latitude and *LONG_W* is the western longitude.

# Answer

```sql
WITH distance AS
(
    SELECT 
        MAX(lat_n) AS a
        , MIN(lat_n) AS b
        , MAX(long_w) AS c
        , MIN(long_w) AS d
    FROM station
)
SELECT
    ROUND(SQRT( POW(a - b, 2) + POW(c - d, 2) ), 4)
FROM distance
```

$Distance = \sqrt{(a-b)^2 + (c-d)^2}$