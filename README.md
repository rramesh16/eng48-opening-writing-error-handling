# Open, Reading, Writing Files and Error Handling 

Topics covered:
- open()
- try & except
- with & finally 
- exceptions and error handling 

## " All that can go wrong, will go wrong"  - Mr. Murphy

### Error handling:
- Assuming things will break and handling the errors when they do. 
- Providing adequate feedback while failing with grace
- When you handle your error, your code can continue to run
### Definitions 
### try: / except: / finally:
- These blocks of code are used in conjunction to error handling 

````
try:
    block of code
    block of code
except <exception> as <placeholder>:
    block of code
    block of code
    print <placeholder>
finally:
    block that runs after 

````
### Using open() and with()
- When using open() you need to close the files you actually open
- you can skip this step using with()
   ```` 
   open(<file>, <option>) as <placeholder>:
        <placeholder>.readlines()
    ````
#### Exceptions
- These occur when an error occurs 


