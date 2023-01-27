import mysql.connector
from tabulate import tabulate
database=mysql.connector.connect(host='localhost',user='root',passwd='password',database='supermarket')
if database.is_connected():
    print("Marginfree Supermarket")
print("")
l1=l2=l3=1
cursor=database.cursor()
cursor.execute("delete from temp")
database.commit()
k1='no'
while l1:
    k2='yes'
    if k1=="yes" or k1=="Yes" or k1=="YES":
        print("Thank you for shopping with us")
        break
    else:
        cursor=database.cursor()
        cursor.execute("select code,item,category,mrp,stocks from items")
        fulldata=cursor.fetchall()
        length=len(fulldata)
        print("Press 1 for purchasing items")
        print("Press 2 for administrator login")
        print("")
        o1=int(input("Enter choice: "))
        if o1==1:
            print(tabulate(fulldata,headers=['Item Code','Item','Category','MRP'],tablefmt='psql'))
            while l2:
                if k2=="yes" or k1=="Yes" or k1=="YES":
                    print("")
                    buy1=int(input("Enter code of item you wish to buy: "))
                    qty1=int(input("Enter number of item(s) you wish to purchase: "))
                    for c1 in range(0,length+1):
                        temp1=fulldata[c1]
                        if temp1[0]==buy1 and temp1[4]>=qty1:
                             u=temp1[0]
                             v=temp1[1]
                             w=temp1[2]
                             x=temp1[3]
                             y=qty1
                             z=x*y
                             add="insert into temp values({},'{}','{}',{},{},{})".format(u,v,w,x,y,z)
                             cursor.execute(add)
                             database.commit()
                             add2="update sales set sale=sale+{} where code={}".format(qty1,buy1)
                             cursor.execute(add2)
                             database.commit()
                             add3="update items set stocks=stocks-{} where code={}".format(qty1,buy1)
                             cursor.execute(add3)
                             database.commit()
                             break
                        elif temp1[4]<qty1:
                            print("Only "+str(temp1[4])+" "+temp1[1]+"(s)"+" are left")
                            break
                        else:
                             continue
                    k2=input("Do you wish to purchase more items: ")
                else:
                    print("")
                    cursor.execute("select code,item,category,mrp,quantity,amount from temp")
                    data2=cursor.fetchall()
                    database.commit()
                    cursor.execute("select sum(amount) from temp")
                    data3=cursor.fetchone()
                    database.commit()
                    total=data3[0]
                    print(tabulate(data2,headers=['Item Code','Item','Category','MRP','Quantity','Amount'],tablefmt='psql'))
                    print("")
                    print("Total amount: Rs."+str(total))
                    break
        elif o1==2:
            passw=input("Enter login password: ")
            if passw!="password":
                print("Incorrect password")
                
            if passw=="password":
                cursor.execute("select code,item,category,mrp,stocks from items")
                fulldata=cursor.fetchall()
                length=len(fulldata)
                print(tabulate(fulldata,headers=['Item Code','Item','Category','MRP','Stock remaining'],tablefmt='psql'))
                cursor.execute("select code,item,category,mrp,sale,mrp*sale from sales")
                salesdata=cursor.fetchall()
                print(tabulate(salesdata,headers=['Item Code','Item','Category','MRP','Sales','Amount'],tablefmt='psql'))
                print("1. Enter new item")
                print("2. Modify existing item")
                print("3. Delete item")
                print("4. Exit")
                o2=int(input("Enter choice: "))
                if o2==1:
                    u1=int(input("Enter code of item: "))
                    v1=input("Enter name of item: ")
                    w1=input("Enter category of item: ")
                    x1=float(input("Enter MRP of item: "))
                    y1=int(input("Enter stock of item: "))
                    add4="insert into items values ({},'{}','{}',{},{})".format(u1,v1,w1,x1,y1)
                    cursor.execute(add4)
                    database.commit()
                    add5="insert into sales values ({},'{}','{}',{},0)".format(u1,v1,w1,x1)
                    cursor.execute(add5)
                    database.commit()
                    print("")
                    print("Changes saved")
                    cursor.execute("select code,item,category,mrp,stocks from items")
                    fulldata=cursor.fetchall()
                    print(tabulate(fulldata,headers=['Item Code','Item','Category','MRP','Stock remaining'],tablefmt='psql'))
                    database.commit()
                    print("")
                    cursor.execute("select code,item,category,mrp,sale,mrp*sale from sales")
                    salesdata=cursor.fetchall()
                    print(tabulate(salesdata,headers=['Item Code','Item','Category','MRP','Sales','Amount'],tablefmt='psql'))
                    database.commit()
                    
                elif o2==2:
                    modify=int(input("Enter code of item to modify: "))
                    u2=int(input("Enter code of item: "))
                    v2=input("Enter name of item: ")
                    w2=input("Enter category of item: ")
                    x2=float(input("Enter MRP of item: "))
                    y2=int(input("Enter stock of item: "))
                    modify1="update items set code={},item='{}',category='{}',mrp={},stocks={} where code={}".format(u2,v2,w2,x2,y2,modify)
                    cursor.execute(modify1)
                    database.commit()
                    modify2="update sales set code={},item='{}',category='{}',mrp={} where code={}".format(u2,v2,w2,x2,modify)
                    cursor.execute(modify2)
                    database.commit()
                    print("")
                    print("Changes saved")
                    cursor.execute("select code,item,category,mrp,stocks from items")
                    fulldata=cursor.fetchall()
                    print(tabulate(fulldata,headers=['Item Code','Item','Category','MRP','Stock remaining'],tablefmt='psql'))
                    database.commit()
                    cursor.execute("select code,item,category,mrp,sale,mrp*sale from sales")
                    print("")
                    salesdata=cursor.fetchall()
                    print(tabulate(salesdata,headers=['Item Code','Item','Category','MRP','Sales','Amount'],tablefmt='psql'))
                    database.commit()
                elif o2==3:
                    delete1=int(input("Enter code of item to delete: "))
                    delete2="delete from items where code={}".format(delete1)
                    delete3="delete from sales where code={}".format(delete1)
                    cursor.execute(delete2)
                    database.commit()
                    cursor.execute(delete3)
                    database.commit()
                    print("")
                    print("Changes saved")
                    cursor.execute("select code,item,category,mrp,stocks from items")
                    fulldata=cursor.fetchall()
                    print(tabulate(fulldata,headers=['Item Code','Item','Category','MRP','Stock remaining'],tablefmt='psql'))
                    database.commit()
                    cursor.execute("select code,item,category,mrp,sale,mrp*sale from sales")
                    print("")
                    salesdata=cursor.fetchall()
                    print(tabulate(salesdata,headers=['Item Code','Item','Category','MRP','Sales','Amount'],tablefmt='psql'))
                    database.commit()
                else:
                    break
        print("")
        k1=input("Do you want to exit?: ")
cursor.execute("delete from temp")
database.commit()
database.close()
last = input()
        
                    
                    
            
