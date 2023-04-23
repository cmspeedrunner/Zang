import interpreter as pret
import os
os.system("")
print("""\033[35m
 /\033[34m$$$$$$$$\033[35m                              
|_____ \033[34m$$\033[35m                                 
     /\033[34m$$\033[35m/   /\033[34m$$$$$$\033[35m  /\033[34m$$$$$$$\033[35m   /\033[34m$$$$$$\033[35m 
    /\033[34m$$\033[35m/   |____  \033[34m$$\033[35m| \033[34m$$\033[35m__  \033[34m$$\033[35m /\033[34m$$\033[35m__  \033[34m$$\033[35m
   /\033[34m$$\033[35m/     /\033[34m$$$$$$$\033[35m| \033[34m$$\033[35m  \ \033[34m$$\033[35m| \033[34m$$\033[35m  \ \033[34m$$\033[35m
  /\033[34m$$\033[35m/     /\033[34m$$\033[35m__  \033[34m$$\033[35m| \033[34m$$\033[35m  | \033[34m$$\033[35m| \033[34m$$\033[35m  | \033[34m$$\033[35m
 /\033[34m$$$$$$$$\033[35m|  \033[34m$$$$$$$\033[35m| \033[34m$$\033[35m  | \033[34m$$\033[35m|  \033[34m$$$$$$$\033[35m
|________/ \_______/|__/  |__/ \____  \033[34m$$\033[35m
                               /\033[34m$$\033[35m  \ \033[34m$$\033[35m
                              |  \033[34m$$$$$$\033[35m/
                               \______/ \033[0m 
  \033[35mZang V/0.45
  ------------------
  DEV: \033[32mCm\033[35m
  VERSION: \033[32m0.45\033[35m
  GITHUB: \033[32mhttps://github.com/cmspeedrunner/zang\033[35m
                                         
""")

history = []

# TODO: function support,
#       tab auto completion
#       issue with scrolling down through history

while True:
    try:
        text = input('\033[35mZang> \033[m')
        
        if text == 'ac.history':
            for idx, com in enumerate(history):
                print(f' \033[34m{idx + 1:>3}.)\033[m {com}')
            continue

        history.append(text)
    except KeyboardInterrupt:
        exit("\n\033[31m^C\033[m")
    
    if text.strip() == "":
        continue
    
    result, error = pret.run('<stdin>', text)
    
    if error:
        history[-1] = f'\033[31m{history[-1]}\033[m'
        print(f'\033[31m{error.as_string()}\033[m')
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
    
    history[-1] = f'\033[32m{history[-1]}\033[m'
