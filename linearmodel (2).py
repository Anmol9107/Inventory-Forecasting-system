import pandas as pd
read=pd.read_csv('gurgaon.csv')

nod=35

def zero(z):
    if(z==0):
        return 1
    else :
        return z
df = pd.DataFrame(columns=('PID','Product','CD','Type'))
df2 = pd.DataFrame(columns=('Product','MRP','SellingPrice','Quantity','Offer','Multiplier','Qty Sold','GrossGmv','NetGmv','Discount','CD','Bump to C/d','Type of Offer'))

uproduct=read['Product'].unique()

o=""
mul=1 
for i in range(0,len(uproduct)):
    break
    print (i)
    if(i==100):
        break
    #Productwise
    product=uproduct[i]
   
        
        
    
    
    pid=read[read['Product']==product]['PID'].unique()
    
    filter1 =read[read['Product']==product]
    nsalep=zero(filter1['Delivered On'].nunique())
    asalep=filter1['Quantity of Items Sold'].sum()
    cdp=asalep/nsalep
    
    
    #Subcat+mrp+product
    subcat=read['sub-Category'][i]
    mrp=read['MRP'][i]
    brand=read['Brand'][i]
    c1=read['sub-Category']==subcat
    c2=read['MRP']==mrp
    c3=read['Brand']==brand
    filter2=read[c1 & c2 & c3]
    nsaleall=zero(filter2['Delivered On'].nunique())
    asaleall=filter2['Quantity of Items Sold'].sum()
    cdall=asaleall/nsaleall
    
    #Anytwo
    
    count=3
    filter3=read[c1 & c2]
    nsale1=zero(filter3['Delivered On'].nunique())
    asale1=filter3['Quantity of Items Sold'].sum()
    if(nsale1<5):
        asale1=0
        count-=1
    cd1=asale1/nsale1
    filter4=read[c1 & c3]
    nsale2=zero(filter4['Delivered On'].nunique())
    asale2=filter4['Quantity of Items Sold'].sum()
    if(nsale2<5):
        asale2=0
        count-=1
    cd2=asale2/nsale2   
    filter5=read[c2 & c3]
    nsale3=zero(filter5['Delivered On'].nunique())
    asale3=filter5['Quantity of Items Sold'].sum()
    if(nsale3<5):
        asale3=0
        count-=1
        
    count=zero(count)
    cd3=asale3/nsale3
    cdtwo=(cd1+cd2+cd3)/count 
    nsaletwo=nsale1+nsale2+nsale3  
    if(nsalep>5):
        cd=cdp*1.1423
        type="Productwise"
    elif(nsalep<=5 and nsaleall>5):
        cd=cdall*0.0743
        type="Subcat+mrp+brand"
    elif (nsalep<=5 and nsaleall<=5 and nsaletwo>5):
        cd=cdtwo*0.021
        type="any two"
    else:
        cd="error"
        type="error"
    df.loc[i]=[int(pid[0]),product,cd,type]
#df.to_csv("newmod.csv",sep=',')
    
read1=pd.read_csv("new.csv")
mrpall=read['MRP']
spall=read['Selling Price']
qall=read['Quantity of Items Sold']
productall=read['Product']


for i in range(1,len(read)):
    
    mrp=mrpall[i]
    sp=spall[i]
    q=qall[i]
    product=productall[i]
    cd=read1[read1['Product']==product]['CD'].unique()
    if(len(cd)==0 or cd=='error'):
        cd=0
    else:
        cd=cd[0]
    offer=product.split("-")
    b=offer[1].split()
    if(b[0]=="Buy" and len(offer[1])<=22):
        o=offer[1]
        if(b[3]=="Get"):
            b[3]=b[4]
        
            
        o="B"+b[1]+"G"+b[3]
        print(i)
        mul=int(b[1])+int(b[3])
    
    
        
    gmv=mul*mrp*q
    netgmv=mul*sp*q
    d=((gmv-netgmv)/gmv)*100
    qs=mul*q
    bcd=float(cd)/float(qs)
    if(o==""):
        if(d<=5):
            tof="0-5"
        elif(d>=6 and d<=15):
            tof="6-15"
        elif(d>=26 and d<=35):
            tof="26-35"
    else :
        tof=o
    df2.loc[i]=[product,mrp,sp,q,o,mul,qs,gmv,netgmv,d,cd,bcd,tof]
 
    
        
    
    
 
df2.to_csv("gmv.csv",sep=',')    

print ('done')               
        
    
        
        
    
    