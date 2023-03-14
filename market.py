print("\t\t\t\t\tsuperMarket Billing system")
total=0
prlst=[]
v=int(input("enter number of products"))
usernm=input("enter user name")
for i in range(v):
  prnm=input("enter product name")
  amt=int(input("enter amount"))
  qty=int(input("enter quantity"))
  prlst.append([prnm,amt,qty])
  total=qty*amt
  print("product name\tamount\tquantity total")
  print(prnm,"\t\t",amt,"\t",qty,"\t",total)
  prlst.append(total)
