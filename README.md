# favorite-fruit


## Guidelines
Program Goal: Determine a user's favorite fruit of options available within a list.

1. Your program should accept a `list` of unknown length containing fruits.
2. Your program should present the user with a binary choice between any two given fruits in the list.
3. Your program should traverse the entire list and print out the most highly ranked fruit when no more list items are available.
4. Your program can not be dependent on a known list length

## Tips
- Consider **using pseudo-code** to plan your program design
- Consider executing program logic within a `while loop`
- Consider using a for loop for traversing the list
- Consider making user input binary (A or B) or making the user input caps-insensitive.

## For Loop
Contary to the bad example I gave during our meeting, please look at this for loop:

```
mylist = ['frog', 'hog', 'dog']

for word in range(len(mylist)):
    print("Current Word is: " + mylist[word])
    print("Next Word is: " + mylist[word+1])
```

Note that one has to use len(mylist) in order to iterate using `word+1` as word+1 is an integer...this gets back to the typing we discussed this evening.
 
Also note that there is a condition missing that protects this loop from accessing out of the list length.

## Contributing

Please contribute code as a branch named as your first name.


