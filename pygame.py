s=input("input: ").split(':')
s=list(s)
a=int(s[0])
b=int(s[1])
if 0<= a <=23 and 0<=b <= 59:
    if a>= 12:
        a = a - 12      # analog clock has only 12 segments if than or equal to 12, we subtract 12 from that
    else:
        a = a
    d = (a * 30 + b * 0.5)   # angle covered hour hand from mean position
    e = (6 * b)  # angle covered minute hand from mean position
    x = d-e   # difference between two angle covered by two hand in same time.
    if x<0:
        x = -x
    else:
        x = x
    if x > 180:
        x = 360 - x
    else:
        x = x
    c=chr(176)
    print("output: %.0f%c"%(x,c))
else:
    print("Enter valid time")                            
