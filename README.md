
# Zang
Zang is a dynamically typed high level programming language.<br>![image](https://user-images.githubusercontent.com/109184310/227681329-6b8cb38f-d7ec-4504-a349-d0faf247faae.png)
<<
Zang's Mascot, Sid


## Running a script
To run a script must go into the command prompt and make sure your working directory has your script you want to run and the run.py file and the intepreter.py file. Then run. `python run.py yourfile.zang` and it will run
## Starting the shell
To start the shell simply run, in the command line `python shell.py` and thats it
## Text Editor
I would **highly** recommend using the text editor to write your programs, it has syntax highlighting and a built in terminal to do everything you need to do, it is very useful to use and is a great tool to help you write better Zang. This is what a simple fibbonachi sequence and fizzbuzz in Zang's Text editor![image](https://user-images.githubusercontent.com/109184310/227738557-c5648b93-e083-4e75-b630-73edb1e345bd.png)
![image](https://user-images.githubusercontent.com/109184310/227738465-a286198a-97b1-47ae-8abf-de42a73b9630.png)


## Tutorial
### Your first Zang Program
Your first Zang program will be a simple hello world program, all it does is output hello world to the console. To output any value to the std.output you would do `writeln` to write a line and then your value between the corresponding brackets, so a simple hello world program would look like this:<br>
```python
writeln("Hello, World!")
```
There it is, now save it, run it and see what it outputs, it should output
```
Hello, World!
```
### Variables
Variables are pretty simple, to allocate memory into a variable you would use the `let` keyword, like this:<br>
```javascript
let message = "Hello, World!"
```
now you can output this to make another hello world program, this time using variables, like this:
```javascript
let message = "Hello, World!"
writeln(message)
```
This, once again should output 
```
Hello, World
```
### For loops
A little step up from the past 2 programs we made, this program we made will include a loop, How exciting! This specific one we will make will count up to 100 and output the numbers:<br>
```javascript
for i = 0 to 100 then
   writeln(i)
end
```

When you run this you should get numbers 0-99 being outputted to your console.<br>

### Endless Loop?!?
Yes, we can do an endless while true loop with Zang:<br>
```javascript
while True then
  writeln("Endless!")
end
```
-Note: I dont suggest running this as it will print "Endless!" to the console forever, but if you want to, go for it!
### Reading Input
To read input you just have to do `read("")` to gather input. Make sure you have a string, cannot be an empty bracket. For example:<br>
```javascript
let x = read(">")
writeln(x)
let x = read_int(">")
writeln(x+x)
```
### Colors!
I specifically wanted it to be easy to print in colored formats in Zang, so i made an easy color library implemented into it. An example of it would be like this:<br>
```python
writeln(col_red+"Red Text!"+col_reset)
writeln(col_purple+"Purple Text!"+col_reset)
writeln(col_blue+"Blue Text!"+col_reset)
writeln(col_yellow+"Yellow Text!"+col_reset)
writeln(col_green+"Green Text!"+col_reset)
```
-Note: It is important to include the col_reset at the end of every color line, otherwise it wont know the bounds and will print everything in that color from there on, you have to tell it where to stop coloring text

### Lets make another, better program
With all this newgiven knowledge, lets write a simple echo program, which takes input from a user, stores it in a variable and then outputs that variable in colored, formatted text:
```javascript
while True then
   let echo = read(">>")
   writeln(col_purple+echo+col_reset)
end
```
This isnt too complex but is still a fun program to mess around in.<br>
### CMD Interop
Zang can interop with cmd systems to pass commands through to the cmd line! It can do some pretty powerful things so be careful with it, this is how it looks:<br>
```javascript
passc("start cmd") 
```
This will pass the command "start cmd" to the command line.<br>

### Command app with Zang
We can now make a simple program with the Zang system library:<br>
```javascript
while True then
   let echo = read(col_purple+"Command>"+col_reset)
   passc(echo)
end
```
This is a simple command line made in Zang.

### Put?
There are 2 ways mainly to write to the std output. These would be `writeln` and `put` and theres an important difference between these.<br>
`put` will print a value with no newline, meaning that if you did:<br>
```javascript
put("hello")
put("world")
```
It would output
```
helloworld
```

Whereas if you did this with `writeln`:<br>
```javascript
writeln("hello")
writeln("world")
```
It would output 
```
hello
world
```
`put` can be useful for various things where you need to output a value with no newline.

### System Messages
Adding again to the extensive system library we can do a system message, that looks like this:<br>
![image](https://user-images.githubusercontent.com/109184310/227674480-e3bf9ed2-e9ed-4522-a467-6aea0432213c.png)<br>
The way you can do this is very easy, its just `msg` so a program that uses it would look like this:<br>
```javascript
msg("Hello, Zang!")
```
Its a very interesting tool to use and can be usd in many projects to display user sucess or error messages
### Web Interop
Just like Zang can interop with Cmd, it can also interop with your native web browser and allows you to open any url you want from Zang, it looks like this:<br>
```javascript
let url = read("What url do you want to open: ")
opentab(url)
```
### Types
You can get the type of something by calling `classof`, here is an example:
```javascript
writeln(classof([1,2,3]))
writeln(classof(1))
writeln(classof(1.1))
writeln(classof(True))
writeln(classof("String!"))
```
This will output:
```
array
number
number
number
string
```
This is because floats and ints share a class, for simplicity and boolean is equal to a number, 1 is true and 0 is false, this is why if you do True + True, it outputs 2.
This little program prompts a user for a url to open and then opens whatever they enter.
### Functions
Functions are done with the `fn` keyword and dont require a `then` keyword, let me show you a function which multiplies 2 numbers<br>
```rust
fn multiply_nums(num1, num2)
   writeln(num1*num2)
end

multiply_nums(5,10)
```
This would output:
```
50
```
Functions can also return values

### Comments
To do comments it is a pipe char, (|) for example:
```python
writeln("hello") | Comment right here!
put("Bye!") | Another comment!
```
-Note: It is important to know that there has to be a newline under the comment, otherewise the interpreter cannot look for a "\n" to stop parsing the comment. Sorry, i know this is bad but it would be better then a grouping based comment system.
### Importing a file
You can import a file through zang using the `using` keyword. Like this
```javascript
using("main.zang")
init()
``` 
Given that you have defined any function in your code, you can call it after using it. Make sure everything in your file is within a function though, otherwise anything in the global scope will run on import.<br>
If you go to `examples/include` you will see all the external libraries for zang and examples of them being imported and used in the `main.zang` file. Descriptions of these:<br>
1. `win.zang` - A windows interop library
2. `bettermath.zang` - A math library to improve the std math library
3. `zecl.zang` - Zang Expanded Color Library expands the already large inbuilt color library and doesnt require closing tags, it goes from `writeln(col_red+"red"+col_reset` to `writeln(red("red"))`. If you are making a program in zang with alot of color change, i would suggest using `zecl.zang`
4. `demos.zang` - A library full of zang demos with things like fizzbuzz to a number, counting up, name printing programs and more.<br>
<br>
If you make any Zang library please! Add it to the `examples/include/libraries` and edit the `main.zang` to include it, i would love for some community libraries<br>

### Nil values
To use Nil values in Zang its as simple as just using `nil` like this:
```javascript
let x = nil
writeln(nil)
```
### Multiline Statements
You can write any Zang program in one line using a semicolon, like this:
```javascript
let x = 100; let x = tostr(x); writeln(x*3); msg(x*3)
```

### Type conversion
You can convert a number to a string from an integer or list. This is how:
```javascript
let num = read_int("Enter num>")
let str_num = tostr(num)
writeln("You typed: "+col_purple+num+col_reset)
```
This can be useful for using numbers in strings

### Arrays
To define an array you just have to type whatever you want within [] like this:
```javascript
let list = [1,2,3]
```
We can do some things with this array, if we want to get an element of the array, and remove it we must pop from the index and that will take it out of the array and store it in whatever else you want. Here is an example:
```javascript
let list = [1,2,3]
let middle = pop(list, 1)
writeln(middle)
writeln(list)
```
This would output:
```
2
1,3
```
But, this removes it from the array, if you just want to get the element and not remove it, you can use the `get` function, for example:
```javascript
let arr = [1,2,3,4,5]
let x = get(arr, 2)
writeln(x)
writeln(arr)
```
this would output:
```
3
[1,2,3,4,5]
```
That is how you can get elements, there are more tools, such as extend, which will extend an array with another array, for example:
```javascript
let list = [1,2,3]
let list2 = [4,5,6]
extend(x, y)
writeln(x)
```
This will output:
```
[1,2,3,4,5,6]
```
You can also traditionally append elements to an array, for example:
```javascript
let list = ["My", "name is"]
append(list, "Jack")
writeln(list)
```
This would output:
```
["My", "name is", "Jack"]
```
You can also split a string into words with the `split` keyword, like this:
```javascript
let string = "Hello World !!!"
writeln(split(string))
```
This would output:
```
["Hello", "World", "!!!"]
```
And last but not least, you can get the length of an array with the `len` keyword, for example:
```javascript
let list = [1,2,3]
writeln(len(list))
```
This would return:
```
3
```
### Random Library
I will soon expand the inbuilt random library because as of now, all it can do is generate a random float between 0-1. But to call this, you just do:
```javascript
writeln(random)
```

### Math Library
There are two inbuilts within the Library, there is Pi and inf. Inf is an infinite number and pi is 3.14159265, this is how you can acess them<br>
```javascript
writeln(math_inf)
writeln(math_pi)
```

### String Library
There is a small string library that is included that includes punctuation, letters and digits. Here is an example:<br>
```javascript
writeln(string_punct)
writeln(string_letters)
writeln(string_digits)
```
There is also a string manipulation tool, `trim` to trim whitespace off either side of the string, an example:
```javascript
let untrimmed = "    hello     "
let trimmed = trim(untrimmed)
if trimmed == "hello" then
     writeln("Trim works!")
end
```

### Sys Library
There is an inbuilt Zang/sys library which has things like the link to the github, the version, the platform, the argv list and the sys version its running on, to call it, all you have to do is:<br>
```javascript
writeln(zang_link)
writeln(zang_platform)
writeln(zang_version)
writeln(zang_argv)
writeln(zang_sysv)
```
#### zang_i
zang_i is part of the sys library and is an interpreter function, lets say you have some zang code, you can interpret that into tokens, its like the compile function in python, heres an example:
```javascript
let code = "tostr(trim(writeln(5+5)))"
let tokens = zang_i(code)
writeln(tokens)
```
This is a very interesting function that tokenises whatever you pass into it. So for example the program above would output:
```
IDENTIFIER:tostr, LPAREN, IDENTIFIER:trim, LPAREN, IDENTIFIER:writeln, LPAREN, INT:5, PLUS, INT:5, RPAREN, RPAREN, RPAREN, EOF
```


### File Library
As of 0.1 the file library is small. It has two functions, `open` and `using`, we looked at `using` already, but in short, `using` takes in a .zang file and imports it so you can use it, like `import` with python. On the other hand `open` will open, read and close a file.
```javascript
let filename = read("What file do you want to print: ")
let contents = open(filename)
writeln(contents)
```
I am looking to expand the file library
## Thats All Folks!
Thats all to see here, Zang is just a little intermediate language for until i create my own compiled language, which will be much better. Thank you for reading and join to our [discord server](https://discord.gg/288gfGxAGr)
