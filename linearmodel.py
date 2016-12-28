import pandas as pd
read=pd.read_csv('gurgaon.csv')
read1=pd.read_csv('mapping.csv')
print (len(read))
nod=35

def zero(z):
    if(z==0):
        return 1
    else :
        return z
df = pd.DataFrame(columns=('PID','Product', 'CD','Type'))

uproduct=read['Product'].unique()

  
for i in range(1,len(uproduct)):
    
    print (i)
    
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
    ic=read1['IC'][:1]
    
    print (ic)
    df.loc[i]=[int(pid[0]),product,cd,type]
df.to_csv("new.csv",sep=',')
print ('done')               
        
    
        
        
    
    