
import requests
import re
import time 

def  GetEmailBySite(Sitelist):
     for i in Sitelist:
          DataSite = requests.get(i)
          ReturnRegex = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+",DataSite.text)
          if ReturnRegex:
               return(list(set(ReturnRegex)))
          else:
            return None
          
#coloque os sites 

sites = [ "http://testphp.vulnweb.com/" , "http://bancocn.com"]



#print (GetEmailBySite([]))
cont_x = 0

try:
    for x in sites:
        mails = (GetEmailBySite([x]))
        if (mails != "None" or mails != None):
            print (mails)
        cont_x = cont_x + 1
except:
    print (x)
    pass 
