from functions import *

#-----Valid Word Lookup------:
#print(f"Successful response (status code): {get_status_code(url,'apple')}")
#print(f"Definition: {get_data(url,'apple')[0]['meanings'][0]['definitions'][0]['definition']}")

#-----Word with Multiple Definitions:------:
#print(f"Definition: {get_data(url,'run')[0]['meanings']}")

#-----Word with No Definitions:------:
#print(f"Definition: {get_data(url,'asdfghjkl')}")

#-----Case Insensitivity:------:
#print(get_data(url,'Hello'))

#-----Special Characters:------:
#print(get_data(url,'c++'))

#-----URI Encoding:------:
#print(get_data(url,'space%20bar'))

#-----Language Parameter:------:
#print(get_data(url,'book','es'))

#-----Empty Input:------:
#print(get_data(url,''))

#-----Rate Limiting:------:
#print(get_data(url,'word'))

#-----Invalid Endpoint:------:
#print(get_data(url,'/invalid'))

#-----Network Errors:------:
#print(get_data(url,'word'))

#-----Long Word Input:------:
#print(f"Definition: {get_data(url,'supercalifragilisticexpialidocious')}")


print(get_data(url,'word'))



