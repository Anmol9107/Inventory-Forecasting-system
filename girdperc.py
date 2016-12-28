# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 08:32:49 2016

@author: Gaurav
"""

# If you want to add or remove any discout category just add it in 'of' array as well as increase the column head

import pandas as pd
from tkinter import filedialog

def zero(z):
    if(z==0):
        return 1
    else :
        return z
        
file=filedialog.askopenfilename(title="Choose Gmv file calculated in previous step")
read=pd.read_csv(file,encoding="ISO-8859-1") #Change encoding accordingly
f=file.split("/")
fout=""
for i in range(0,len(f)-1):
    fout=fout+f[i]+"/"
fout=fout+"gridsubcatper.csv"
o={}
of={}

c={}
n1={}
n2={}
base={}
count=0

n=read['Offer']
num=n.nunique()
p=n.unique()

#of[13]="B1G2"
#of[12]="B1G1"
#of[11]="B2G3"
#of[10]=">35"
#of[9]="B2G1"
#of[8]="26-35"
#of[7]="16-25"
#of[6]="B3G1"
#of[5]="B4G2"
#of[4]="6-15"
#of[3]="B4G1"
#of[2]="B5G1"
#of[1]="B6G1"
of[0]="0-5"
of[1]="6-15"
of[2]="16-25"
of[3]="26-35"
of[4]=">35"
val=1.05 
for i in range (0,len(of)):
    o[i]=read['Type of Offer']==of[i]
    base[i]=val
    val+=0.05
   
a=""

df=pd.DataFrame(columns=('Sub-Category','MRP Range','Type','Category','0-5','B6G1','B5G1','B4G1','6-15','B4G2','B3G1','16-25','26-35','B2G1','>35','B2G3','B1G1','B1G2','mul','min','Category-type'))

n1=read['Sub-Category'].unique()

#cond1=read['CD']>5
co=read['Bump to C/d']>1
n2[1]="medium"
n2[0]="cheap"
n2[2]="expensive"
c[1]=read['Costtype']=="medium"
c[0]=read['Costtype']=="cheap"
c[2]=read['Costtype']=="expensive"
for i in range(0,len(n1)):
    
    b=""
    s=n1[i]
    d=read['Sub-Category']==s
    b=read[d]['Category'].unique()
    if(len(b)!=0):
        b=b[0]
        
    
    #if(len(b)!=0):
        #b=b[0]
    
        
    
    for j in range(0,len(n2)):
        name=str(n1[i])+"-"+n2[j]
        df.loc[count,'Type']=name
        df.loc[count,'Sub-Category']=n1[i]
        df.loc[count,'Category']=b
        
        df.loc[count,'MRP Range']=n2[j]
        for z in range(0,len(of)):
            #oe="o"+str(z)
           
           
           
            sum=read[(o[z]) & (d ) & (c[j]) & (co) ]['Bump to C/d'].sum()
            n=read[(o[z]) & (d)  & (c[j]) & (co )]['Bump to C/d'].count()
            
            #a[z-1]=(sum/zero(n))
            df.loc[count,of[z]]=(sum/zero(n))
            #[name,a[0],a[1],a[2],a[3]]
        d=0
        min=1000
        countd=0
        ar={}
        for ab in range(0,len(of)):
            ar[ab]=df[of[ab]][count]
            value=ar[ab]
            if(value!=0):
                if(min>=value):
                    min=value
        
                
                    
            
                    
        
        df.loc[count,'min']=min
        count+=1
          
df.to_csv('grid1.csv',sep=',')
reada=pd.read_csv('grid1.csv')


for i in range(0,len(reada)):
    countd=0
    
    d=0
    for j in range(0,len(of)-1):
        value=reada[of[j]][i]
        if(value!=0):
            for k in range(j+1,len(of)):
                value1=reada[of[k]][i]
                if(value1!=0):
                    
                    d=float(abs((value-value1)/(k-j)))
                    countd+=1

    if(countd!=0):
        d=d/countd
        
    reada.loc[i,'mul']=d
    reada.loc[i,'Category-type']="Genuine"
        
   

for i in range(0,len(reada)):
    mul=reada['mul'][i]
    min=reada['min'][i]
    subcat=reada['Sub-Category'][i]
    mrange=reada['MRP Range'][i]
    if(mul==0.0):
        
        mins=reada[(reada['Sub-Category']==subcat) & (reada['mul']>0.0)]['min'].sum()
        minc=reada[(reada['Sub-Category']==subcat) & (reada['mul']>0.0)]['min'].count()
        min=float(mins/zero(minc))
        
        
        muls=reada[(reada['Sub-Category']==subcat) & (reada['mul']>0.0)]['mul'].sum()
        mulc=reada[(reada['Sub-Category']==subcat) & (reada['mul']>0.0)]['mul'].count()  
        mul=float(muls/zero(mulc))
        reada.loc[i,'mul']=mul
        reada.loc[i,'min']=min
        reada.loc[i,'Category-type']="Subcat"
        
    
for i in range(0,len(reada)):
    mul=reada['mul'][i]
    min=reada['min'][i]
    subcat=reada['Sub-Category'][i]
    cat=reada['Category'][i]
    mrange=reada['MRP Range'][i]
    if(mul==0.0):
        
        mins=reada[(reada['Category']==cat) & (reada['mul']>0.0)& (reada['MRP Range']==mrange)]['min'].sum()
        minc=reada[(reada['Category']==cat) & (reada['mul']>0.0)& (reada['MRP Range']==mrange)]['min'].count()
        min=float(mins/zero(minc))
        
        
        muls=reada[(reada['Category']==cat) & (reada['mul']>0.0)& (reada['MRP Range']==mrange)]['mul'].sum()
        mulc=reada[(reada['Category']==cat) & (reada['mul']>0.0)& (reada['MRP Range']==mrange)]['mul'].count()  
        mul=float(muls/zero(mulc))
        reada.loc[i,'mul']=mul
        reada.loc[i,'min']=min
        reada.loc[i,'Category-type']="Cat-Mrp"
          

for i in range(0,len(reada)):
    mul=reada['mul'][i]
    min=reada['min'][i]
    subcat=reada['Sub-Category'][i]
    mrange=reada['MRP Range'][i]
    cat=reada['Category'][i]
   
    
    if(mul==0.0):
        mins=reada[(reada['Category']==cat) & (reada['mul']>0.0)]['min'].sum()
        minc=reada[(reada['Category']==cat) & (reada['mul']>0.0)]['min'].count()
        min=float(mins/zero(minc))
        
        print(min)
        mul=reada[(reada['Category']==cat) & (reada['mul']>0.0)]['mul'].sum()
        mulc=reada[(reada['Sub-Category']==subcat) & (reada['mul']>0.0)]['mul'].count()  
        mul=float(muls/zero(mulc))
        reada.loc[i,'mul']=mul
        reada.loc[i,'min']=min
        cat="Cat"
        reada.loc[i,'Category-type']=cat
   

for i in range(0,len(reada)):
    mul=reada['mul'][i]
    min=reada['min'][i]
    subcat=reada['Sub-Category'][i]
    mrange=reada['MRP Range'][i]
    
   
    
    if(mul==0.0):
        min=reada[(reada['MRP Range']==mrange) & (reada['mul']>0.0)]['min'].mean()
        #minc=reada[(reada['MRP Range']==mrange) & (reada['mul']>0.0)]['min'].count()
        #min=float(mins/zero(minc))
        
        print(min)
        mul=reada[(reada['MRP Range']==mrange) & (reada['mul']>0.0)]['mul'].mean()
        #mulc=reada[(reada['Sub-Category']==subcat) & (reada['mul']>0.0)]['mul'].sum()  
        #mul=float(muls/zero(mulc))
        reada.loc[i,'mul']=mul
        reada.loc[i,'min']=min
        cat="Mrp"
        reada.loc[i,'Category-type']=cat    
                  
    
for i in range (0,len(reada)):
    min=reada['min'][i]
    d=reada['mul'][i]
    il=0
    max=0
    for j in range(0,len(of)):
        
        if(reada[of[j]][i]!=0):
            if(max<=reada[of[j]][i]):            
                
                max=reada[of[j]][i]
                il=j
                
                
    if(max!=0):
        
           
            value=max
            value1=max        
            for j1 in range(il,len(of)):
                
                if(value1<base[j1]):
                    reada.loc[i,of[j1]]=base[j1]
                else:
                    reada.loc[i,of[j1]]=value1
                value1=value1+d
                
            for j2 in range(il,-1,-1):
                
                if(value<base[j2]):
                    reada.loc[i,of[j2]]=base[j2]
                else:    
                    reada.loc[i,of[j2]]=value
                value=value-d
    else:
        value=1.1
        for j3 in range(0,len(of)):
            reada.loc[i,of[j3]]=value
            value=value+d
                
                    
       
            
print(len(reada))

reada.to_csv(fout,sep=',')
