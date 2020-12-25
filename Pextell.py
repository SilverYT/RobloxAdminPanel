# imports
import robloxpy
import time
import os
import colorama
from colorama import *
init()

print(Fore.RED + '')
print('''----------------------------------------------------''')
print(r"""
    
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄           
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌          
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▐░▌   ▐░▌  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌          
▐░▌       ▐░▌▐░▌            ▐░▌ ▐░▌       ▐░▌     ▐░▌          ▐░▌          ▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄    ▐░▐░▌        ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌          
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ▐░▌         ▐░▌     ▐░░░░░░░░░░░▌▐░▌          ▐░▌          
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀    ▐░▌░▌        ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌          
▐░▌          ▐░▌            ▐░▌ ▐░▌       ▐░▌     ▐░▌          ▐░▌          ▐░▌          
▐░▌          ▐░█▄▄▄▄▄▄▄▄▄  ▐░▌   ▐░▌      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌          ▐░░░░░░░░░░░▌▐░▌     ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                         
""")
print(r"""

                                                                                                   
█▄▄▄▄ ████▄ ███   █     ████▄     ▄      ██   ██▄   █▀▄▀█ ▄█    ▄       █ ▄▄  ██      ▄   ▄███▄   █     
█  ▄▀ █   █ █  █  █     █   █ ▀▄   █     █ █  █  █  █ █ █ ██     █      █   █ █ █      █  █▀   ▀  █     
█▀▀▌  █   █ █ ▀ ▄ █     █   █   █ ▀      █▄▄█ █   █ █ ▄ █ ██ ██   █     █▀▀▀  █▄▄█ ██   █ ██▄▄    █     
█  █  ▀████ █  ▄▀ ███▄  ▀████  ▄ █       █  █ █  █  █   █ ▐█ █ █  █     █     █  █ █ █  █ █▄   ▄▀ ███▄  
  █         ███       ▀       █   ▀▄        █ ███▀     █   ▐ █  █ █      █       █ █  █ █ ▀███▀       ▀ 
 ▀                             ▀           █          ▀      █   ██       ▀     █  █   ██               
                                          ▀                                    ▀                        
""")
print("By, SilveR#4315")
print('''----------------------------------------------------''')

print(Style.RESET_ALL)
print(Fore.GREEN + '')

print(Fore.RED + '')
print('''Help? type "cmds" for a list of commands!''')
print(Fore.GREEN + '')

PanelLaunchCode = 155
while PanelLaunchCode > 42:
    process = input('> ')
    
    def cmds():
        print(Fore.GREEN + '')
        print ('''
        cmds -- Display a list of commands
        UsernameCheck -- Check If a ROBLOX Username Is Chartered
        AccountAge -- Check how old an account is in days
        BanCheck -- Check if a user is deleted or not
        AccountCreation -- Check the year, month, and day an account was made
        FollowerCount -- Check the amount of followers for an account
        FollowingCount -- Check the amount of users an account is following
        GroupCheck -- See the Groups a user is in
        cls -- Clear the console
        anticls -- Launch the main menu
        Hee Ho -- filler
        ''')
        print(Fore.GREEN + '')
        
    if process.lower().strip() == 'cmds':
        cmds()

    def usercheck():
        print(Fore.RED + '')
        print("Please enter a username")
        print(Fore.GREEN + '')
        NameToScan = input('> ')
        print(Fore.RED + '')
        print(robloxpy.DoesNameExist(NameToScan))
        print(Fore.GREEN + '')
        
    if process.lower().strip() == 'usernamecheck':
        usercheck()
                
    def accountage():
        print(Fore.RED + '')
        print("Please enter a username")
        print(Fore.GREEN + '')
        AccountAgeToCheck = input('> ')
        print(Fore.RED + '')
        id = robloxpy.NameToID(AccountAgeToCheck)
        print(robloxpy.AccountAgeDays(id) + ' Day(s) old')
        print(Fore.GREEN + '')
        
    if process.lower().strip() == 'accountage':
        accountage()
    
    def bancheck():
        print(Fore.RED + '')
        print("Please enter a username")
        print(Fore.GREEN + '')
        CheckIfUserIsBanned = input('> ')
        id = robloxpy.NameToID(CheckIfUserIsBanned)
        print(robloxpy.IsBanned(id))
        print(Fore.GREEN + '')
        
    if process.lower().strip() == "bancheck":
        bancheck()
    
    def accountmade():
        print(Fore.RED + '')
        print("Please enter a username")
        print(Fore.GREEN + '')
        CheckWhenAccountWasMade = input('> ')
        print(Fore.RED + '')
        id = robloxpy.NameToID(CheckWhenAccountWasMade)
        time.sleep(0.3)
        print("The Year")
        time.sleep(0.3)
        print(robloxpy.UserCreationDate(id, 'Year'))
        time.sleep(0.3)
        print("The Month")
        time.sleep(0.5)
        print(robloxpy.UserCreationDate(id, 'Month'))
        time.sleep(0.3)
        print("The Day")
        time.sleep(1)
        print(robloxpy.UserCreationDate(id, 'Day'))
        time.sleep(0.3)
        print(Fore.GREEN + '')
        
    if process.lower().strip() == "accountcreation":
        accountmade()
    
    def followercount():
        print(Fore.RED + '')
        print("Please enter a username")
        print(Fore.GREEN + '')
        GetFollowerCount = input('> ')
        id = robloxpy.NameToID(GetFollowerCount)
        print(Fore.RED + '')
        print("This user has")
        print(robloxpy.GetFollowersCount(id))
        print("follower(s)")
        print(Fore.GREEN + '')
        
    if process.lower().strip() == "followercount":
        followercount()

    def clear():
        os.system('cls')
        print("Type anticls for a relaunch")
    
    if process.lower().strip() == 'cls':
        clear()
    
    def anticls():
        print(Fore.RED + '')
        print('''----------------------------------------------------''')
        print(r"""
            
        ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄           
        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌          
        ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▐░▌   ▐░▌  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌          
        ▐░▌       ▐░▌▐░▌            ▐░▌ ▐░▌       ▐░▌     ▐░▌          ▐░▌          ▐░▌          
        ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄    ▐░▐░▌        ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌          
        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ▐░▌         ▐░▌     ▐░░░░░░░░░░░▌▐░▌          ▐░▌          
        ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀    ▐░▌░▌        ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌          
        ▐░▌          ▐░▌            ▐░▌ ▐░▌       ▐░▌     ▐░▌          ▐░▌          ▐░▌          
        ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄  ▐░▌   ▐░▌      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
        ▐░▌          ▐░░░░░░░░░░░▌▐░▌     ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
        ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                                
        """)

        print(r"""

                                                                                                          
        █▄▄▄▄ ████▄ ███   █     ████▄     ▄      ██   ██▄   █▀▄▀█ ▄█    ▄       █ ▄▄  ██      ▄   ▄███▄   █     
        █  ▄▀ █   █ █  █  █     █   █ ▀▄   █     █ █  █  █  █ █ █ ██     █      █   █ █ █      █  █▀   ▀  █     
        █▀▀▌  █   █ █ ▀ ▄ █     █   █   █ ▀      █▄▄█ █   █ █ ▄ █ ██ ██   █     █▀▀▀  █▄▄█ ██   █ ██▄▄    █     
        █  █  ▀████ █  ▄▀ ███▄  ▀████  ▄ █       █  █ █  █  █   █ ▐█ █ █  █     █     █  █ █ █  █ █▄   ▄▀ ███▄  
        █         ███       ▀       █   ▀▄        █ ███▀     █   ▐ █  █ █      █       █ █  █ █ ▀███▀       ▀ 
        ▀                             ▀           █          ▀      █   ██       ▀     █  █   ██               
                                                ▀                                    ▀                        
        """)
        print("By, SilveR#4315")
        print('''----------------------------------------------------''')

        print(Style.RESET_ALL)
        print(Fore.GREEN + '')

        print(Fore.RED + '')
        print('''Help? type "cmds" for a list of commands!''')
        print(Fore.GREEN + '')
    
    if process.lower().strip() == 'anticls':
        anticls()

    def followingcount():
        print(Fore.RED + '')
        print("Please enter a username")
        print(Fore.GREEN + '')
        GetFollowingCount = input('> ')
        id = robloxpy.NameToID(GetFollowingCount)
        print(Fore.RED + '')
        print("This user is following")
        print(robloxpy.GetFollowingCount(id))
        print("Account(s)")
        print(Fore.GREEN + '')
        
    if process.lower().strip() == "followingcount":
        followingcount()
    
    def groupcheck():
        print(Fore.RED + '')
        print("Please enter a username")
        print(Fore.GREEN + '')
        GroupCheck = input('> ')
        id = robloxpy.NameToID(GroupCheck)
        print(Fore.RED + '')
        print("Group(s) this user is currently in: ")
        print(robloxpy.GetUserGroups(id))
        print(Fore.GREEN + '')
    
    if process.lower().strip() == "groupcheck":
        groupcheck()


















    







