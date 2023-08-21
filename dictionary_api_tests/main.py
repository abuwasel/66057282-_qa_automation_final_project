from functions import *

#-----Valid Word Lookup------:
#print(f"Successful response (status code): {get_status_code(url,'apple')}")
#print(f"Definition: {get_data(url,'apple')[0]['meanings'][0]['definitions'][0]['definition']}")

#-----Word with Multiple Definitions:------:
#print(f"Definition: {get_data(url,'run')[0]['meanings']}")

#-----Word with No Definitions:------:
#print(f"Definition: {get_data(url,'asdfghjkl')}")

#print(f"Definition: {get_data(url,'supercalifragilisticexpialidocious')}")

print(get_data(url,'word'))



