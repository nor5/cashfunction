"""
bill function that retourn change:
the most minimal amount of bills possible  (2 , 5 or 10 ) or a -1 if it is not possible
"""
def bill (cash ):
    r10 = (cash -( cash // 10)*10)
    if cash % 10 == 0:
        return { "ten": cash/10,
                 "five": 0,
                 "two": 0
                 }
    elif cash % 10 !=0 and r10 % 5 == 0:
        return { "ten": cash//10,
                 "five": r10/5,
                 "two": 0
                 }
    elif cash % 10 !=0 and r10 % 5 != 0 and (r10 - (r10//5)*5) % 2 == 0 :
      
        return { "ten": cash//10,
                 "five": (cash -( cash // 10)*10)//5,
                 "two": (r10 - (r10//5)*5) / 2
                 }
    
    elif cash % 10 !=0 and r10 % 5 != 0 and (r10 - (r10//5)*5) % 2 != 0 and r10 % 2 == 0 :
        
         return { "ten": cash//10,
                 "five":0,
                 "two":  r10/2
                 }
    elif cash % 5 == 0:
        return { "ten": 0,
                 "five": cash /5,
                 "two": 0
                 }
    elif cash % 5 !=0 and (cash -( cash // 5)*5) % 2 == 0:
        return { "ten": 0,
                 "five": cash//5,
                 "two": (cash -( cash // 5)*5)/2
                 }
    elif cash % 2 == 0:
        return { "ten": 0,
                 "five": 0,
                 "two": cash /2
                
                 }
    else:
        return -1



print(bill(48))
