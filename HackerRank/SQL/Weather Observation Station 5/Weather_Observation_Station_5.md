# Questions

Query the two cities in **STATION** with the shortest and longest *CITY* names,
as well as their respective lengths (i.e.: number of characters in the name).
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
The **STATION** table is described as follows:

![Untitled](../../../image/HackerRank/Weather_Observation_Station_5/image.jpeg)

where **LAT_N** is the northern latitude and **LONG_W** is the western longitude.

**Sample Input**

For example, **CITY** has four entries: **DEF, ABC, PQRS** and **WXY**.

**Sample Output**

`ABC 3
PQRS 4`

**Explanation**

When ordered alphabetically, the **CITY** names are listed as **ABC, DEF, PQRS,** and **WXY**, with lengths  and . The longest name is **PQRS**, but there are  options for shortest named city. Choose **ABC**, because it comes first alphabetically.

**Note**You can write two separate queries to get the desired output. It need not be a single query.

# Answer

```sql
SELECT
    city
    , LENGTH(city)
FROM station
WHERE LENGTH(city) = (SELECT MIN(LENGTH(city)) FROM station)
ORDER BY city ASC LIMIT 1;

SELECT
    city
    , LENGTH(city)
FROM station
WHERE LENGTH(city) = (SELECT MAX(LENGTH(city)) FROM station)
ORDER BY city DESC LIMIT 1
```