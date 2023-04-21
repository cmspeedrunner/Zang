import interpreter as pret
import time
import sys
import os
os.system("")
start_time = time.time()  # Start the timer

if not len(sys.argv)-1:
    exit("\033[31mplease supply a file to run\033[m")

file = str(sys.argv[1])
if "-c" in sys.argv:
    import sys
    file = str(sys.argv[1])
    with open(file) as f:
        contents = f.read()
        f.close()

    contents = contents.splitlines()

    def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""


    def transpile(item):
        base = item.split(" ")
    
        if base[0] == "|":
            base[0] = "//"
            pass
        if base[0] == '':
            base = [x for x in base if x != '']
            cop = base 
    
        if len(base) < 1:
            return ""
    
        if base[0] == "writeln":
            base[0] = "printf("
            base.append(");")
            base = " ".join(base)
            cop = base
        if base[0] == "let":
            if "\"" in base[3]:
                base[0] = "char "
                lengthof = len(find_between(str(base),"\"", "\""))
                base[1] = str(base[1])+"["+str(lengthof)+"]"
                base.append(";")
                cop = " ".join(base)
            if "\"" not in base[3] and "." in base[3]:
                base[0] = "float "
                base.append(";")
                cop = " ".join(base)
            if "\"" not in base[3] and "." not in base[3]:
                base[0] = "int "
                base.append(";")
                cop = " ".join(base)
            
            if base[3] == "true" or base[3] == "false":
                base[0] = "bool "
                base.append(";")
                cop = " ".join(base)
            if base[3] == "read_int":
                base[0] = "int "
                var = base[1]
                base[1] = str(base[1])+";"
                base[2] = ""
                base[3] = "scanf(\"%d\", &"+str(var)
                base[len(base)-1] = ");"            

            #let x = readint "Hello World!" 
            #int x; x = scanf("Hello World! %d", x)
            #int x; x = scanf( "Hello World!" );
            
                cop = " ".join(base)
            if base[3] == "read_str":
                base[0] = "char "
                var = base[1]
                base[1] = str(base[1])+"[200];"
            
                base[2] = ""
                base[3] = "scanf(\"%s\", &"+str(var)
                base[len(base)-1] = ");"            

            #let x = readint "Hello World!" 
            #int x; x = scanf("Hello World! %d", x)
            #int x; x = scanf( "Hello World!" );
            
                cop = " ".join(base)
        if base[0] == "if":
            base[0] = "if("
            base[len(base)-1] = str(base[len(base)-1])+"){"
            cop = " ".join(base)
        if base[0] == "elif":
            base[0] = "else if("
            base[len(base)-1] = str(base[len(base)-1])+"){"
            cop = " ".join(base)
        if base[0] == "else":
            base[0] = "else("
            base[len(base)-1] = str(base[len(base)-1])+"){"
            cop = " ".join(base)
        if base[0] == "for":
            base[0] = "for("
            base[len(base)-1] = str(base[len(base)-1])+"){"
            cop = " ".join(base)
        if base[0] == "while":
            base[0] = "while("
            base[len(base)-1] = str(base[len(base)-1])+"){"
            cop = " ".join(base)
        if base[0] == "continue":
            base[0] = "continue"
            cop = " ".join(base)
        if "++" in base[0]:
            base.append(";")
            cop = " ".join(base)
        if base[0] == "buffer":
            base[0] = "int buffer; scanf(\"%d\", &buffer);"
            cop = " ".join(base)
        if base[0] == "read_int":
        
            base[0] = "int tempvar; scanf(\"%d\", &tempvar); tempvar = 0;"
            cop = " ".join(base)
        if base[0] == "read_str":
        
            base[0] = "int tempvar2; scanf(\"%d\", &tempvar2); tempvar2 = 0;"
            cop = " ".join(base)
    
        if base[0] == "fn":
            type2 = base[len(base)-1]
            base[0] = str(type2)+" "
            base[len(base)-1] = "{"
            base[1] = str(base[1]).replace(":", "")       
            cop = " ".join(base) 
        if "()" in base[0] and "\"" not in base[0]:
            base.append(";")
            cop = " ".join(base)
        if base[0] == "return":
            base.append(";")
            cop = " ".join(base)
        if base[0] == "end":
            base[0] = "}"
            cop = " ".join(base)
    
    
    
    
            
        else:
        # No match, set cop to empty string
            cop = "".join(base)
        return cop

    for i, item in enumerate(contents):
        contents[i] = transpile(item)
    with open("temp988.c", "a") as f:
        import sys

    
        f.write("#include <stdio.h>\n#define math_pi \"%f\", 3.14159\n#define zang_argv \"%s\", \""+str(sys.argv)+"\"\n#define zang_vers \"%s\", \"V/0.45\\n\"\n#define zang_platform \"%s\", \""+str(sys.platform)+"\\n\"\n#define zang_link \"%s\", \"https://github.com/cmspeedrunner/zang\\n\"\n")
        f.write("struct None {};\ntypedef struct None None;")
        f.write("int main(){\n")
    for item in contents:
        with open("temp988.c", "a") as f:
            f.write(str(item)+"\n")
            f.close()
   
    with open("temp988.c", "a") as f:
        f.write("return 0;")
        f.write("}")
        f.close()

    import os
    filen = file.split(".")[0]

    if "-code" in sys.argv:
        print("\033[0;32m<<-- "+str(filen)+".c -->>\033[0;36m")
        print(open("temp988.c", "r").read()+"\033[0m")


    import time
    start = time.time()
    os.system("gcc "+"temp988.c -o "+str(filen)+".exe")
    end = time.time()
    final = end-start

    print("\033[0;32m"+str(file)+" compiled in "+str(round(final,3))+"s \033[0m",end="")

    os.remove("temp988.c")
    exit()
    quit()
if "-c" not in sys.argv:  
    text = "run(\""+file+"\")"
try:
    result, error = pret.run('<stdin>', text)
except KeyboardInterrupt:
    print("\n\033[31m^C\033[0m",end="")
    exit()

if error:
    print("\033[31m" + error.as_string() + "\033[0m")  # Print error message in red text
elif result:
    if len(result.elements) == 1:
        print(repr(result.elements[0]))
    else:
        print(repr(result))

if "-s" in sys.argv:
    end_time = time.time()  
    elapsed_time = end_time - start_time 
    print('\033[32m' + f"Zang executed in {elapsed_time:.2f}" + '\033[0m', end="")


