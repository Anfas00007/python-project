import csv
import pandas
import matplotlib.pyplot as plt
print("EXPENSE CALC")
ch=0
while(ch!=4):
    print("1.ADD EXPENSE : \n2.load data \n3.visualize \n4.exit")
    ch=int(input("enter the choice :"))
    if(ch==1):
        cat=input("Enter the category : ")
        amount=int(input("Enter the amount : "))
        date1=input("Enter the date : ")
        try:
            file=open("expenses.csv",'r')
            file.close()
        except:
            file=open("expenses.csv",mode='w',newline='')
            writer=csv.writer(file)
            writer.writerow(["category","amount","date"])
            file.close()
        row=[cat,amount,date1]
        file=open("expenses.csv",'a')
        writer=csv.writer(file)
        writer.writerow(row)
        file.close()
    if(ch==2):
        pd=pandas.read_csv("expenses.csv")
        print(pd.tail(10))
        sum=0
        for i in pd["amount"]:
            sum=sum+i
        print("total = ",sum)
    if(ch==3):
        pd=pandas.read_csv("expenses.csv")
        print("1.catogorey vs amonut")
        print("2.date vs amount")
        x=input("enter the type")
        
        if(x=="1"):

         show=pd.groupby("category")["amount"].sum()
         show.plot(kind="bar", figsize=(8, 6), title="Expenses by Category")
         plt.xlabel("Category")
         plt.ylabel("Total Amount")
         plt.show()
        if(x=="2"):
         show1=pd.groupby("date")["amount"].sum()
         show1.plot(kind="bar", figsize=(8, 6), title="Expenses by date")
         plt.xlabel("date")
         plt.ylabel("Total Amount")
         plt.show()
