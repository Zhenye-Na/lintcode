/*
Enter your query here.
*/


/*

LENGTH()      returns the length of the string measured in bytes. 
CHAR_LENGTH() returns the length of the string measured in characters.

*/


(SELECT CITY, char_length(CITY)
FROM STATION
WHERE char_length(CITY) = (SELECT MAX(char_length(CITY))
                           FROM STATION
                          )
ORDER BY CITY
LIMIT 1
)
UNION
(SELECT CITY, char_length(CITY)
FROM STATION
WHERE char_length(CITY) = (SELECT MIN(char_length(CITY))
                           FROM STATION
                          )
ORDER BY CITY
LIMIT 1
)
;