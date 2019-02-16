# Simple demo of searching for a book through different editions

A book is normally printed in many editions and book types, each of these varience would have a unique ISBN number associated with it. Therefore many editions and varience of the same book may come across as a different item when searching online. E.g A hardcover and a paperback version of the same book might be treated as a different item. 

In this demo we demonstrate how we can collapse all the varience of the same book into one. Specifically demostrating a searching ability when looking for a book and presents the most relevant edition as a result. 

## Demo

In this demostration, we have added 2 books - 4 editions of "Harry Potter and the Half-blood Prince" and 2 editions of "Harry Potter and the Prisoner of Azkaban"

Here is a table representation of ```Books.csv```

| Title                                    | Author      | Edition | ISBN          | Booktype  | Rating | Language  |
|------------------------------------------|-------------|---------|---------------|-----------|--------|-----------|
| harry potter and the half-blood prince   | j.k rowling | 01      | 9781408855706 | paperback | 4.5    | English   |
| harry potter and the half-blood prince   | j.k rowling | 01      | 1408855941    | hardcover | 4      | English   |
| harri potter i napivkrovnyi prynts       | j.k rowling | 01      | 9667047296    | hardcover | 5      | Ukrainian |
| harry potter and the half-blood prince   | j.k rowling | 01      | 9654822318    | paperback | 4      | Hebrew    |
| harry potter and the prisoner of azkaban | j.k rowling | 01      | 1408855674    | paperback | 4      | English   |
| harry potter e il prigioniero di azkaban | j.k rowling | 01      | 886715267X    | paperback | 4      | Italian   |


Here are some commands to play with:
prerequisite: Python >3.0

```bash
python BookSearch.py "Harry"
python BookSearch.py "half-blood price"
python BookSearch.py "Azkaban"
python BookSearch.py "J.K Rowling"

# Try differnet language (in Ukrainian)
python BookSearch.py "Harri Potter"
```
