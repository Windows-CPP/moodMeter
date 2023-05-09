# note: this file gets named moodMonitor.exe when compiled

"""
This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://www.wtfpl.net/ for more details. */
"""


GRN = "\u001b[42m"
END = "\u001b[0m"
logLocation = "C:/Program Files/moodMeter/moods.log"
moodLoggerVer = "0.3"
moodMonitorVer = "0.4"

from os import system
def clear():
    system("cls")



option = str(input("Enter Command: "))
option = option.lower()

while(option != "exit"):
    # cmd:clearlogs
    if(option == "clearlogs"):
        with(open(logLocation, "w")) as f:
            f.write("")
            print("Cleared Logs")

    # cmd:readLogs        
    elif(option == "readlogs"):
        with(open(logLocation, "r")) as f:
            print(GRN + "Read from File: " + END)
            print(f.read())

    # cmd:help
    elif(option == "help"):
        print("moodLogger v{0} | moodMonitor v{1}\n".format(moodLoggerVer, moodMonitorVer))
        print("Commands: clearLogs, readLogs, exit\n\nclearLogs: Clears the logs of all data\nreadLogs: Read the data from the logs\nexit: Exit the program\n\n")

        input("Press Enter to Continue...")
        clear()

    # cmd: logmood
    elif(option == "logmood"):
         system("run 'C:/Program Files/moodMeter/moodLogger.exe'")

    # cmd:exit
    else:
        print("Invalid Command")
    
    

    option = str(input("Enter Command: "))
    option = option.lower()

exit()