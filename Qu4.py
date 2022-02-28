xyz=open('people.txt','r')
for i in xyz:
    if "delhi" in i:
        a=open("delhi.txt","a")
        a.write(i)
        a.close()
    elif "shimla" in i :
        b=open("shimal","a")
        b.write(i)
        b.close()
    else:
        c=open("other","a")
        c.write(i)
        c.close()

        

