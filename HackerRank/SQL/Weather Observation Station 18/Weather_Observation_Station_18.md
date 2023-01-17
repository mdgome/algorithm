# Question

Consider $P_1(a,b)$ and $P_2(c,d)$ to be two points on a *2D* plane.

- `a` happens to equal the minimum value in *Northern Latitude* (*LAT_N* in **STATION**).
- `b` happens to equal the minimum value in *Western Longitude* (*LONG_W* in **STATION**).
- `c` happens to equal the maximum value in *Northern Latitude* (*LAT_N* in **STATION**).
- `d` happens to equal the maximum value in *Western Longitude* (*LONG_W* in **STATION**).

Query the [Manhattan Distance](https://xlinux.nist.gov/dads/HTML/manhattanDistance.html) between points $P_1$ and $P_2$ and round it to a scale of `4` decimal places.

**Input Format**

The **STATION** table is described as follows:


![Untitled](../../../image/HackerRank/Weather_Observation_Station_18/image.jpg)

where *LAT_N* is the northern latitude and *LONG_W* is the western longitude.

# Answer

```sql
WITH distance AS
(
    SELECT 
        MIN(lat_n) AS a
        , MIN(long_w) AS b
        , MAX(lat_n) AS c
        , MAX(long_w) AS d
    FROM station
)

SELECT
    ROUND( (c - a) + ( d - b ), 4)
FROM distance

/*
SIMPLE VERSION
SELECT
    ROUND( ((MAX(lat_n) - MIN(lat_n)) + ( ( MAX(long_w) - MIN(long_w) ) ) ) ,4)
FROM station
*/
```
   
$Distance = (c-a) + (b-d)$