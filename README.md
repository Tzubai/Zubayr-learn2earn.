# Zubayr-learn2earn.Python
## to override the official documentation for print function: Default (print(*objects, sep=' ', end='\n'))
### What this indicates as follows is this--
```
1- print : the name of this function is, of course print.

2- Then there's a parenthesis over here and another close parenthesis () : Everything inside of those parentheses are the arguments, the potential arguments, to the function.
"""
However, when we're looking at these arguments in the documentation like this, there's technically a different termthat we would use.
These are technically the parameters to the function.
So when you're talking about what you can pass to a function and what those inputs are called, those are parameters.
When you actually use the function and pass in values inside of those parentheses, those inputs, those values are arguments.
"""

3- *objects :
"""
just know that an asterisk, a star, and then the word "objects" means that the print function can take any number of objects.
You can pass in 0 strings of text, one string, two strings, or, technically, infinitely many
"""

4- sep=' ': stands for seperator and the default value of separator is apparently a single blank space.
So this just means that when you pass multiple arguments to print, by default they're going to be separated by a single space.

5- end='\n' : Backslash n means new line, and it's a way textually of indicating if and when you want the computer effectively to move the cursor to the next line, create a new line of text. just means that By default, when you pass arguments to print,
it's the whole thing is going to be ended with a new line (/n).
```
## we can leverage the print documentation to solve problems by overriding the default values to any value of our choice, Eg:
```
print("hello,", sep=' ', end='??')
print("hello", sep='_', end='')
```
