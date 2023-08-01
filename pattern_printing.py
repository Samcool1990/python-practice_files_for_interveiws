for i in range(4):
    for j in range(4):
        print("#",end="")
    print()
####
####
####
####

for i in range(4):
    for j in range(i,4):
        print("#",end='')
    print()
####
###
##
#

for i in range(4):
    for j in range(i+1):
        print("#",end='')
    print()
#
##
###
####


for i in range(4):
    for j in range(i,4):
        print(" ",end="")
    
    for j in range(i+1):
        print("#",end="")

    print()
    #
   ##
  ###
 ####

for i in range(4):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,4):
        print("#",end="")     

    print()

####
 ###
  ##
   #

for i in range(4):
    for j in range(i,4):
        print(" ",end="")
    
    for j in range(i):
        print("#",end="")

    for j in range(i+1):
        print("#",end="")

    print()
    #
   ###
  #####
 #######

for i in range(4):
    for j in range(i+1):
        print(" ",end="")
    
    for j in range(i,4-1):
        print("#",end="")

    for j in range(i,4):
        print("#",end="")

    print()
   #######
    #####
     ###
      #

for i in range(4 - 1):
    for j in range(i,4):
        print(" ",end="")
    
    for j in range(i):
        print("#",end="")

    for j in range(i+1):
        print("#",end="")

    print()
for i in range(4):
    for j in range(i+1):
        print(" ",end="")
    
    for j in range(i,4-1):
        print("#",end="")

    for j in range(i,4):
        print("#",end="")

    print()

    #
   ###
  #####
 #######
  #####
   ###
    #