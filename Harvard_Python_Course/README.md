# Zubayr-learn2earn.Python
## ***STRING(str)***
### to override the official documentation for print function: Default (print(*objects, sep=' ', end='\n'))
#### What this indicates as follows is this--
```
1- print : the name of this function is, of course print.

2- Then there's a parenthesis over here and another close parenthesis () : Everything inside of those parentheses are the arguments, the potential arguments, to the function.
"""
However, when we're looking at these arguments in the documentation like this, there's technically a different term that we would use.
These are technically the parameters to the function.
So when you're talking about what you can pass to a function and what those inputs are called, those are parameters.
When you actually use the function and pass in values inside of those parentheses, those inputs, those values are arguments.
"""

3- *objects :
"""
just know that an asterisk, a star, and then the word "objects" means that the print function can take any number of objects.
You can pass in 0 strings of text, one string, two strings, or, technically, infinitely many
"""

4- sep=' ': stands for separator and the default value of separator is apparently a single blank space.
So this just means that when you pass multiple arguments to print, by default they're going to be separated by a single space.

5- end='\n' : Backslash n means new line, and it's a way textually of indicating if and when you want the computer effectively to move the cursor to the next line, create a new line of text. just means that By default, when you pass arguments to print,
it's the whole thing is going to be ended with a new line (/n).
```
### we can leverage the print documentation to solve problems by overriding the default values to any value of our choice, Eg:
```
print("hello,", sep=' ', end='??')
print("hello", sep='_', end='')
```
### Positional Parameters VS Named Parameters
```
Positional parameters:
positional in the sense that the first thing you pass to print gets printed first.
The second thing you pass to print after a comma gets printed second. And so forth.

Named parameters: [print("hello,", sep=' ', end='??')]
Named: [SEP = separator, or END, E-N-D for the line ending.]
With named parameters (also called keyword arguments), you specify the parameter name when passing the value. Order doesn't matter.
```
## ***FLOAT***
### Float function in Python Documentation:
```
round(number[, ndigits])
```
### What this indicates:
```
1- round: The name of this function here is of course Round and its first argument is a number.
the arguments in parenthesis: Notice this time there's no star, there's no star objects
like there was for print.
The Round function takes just one number as its first argument, period. That's its positional parameter.
2- (number[, ndigits]): But notice this syntax in square brackets,this is a convention in programming or technology more generally, when you see square brackets and documentation like this, this means that you're about to see something optional.
And so what this means is that if you want to specify more precisely the number of digits that you want the round function to round to, you can specify it here by adding a comma and then that number.
So if we read the documentation, if you don't specify a number of digits,
you just specify the number to round, it rounds to the nearest integer. But suppose you want around to the tenths place, or the hundredths place that is one or two digits after the decimal point, you could additionally pass in comma 1 or comma 2 to be more precise.
```
## ***FUNCTIONS***
```
DEF, DEF for define:
So here too, just as STR is short for string and INT is short for integer,
DEF is short form for define.
If and when you want to define, create, invent your own functions,
you can do so using this keyword in Python.
```
***Usage***
```
def funcName():
The parentheses with nothing inside means that this function at the moment is not going to take any inputs, no arguments there too.
The colon means, stay tuned for some indentation. Everything that's indented beneath this line of code is going to be part of this function.
```
