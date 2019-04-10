import math
import matplotlib.pyplot as plt

print ("Welcome to the Shape Identifier Program!")
print ("")

coordNumber = input ("Will you be entering 3 or 4 co-ordinates? (Please enter an integer response) ")
print ("")

while coordNumber == "3" or "4":
    
    if coordNumber == "3":
        threeInputXOne = int(input ("Please enter the x value of the first co-ordinate "))
        threeInputYOne = int(input ("Please enter the y value of the first co-ordinate "))
        print ("")
        threeInputXTwo = int(input ("Please enter the x value of the second co-ordinate "))
        threeInputYTwo = int(input ("Please enter the y value of the second co-ordinate "))
        print ("")
        threeInputXThree = int(input ("Please enter the x value of the third co-ordinate "))
        threeInputYThree = int(input ("Please enter the y value of the third co-ordinate "))
        print ("")
        
        print ("Here are the co-ordinates you have entered:")
        print ("1: (",threeInputXOne,",",threeInputYOne,")")
        print ("2: (",threeInputXTwo,",",threeInputYTwo,")")
        print ("3: (",threeInputXThree,",",threeInputYThree,")")
        print ("")

        print ("In vector format they are:")
        print ("1: ",threeInputXOne,"i + ",threeInputYOne,"j")
        print ("2: ",threeInputXTwo,"i + ",threeInputYTwo,"j")
        print ("3: ",threeInputXThree,"i + ",threeInputYThree,"j")
        print ("")
        print ("This shape is a triangle!")
        
        break
    
    elif coordNumber == "4":
        fourInputXOne = int(input ("Please enter the x value of the first co-ordinate "))
        fourInputYOne = int(input ("Please enter the y value of the first co-ordinate "))
        print ("")
        fourInputXTwo = int(input ("Please enter the x value of the second co-ordinate "))
        fourInputYTwo = int(input ("Please enter the y value of the second co-ordinate "))
        print ("")
        fourInputXThree = int(input ("Please enter the x value of the third co-ordinate "))
        fourInputYThree = int(input ("Please enter the y value of the third co-ordinate "))
        print ("")
        fourInputXFour = int(input ("Please enter the x value of the fourth co-ordinate "))
        fourInputYFour = int(input ("Please enter the y value of the fourth co-ordinate "))
        print ("")

        print ("Here are the co-ordinates you have entered:")
        print ("1: (",fourInputXOne,",",fourInputYOne,")")
        print ("2: (",fourInputXTwo,",",fourInputYTwo,")")
        print ("3: (",fourInputXThree,",",fourInputYThree,")")
        print ("4: (",fourInputXFour,",",fourInputYFour,")")

        print ("")
        print ("In vector format they are:")
        print ("1: ",fourInputXOne,"i + ",fourInputYOne,"j")
        print ("2: ",fourInputXTwo,"i + ",fourInputYTwo,"j")
        print ("3: ",fourInputXThree,"i + ",fourInputYThree,"j")
        print ("4: ",fourInputXFour,"i + ",fourInputYFour,"j")
        print ("")

        sideOneLength = math.sqrt((fourInputXTwo-fourInputXOne)**2 + (fourInputYTwo-fourInputYOne)**2 )
        sideTwoLength = math.sqrt((fourInputXThree-fourInputXTwo)**2 + (fourInputYThree-fourInputYTwo)**2 )
        sideThreeLength = math.sqrt((fourInputXFour-fourInputXThree)**2 + (fourInputYFour-fourInputYThree)**2 )
        sideFourLength = math.sqrt((fourInputXOne-fourInputXFour)**2 + (fourInputYOne-fourInputYFour)**2 )

        AOneFirstVectI = fourInputXOne-fourInputXFour
        AOneFirstVectJ = fourInputYOne-fourInputYFour
        AOneSecondVectI = fourInputXOne-fourInputXTwo
        AOneSecondVectJ = fourInputYOne-fourInputYTwo

        ATwoFirstVectI = fourInputXTwo-fourInputXOne
        ATwoFirstVectJ = fourInputYTwo-fourInputYOne
        ATwoSecondVectI = fourInputXTwo-fourInputXThree
        ATwoSecondVectJ = fourInputYTwo-fourInputYThree

        AThreeFirstVectI = fourInputXThree-fourInputXTwo
        AThreeFirstVectJ = fourInputYThree-fourInputYTwo
        AThreeSecondVectI = fourInputXThree-fourInputXFour
        AThreeSecondVectJ = fourInputYThree-fourInputYFour

        AFourFirstVectI = fourInputXFour-fourInputXThree
        AFourFirstVectJ = fourInputYFour-fourInputYThree
        AFourSecondVectI = fourInputXFour-fourInputXOne
        AFourSecondVectJ = fourInputYFour-fourInputYOne

        AOneMagOne = math.sqrt((AOneFirstVectI)**2 + (AOneFirstVectJ)**2 )
        AOneMagTwo = math.sqrt((AOneSecondVectI)**2 + (AOneSecondVectJ)**2 )
        AOneDotProduct = AOneFirstVectI*AOneSecondVectI + AOneFirstVectJ*AOneSecondVectJ
        AngleOne = (math.acos(AOneDotProduct/(AOneMagOne*AOneMagTwo))*180)/math.pi

        ATwoMagOne = math.sqrt((ATwoFirstVectI)**2 + (ATwoFirstVectJ)**2 )
        ATwoMagTwo = math.sqrt((ATwoSecondVectI)**2 + (ATwoSecondVectJ)**2 )
        ATwoDotProduct = ATwoFirstVectI*ATwoSecondVectI + ATwoFirstVectJ*ATwoSecondVectJ
        AngleTwo = (math.acos(ATwoDotProduct/(ATwoMagOne*ATwoMagTwo))*180)/math.pi

        AThreeMagOne = math.sqrt((AThreeFirstVectI)**2 + (AThreeFirstVectJ)**2 )
        AThreeMagTwo = math.sqrt((AThreeSecondVectI)**2 + (AThreeSecondVectJ)**2 )
        AThreeDotProduct = AThreeFirstVectI*AThreeSecondVectI + AThreeFirstVectJ*AThreeSecondVectJ
        AngleThree = (math.acos(AThreeDotProduct/(AThreeMagOne*AThreeMagTwo))*180)/math.pi

        AFourMagOne = math.sqrt((AFourFirstVectI)**2 + (AFourFirstVectJ)**2 )
        AFourMagTwo = math.sqrt((AFourSecondVectI)**2 + (AFourSecondVectJ)**2 )
        AFourDotProduct = AFourFirstVectI*AFourSecondVectI + AFourFirstVectJ*AFourSecondVectJ
        AngleFour = (math.acos(AFourDotProduct/(AFourMagOne*AFourMagTwo))*180)/math.pi

        print ("The angle sizes are:")
        print ("Angle 1: ",AngleOne)
        print ("Angle 2: ",AngleTwo)
        print ("Angle 3: ",AngleThree)
        print ("Angle 4: ",AngleFour)
        print ("")

        print ("The lengths of each side are:")
        print ("Length 1: ",sideOneLength)
        print ("Length 2: ",sideTwoLength)
        print ("Length 3: ",sideThreeLength)
        print ("Length 4: ",sideFourLength)
        print ("")

        if AngleOne == AngleTwo == AngleThree == AngleFour:
            if sideOneLength == sideTwoLength == sideThreeLength == sideFourLength:
                print ("This shape is a square")
            else:
                print ("This shape is a rectangle")
        else:
            print ("This shape is neither a square triangle or rectangle")

        print ("")

        UserXCoord = [fourInputXOne, fourInputXTwo, fourInputXThree, fourInputXFour]
        UserYCoord = [fourInputYOne, fourInputYTwo, fourInputYThree, fourInputYFour]
        plt.plot(UserXCoord, UserYCoord)
        plt.show()
        
        break
    else:
        print ("Please try again")
        coordNumber = input ("Will you be entering 3 or 4 co-ordinates? ")




        
    
