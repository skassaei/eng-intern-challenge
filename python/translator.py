import sys
def EngToBri(str):
    
    eng_to_bri_alph = {"a":"O.....","b":"O.O...","c":"OO....","d":"OO.O..","e":"O..O..","f":"OOO...","g":"OOOO..","h":"O.OO..","i":".OO...","j":".OOO..","k":"O...O.","l":"O.O.O.","m":"OO..O.","n":"OO.OO.","o":"O..OO.","p":"OOO.O.","q":"OOOOO.","r":"O.OOO.","s":".OO.O.","t":".OOOO.","u":"O...OO","v":"O.O.OO","w":".OOO.O","x":"OO..OO","y":"OO.OOO","z":"O..OOO"}
    eng_to_bri_num = {"1":"O.....","2":"O.O...","3":"OO....","4":"OO.O..","5":"O..O..","6":"OOO...","7":"OOOO..","8":"O.OO..","9":".OO...","0":".OOO.."}
    eng_to_bri_dec = {".":"..OO.O",",":"..O...","?":"..O.OO","!":"..OOO.",":":"..OO..",";":"..O.O.","-":"....OO","/":".O..O.","<":".OO..O",">":"O..OO.","(":"O.O..O",")":".O.OO."," ":"......"}
    eng_to_bri_rules = {"captial":".....O","number":".O.OOO","decimal":".O...O"}
    num = False
    decimal = False
    for c in str:
        if c !=" ":
            if ord(c) in range(ord('a'),ord('z')+1):
                # print("its alph")
                num = False
                decimal = False
                print(eng_to_bri_alph[c],end='')
            elif ord(c) in range(ord('A'),ord('Z')+1):
                # print("its Cap")
                num = False
                decimal = False
                print(eng_to_bri_rules["captial"],end='')
                print(eng_to_bri_alph[c.lower()],end='')
            elif ord(c) in range(ord('0'),ord('9')+1):
                # its a Number:
                if num!=True:
                    num = True
                    print(eng_to_bri_rules["number"],end='')
                print(eng_to_bri_num[c],end='')
            else:
                num = False
                if decimal!=True:
                    decimal = True
                    print(eng_to_bri_rules["decimal"],end='')
                print(eng_to_bri_dec[c],end='')
        else:
            num = False
            decimal = False
            print("......",end='')

def briToEng(str):
    bri_to_eng_alph = {"O.....":"a","O.O...":"b","OO....":"c","OO.O..":"d","O..O..":"e","OOO...":"f","OOOO..":"g","O.OO..":"h",".OO...":"i",".OOO..":"j","O...O.":"k","O.O.O.":"l","OO..O.":"m","OO.OO.":"n","O..OO.":"o","OOO.O.":"p","OOOOO.":"q","O.OOO.":"r",".OO.O.":"s",".OOOO.":"t","O...OO":"u","O.O.OO":"v",".OOO.O":"w","OO..OO":"x","OO.OOO":"y","O..OOO":"z"}
    bri_to_eng_num = {"O.....":"1","O.O...":"2","OO....":"3","OO.O..":"4","O..O..":"5","OOO...":"6","OOOO..":"7","O.OO..":"8",".OO...":"9",".OOO..":"0"}
    bri_to_eng_dec = {"..OO.O":".","..O...":",","..O.OO":"?","..OOO.":"!","..OO..":":","..O.O.":";","....OO":"-",".O..O.":"/",".OO..O":"<","O..OO.":">","O.O..O":"(",".O.OO.":")","......":" "}
    bri_to_eng_rules = {".....O":"captial",".O.OOO":"number",".O...O":"decimal"}
    start = 0
    end = 6
    rounds = len(str)//6
    num = False
    decimal = False
    captial = False
    for i in range(rounds):
        if end>len(str):
            print("out of bound!")
        c = str[start:end]
        if c !="......":
            if c not in bri_to_eng_rules and num ==False and decimal ==False:
                # it is a lower case letter:
                if captial:
                    captial = False
                    print(bri_to_eng_alph[c].upper(),end='')
                else: print(bri_to_eng_alph[c],end='')

            elif num or (c in bri_to_eng_rules and bri_to_eng_rules[c] == "number"):
                decimal = False
                captial = False
                if num==False:
                    num = True
                else:print(bri_to_eng_num[c],end='')

            elif decimal or (c in bri_to_eng_rules and bri_to_eng_rules[c] == "decimal"):
                num = False
                captial = False
                if decimal==False:
                    decimal = True
                else:print(bri_to_eng_dec[c],end='')            
            elif (c in bri_to_eng_rules and bri_to_eng_rules[c] == "captial"):
                if captial==False:
                    captial = True
        else:
            num = False
            decimal = False
            captial = False
            print(" ",end='') 

        start= end
        end +=6


def translator():
    if len(sys.argv) > 1:
        inputString = " ".join(sys.argv[1:])  # Combine all arguments into one string
        check_language = set(inputString)
        
        # Decide whether to translate to Braille or to English
        if len(check_language) > 2 or ("O" not in check_language or "." not in check_language):
            # Translate English to Braille
            EngToBri(inputString)
        else:
            # Translate Braille to English
            briToEng(inputString)
    else:
        print("No input provided")

if __name__ == "__main__":
    translator()
