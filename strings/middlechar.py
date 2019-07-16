'''Given a string of odd length greater 7, return a string made of the middle three chars of a given String'''

def getthreemiddlechar(samplestr):
    middleindex = int(len(samplestr)/2)
    print("The original string is ", samplestr)
    middlethreechar = samplestr[middleindex-1:middleindex+2]
    print("The middle three chars are :", middlethreechar)
    
getthreemiddlechar("structure")
getthreemiddlechar("python")
getthreemiddlechar("kajendran")
