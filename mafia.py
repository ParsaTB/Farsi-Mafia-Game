import random
import os
from termcolor import colored

bold_text = "\033[1m"
reset_text = "\033[0m"

def shuffle_roles():
    all_roles.extend(shahrvand_roles)
    
    for i in range(mafia_count -1):
        all_roles.append("Mafia Sade")
        
    shahrvand_player_calc = player_count - len(shahrvand_roles) - mafia_count
    
    if shahrvand_player_calc != 0:
        for i in range(shahrvand_player_calc):
            all_roles.append("Shahrvand Sade")

    random.shuffle(all_roles)
    
    for role in all_roles:
        next_role = input(colored("Baray Didan Naqsh " , "cyan") + colored("ENTER" , "red") + colored(" Bezanid." , "cyan"))
        print(colored(f"{bold_text}{role}{bold_text}" , "magenta"))
        
        empty_terminal = input(colored("Baray Khali Shodan Safhe " , "grey") + colored("ENTER" , "red") + colored(" Bezandi.", "grey"))
        
        if not empty_terminal:
            os.system('cls' if os.name == 'nt' else 'clear')


shahrvand_roles = ["Doctor", "Karagah", "Sniper", "ZerehPosh"]

all_roles = ["GodFather"]

while True:
    try:
        player_count = int(input(colored("Tedad Bazikonan Ra Vared Konid: ", "cyan")))
        mafia_count = int(input(colored("Tedad Mafia Ha Ra Vared Konid: ", "green")))
        
    except ValueError:
        print(colored(f"{bold_text}Lotfa Tedad Bazikonan Va Mafia Ra Moshakhas Konid.{bold_text}" , "red"))
        continue

    if player_count < 6:
        message = colored(f"{bold_text} Tedad Bazikonan Nemitavand az {bold_text}", "grey") + \
        colored(f"{bold_text} 4 {bold_text}", "red") + \
        colored(f"{bold_text} Kamtar Bashad!{bold_text}", "grey")
        
        print(message)
        continue
    
    elif mafia_count > player_count or mafia_count == player_count:
        print(colored(f"{bold_text}Tedad Mafia Nemitavanad Bishtar Az Tedad Bazikonan Bashad!{bold_text}", "red"))
        
    else:
        break


shuffle_roles()