#!/usr/bin/python 3.9
#info.py
#This code for education purpose only.
#Use it at your own risk !!!
# Python 3 rewrite by Omicron166


import os
import smtplib
import getpass
import sys
import time

print ('')
print ('')

print ('*****//&&&%%#%%%#####(////(,(((*(#//#((#((#/#(/#//(*###%%%(%%%&&@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@&&&@@@@@@@@@&@@@@@@@&%%&&&&%%%@@@@@@@&&&@@@')
print ('*****/#@@@&&%%&%##(/(((**/(/*#(/((((#((#/##(#((#((/*((#/%#%(%%%&@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&@&&&&%&@@@@@@@@@@@@@@&%%%%%&%%%%%&&&@@@@&@@@@')
print ('**//*/%@@@@&&&&###(/*/(/*((//((/#//(#//#(##(#/(#*(/(#*###&%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@&&&&@@@@@@@@@@@@@@&@&%%%@@@%%%%&&&@@@@@@@@@')
print ('**////@@@@@@@@&##((#%(///(*(/(**#//(#((#(%((#(/#(((((*(%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&@@@@@&&&&&&&@@@@@@@@')
print ('***//(@@@@@@@@&%##(/#(*//(/,/((/#(((((((*%((%/##(#/((/(*##%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@&&&&&&@@@@@@@&')
print ('****/#@&@@@@@@&####/((/*/(//((((#*(((*#((%((#((#/#((###((((#%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@&&@@@@@@@@@@@@&&&@&@@@@@@@@&%&&&@@@@@@@@&%')
print ('*****%&&@@@@@&%###(##(/(#&&&@@@@@@@@@@@@@@&##(##(#(**//(##%%(///#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@&&&&@@@@@@@@@&&&&&@@@@@@@@&&&&%&@@@@@@@@%%%%%&@@@@@@@&%%')
print ('##((((###%&&@&#%&&&&&&&&%%%%%%%%%%%%%%%%&&&@@@@@@@@@&&&&&&&&%%%&&(/#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@&&@@@@@@@@@@@&&&@@@@@@@@@@@&&&@@@@@@@@@@&%%&@@@@@@@@@@%')
print ('****//*//(#%%%##%&%#(((((((((((((((((((##%%&&&@@@@@@@@@@@@@&&&@@@@@%//&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print (',*,*/((((((///////(((((((((((/(((((((((#%%&&&@@@@@@@@@&&&&&&%##%&&&&&//#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@&@@@@@@')
print ('///*********(###%%((/(/((((/(/(((((((#%&@@@@@@@@@&&&&&&&&&%%%##((#####**/%&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@&%&&@@@@@@@@@@@&&@@@@@&&@@@&%%%@@@@')
print ('**********/((/////((//((((//((((((#&&&@@@@@@@@@@&&&&&%%%%######((((((//**/####%%%%%%%&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&@@@@@@@@@@@@&@@@@@@@@@&%%%%&@@@@@@@@@&&&&&@&&&&&@@%%%%%&@&')
print ('*****,/(/*/*******/////////(/(((#&&&&&&&@@&&&&&%%%%%%%%%#((((((((((((((///((#((#(##########%%%&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@&%&@&@@@@@@@@@&&&&&&&&&@@@@&%%&&&&')
print (',,,*/************////////(/(((#%%&&&&&&&&&&%%%%%########(((((((/((((((##(//((((((((((((((###((#####%%%%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@&@&&&&&@@@@@@@&&&&&&&@@@@@@@&&&&&')
print (',**************/////////(((((%%&&%%%%&&&&&%%###(((((((((((#((((##(/////////(((##((((((((((((((#((((#######%%&&@&(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@&&&&@@@@@@@@&&&&@@@@@@@@&&&&&&&&@@@@@@@&&&&')
print ('******(%%%/**/((((//(///((/(#%##((((#%&&%#((((((((/(#(((((##(/////*///((#%%%##(((#((((((((((##########(((((####%%(((#@@@@@@@&&&@@@@&&&@@@@@@@@@@@@@@@@@@&&&&@@@&&%&@@@@@@@@&@@@@@@@&%%%%&&&%%%%@@@@@@@&@')
print (',*****/////(//((((//((/((((#(((/#&&@&&&%##(((((((///((//////((/#####(##%#%##/////(///*//((/(((####(#((((((((((##(//*//&@@@@&&&&&@@&&&&&&@@@@@@@@@@@@@@@&%&%%&@&%%%%&@@@@@@@@@@@@@@@%%%%%&@&%%%%%@&&@@@@@')
print ('*************/(((/(######%%%%&&&&&&&%###((//(///****//*,**//(#%%%%#(##%#%#%#(((///*/**(((#((******/////////(((((//*/**/#@@@@@&&@@@@@&%@@@@@@@@@@@@@@@@@&&%%@@@@&%%&@&@@@@@@@@@@@@&&&&%%&@@@&%%&&&&@@@@@@')
print (',,,**********//**//***//***/////(###(((////***,,,***,,,,/**//(((((/#%%%#%##((///((####(/(#%#/(////*//////(//(((/******/*(@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&@@@@@@@&&&&&&@@@@@@@@@&&&&&&@@@@@@@&&&&&&&@@@@')
print (',,****,**************,,,*,****///////***,**,*..*,*.,*,**,,***/**//(#((((((/////(((###%#####((///////****/////****/*******(%&&&@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@&@&&&&@@@@@@@@@@&&&&&%@@@@@@&&&&&&@@@@@')
print (',,,,,,****,,****,,,,..,,,,,,*********,,,,,,...,,,,,,,,***,********/*****/***////(((((######(###(/*,****,,*****,,,****//(/(///((@@@@@@@@@@@@@@@@@@&&@@@@&&&&&@@@&%%%&&&@@@@@@@@@@@&&&%%%%&@@&%%%&&&@@@@@@')
print (',,*****,,,,,/#%%#/*****,,,,,**,,,,,,,.,,,.....,,,,.,*.//**,*,,,,******,,,*****////((((((((((((##((/*,,,,*,,**********/*///***/#&&%&&@@&&&&%&&%&@@@&&%%&&&&%&&&&&%%%%%@@@@@@@@@@@@&&&%%%%%%@%%%%%%&@@@@@@')
print ('*/**,***,*,,,*((((((***,*,,,,,,....,,.,,.......,..,*,,*,,,,,,,,,,,,,,,*,*******/////((((((((((####((/,,,,,******,*******//*///(&@&&&@@@&&@@@@&&@&&&@@@@@@&%%&&&&&%%&@@@@@@@&&@@@@@@@@%%#%&@&%%%%@@@@@@@&')
print ('/(/**,*,,,**,,,,**,***,,,,,...,,......,..,.,,.,*,..,.,,,,,,,,.,,,,,,,,,,,*,***///////((((((((((((####((,,,,,,*,*,,******//*/(((%@&&&%&&&&&&@@@@@@@@@&&&&&&%&&&&&&&@@@@@@@@&&&&&&@@@@@@&&&&&&&&&@@@@@@@&&')
print ('*%%**,,,,,,,,,,,*,,,,,.,...,,,,.........,..,,,..,.,.,,,,,,,,,,,,,,,,,,,,,*******///////(((((((((((((####(*,,,,,,*,**********//(%@@&@@@@@@@@@@@@@@@@@@&#%@@@&&&&&&&@@@@@@@@&&&&&&&@@@@@@&&&&&&&&@@@@@@&&&')
print ('/%%/(*,,,,,.,,,,,,,,,...,,.......,,.....,,,,,,...,.,,,,,,,..,,,,,.,,,,,,**,*******/////////(((((((((((#####(,,,,,,,,*,***,**,**/%&&@@@@@@@@@@@@@&///(%@@@@&&&&&&&&&&@@@@@@@&&&%%%%@@@&&&&&&&&&&&&@@@@@@&')
print ('*/(/(/*,....,.........................,,,,,.,,,.,.,,.,,,.,,,,,,,,,,,,,,,,******//*////////((((((((((((((((((//***,,,,,,,********((%%#((((%%%(#((#%#%%%%&@&&&&&&&&&&&&&@@@@&&%&%%###%&&%%&&&&&&&&&&&@@@@&')
print ('(##/*,.........................,.....,,,..,.,.,,,.,,,,,,,.,,,,,,,,,,,,,,,,,****/////////(/////////((((((/*,,*,*///,.,,,*,,****,**#&&&&&&@@@@@@&@@&%%%%@@@&&&&@@@&&&&&@@@@@@&@@&%%%%@@&&&&&@@@&&&&&@@@@@&')
print ('(/*,*.,..,.,................,...,...,,....,....,,.,,,,,,,,.,,.,,,,,,,,,,,******////////////////////////*,,,,*////((,..,,,,*,,*****#&&&@@@@@@@@@@@@@&%@@@@&&&@@@@@@&@@@@@@@@@@@@@%&@@@&&&&@@@@@@&@@@@@@@@')
print ('/**,,,*,,.................,,....,..,..,.,....,,.,,,,,,,,,,,,.,,,.,,,,,,,*******/////(//////////////////,,****/*/////...,,,,,,***,**#@&@@@@@@&@@@@@@@@@@@@&&&@@@@@@&@@@@@@&@@@@@@@@@@&&&&&@@@@@@&@@@@@@%@')
print (',*,.,,.,,,. ................,...,..,...........,,..,,.,,,,,,,,,.,,.,,,,**,***////////////*******///////*********/////...,,,,,******/%@@&&@@@&%@@@@@@@@@@@&&%%@@@@@@@@@@@&%%&@@@@@@@@@@&%%%@@@@@@@@@&&%%#')
print (',,,*,,................., ..,....,.,........,,,..,,,,,.,,,,,,,,.,,.,.,,,******/////,,.,,,,*,,********////**,****,,,*,,,,,,*,..,,******%%%&&@&%%%%@@@@@@@@@&%%%%&@@@@&&&@&%###%@@@@@@@&&%####&@@@&&&&&%###')
print ('.,*,,,.,,,..............,,..,,,..,...,........,,.,..,.,.,,,,,,,..,,.,,,,******,,,...,,*,*************////,*,,,.,,///**/*,......,,,***(##%%%%%%%%@@@@@@@@&%%%%#&@@@@&&&&%#%###@@@@@@&&&%####&@@&&&%%%%###')
print (',*,,,......,.......,...,......,.,.,.,.,,,...,,,.,,,,,.....,,,,,.,.,,,,,**,,,,.,****/******************//(((*.,,,./**//////(*,...,,,,*/##%#####%@@@@@@@@&%%%%#&@@@@@@@&%%%%#%@@@@@@&&%%%%##@@@@@@@@&%%%##')
print (',*,.,...,..,..........,.,,,..,...,..,,.,...,..,,..,.,....,.,..,...,,,,,,...,***///***********,,,*,,*****/(#%%&&%(*////(((#####(,..,,*(#((((##%@@@@@@&&%%%%%%@@@@@@@&&&%%%%%@@@@@@&&&%%%%%&@@@@@@&&%%%%%%')
print (',,,,,,...........,,.,......,.,.......,,,,,,,...............,,,..,.,,,..,********************,,***,*****////(#%%&&&&%###########%%(,.,*(//(((#&&@@@@@@&%%%%%%&@@@@@@%%%%%%%&@@@@@@@@&%%%%%#@@@@@@%%%%%%&&')
print ('*,,,,...,,.,...,,.....,..,.,................,....,,,...,,,,,,,,,,,,.,,,*********,****/*,,,,,.,,,**********///(#%%&&&&&&%%##########(,,**/((##(#&@&@@&&&%%%&###@@@&####%%&@&&&@@@&&&%&%%%####@@&####%%&&&')
print (',,.....,......,,.....,.,,..,.........,..,.,,.,,.,,...,,,,,,.,,,,,,.,,,*******,.,**,,..,////*,,************///((##%#####((((((((((((((..,**#(#(((##&&%&&########%%######%&&&&&&%&@&&&%%%#(####%######%&&&')
print (',,,....,,.....,.,,.,,,....,........,.....,,.,,..,...,,,,,,,,.,.,.,,,,*******,,,........*/**********/*********////(((/(///////////((//*.,,*((/(%#((#%#%%&@@###(#&%%####@@@@&&&&%%&&&&&@@&####%%%%###&@@@&')
print (',.,......,.,,..,,.,.,,,.,.....,.,...,,..,,,,....,...,,,,,,..,,,,.,,,,****,*,,......,*,*********/////*/**********//////////////////////...,*/(//(((((%&&@&@@&#%%%%%%%%@@@@@@&%%%%%%&@@@@@@%%%%%%%%#@@@@@@')
print ('.....,..,...,.,....,,,...............,,..,,....,*.,,,,,,....,.,,,,,*,,,,,,.,,,,,,************/////////******//////**,,****/((////////*....,,*//**/((/%&&@&&&%%%%%#%%&@@@@@@%%%%%%%#@@@@@@@%%%%%%#%@@@@@@')
print (',,,......,,.,.,...,,..............,,...,..,,.,,,,.,,,,,,,..,,,,..,,,*,,,,,**********/////////////////*********//,,,*******/(((#(/*/***.....,.,*/////((#&&&@%##%%%%%%%%@@@@&&@&%%%##(%@@@&%%%%%%#%##&@@@@')
print (',.,...,.....,..,..........,,....,,,...........,,,,,.,,.,,.,,.,,.,*,,,*,********//////((((((((((((//*/*********,,***********////*******......,..**(/*//((&&#####%%%%%%%#&@&&&%%%%%#####@&%#%%%%%%%###%&&&')
print ('..,..,,....,......,........,,....,.,,,.,,,,..,.,,,,,,.,,,....,...,,,,,,,,******//////((((((((((((/////************************,,,,,***,.......,,.*//**///(#####(%%%#%#%%&&&&&%%@%##(((%%%#%%%%&%#%#%#%&&')
print ('....,,,,....,..,.,..,................,.,,,..,.,,,,,..,,,,.,,,.,.,,,,,,*********/////((((((((((((((///////*/*/****************,...,****, ..........,*//*/(%%####&&%@%%%%&&&&&@&@@@@##(&&&@%%%&@@@&%%#&&&&')
print ('.,.,,,,..,..,........,....,.......,,,....,..,,,,,...,,.,..,,,.,...,,,,,,,*******///////(((((((((((//**/////////*/****,*/////((,,**/*/**..,......,..,*(((//((#%@@@&%@&&&&&&&&&@@@@@@%&&&&%%&&@@@@@@%&&&&&')
print ('..,.,,.,,.,.,........,,,,.....,.,,.,..,.,,,,,.,..,,,,,...,,,,..,,,,,,,,,*******//////////(((((((//////////////***,***//((((((**////*//*....,..,..*/..**(#/*(##@@@@@%%%&&&&&&#@@@@@@&&&%&%###@@@@@@&&&&&&')
print ('..,..,,..,..,,,,......,.....,.........,,.,.,..,,..,,,..,..,,....,....,,,,,*****/////////////////////**********,**//(//*/(/,*/////***//*,....,..,.../,../(#(*/((&@@@&%&&&&&%###&@@@&&&&&&@%##(%@@@@&&&&&&')
print ('...................,....,....,......,,.,..,,,,,,,.,...........,...,,.,,,*,******////////////////////******,,,*///*,,****/////*******///*,...,,......,*,.,/(/**/(%@&&%###&%#(#(##@&&&&&&&%#((((#&&&&&%%&%')
print ('..,..,..............,...,.....,,..,,,..,..,,,.,................,.....,.,,,,,*******/////////////////**,,.,**,,,*****///*/***,****///////*.*...,...,,,./,,.*///*/(@&&&%(#%###(((#@&&&&&&%##(((##@&%&&%#%#')
print ('...,.,....,,..,...,,....,......,....,.........,.,,..............,,...,.,,****************/*////*///****,,******************/**/////////(/,...,,,...,,..**.,,,//((%@@&&&#%###((%@@@@&&%%#####(%@@@@&&@%%#')
print ('.,,.,..,,,.,.......,................,......,..,,..... ............,.,.,,,,,*******************/**///////***/***************///////////////..,..**...*....*,.,,/&%/%&@%#(%%#%#%@@@@@@&%####%#%@@@@@@&%%##')
print (' .,..,..,,,.......,.........,.,,,,...,,,..,,,,.....................,.,,,,,,,,***************/*/****////******/*/////////*/*//////////////*....,.,*,.,/.,,,,*.,,/&&(&%#####%#%&@@@@@@%######%&@@@@@@%(###')
print ('...,..,.,.,,. ...,,....,., ,.........,,.,.,............................,,,,,,,****************/****//**********////*///////////////*****,.   ..,.,,..,,.,*.,/,.,*%#/(/((###%&&&&@@@#(#(####&&&&@@@##((##')
print ('...,,,,,,,,....,...,...,.,,...,....,..,,,,...,............................,,,***************************************/*//////////**,,,,........,....,..,*,,*,,*,,.,(/*((((#%&&&&&&&#(((((#%#%&&&&%#((((((')
print ('....,...,,,...,...........,....,..,........................ .............  .,,,,,*************************,*,***,**********,.........,,,*,*****//**,...,**.**,*,.,,/*/(((#%&&&&&&@&(((((%&%%%%%%@@%#(((%')
print ('......,.,,....,,.,....,..,.............  .,........................................,,,,**,*,,*,,,,,,,.,,,,,,....................,,,,,,*//**//**///********(,*/,..,.,/*/(#%&&&&&&@@@@%((%&&&&&&&@@@@@#(#%')
print (',..,,..,,......,,,,..,,.,,,.....,.,........,.,..,.................................. ...........,....,..........................,,,,***/((/*///*/////*/*********,,...,//###%%&&%@@@@@@&%&&&&&&%@@@@@@@##%')
print ('.,.,,,,.,.....,,,,,,...,..,..,....,.......,,.............................. ........ ................ ...........................,,,,,*,*/***////////********/*****,.,*/####%%%#&@@@@@&&&&&&%%%%@@@@@&%##')
print (',.........,......,,..,,.,,....,...,.. .........,,.. .. ................... . ......... ......................................,,,,,,,,,,**,,,********//***/*********,,,*##%%%%(((#@@@&@&&&%%%%###&&&%####')
print (',.........,.........,,....,........,..,..................... .... .  ....... ..................................................,.,,,,,,,****,,***,*******************/*(#(##((((((%%#%%%&%##############')
print ('.,..,.,,... .....,.....,.,........,.,..,.. .,...... .............. .... .....................................................,..,,,,,,,,,****,,*,*,,,,,,****,*,,,,*,*****(%&((((((####%%%%@%############')
print (',,........... ...,.,.,..,....................,....................  .......................................................,,..,,.,,,,,,**,**,,*,,,,,,,,,,,**,,,,,,,,,,,,,/@@%(((####&&%&@@@&###########')
print (',.........,.......,,,,,,.....,..... .....,........... ....................................,.......,....................,.............,,,,,,,**,,,,,,,,,,,,,,,*,,,,,,,,,.*,,/&@&(##(####%@@@@@@#########&')
print ('............,...,.,..,,,.,.,,,.....,..........,. ....,.........,...........................................................,.....,...,..,,,,,,,,,,,,.,.,,,,,,,,,,,,,,,,,,,,,,%&%####(#%&@@@@@@%#######(#')
print ('......,.....,....,...,,....,....................................... .,..............................................,.................,..,,,,,,.,,,,,.,.,.,,.,,,,.,,.,.,,,.,,,%&%%#(##%%%&@@&#(/(#####((')
print (',.,.,..,........,.......,..................................................................,........................,......,,,,,.,..,.,,,,,,,,,,,,,..,,,,.,,.,,,,,,,,,.,,,..,.,(%%%#%%%%%%%&#((((((#((((')
print (' .....,.,....,.......,...,,,.......,................,...................,............................................,......,..,...,...,.,,,,,,,,,,,,.,...,.,,,,,,,,,,,,,,,....*#&%&%%%%%%%#(((((/(@%(((')
print ('.,.,,...,.........,.....,... ..................,.,,..................,....... .......,...............,.,.......,.....,.,.,,,,,.,.,,,.,..,,,,..,,,,,,,,,.....,.,,,,,,,,.,,.,,..,.,%&@@&%%%%####(//(@@@&((')
print ('...,,....................,....,. .....,. .......,...,..................... ...,.............................,..,....,.,,..,.,,.,,,.,...,.,,,.,,,,,,.........,,,,....,..,,,.....,,(@@@@&%%###((#(#&@@@@@%')
print ('.,..., ,.....,,..,.....,.,,.........,.,....,....,........,....,...............,................................,..,,,,,,.,.,.,.,,.,,,,..,.,..,,,,,............,,.....,,,.....,..,*&&&&&&(##(((##%&&&&&&&')
print ('..............,.,,.....,...... ...........................,.,.,..................................................,,,,..,.,,,.,..,,...,.,,,....,....,.....,..,...,....,.,,,,,,.,..,%&&&&#((((((#&%%&&&&&#')
print ('..........,.,,,,,...................................,..,..,.........,.,....,....................................,,.,,,,,.,,,,........,........,....,.......,.,...,........,..,.,.,#%&%(///((((##%##%&%((')
print ('...,...........,.,.,...,,....   ...............,......,....,...,.,..,.,........,............. .................,.,.,,,,,,,,,...,...,..,,.,.,..,...,.....................,,,,,....,(##(/(/////(##%%%#((//')
print ('..,,.........,....,.......,.... .. ..,,..,,...............,,,...,.,,,.....,............................ ......,,...,,.,,.,,,.....,,,..,,.,...,........,....,.,,.....,,,,,,,,.....,(%&&(/////%%(#%##%&&#(')
print (' ....,........................... ................,,....,..,.........,.. ,...,.,.............. . ..........,.....,....,,,,,...,.,...,...,,.,.,,............,,.......,.,..,,,,.....#%&&&%//(%%%%%%%%&&&&&')
print (',. .. ..,....,...,*,.........,..,.........,...,....,,,,......,,.......,..,......,,.........................,,......,.,.,.,,....,,.,,..,.,......,...........,,,,.,....,,.,..,,,....#%&&&&&(%#%%%%%#&&&&&&')
print (',......,,,....,,,,,...,.,...................,,..,,.,,,,.,.,.,...........,,...................... .........,....,......,,,.,,..,..,,.........,.........,....,.,,,......,,,,,.,....,#%&&&&&#########%&&&&&')
print ('...........,,,,,..,,.. . ......,....,.,... .,.,,,,,..,,,,,..,.....,.......,...,..........................,........,,,.,.,,.,,............,..............,..............,....,.,,..*##%&&&%%#########%&&%')
print ('.........,,,.,....,......,..............,,,.,..,,...,,,,.,.....,,..,,..,.......,.....................,.,.,..............,,,.,,,,..,......,..,.,............,,..............,,......*/%%#(######((((((%%#')
print ('.............,,.........,............,..............,,,....,,.,....,.....,,......,...,.............,,...,.,..,.,...,,,,.....,,,,......,.,......,,...........,...........,..,.,......*//(###%%##(((((((((')
print ('.....,.....,,,,.........,..............,.,..,..,,.,.,............,.......,,..........,.....................,,,...,,,,.,,..,.,...,,.,,....,..............,,,,.,.......................//((####&&%((((((((')
print ('........,..,..,.,..,......,,,...... ..,...,........,,..,.....,....,....,..,.........,...........,...,,.,..,..,,..,.....,....,,,,,.,,,...,,..,.............,........,........,..... ..,/((#%%&&&&&#/(((((')
print ('.......,.,...,..............,.....,.,....,,,.,.,.,...,.,...............,.,..,....,.......,,,....,..,...,..,,.,,,,,,.,.,,,.,,,.,.,,...,.,...............,....,........................,.*/(/%&&&&&&((((((')
print ('...,.,......,,.................,.........,........,,...........,...........................,,,..,...,,,.,.,,..,,.*,......,,...,,.,,....,,...,.,,...,.,...,................,......... ..,/(#%%&&&&%((((((')
print (' ..,..,..,........ ....................,,,.........,....,...,,....,......,.............. .......,.,,......,..,...,,,.,....,.,..,.,,,,..,..,....,..,,.,....,,...,..................... .,,(###%%%%(///(((')
print (',..,....................,.....,.,,.,.,,.............,,.,.,,...........,,.,..,..............,........,,,,,...,,..,,..,...,,.,.,,..,.,,,,.,,...........,..,...........,..................,,,((####///////(')
print ('..,,.,..................,..........,..,.........,.,,,,.,,....... ..,....,...................,..,.,...,............,.........,,,.........,...,,......,,.,.,.................,............,.*((#((///*/*/%')
print ('..............,...,.......  .....,..,.,..,..,...,.,,,,,.....,,.. ..,...,,..................... ,.,....,,..,,.,.......,,............,........,.........,.................,,,...............,((((((/**//%&')
print ('............ ...............,.,. ......,,.,,..,,..,.,...................,,....... .......,,.,......,..,..,,.,...,.....,,.....,,,......,..,........,....,..,........,............. .........*((//(///*&&&')
print ('...,............,...., ........,.....,,.......,,,....,.............,.,...... .,.......,...,.. ,..........,..,,....,.,,,.,.,.,.......,..,..............,,..,,...,....,......................,/////(((#%%%')
print ('*...............,..,..........,......,.,,,.....,....,,. .,............,,......,.........,,.......,..,...,.............,......,,...,..,.....,.....,..,.,,.,................................,.,/((////(%%&')
print ('...................,.,,....., ..,..,.,,,...,....,..,,,.. ....,............,.... ....................,.................,...,,,,,,.,.,,..............,,....,...,...........,.... ...... .......(///////*#%')
print ('..............,.,..,...,....,,,......,,...,..,...,,.,,...,,....... ...,,.......,........ ..,... .,.. .......,,..,,,.....,,,,..,................,.,......,....,.....................,.........,/((///*/*(')
print ('...... ,.,................,........,.,.,*.,..,..,.,..,............ ,..........,....,......,. . ......,......,..,...,.,,,,,.,..,,,,,....,. ...,....................................,...........////*****/')
print (' ...............,................,...,..,........ .....,..........., .,,,..  .  . .............,...,........,..,,...,...,..,,,.,.....,,,,.,...,...,,...,,..........................,..........*#%%/***//')
print (',, ........,...............,.,......,,...,,..............,,,.....,,...,..... ,,..... .....,,................,,,,.,,,.,.,,..,,,,,,......,..,.,,.,..,.,,..,........,..,............,... ........,#%%%#/*((')
print (',..,.,.... ..................,.,,,.,.,..., .,....,,.......,...,.,.........,.............,.......,,..,........,.,.,,.,,,..,.,,,,,.,...,..,,,,.,,..............,..................... .........,./%%%%%///')
print (' . ..,.......... ..............,...,......,..........,..,,..,..................................,...,....,........,.,,,.,...,.,,...,..,...,..,.........,,.....,.............................,..,,##%%%///')
print ('..... .............................,,..,..,.....,.......,,................,.............. .. ........,..........,....,,...,,,,..,,.,,,...,..,......,,..,....,,.,.......,.......................,(#%%(///')
print (' ...  ......,.,. ........ .......,,.,.......,,...........,........,.........................,,.....,...,.,.....,,.....,....,,....,,.....,.,,..,..,.,...,.,,.,,......,,..........................*##(////')
print ('... ,.......,............,,.....,....,...,..... ........,,.................,......,.......,.,,,,..,.,.,,......,..,.,....,,,,.,....,.,,...........,.,,.,..,..,...............................,,..,*//////')
print ('... . .....,....... ......,.,......,.,..............,,,...,,.,.....,.................................,..,...,...,,..,.,...,,..,,,,,.,...,,,,..,...,...............,,..,............  ............///////')
print (' . .......,.,................,,..,.......,..........,,..........,,...... .  .,..... ... ........,,,,.,........,.,,,.,,,,.,,,.,...,....,,,...,.....,,.....,.... ....... .....................,...,/(#(///')
print ('.....,.. ...............,.,...,..............  .............................,.......,..........,..............,..,...,..,,,,,,,..,....,,,,,.,,,......................... .................*......,////(#')
print ('................    ... ........,.. ....,..,...........,,... .............. ...... ............,.,...,,..........,.,,....,,,,,,,.,...,.,,,,,.,.,,,.,,.,...................................,,,...,,/(/*/#')
print (',.,. .... ....   ... ....,,.......,..,..,....,,,,,.....,... .... ,,..,....,....................,.,..... ........,.,,.,,...,,,,..,...,.,.,,,,,,*,,,,*,,,,..,....,.......................  .,,,...,.*(///*')
print (' . ,.. .... ...................,...,......,..,.. . ...,,....,.............,..........,... . ...............,.....,...,...,,.....,.....,,.,.,,*,,*,,**,,,,,,.............,,.....,...........,.. ..,/##/**')
print (',. ....,.. ......... ...........,.,,...........,......,,.............. . ....,.,..,...............,..................,.....,......,...,...,,...,.,,.,,.,,,,,,,,,...,.......,...............*....../(/***')
print ('..........,.........  ..... .,,......,......,.........,............. ,..........,, ....,............,.........,,.,.....,,..,...,.......,.........,,...,..,....,,..,,..,. ... ..............*,...,.(*****')
print ('.............,....... ...,..,..,...,...........................,. ........ ..................,. ,,..,.,.......,.........................,....,,.,....,........,.,........... ..... ........(,...*.////**')
print (' ............................,.......... ..,,......,,. .. ........,..., .. .........  .......,,.........,..,..,..,........ ...,............,..,.,,........................,.......... .....(,.,,*,,*//(*')
print ('.................   . , .....,........,......... .,................. ........,.. .,,.... ...............,,,.,.,,.......,.........,,....,...,,,.,.,*...............,..,.... ...............,(...**///(((#')
print (' .............. ..... .. .,..,.....,.......,........,. ... ... ................ ...............,.......,,....,.,..,,......................,,...,,,.,...........,..........................*,,.*/(#######')
print ('.... ....... ,...................., ..........,,....,.  ..  ....................... ...   ....... .. .. . .......,,.,,.,......,...,.......,.,.,,..,.. ... ...... ..............  .. .,,.. ...,((#%%%####')
print (' .  ..... ...... ...., . ....,.....,......,,.,...,...,..,. . ... ..,......... ... .. ... ......,.............,,,.,.........,....................,...,......    .. .. ............. .,,.......*((%%%%%%%#')
print (', . . ....... .............,...., ..................,... .. .............. .. .................................,.........,..................................... ........... ..... .,,,......*/*,,,*(%%%%')
print ('.   ....... ..... .  ........... ........,.................. . ...,,...... .... ...,.......... . ....,.....................,.,...... ,. .....,.................. ... ..... ...,....,......,/(((((//**/(#')
print ('................... .....,......................,............  .......,.... .... ..,,.,...... .. ..............,.,,.... ,............. ...,,........,,....................................*#((////*//*//')
print ('...,.............,...  ....   .. ......,... ,,..............  .,.. ........ .....,,............. ........ ....,....,.,,.,....,.....,......,,...,,............. ..... ........,............,////(//*****/')
print ('..... ........ ......................,.........,................. ...,......... ... ... ..............   ........................,,...,....,...................... ..................,....,///(######%%%')
print ('....,........... ..... .,..,.  ........,...,...,,......,,........ ...........,.,.... ....,,.................,...,,........,.,....,..,,.........,..,.,.,.. ............ ............ .......*((((###%&@@@')
print ('...... ........ .,. ... ..... ..   ..............,,........,... .......,.,....... .,........ ....... , ..,........,......... ......................,,,.. .........,........ ...............,(#%%&@@@@@@@')
print ('............................ ...  .........,,... ............  ... ....,.........,.... .... .,........... ...............,..,......................,,....,.,....................... .....,,,(@@@@&&@@@&&')

print ('')
print ('')
print (' NAME :-  PARIDHI DOGRA')  
print ('')
print ('')
print (' BIRTH OF DATE :- 25 SEP 2008')
print ('')
print ('')
print (' FATHER NAME :- SANJAY KUMAR')
print ('')
print ('')
print (' MOTHER NAME :- MANJU DOGRA')
print ('')
print ('')
print (' BANK A/C NO. :- 5112451327')
print ('')
print ('')
print (' BANK NAME:- CENTRAL BANK OF INDIA')
print ('')
print ('')
print (' IFSC CODE:- CBIN0283801')
print ('')
print ('')
print (' MICR NO :- 110016139')
print ('')
print ('')
print (' AADHAR CARD :- 375605070827')
print ('')
print ('')
print (' MOBILE NUMBER:- 9810404681')
print ('')
print ('')
print (' ADDRESS :- E-39, FLAT NO. C-4 GOKUL DHAM APARTMENT, GALI NO.8, VISWAR PARK, UTTAM NAGAR, WEST DELHI, DELHI 110059')
print ('')
print ('')
