# Return true if s2 contains a permutation of s1.

## Strategy

Create a counter of s1, tracking the characters and frequency of characters. Then
create a fixed window size s1 that slides over s2. Check to see if that window == the
counter of s1.

## Key Insights

## Common Mistakes
