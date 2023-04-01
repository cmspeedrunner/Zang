import interpreter as pret
import time
import sys
import os
os.system("")
start_time = time.time()  # Start the timer


file = str(sys.argv[1])
text = "run(\""+file+"\")"
result, error = pret.run('<stdin>', text)

if error:
    print("\033[31m" + error.as_string() + "\033[0m")  # Print error message in red text
elif result:
    if len(result.elements) == 1:
        print(repr(result.elements[0]))
    else:
        print(repr(result))

end_time = time.time()  
elapsed_time = end_time - start_time 
print('\033[32m' + f"Zang executed in {elapsed_time:.2f}" + '\033[0m', end="")
