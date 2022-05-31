# teams

teams partitions players into teams with minimum variance and equal skill level.

## sample

modify the PATH to a csv file for reading and writing and run the python file to update the csv with a better team combination.

### initial

```bash
GREEN : ['A', 'B', 'C', 'D', 'E', 'F'] (650, 600, 600, 1850)
RED : ['G', 'H', 'I', 'J', 'K', 'L'] (633, 566, 583, 1783)
BLACK : ['M', 'N', 'O', 'P', 'Q', 'R', 'S'] (628, 585, 600, 1814)
WHITE : ['T', 'U', 'V', 'W', 'X', 'Y', 'Z'] (657, 542, 557, 1757)

VARIANCE: [141.5, 470.6875, 309.5]
```

### after

```bash
GREEN : ['A', 'W', 'V', 'E', 'N', 'I', 'Y'] (642, 571, 585, 1800)
RED : ['G', 'D', 'Q', 'L', 'X', 'O', 'Z'] (642, 585, 585, 1814)
BLACK : ['M', 'C', 'H', 'K', 'U', 'F'] (650, 566, 583, 1800)
WHITE : ['T', 'R', 'S', 'B', 'P', 'J'] (633, 566, 583, 1783)

VARIANCE: [36.1875, 60.5, 1.0]
```
