import interpreter as pret
import os
import readline
os.system("")
print("""\033[35m
 /\u001b[34m$$$$$$$$\033[35m                              
|_____ \u001b[34m$$\033[35m                                 
     /\u001b[34m$$\033[35m/   /\u001b[34m$$$$$$\033[35m  /\u001b[34m$$$$$$$\033[35m   /\u001b[34m$$$$$$\033[35m 
    /\u001b[34m$$\033[35m/   |____  \u001b[34m$$\033[35m| \u001b[34m$$\033[35m__  \u001b[34m$$\033[35m /\u001b[34m$$\033[35m__  \u001b[34m$$\033[35m
   /\u001b[34m$$\033[35m/     /\u001b[34m$$$$$$$\033[35m| \u001b[34m$$\033[35m  \ \u001b[34m$$\033[35m| \u001b[34m$$\033[35m  \ \u001b[34m$$\033[35m
  /\u001b[34m$$\033[35m/     /\u001b[34m$$\033[35m__  \u001b[34m$$\033[35m| \u001b[34m$$\033[35m  | \u001b[34m$$\033[35m| \u001b[34m$$\033[35m  | \u001b[34m$$\033[35m
 /\u001b[34m$$$$$$$$\033[35m|  \u001b[34m$$$$$$$\033[35m| \u001b[34m$$\033[35m  | \u001b[34m$$\033[35m|  \u001b[34m$$$$$$$\033[35m
|________/ \_______/|__/  |__/ \____  \u001b[34m$$\033[35m
                               /\u001b[34m$$\033[35m  \ \u001b[34m$$\033[35m
                              |  \u001b[34m$$$$$$\033[35m/
                               \______/ \033[0m 
  \033[35mZang V/0.45
  ------------------
  DEV: \u001b[32mCm\u001b[35m
  VERSION: \u001b[32m0.45\u001b[35m
  GITHUB: \u001b[32mhttps://github.com/cmspeedrunner/zang\u001b[35m
                                         
""")

history = []

while True:
    try:
        text = input('\033[35mZang>\033[0m')
        if text != "ac.history":
            history.append(text)
        if text == "ac.history":
            print(history)
          # Add input to history list
    except KeyboardInterrupt:
        print("\n\033[31m^C\033[0m",end="")
        exit()
    if text.strip() == "":
        continue

    if text != "ac.history":
        result, error = pret.run('<stdin>', text)
    

        if error:
            print("\033[31m" + error.as_string() + "\033[0m")  # Print error message in red text
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))

