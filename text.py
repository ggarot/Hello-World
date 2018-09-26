f = open("file.txt", "r")

arraysDict = {}
for i in range(1,10):
    arraysDict['P{0}AK'.format(i)] = "*0" + str(i) +"AH#"
    arraysDict['P{0}OK'.format(i)] = "*0" + str(i) +"AO#"
    arraysDict['P{0}AE'.format(i)] = "*0" + str(i) +"AH="
    arraysDict['P{0}OE'.format(i)] = "*0" + str(i) +"AO="
    arraysDict['P{0}AA'.format(i)] = "*0" + str(i) +"A"
    arraysDict['P{0}SK'.format(i)] = "*0" + str(i) +"SH#"
    arraysDict['P{0}SE'.format(i)] = "*0" + str(i) +"SH="
    arraysDict['P{0}SA'.format(i)] = "*0" + str(i) +"S"
    arraysDict['P{0}EK'.format(i)] = "*0" + str(i) +"EH#"
    arraysDict['P{0}EE'.format(i)] = "*0" + str(i) +"EH="
    arraysDict['P{0}EA'.format(i)] = "*0" + str(i) +"E"
    arraysDict['P{0}RK'.format(i)] = "*0" + str(i) +"RH#"
    arraysDict['P{0}RP'.format(i)] = "*0" + str(i) +"RH+"
    arraysDict['P{0}RM'.format(i)] = "*0" + str(i) +"RH-"
    arraysDict['P{0}RE'.format(i)] = "*0" + str(i) +"RH="
    arraysDict['P{0}RA'.format(i)] = "*0" + str(i) +"R"
    arraysDict['P{0}DK'.format(i)] = "*0" + str(i) +"DH#"
    arraysDict['P{0}DP'.format(i)] = "*0" + str(i) +"DH+"
    arraysDict['P{0}DM'.format(i)] = "*0" + str(i) +"DH-"
    arraysDict['P{0}DE'.format(i)] = "*0" + str(i) +"DH="
    arraysDict['P{0}DA'.format(i)] = "*0" + str(i) +"D"
    arraysDict['P{0}BK'.format(i)] = "*0" + str(i) +"BH#"
    arraysDict['P{0}BE'.format(i)] = "*0" + str(i) +"BH="
    arraysDict['P{0}BA'.format(i)] = "*0" + str(i) +"B"
    arraysDict['P{0}A_kills'.format(i)] = 0
    arraysDict['P{0}A_errors'.format(i)] = 0
    arraysDict['P{0}A_total'.format(i)] = 0
    arraysDict['P{0}S_aces'.format(i)] = 0
    arraysDict['P{0}S_errors'.format(i)] = 0
    arraysDict['P{0}S_total'.format(i)] = 0
    arraysDict['P{0}S_points'.format(i)] = 0
    arraysDict['P{0}E_kills'.format(i)] = 0
    arraysDict['P{0}E_errors'.format(i)] = 0
    arraysDict['P{0}E_total'.format(i)] = 0
    arraysDict['P{0}R_success'.format(i)] = 0
    arraysDict['P{0}R_errors'.format(i)] = 0
    arraysDict['P{0}R_total'.format(i)] = 0
    arraysDict['P{0}D_success'.format(i)] = 0
    arraysDict['P{0}D_errors'.format(i)] = 0
    arraysDict['P{0}D_total'.format(i)] = 0
    arraysDict['P{0}B_success'.format(i)] = 0
    arraysDict['P{0}B_errors'.format(i)] = 0
    arraysDict['P{0}B_assists'.format(i)] = 0
    arraysDict['P{0}B_total'.format(i)] = 0
    arraysDict['P{0}'.format(i)] = i
    arraysDict['P{0}_MGP'.format(i)] = 0

for i in range(10,30):
    arraysDict['P{0}AK'.format(i)] = "*" + str(i) +"AH#"
    arraysDict['P{0}OK'.format(i)] = "*" + str(i) +"AO#"
    arraysDict['P{0}AE'.format(i)] = "*" + str(i) +"AH="
    arraysDict['P{0}OE'.format(i)] = "*" + str(i) +"AO="
    arraysDict['P{0}AA'.format(i)] = "*" + str(i) +"A"
    arraysDict['P{0}SK'.format(i)] = "*" + str(i) +"SH#"
    arraysDict['P{0}SE'.format(i)] = "*" + str(i) +"SH="
    arraysDict['P{0}SA'.format(i)] = "*" + str(i) +"S"
    arraysDict['P{0}EK'.format(i)] = "*" + str(i) +"EH#"
    arraysDict['P{0}EE'.format(i)] = "*" + str(i) +"EH="
    arraysDict['P{0}EA'.format(i)] = "*" + str(i) +"E"
    arraysDict['P{0}RK'.format(i)] = "*" + str(i) +"RH#"
    arraysDict['P{0}RP'.format(i)] = "*" + str(i) +"RH+"
    arraysDict['P{0}RM'.format(i)] = "*" + str(i) +"RH-"
    arraysDict['P{0}RE'.format(i)] = "*" + str(i) +"RH="
    arraysDict['P{0}RA'.format(i)] = "*" + str(i) +"R"
    arraysDict['P{0}DK'.format(i)] = "*" + str(i) +"DH#"
    arraysDict['P{0}DP'.format(i)] = "*" + str(i) +"DH+"
    arraysDict['P{0}DM'.format(i)] = "*" + str(i) +"DH-"
    arraysDict['P{0}DE'.format(i)] = "*" + str(i) +"DH="
    arraysDict['P{0}DA'.format(i)] = "*" + str(i) +"D"
    arraysDict['P{0}BK'.format(i)] = "*" + str(i) +"BH#"
    arraysDict['P{0}BE'.format(i)] = "*" + str(i) +"BH="
    arraysDict['P{0}BA'.format(i)] = "*" + str(i) +"B"
    arraysDict['P{0}A_kills'.format(i)] = 0
    arraysDict['P{0}A_errors'.format(i)] = 0
    arraysDict['P{0}A_total'.format(i)] = 0
    arraysDict['P{0}S_aces'.format(i)] = 0
    arraysDict['P{0}S_errors'.format(i)] = 0
    arraysDict['P{0}S_total'.format(i)] = 0
    arraysDict['P{0}S_points'.format(i)] = 0
    arraysDict['P{0}E_kills'.format(i)] = 0
    arraysDict['P{0}E_errors'.format(i)] = 0
    arraysDict['P{0}E_total'.format(i)] = 0
    arraysDict['P{0}R_success'.format(i)] = 0
    arraysDict['P{0}R_errors'.format(i)] = 0
    arraysDict['P{0}R_total'.format(i)] = 0
    arraysDict['P{0}D_success'.format(i)] = 0
    arraysDict['P{0}D_errors'.format(i)] = 0
    arraysDict['P{0}D_total'.format(i)] = 0
    arraysDict['P{0}B_success'.format(i)] = 0
    arraysDict['P{0}B_errors'.format(i)] = 0
    arraysDict['P{0}B_assists'.format(i)] = 0
    arraysDict['P{0}B_total'.format(i)] = 0
    arraysDict['P{0}'.format(i)] = i
    arraysDict['P{0}_MGP'.format(i)] = 0


#print (arraysDict)

#for key in arraysDict:
#   print (arraysDict.get(key))


for line in f:  
#2
#Attacks attempts
    if arraysDict['P2AK'] in line:
      arraysDict['P2A_kills'] = arraysDict['P2A_kills'] + 1
    if arraysDict['P2OK'] in line:
      arraysDict['P2A_kills'] = arraysDict['P2A_kills'] + 1
    if arraysDict['P2AE'] in line:
      arraysDict['P2A_errors'] = arraysDict['P2A_errors'] + 1
    if arraysDict['P2OE'] in line:
      arraysDict['P2A_errors'] = arraysDict['P2A_errors'] + 1
    if arraysDict['P2AA'] in line:
      arraysDict['P2A_total'] = arraysDict['P2A_total'] + 1

#Serve attempts
    if arraysDict['P2SK'] in line:
      arraysDict['P2S_aces'] = arraysDict['P2S_aces'] + 1
    if arraysDict['P2SE'] in line:
      arraysDict['P2S_errors'] = arraysDict['P2S_errors'] + 1
    if arraysDict['P2SA'] in line:
      arraysDict['P2S_total'] = arraysDict['P2S_total'] + 1

#Assists attempts
    if arraysDict['P2EK'] in line:
      arraysDict['P2E_kills'] = arraysDict['P2E_kills'] + 1
    if arraysDict['P2EE'] in line:
      arraysDict['P2E_errors'] = arraysDict['P2E_errors'] + 1
    if arraysDict['P2EA'] in line:
      arraysDict['P2E_total'] = arraysDict['P2E_total'] + 1

#Receive attempts
    if arraysDict['P2RK'] in line:
      arraysDict['P2R_success'] = arraysDict['P2R_success'] + 1
    if arraysDict['P2RP'] in line:
      arraysDict['P2R_success'] = arraysDict['P2R_success'] + 1
    if arraysDict['P2RM'] in line:
      arraysDict['P2R_success'] = arraysDict['P2R_success'] + 1
    if arraysDict['P2RE'] in line:
      arraysDict['P2R_errors'] = arraysDict['P2R_errors'] + 1
    if arraysDict['P2RA'] in line:
      arraysDict['P2R_total'] = arraysDict['P2R_total'] + 1

#Block attempts
    if arraysDict['P2BK'] in line:
      arraysDict['P2B_success'] = arraysDict['P2B_success'] + 1
    if arraysDict['P2BE'] in line:
      arraysDict['P2B_errors'] = arraysDict['P2B_errors'] + 1
    if arraysDict['P2BA'] in line:
      arraysDict['P2B_total'] = arraysDict['P2B_total'] + 1

#Dig attempts
    if arraysDict['P2DK'] in line:
      arraysDict['P2D_success'] = arraysDict['P2D_success'] + 1
    if arraysDict['P2DP'] in line:
      arraysDict['P2D_success'] = arraysDict['P2D_success'] + 1
    if arraysDict['P2DM'] in line:
      arraysDict['P2D_success'] = arraysDict['P2D_success'] + 1
    if arraysDict['P2DE'] in line:
      arraysDict['P2D_errors'] = arraysDict['P2D_errors'] + 1
    if arraysDict['P2DA'] in line:
      arraysDict['P2D_total'] = arraysDict['P2D_total'] + 1

#3
#Attacks attempts
    if arraysDict['P3AK'] in line:
      arraysDict['P3A_kills'] = arraysDict['P3A_kills'] + 1
    if arraysDict['P3OK'] in line:
      arraysDict['P3A_kills'] = arraysDict['P3A_kills'] + 1
    if arraysDict['P3AE'] in line:
      arraysDict['P3A_errors'] = arraysDict['P3A_errors'] + 1
    if arraysDict['P3OE'] in line:
      arraysDict['P3A_errors'] = arraysDict['P3A_errors'] + 1
    if arraysDict['P3AA'] in line:
      arraysDict['P3A_total'] = arraysDict['P3A_total'] + 1

#Serve attempts
    if arraysDict['P3SK'] in line:
      arraysDict['P3S_aces'] = arraysDict['P3S_aces'] + 1
    if arraysDict['P3SE'] in line:
      arraysDict['P3S_errors'] = arraysDict['P3S_errors'] + 1
    if arraysDict['P3SA'] in line:
      arraysDict['P3S_total'] = arraysDict['P3S_total'] + 1

#Assists attempts
    if arraysDict['P3EK'] in line:
      arraysDict['P3E_kills'] = arraysDict['P3E_kills'] + 1
    if arraysDict['P3EE'] in line:
      arraysDict['P3E_errors'] = arraysDict['P3E_errors'] + 1
    if arraysDict['P3EA'] in line:
      arraysDict['P3E_total'] = arraysDict['P3E_total'] + 1

#Receive attempts
    if arraysDict['P3RK'] in line:
      arraysDict['P3R_success'] = arraysDict['P3R_success'] + 1
    if arraysDict['P3RP'] in line:
      arraysDict['P3R_success'] = arraysDict['P3R_success'] + 1
    if arraysDict['P3RM'] in line:
      arraysDict['P3R_success'] = arraysDict['P3R_success'] + 1
    if arraysDict['P3RE'] in line:
      arraysDict['P3R_errors'] = arraysDict['P3R_errors'] + 1
    if arraysDict['P3RA'] in line:
      arraysDict['P3R_total'] = arraysDict['P3R_total'] + 1

#Block attempts
    if arraysDict['P3BK'] in line:
      arraysDict['P3B_success'] = arraysDict['P3B_success'] + 1
    if arraysDict['P3BE'] in line:
      arraysDict['P3B_errors'] = arraysDict['P3B_errors'] + 1
    if arraysDict['P3BA'] in line:
      arraysDict['P3B_total'] = arraysDict['P3B_total'] + 1

#Dig attempts
    if arraysDict['P3DK'] in line:
      arraysDict['P3D_success'] = arraysDict['P3D_success'] + 1
    if arraysDict['P3DP'] in line:
      arraysDict['P3D_success'] = arraysDict['P3D_success'] + 1
    if arraysDict['P3DM'] in line:
      arraysDict['P3D_success'] = arraysDict['P3D_success'] + 1
    if arraysDict['P3DE'] in line:
      arraysDict['P3D_errors'] = arraysDict['P3D_errors'] + 1
    if arraysDict['P3DA'] in line:
      arraysDict['P3D_total'] = arraysDict['P3D_total'] + 1

#5
#Attacks attempts
    if arraysDict['P5AK'] in line:
      arraysDict['P5A_kills'] = arraysDict['P5A_kills'] + 1
    if arraysDict['P5OK'] in line:
      arraysDict['P5A_kills'] = arraysDict['P5A_kills'] + 1
    if arraysDict['P5AE'] in line:
      arraysDict['P5A_errors'] = arraysDict['P5A_errors'] + 1
    if arraysDict['P5OE'] in line:
      arraysDict['P5A_errors'] = arraysDict['P5A_errors'] + 1
    if arraysDict['P5AA'] in line:
      arraysDict['P5A_total'] = arraysDict['P5A_total'] + 1

#Serve attempts
    if arraysDict['P5SK'] in line:
      arraysDict['P5S_aces'] = arraysDict['P5S_aces'] + 1
    if arraysDict['P5SE'] in line:
      arraysDict['P5S_errors'] = arraysDict['P5S_errors'] + 1
    if arraysDict['P5SA'] in line:
      arraysDict['P5S_total'] = arraysDict['P5S_total'] + 1

#Assists attempts
    if arraysDict['P5EK'] in line:
      arraysDict['P5E_kills'] = arraysDict['P5E_kills'] + 1
    if arraysDict['P5EE'] in line:
      arraysDict['P5E_errors'] = arraysDict['P5E_errors'] + 1
    if arraysDict['P5EA'] in line:
      arraysDict['P5E_total'] = arraysDict['P5E_total'] + 1

#Receive attempts
    if arraysDict['P5RK'] in line:
      arraysDict['P5R_success'] = arraysDict['P5R_success'] + 1
    if arraysDict['P5RP'] in line:
      arraysDict['P5R_success'] = arraysDict['P5R_success'] + 1
    if arraysDict['P5RM'] in line:
      arraysDict['P5R_success'] = arraysDict['P5R_success'] + 1
    if arraysDict['P5RE'] in line:
      arraysDict['P5R_errors'] = arraysDict['P5R_errors'] + 1
    if arraysDict['P5RA'] in line:
      arraysDict['P5R_total'] = arraysDict['P5R_total'] + 1

#Block attempts
    if arraysDict['P5BK'] in line:
      arraysDict['P5B_success'] = arraysDict['P5B_success'] + 1
    if arraysDict['P5BE'] in line:
      arraysDict['P5B_errors'] = arraysDict['P5B_errors'] + 1
    if arraysDict['P5BA'] in line:
      arraysDict['P5B_total'] = arraysDict['P5B_total'] + 1

#Dig attempts
    if arraysDict['P5DK'] in line:
      arraysDict['P5D_success'] = arraysDict['P5D_success'] + 1
    if arraysDict['P5DP'] in line:
      arraysDict['P5D_success'] = arraysDict['P5D_success'] + 1
    if arraysDict['P5DM'] in line:
      arraysDict['P5D_success'] = arraysDict['P5D_success'] + 1
    if arraysDict['P5DE'] in line:
      arraysDict['P5D_errors'] = arraysDict['P5D_errors'] + 1
    if arraysDict['P5DA'] in line:
      arraysDict['P5D_total'] = arraysDict['P5D_total'] + 1
#6
#Attacks attempts
    if arraysDict['P6AK'] in line:
      arraysDict['P6A_kills'] = arraysDict['P6A_kills'] + 1
    if arraysDict['P6OK'] in line:
      arraysDict['P6A_kills'] = arraysDict['P6A_kills'] + 1
    if arraysDict['P6AE'] in line:
      arraysDict['P6A_errors'] = arraysDict['P6A_errors'] + 1
    if arraysDict['P6OE'] in line:
      arraysDict['P6A_errors'] = arraysDict['P6A_errors'] + 1
    if arraysDict['P6AA'] in line:
      arraysDict['P6A_total'] = arraysDict['P6A_total'] + 1

#Serve attempts
    if arraysDict['P6SK'] in line:
      arraysDict['P6S_aces'] = arraysDict['P6S_aces'] + 1
    if arraysDict['P6SE'] in line:
      arraysDict['P6S_errors'] = arraysDict['P6S_errors'] + 1
    if arraysDict['P6SA'] in line:
      arraysDict['P6S_total'] = arraysDict['P6S_total'] + 1

#Assists attempts
    if arraysDict['P6EK'] in line:
      arraysDict['P6E_kills'] = arraysDict['P6E_kills'] + 1
    if arraysDict['P6EE'] in line:
      arraysDict['P6E_errors'] = arraysDict['P6E_errors'] + 1
    if arraysDict['P6EA'] in line:
      arraysDict['P6E_total'] = arraysDict['P6E_total'] + 1

#Receive attempts
    if arraysDict['P6RK'] in line:
      arraysDict['P6R_success'] = arraysDict['P6R_success'] + 1
    if arraysDict['P6RP'] in line:
      arraysDict['P6R_success'] = arraysDict['P6R_success'] + 1
    if arraysDict['P6RM'] in line:
      arraysDict['P6R_success'] = arraysDict['P6R_success'] + 1
    if arraysDict['P6RE'] in line:
      arraysDict['P6R_errors'] = arraysDict['P6R_errors'] + 1
    if arraysDict['P6RA'] in line:
      arraysDict['P6R_total'] = arraysDict['P6R_total'] + 1

#Block attempts
    if arraysDict['P6BK'] in line:
      arraysDict['P6B_success'] = arraysDict['P6B_success'] + 1
    if arraysDict['P6BE'] in line:
      arraysDict['P6B_errors'] = arraysDict['P6B_errors'] + 1
    if arraysDict['P6BA'] in line:
      arraysDict['P6B_total'] = arraysDict['P6B_total'] + 1

#Dig attempts
    if arraysDict['P6DK'] in line:
      arraysDict['P6D_success'] = arraysDict['P6D_success'] + 1
    if arraysDict['P6DP'] in line:
      arraysDict['P6D_success'] = arraysDict['P6D_success'] + 1
    if arraysDict['P6DM'] in line:
      arraysDict['P6D_success'] = arraysDict['P6D_success'] + 1
    if arraysDict['P6DE'] in line:
      arraysDict['P6D_errors'] = arraysDict['P6D_errors'] + 1
    if arraysDict['P6DA'] in line:
      arraysDict['P6D_total'] = arraysDict['P6D_total'] + 1

#7
#Attacks attempts
    if arraysDict['P7AK'] in line:
      arraysDict['P7A_kills'] = arraysDict['P7A_kills'] + 1
    if arraysDict['P7OK'] in line:
      arraysDict['P7A_kills'] = arraysDict['P7A_kills'] + 1
    if arraysDict['P7AE'] in line:
      arraysDict['P7A_errors'] = arraysDict['P7A_errors'] + 1
    if arraysDict['P7OE'] in line:
      arraysDict['P7A_errors'] = arraysDict['P7A_errors'] + 1
    if arraysDict['P7AA'] in line:
      arraysDict['P7A_total'] = arraysDict['P7A_total'] + 1

#Serve attempts
    if arraysDict['P7SK'] in line:
      arraysDict['P7S_aces'] = arraysDict['P7S_aces'] + 1
    if arraysDict['P7SE'] in line:
      arraysDict['P7S_errors'] = arraysDict['P7S_errors'] + 1
    if arraysDict['P7SA'] in line:
      arraysDict['P7S_total'] = arraysDict['P7S_total'] + 1

#Assists attempts
    if arraysDict['P7EK'] in line:
      arraysDict['P7E_kills'] = arraysDict['P7E_kills'] + 1
    if arraysDict['P7EE'] in line:
      arraysDict['P7E_errors'] = arraysDict['P7E_errors'] + 1
    if arraysDict['P7EA'] in line:
      arraysDict['P7E_total'] = arraysDict['P7E_total'] + 1

#Receive attempts
    if arraysDict['P7RK'] in line:
      arraysDict['P7R_success'] = arraysDict['P7R_success'] + 1
    if arraysDict['P7RP'] in line:
      arraysDict['P7R_success'] = arraysDict['P7R_success'] + 1
    if arraysDict['P7RM'] in line:
      arraysDict['P7R_success'] = arraysDict['P7R_success'] + 1
    if arraysDict['P7RE'] in line:
      arraysDict['P7R_errors'] = arraysDict['P7R_errors'] + 1
    if arraysDict['P7RA'] in line:
      arraysDict['P7R_total'] = arraysDict['P7R_total'] + 1

#Block attempts
    if arraysDict['P7BK'] in line:
      arraysDict['P7B_success'] = arraysDict['P7B_success'] + 1
    if arraysDict['P7BE'] in line:
      arraysDict['P7B_errors'] = arraysDict['P7B_errors'] + 1
    if arraysDict['P7BA'] in line:
      arraysDict['P7B_total'] = arraysDict['P7B_total'] + 1

#Dig attempts
    if arraysDict['P7DK'] in line:
      arraysDict['P7D_success'] = arraysDict['P7D_success'] + 1
    if arraysDict['P7DP'] in line:
      arraysDict['P7D_success'] = arraysDict['P7D_success'] + 1
    if arraysDict['P7DM'] in line:
      arraysDict['P7D_success'] = arraysDict['P7D_success'] + 1
    if arraysDict['P7DE'] in line:
      arraysDict['P7D_errors'] = arraysDict['P7D_errors'] + 1
    if arraysDict['P7DA'] in line:
      arraysDict['P7D_total'] = arraysDict['P7D_total'] + 1

#9

#Attacks attempts

    if arraysDict['P9AK'] in line:
      arraysDict['P9A_kills'] = arraysDict['P9A_kills'] + 1
    if arraysDict['P9OK'] in line:
      arraysDict['P9A_kills'] = arraysDict['P9A_kills'] + 1
    if arraysDict['P9AE'] in line:
      arraysDict['P9A_errors'] = arraysDict['P9A_errors'] + 1
    if arraysDict['P9OE'] in line:
      arraysDict['P9A_errors'] = arraysDict['P9A_errors'] + 1
    if arraysDict['P9AA'] in line:
      arraysDict['P9A_total'] = arraysDict['P9A_total'] + 1

#Serve attempts
    if arraysDict['P9SK'] in line:
      arraysDict['P9S_aces'] = arraysDict['P9S_aces'] + 1
    if arraysDict['P9SE'] in line:
      arraysDict['P9S_errors'] = arraysDict['P9S_errors'] + 1
    if arraysDict['P9SA'] in line:
      arraysDict['P9S_total'] = arraysDict['P9S_total'] + 1

#Assists attempts
    if arraysDict['P9EK'] in line:
      arraysDict['P9E_kills'] = arraysDict['P9E_kills'] + 1
    if arraysDict['P9EE'] in line:
      arraysDict['P9E_errors'] = arraysDict['P9E_errors'] + 1
    if arraysDict['P9EA'] in line:
      arraysDict['P9E_total'] = arraysDict['P9E_total'] + 1

#Receive attempts
    if arraysDict['P9RK'] in line:
      arraysDict['P9R_success'] = arraysDict['P9R_success'] + 1
    if arraysDict['P9RP'] in line:
      arraysDict['P9R_success'] = arraysDict['P9R_success'] + 1
    if arraysDict['P9RM'] in line:
      arraysDict['P9R_success'] = arraysDict['P9R_success'] + 1
    if arraysDict['P9RE'] in line:
      arraysDict['P9R_errors'] = arraysDict['P9R_errors'] + 1
    if arraysDict['P9RA'] in line:
      arraysDict['P9R_total'] = arraysDict['P9R_total'] + 1

#Block attempts
    if arraysDict['P9BK'] in line:
      arraysDict['P9B_success'] = arraysDict['P9B_success'] + 1
    if arraysDict['P9BE'] in line:
      arraysDict['P9B_errors'] = arraysDict['P9B_errors'] + 1
    if arraysDict['P9BA'] in line:
      arraysDict['P9B_total'] = arraysDict['P9B_total'] + 1

#Dig attempts
    if arraysDict['P9DK'] in line:
      arraysDict['P9D_success'] = arraysDict['P9D_success'] + 1
    if arraysDict['P9DP'] in line:
      arraysDict['P9D_success'] = arraysDict['P9D_success'] + 1
    if arraysDict['P9DM'] in line:
      arraysDict['P9D_success'] = arraysDict['P9D_success'] + 1
    if arraysDict['P9DE'] in line:
      arraysDict['P9D_errors'] = arraysDict['P9D_errors'] + 1
    if arraysDict['P9DA'] in line:
      arraysDict['P9D_total'] = arraysDict['P9D_total'] + 1

#10
#Attacks attempts
    if arraysDict['P10AK'] in line:
      arraysDict['P10A_kills'] = arraysDict['P10A_kills'] + 1
    if arraysDict['P10OK'] in line:
      arraysDict['P10A_kills'] = arraysDict['P10A_kills'] + 1
    if arraysDict['P10AE'] in line:
      arraysDict['P10A_errors'] = arraysDict['P10A_errors'] + 1
    if arraysDict['P10OE'] in line:
      arraysDict['P10A_errors'] = arraysDict['P10A_errors'] + 1
    if arraysDict['P10AA'] in line:
      arraysDict['P10A_total'] = arraysDict['P10A_total'] + 1

#Serve attempts
    if arraysDict['P10SK'] in line:
      arraysDict['P10S_aces'] = arraysDict['P10S_aces'] + 1
    if arraysDict['P10SE'] in line:
      arraysDict['P10S_errors'] = arraysDict['P10S_errors'] + 1
    if arraysDict['P10SA'] in line:
      arraysDict['P10S_total'] = arraysDict['P10S_total'] + 1

#Assists attempts
    if arraysDict['P10EK'] in line:
      arraysDict['P10E_kills'] = arraysDict['P10E_kills'] + 1
    if arraysDict['P10EE'] in line:
      arraysDict['P10E_errors'] = arraysDict['P10E_errors'] + 1
    if arraysDict['P10EA'] in line:
      arraysDict['P10E_total'] = arraysDict['P10E_total'] + 1

#Receive attempts
    if arraysDict['P10RK'] in line:
      arraysDict['P10R_success'] = arraysDict['P10R_success'] + 1
    if arraysDict['P10RP'] in line:
      arraysDict['P10R_success'] = arraysDict['P10R_success'] + 1
    if arraysDict['P10RM'] in line:
      arraysDict['P10R_success'] = arraysDict['P10R_success'] + 1
    if arraysDict['P10RE'] in line:
      arraysDict['P10R_errors'] = arraysDict['P10R_errors'] + 1
    if arraysDict['P10RA'] in line:
      arraysDict['P10R_total'] = arraysDict['P10R_total'] + 1

#Block attempts
    if arraysDict['P10BK'] in line:
      arraysDict['P10B_success'] = arraysDict['P10B_success'] + 1
    if arraysDict['P10BE'] in line:
      arraysDict['P10B_errors'] = arraysDict['P10B_errors'] + 1
    if arraysDict['P10BA'] in line:
      arraysDict['P10B_total'] = arraysDict['P10B_total'] + 1

#Dig attempts
    if arraysDict['P10DK'] in line:
      arraysDict['P10D_success'] = arraysDict['P10D_success'] + 1
    if arraysDict['P10DP'] in line:
      arraysDict['P10D_success'] = arraysDict['P10D_success'] + 1
    if arraysDict['P10DM'] in line:
      arraysDict['P10D_success'] = arraysDict['P10D_success'] + 1
    if arraysDict['P10DE'] in line:
      arraysDict['P10D_errors'] = arraysDict['P10D_errors'] + 1
    if arraysDict['P10DA'] in line:
      arraysDict['P10D_total'] = arraysDict['P10D_total'] + 1

#10
#Attacks attempts
    if arraysDict['P10AK'] in line:
      arraysDict['P10A_kills'] = arraysDict['P10A_kills'] + 1
    if arraysDict['P10OK'] in line:
      arraysDict['P10A_kills'] = arraysDict['P10A_kills'] + 1
    if arraysDict['P10AE'] in line:
      arraysDict['P10A_errors'] = arraysDict['P10A_errors'] + 1
    if arraysDict['P10OE'] in line:
      arraysDict['P10A_errors'] = arraysDict['P10A_errors'] + 1
    if arraysDict['P10AA'] in line:
      arraysDict['P10A_total'] = arraysDict['P10A_total'] + 1

#Serve attempts
    if arraysDict['P10SK'] in line:
      arraysDict['P10S_aces'] = arraysDict['P10S_aces'] + 1
    if arraysDict['P10SE'] in line:
      arraysDict['P10S_errors'] = arraysDict['P10S_errors'] + 1
    if arraysDict['P10SA'] in line:
      arraysDict['P10S_total'] = arraysDict['P10S_total'] + 1

#Assists attempts
    if arraysDict['P10EK'] in line:
      arraysDict['P10E_kills'] = arraysDict['P10E_kills'] + 1
    if arraysDict['P10EE'] in line:
      arraysDict['P10E_errors'] = arraysDict['P10E_errors'] + 1
    if arraysDict['P10EA'] in line:
      arraysDict['P10E_total'] = arraysDict['P10E_total'] + 1

#Receive attempts
    if arraysDict['P10RK'] in line:
      arraysDict['P10R_success'] = arraysDict['P10R_success'] + 1
    if arraysDict['P10RP'] in line:
      arraysDict['P10R_success'] = arraysDict['P10R_success'] + 1
    if arraysDict['P10RM'] in line:
      arraysDict['P10R_success'] = arraysDict['P10R_success'] + 1
    if arraysDict['P10RE'] in line:
      arraysDict['P10R_errors'] = arraysDict['P10R_errors'] + 1
    if arraysDict['P10RA'] in line:
      arraysDict['P10R_total'] = arraysDict['P10R_total'] + 1

#Block attempts
    if arraysDict['P10BK'] in line:
      arraysDict['P10B_success'] = arraysDict['P10B_success'] + 1
    if arraysDict['P10BE'] in line:
      arraysDict['P10B_errors'] = arraysDict['P10B_errors'] + 1
    if arraysDict['P10BA'] in line:
      arraysDict['P10B_total'] = arraysDict['P10B_total'] + 1

#Dig attempts
    if arraysDict['P10DK'] in line:
      arraysDict['P10D_success'] = arraysDict['P10D_success'] + 1
    if arraysDict['P10DP'] in line:
      arraysDict['P10D_success'] = arraysDict['P10D_success'] + 1
    if arraysDict['P10DM'] in line:
      arraysDict['P10D_success'] = arraysDict['P10D_success'] + 1
    if arraysDict['P10DE'] in line:
      arraysDict['P10D_errors'] = arraysDict['P10D_errors'] + 1
    if arraysDict['P10DA'] in line:
      arraysDict['P10D_total'] = arraysDict['P10D_total'] + 1

#11

#Attacks attempts
    if arraysDict['P11AK'] in line:
      arraysDict['P11A_kills'] = arraysDict['P11A_kills'] + 1
    if arraysDict['P11OK'] in line:
      arraysDict['P11A_kills'] = arraysDict['P11A_kills'] + 1
    if arraysDict['P11AE'] in line:
      arraysDict['P11A_errors'] = arraysDict['P11A_errors'] + 1
    if arraysDict['P11OE'] in line:
      arraysDict['P11A_errors'] = arraysDict['P11A_errors'] + 1
    if arraysDict['P11AA'] in line:
      arraysDict['P11A_total'] = arraysDict['P11A_total'] + 1

#Serve attempts
    if arraysDict['P11SK'] in line:
      arraysDict['P11S_aces'] = arraysDict['P11S_aces'] + 1
    if arraysDict['P11SE'] in line:
      arraysDict['P11S_errors'] = arraysDict['P11S_errors'] + 1
    if arraysDict['P11SA'] in line:
      arraysDict['P11S_total'] = arraysDict['P11S_total'] + 1

#Assists attempts
    if arraysDict['P11EK'] in line:
      arraysDict['P11E_kills'] = arraysDict['P11E_kills'] + 1
    if arraysDict['P11EE'] in line:
      arraysDict['P11E_errors'] = arraysDict['P11E_errors'] + 1
    if arraysDict['P11EA'] in line:
      arraysDict['P11E_total'] = arraysDict['P11E_total'] + 1

#Receive attempts
    if arraysDict['P11RK'] in line:
      arraysDict['P11R_success'] = arraysDict['P11R_success'] + 1
    if arraysDict['P11RP'] in line:
      arraysDict['P11R_success'] = arraysDict['P11R_success'] + 1
    if arraysDict['P11RM'] in line:
      arraysDict['P11R_success'] = arraysDict['P11R_success'] + 1
    if arraysDict['P11RE'] in line:
      arraysDict['P11R_errors'] = arraysDict['P11R_errors'] + 1
    if arraysDict['P11RA'] in line:
      arraysDict['P11R_total'] = arraysDict['P11R_total'] + 1

#Block attempts
    if arraysDict['P11BK'] in line:
      arraysDict['P11B_success'] = arraysDict['P11B_success'] + 1
    if arraysDict['P11BE'] in line:
      arraysDict['P11B_errors'] = arraysDict['P11B_errors'] + 1
    if arraysDict['P11BA'] in line:
      arraysDict['P11B_total'] = arraysDict['P11B_total'] + 1

#Dig attempts
    if arraysDict['P11DK'] in line:
      arraysDict['P11D_success'] = arraysDict['P11D_success'] + 1
    if arraysDict['P11DP'] in line:
      arraysDict['P11D_success'] = arraysDict['P11D_success'] + 1
    if arraysDict['P11DM'] in line:
      arraysDict['P11D_success'] = arraysDict['P11D_success'] + 1
    if arraysDict['P11DE'] in line:
      arraysDict['P11D_errors'] = arraysDict['P11D_errors'] + 1
    if arraysDict['P11DA'] in line:
      arraysDict['P11D_total'] = arraysDict['P11D_total'] + 1

#13

#Attacks attempts
    if arraysDict['P13AK'] in line:
      arraysDict['P13A_kills'] = arraysDict['P13A_kills'] + 1
    if arraysDict['P13OK'] in line:
      arraysDict['P13A_kills'] = arraysDict['P13A_kills'] + 1
    if arraysDict['P13AE'] in line:
      arraysDict['P13A_errors'] = arraysDict['P13A_errors'] + 1
    if arraysDict['P13OE'] in line:
      arraysDict['P13A_errors'] = arraysDict['P13A_errors'] + 1
    if arraysDict['P13AA'] in line:
      arraysDict['P13A_total'] = arraysDict['P13A_total'] + 1

#Serve attempts
    if arraysDict['P13SK'] in line:
      arraysDict['P13S_aces'] = arraysDict['P13S_aces'] + 1
    if arraysDict['P13SE'] in line:
      arraysDict['P13S_errors'] = arraysDict['P13S_errors'] + 1
    if arraysDict['P13SA'] in line:
      arraysDict['P13S_total'] = arraysDict['P13S_total'] + 1

#Assists attempts
    if arraysDict['P13EK'] in line:
      arraysDict['P13E_kills'] = arraysDict['P13E_kills'] + 1
    if arraysDict['P13EE'] in line:
      arraysDict['P13E_errors'] = arraysDict['P13E_errors'] + 1
    if arraysDict['P13EA'] in line:
      arraysDict['P13E_total'] = arraysDict['P13E_total'] + 1

#Receive attempts
    if arraysDict['P13RK'] in line:
      arraysDict['P13R_success'] = arraysDict['P13R_success'] + 1
    if arraysDict['P13RP'] in line:
      arraysDict['P13R_success'] = arraysDict['P13R_success'] + 1
    if arraysDict['P13RM'] in line:
      arraysDict['P13R_success'] = arraysDict['P13R_success'] + 1
    if arraysDict['P13RE'] in line:
      arraysDict['P13R_errors'] = arraysDict['P13R_errors'] + 1
    if arraysDict['P13RA'] in line:
      arraysDict['P13R_total'] = arraysDict['P13R_total'] + 1

#Block attempts
    if arraysDict['P13BK'] in line:
      arraysDict['P13B_success'] = arraysDict['P13B_success'] + 1
    if arraysDict['P13BE'] in line:
      arraysDict['P13B_errors'] = arraysDict['P13B_errors'] + 1
    if arraysDict['P13BA'] in line:
      arraysDict['P13B_total'] = arraysDict['P13B_total'] + 1

#Dig attempts
    if arraysDict['P13DK'] in line:
      arraysDict['P13D_success'] = arraysDict['P13D_success'] + 1
    if arraysDict['P13DP'] in line:
      arraysDict['P13D_success'] = arraysDict['P13D_success'] + 1
    if arraysDict['P13DM'] in line:
      arraysDict['P13D_success'] = arraysDict['P13D_success'] + 1
    if arraysDict['P13DE'] in line:
      arraysDict['P13D_errors'] = arraysDict['P13D_errors'] + 1
    if arraysDict['P13DA'] in line:
      arraysDict['P13D_total'] = arraysDict['P13D_total'] + 1

#16

#Attacks attempts
    if arraysDict['P16AK'] in line:
      arraysDict['P16A_kills'] = arraysDict['P16A_kills'] + 1
    if arraysDict['P16OK'] in line:
      arraysDict['P16A_kills'] = arraysDict['P16A_kills'] + 1
    if arraysDict['P16AE'] in line:
      arraysDict['P16A_errors'] = arraysDict['P16A_errors'] + 1
    if arraysDict['P16OE'] in line:
      arraysDict['P16A_errors'] = arraysDict['P16A_errors'] + 1
    if arraysDict['P16AA'] in line:
      arraysDict['P16A_total'] = arraysDict['P16A_total'] + 1

#Serve attempts
    if arraysDict['P16SK'] in line:
      arraysDict['P16S_aces'] = arraysDict['P16S_aces'] + 1
    if arraysDict['P16SE'] in line:
      arraysDict['P16S_errors'] = arraysDict['P16S_errors'] + 1
    if arraysDict['P16SA'] in line:
      arraysDict['P16S_total'] = arraysDict['P16S_total'] + 1

#Assists attempts
    if arraysDict['P16EK'] in line:
      arraysDict['P16E_kills'] = arraysDict['P16E_kills'] + 1
    if arraysDict['P16EE'] in line:
      arraysDict['P16E_errors'] = arraysDict['P16E_errors'] + 1
    if arraysDict['P16EA'] in line:
      arraysDict['P16E_total'] = arraysDict['P16E_total'] + 1

#Receive attempts
    if arraysDict['P16RK'] in line:
      arraysDict['P16R_success'] = arraysDict['P16R_success'] + 1
    if arraysDict['P16RP'] in line:
      arraysDict['P16R_success'] = arraysDict['P16R_success'] + 1
    if arraysDict['P16RM'] in line:
      arraysDict['P16R_success'] = arraysDict['P16R_success'] + 1
    if arraysDict['P16RE'] in line:
      arraysDict['P16R_errors'] = arraysDict['P16R_errors'] + 1
    if arraysDict['P16RA'] in line:
      arraysDict['P16R_total'] = arraysDict['P16R_total'] + 1

#Block attempts
    if arraysDict['P16BK'] in line:
      arraysDict['P16B_success'] = arraysDict['P16B_success'] + 1
    if arraysDict['P16BE'] in line:
      arraysDict['P16B_errors'] = arraysDict['P16B_errors'] + 1
    if arraysDict['P16BA'] in line:
      arraysDict['P16B_total'] = arraysDict['P16B_total'] + 1

#Dig attempts
    if arraysDict['P16DK'] in line:
      arraysDict['P16D_success'] = arraysDict['P16D_success'] + 1
    if arraysDict['P16DP'] in line:
      arraysDict['P16D_success'] = arraysDict['P16D_success'] + 1
    if arraysDict['P16DM'] in line:
      arraysDict['P16D_success'] = arraysDict['P16D_success'] + 1
    if arraysDict['P16DE'] in line:
      arraysDict['P16D_errors'] = arraysDict['P16D_errors'] + 1
    if arraysDict['P16DA'] in line:
      arraysDict['P16D_total'] = arraysDict['P16D_total'] + 1

#18

#Attacks attempts
    if arraysDict['P18AK'] in line:
      arraysDict['P18A_kills'] = arraysDict['P18A_kills'] + 1
    if arraysDict['P18OK'] in line:
      arraysDict['P18A_kills'] = arraysDict['P18A_kills'] + 1
    if arraysDict['P18AE'] in line:
      arraysDict['P18A_errors'] = arraysDict['P18A_errors'] + 1
    if arraysDict['P18OE'] in line:
      arraysDict['P18A_errors'] = arraysDict['P18A_errors'] + 1
    if arraysDict['P18AA'] in line:
      arraysDict['P18A_total'] = arraysDict['P18A_total'] + 1

#Serve attempts
    if arraysDict['P18SK'] in line:
      arraysDict['P18S_aces'] = arraysDict['P18S_aces'] + 1
    if arraysDict['P18SE'] in line:
      arraysDict['P18S_errors'] = arraysDict['P18S_errors'] + 1
    if arraysDict['P18SA'] in line:
      arraysDict['P18S_total'] = arraysDict['P18S_total'] + 1

#Assists attempts
    if arraysDict['P18EK'] in line:
      arraysDict['P18E_kills'] = arraysDict['P18E_kills'] + 1
    if arraysDict['P18EE'] in line:
      arraysDict['P18E_errors'] = arraysDict['P18E_errors'] + 1
    if arraysDict['P18EA'] in line:
      arraysDict['P18E_total'] = arraysDict['P18E_total'] + 1

#Receive attempts
    if arraysDict['P18RK'] in line:
      arraysDict['P18R_success'] = arraysDict['P18R_success'] + 1
    if arraysDict['P18RP'] in line:
      arraysDict['P18R_success'] = arraysDict['P18R_success'] + 1
    if arraysDict['P18RM'] in line:
      arraysDict['P18R_success'] = arraysDict['P18R_success'] + 1
    if arraysDict['P18RE'] in line:
      arraysDict['P18R_errors'] = arraysDict['P18R_errors'] + 1
    if arraysDict['P18RA'] in line:
      arraysDict['P18R_total'] = arraysDict['P18R_total'] + 1

#Block attempts
    if arraysDict['P18BK'] in line:
      arraysDict['P18B_success'] = arraysDict['P18B_success'] + 1
    if arraysDict['P18BE'] in line:
      arraysDict['P18B_errors'] = arraysDict['P18B_errors'] + 1
    if arraysDict['P18BA'] in line:
      arraysDict['P18B_total'] = arraysDict['P18B_total'] + 1

#Dig attempts
    if arraysDict['P18DK'] in line:
      arraysDict['P18D_success'] = arraysDict['P18D_success'] + 1
    if arraysDict['P18DP'] in line:
      arraysDict['P18D_success'] = arraysDict['P18D_success'] + 1
    if arraysDict['P18DM'] in line:
      arraysDict['P18D_success'] = arraysDict['P18D_success'] + 1
    if arraysDict['P18DE'] in line:
      arraysDict['P18D_errors'] = arraysDict['P18D_errors'] + 1
    if arraysDict['P18DA'] in line:
      arraysDict['P18D_total'] = arraysDict['P18D_total'] + 1

#21

#Attacks attempts
    if arraysDict['P21AK'] in line:
      arraysDict['P21A_kills'] = arraysDict['P21A_kills'] + 1
    if arraysDict['P21OK'] in line:
      arraysDict['P21A_kills'] = arraysDict['P21A_kills'] + 1
    if arraysDict['P21AE'] in line:
      arraysDict['P21A_errors'] = arraysDict['P21A_errors'] + 1
    if arraysDict['P21OE'] in line:
      arraysDict['P21A_errors'] = arraysDict['P21A_errors'] + 1
    if arraysDict['P21AA'] in line:
      arraysDict['P21A_total'] = arraysDict['P21A_total'] + 1

#Serve attempts
    if arraysDict['P21SK'] in line:
      arraysDict['P21S_aces'] = arraysDict['P21S_aces'] + 1
    if arraysDict['P21SE'] in line:
      arraysDict['P21S_errors'] = arraysDict['P21S_errors'] + 1
    if arraysDict['P21SA'] in line:
      arraysDict['P21S_total'] = arraysDict['P21S_total'] + 1

#Assists attempts
    if arraysDict['P21EK'] in line:
      arraysDict['P21E_kills'] = arraysDict['P21E_kills'] + 1
    if arraysDict['P21EE'] in line:
      arraysDict['P21E_errors'] = arraysDict['P21E_errors'] + 1
    if arraysDict['P21EA'] in line:
      arraysDict['P21E_total'] = arraysDict['P21E_total'] + 1

#Receive attempts
    if arraysDict['P21RK'] in line:
      arraysDict['P21R_success'] = arraysDict['P21R_success'] + 1
    if arraysDict['P21RP'] in line:
      arraysDict['P21R_success'] = arraysDict['P21R_success'] + 1
    if arraysDict['P21RM'] in line:
      arraysDict['P21R_success'] = arraysDict['P21R_success'] + 1
    if arraysDict['P21RE'] in line:
      arraysDict['P21R_errors'] = arraysDict['P21R_errors'] + 1
    if arraysDict['P21RA'] in line:
      arraysDict['P21R_total'] = arraysDict['P21R_total'] + 1

#Block attempts
    if arraysDict['P21BK'] in line:
      arraysDict['P21B_success'] = arraysDict['P21B_success'] + 1
    if arraysDict['P21BE'] in line:
      arraysDict['P21B_errors'] = arraysDict['P21B_errors'] + 1
    if arraysDict['P21BA'] in line:
      arraysDict['P21B_total'] = arraysDict['P21B_total'] + 1

#Dig attempts
    if arraysDict['P21DK'] in line:
      arraysDict['P21D_success'] = arraysDict['P21D_success'] + 1
    if arraysDict['P21DP'] in line:
      arraysDict['P21D_success'] = arraysDict['P21D_success'] + 1
    if arraysDict['P21DM'] in line:
      arraysDict['P21D_success'] = arraysDict['P21D_success'] + 1
    if arraysDict['P21DE'] in line:
      arraysDict['P21D_errors'] = arraysDict['P21D_errors'] + 1
    if arraysDict['P21DA'] in line:
      arraysDict['P21D_total'] = arraysDict['P21D_total'] + 1

#29

#Attacks attempts
    if arraysDict['P29AK'] in line:
      arraysDict['P29A_kills'] = arraysDict['P29A_kills'] + 1
    if arraysDict['P29OK'] in line:
      arraysDict['P29A_kills'] = arraysDict['P29A_kills'] + 1
    if arraysDict['P29AE'] in line:
      arraysDict['P29A_errors'] = arraysDict['P29A_errors'] + 1
    if arraysDict['P29OE'] in line:
      arraysDict['P29A_errors'] = arraysDict['P29A_errors'] + 1
    if arraysDict['P29AA'] in line:
      arraysDict['P29A_total'] = arraysDict['P29A_total'] + 1

#Serve attempts
    if arraysDict['P29SK'] in line:
      arraysDict['P29S_aces'] = arraysDict['P29S_aces'] + 1
    if arraysDict['P29SE'] in line:
      arraysDict['P29S_errors'] = arraysDict['P29S_errors'] + 1
    if arraysDict['P29SA'] in line:
      arraysDict['P29S_total'] = arraysDict['P29S_total'] + 1

#Assists attempts
    if arraysDict['P29EK'] in line:
      arraysDict['P29E_kills'] = arraysDict['P29E_kills'] + 1
    if arraysDict['P29EE'] in line:
      arraysDict['P29E_errors'] = arraysDict['P29E_errors'] + 1
    if arraysDict['P29EA'] in line:
      arraysDict['P29E_total'] = arraysDict['P29E_total'] + 1

#Receive attempts
    if arraysDict['P29RK'] in line:
      arraysDict['P29R_success'] = arraysDict['P29R_success'] + 1
    if arraysDict['P29RP'] in line:
      arraysDict['P29R_success'] = arraysDict['P29R_success'] + 1
    if arraysDict['P29RM'] in line:
      arraysDict['P29R_success'] = arraysDict['P29R_success'] + 1
    if arraysDict['P29RE'] in line:
      arraysDict['P29R_errors'] = arraysDict['P29R_errors'] + 1
    if arraysDict['P29RA'] in line:
      arraysDict['P29R_total'] = arraysDict['P29R_total'] + 1

#Block attempts
    if arraysDict['P29BK'] in line:
      arraysDict['P29B_success'] = arraysDict['P29B_success'] + 1
    if arraysDict['P29BE'] in line:
      arraysDict['P29B_errors'] = arraysDict['P29B_errors'] + 1
    if arraysDict['P29BA'] in line:
      arraysDict['P29B_total'] = arraysDict['P29B_total'] + 1

#Dig attempts
    if arraysDict['P29DK'] in line:
      arraysDict['P29D_success'] = arraysDict['P29D_success'] + 1
    if arraysDict['P29DP'] in line:
      arraysDict['P29D_success'] = arraysDict['P29D_success'] + 1
    if arraysDict['P29DM'] in line:
      arraysDict['P29D_success'] = arraysDict['P29D_success'] + 1
    if arraysDict['P29DE'] in line:
      arraysDict['P29D_errors'] = arraysDict['P29D_errors'] + 1
    if arraysDict['P29DA'] in line:
      arraysDict['P29D_total'] = arraysDict['P29D_total'] + 1


# players 2,3,4,5,6,7,9,10,11,13,16,18,21,29


arraysDict['P2_MGP']=3
arraysDict['P3_MGP']=3
arraysDict['P5_MGP']=3
arraysDict['P7_MGP']=3
arraysDict['P9_MGP']=3
arraysDict['P10_MGP']=3
arraysDict['P11_MGP']=3
arraysDict['P16_MGP']=3

arraysDict['P7S_points']=3
arraysDict['P10S_points']=11
arraysDict['P5S_points']=7
arraysDict['P3S_points']=10
arraysDict['P2S_points']=8
arraysDict['P9S_points']=0


print ("Jersey|MatchGamesPlayed|AttacksKills|AttacksErrors|AttacksAttempts|TotalServes|ServingAces|ServingErrors|ServingPoints|BallHandlingAttempts|Assists|AssistsErrors|ServingReceivedErrors|ServingReceivedSuccess|Digs|DigsErrors|BlocksSolo|BlocksAssists|BlockingErrors")
print (str(arraysDict['P2'])+'|'+str(arraysDict['P2_MGP'])+'|'+str(arraysDict['P2A_kills'])+'|'+str(arraysDict['P2A_errors'])+'|'+str(arraysDict['P2A_total'])+'|'+str(arraysDict['P2S_total'])+'|'+str(arraysDict['P2S_aces'])+'|'+str(arraysDict['P2S_errors'])+'|'+str(arraysDict['P2S_points'])+'|'+str(arraysDict['P2E_total'])+'|'+str(arraysDict['P2E_kills'])+'|'+str(arraysDict['P2E_errors'])+'|'+str(arraysDict['P2R_errors'])+'|'+str(arraysDict['P2R_success'])+'|'+str(arraysDict['P2D_total'])+'|'+str(arraysDict['P2D_errors'])+'|'+str(arraysDict['P2B_success'])+'|'+str(arraysDict['P2B_assists'])+'|'+str(arraysDict['P2B_errors'])  )

print (str(arraysDict['P3'])+'|'+str(arraysDict['P3_MGP'])+'|'+str(arraysDict['P3A_kills'])+'|'+str(arraysDict['P3A_errors'])+'|'+str(arraysDict['P3A_total'])+'|'+str(arraysDict['P3S_total'])+'|'+str(arraysDict['P3S_aces'])+'|'+str(arraysDict['P3S_errors'])+'|'+str(arraysDict['P3S_points'])+'|'+str(arraysDict['P3E_total'])+'|'+str(arraysDict['P3E_kills'])+'|'+str(arraysDict['P3E_errors'])+'|'+str(arraysDict['P3R_errors'])+'|'+str(arraysDict['P3R_success'])+'|'+str(arraysDict['P3D_total'])+'|'+str(arraysDict['P3D_errors'])+'|'+str(arraysDict['P3B_success'])+'|'+str(arraysDict['P3B_assists'])+'|'+str(arraysDict['P3B_errors'])  )

print (str(arraysDict['P5'])+'|'+str(arraysDict['P5_MGP'])+'|'+str(arraysDict['P5A_kills'])+'|'+str(arraysDict['P5A_errors'])+'|'+str(arraysDict['P5A_total'])+'|'+str(arraysDict['P5S_total'])+'|'+str(arraysDict['P5S_aces'])+'|'+str(arraysDict['P5S_errors'])+'|'+str(arraysDict['P5S_points'])+'|'+str(arraysDict['P5E_total'])+'|'+str(arraysDict['P5E_kills'])+'|'+str(arraysDict['P5E_errors'])+'|'+str(arraysDict['P5R_errors'])+'|'+str(arraysDict['P5R_success'])+'|'+str(arraysDict['P5D_total'])+'|'+str(arraysDict['P5D_errors'])+'|'+str(arraysDict['P5B_success'])+'|'+str(arraysDict['P5B_assists'])+'|'+str(arraysDict['P5B_errors'])  )

print (str(arraysDict['P7'])+'|'+str(arraysDict['P7_MGP'])+'|'+str(arraysDict['P7A_kills'])+'|'+str(arraysDict['P7A_errors'])+'|'+str(arraysDict['P7A_total'])+'|'+str(arraysDict['P7S_total'])+'|'+str(arraysDict['P7S_aces'])+'|'+str(arraysDict['P7S_errors'])+'|'+str(arraysDict['P7S_points'])+'|'+str(arraysDict['P7E_total'])+'|'+str(arraysDict['P7E_kills'])+'|'+str(arraysDict['P7E_errors'])+'|'+str(arraysDict['P7R_errors'])+'|'+str(arraysDict['P7R_success'])+'|'+str(arraysDict['P7D_total'])+'|'+str(arraysDict['P7D_errors'])+'|'+str(arraysDict['P7B_success'])+'|'+str(arraysDict['P7B_assists'])+'|'+str(arraysDict['P7B_errors'])  )

print (str(arraysDict['P9'])+'|'+str(arraysDict['P9_MGP'])+'|'+str(arraysDict['P9A_kills'])+'|'+str(arraysDict['P9A_errors'])+'|'+str(arraysDict['P9A_total'])+'|'+str(arraysDict['P9S_total'])+'|'+str(arraysDict['P9S_aces'])+'|'+str(arraysDict['P9S_errors'])+'|'+str(arraysDict['P9S_points'])+'|'+str(arraysDict['P9E_total'])+'|'+str(arraysDict['P9E_kills'])+'|'+str(arraysDict['P9E_errors'])+'|'+str(arraysDict['P9R_errors'])+'|'+str(arraysDict['P9R_success'])+'|'+str(arraysDict['P9D_total'])+'|'+str(arraysDict['P9D_errors'])+'|'+str(arraysDict['P9B_success'])+'|'+str(arraysDict['P9B_assists'])+'|'+str(arraysDict['P9B_errors'])  )

print (str(arraysDict['P10'])+'|'+str(arraysDict['P10_MGP'])+'|'+str(arraysDict['P10A_kills'])+'|'+str(arraysDict['P10A_errors'])+'|'+str(arraysDict['P10A_total'])+'|'+str(arraysDict['P10S_total'])+'|'+str(arraysDict['P10S_aces'])+'|'+str(arraysDict['P10S_errors'])+'|'+str(arraysDict['P10S_points'])+'|'+str(arraysDict['P10E_total'])+'|'+str(arraysDict['P10E_kills'])+'|'+str(arraysDict['P10E_errors'])+'|'+str(arraysDict['P10R_errors'])+'|'+str(arraysDict['P10R_success'])+'|'+str(arraysDict['P10D_total'])+'|'+str(arraysDict['P10D_errors'])+'|'+str(arraysDict['P10B_success'])+'|'+str(arraysDict['P10B_assists'])+'|'+str(arraysDict['P10B_errors'])  )

print (str(arraysDict['P11'])+'|'+str(arraysDict['P11_MGP'])+'|'+str(arraysDict['P11A_kills'])+'|'+str(arraysDict['P11A_errors'])+'|'+str(arraysDict['P11A_total'])+'|'+str(arraysDict['P11S_total'])+'|'+str(arraysDict['P11S_aces'])+'|'+str(arraysDict['P11S_errors'])+'|'+str(arraysDict['P11S_points'])+'|'+str(arraysDict['P11E_total'])+'|'+str(arraysDict['P11E_kills'])+'|'+str(arraysDict['P11E_errors'])+'|'+str(arraysDict['P11R_errors'])+'|'+str(arraysDict['P11R_success'])+'|'+str(arraysDict['P11D_total'])+'|'+str(arraysDict['P11D_errors'])+'|'+str(arraysDict['P11B_success'])+'|'+str(arraysDict['P11B_assists'])+'|'+str(arraysDict['P11B_errors'])  )

print (str(arraysDict['P16'])+'|'+str(arraysDict['P16_MGP'])+'|'+str(arraysDict['P16A_kills'])+'|'+str(arraysDict['P16A_errors'])+'|'+str(arraysDict['P16A_total'])+'|'+str(arraysDict['P16S_total'])+'|'+str(arraysDict['P16S_aces'])+'|'+str(arraysDict['P16S_errors'])+'|'+str(arraysDict['P16S_points'])+'|'+str(arraysDict['P16E_total'])+'|'+str(arraysDict['P16E_kills'])+'|'+str(arraysDict['P16E_errors'])+'|'+str(arraysDict['P16R_errors'])+'|'+str(arraysDict['P16R_success'])+'|'+str(arraysDict['P16D_total'])+'|'+str(arraysDict['P16D_errors'])+'|'+str(arraysDict['P16B_success'])+'|'+str(arraysDict['P16B_assists'])+'|'+str(arraysDict['P16B_errors'])  )
