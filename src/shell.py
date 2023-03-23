import interpreter as pret
print("""\033[35m
 /$$$$$$$$                              
|_____ $$                               
     /$$/   /$$$$$$  /$$$$$$$   /$$$$$$ 
    /$$/   |____  $$| $$__  $$ /$$__  $$
   /$$/     /$$$$$$$| $$  \ $$| $$  \ $$
  /$$/     /$$__  $$| $$  | $$| $$  | $$
 /$$$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$
|________/ \_______/|__/  |__/ \____  $$
                               /$$  \ $$
                              |  $$$$$$/
                               \______/ \033[0m 
  \033[36mZang V/0.1
  ------------------
  DEV: Cm
  VERSION: 0.1
  GITHUB: https://github.com/cmspeedrunner/zang
                                         
""")

while True:
    text = input('\033[35mZang>\033[0m')
    if text.strip() == "":
        continue

    result, error = pret.run('<stdin>', text)

    if error:
        print("\033[31m" + error.as_string() + "\033[0m")  # Print error message in red text
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
