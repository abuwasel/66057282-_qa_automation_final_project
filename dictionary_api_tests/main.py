from functions import *

#-----Valid Word Lookup------:
#Input: "apple"
#Expected Output: Successful response with the definition and relevant information about the word "apple".
#-----------------------------#
#print(f"Successful response (status code): {get_status_code(url,'apple')}")
#print(f"Definition: {get_data(url,'apple')[0]['meanings'][0]['definitions'][0]['definition']}")

#-----Word with Multiple Definitions:------:
#Input: "run"
#Expected Output: Verify that the response contains multiple definitions for the word "run".
#-----------------------------#
#print(f"Definition: {get_data(url,'run')[0]['meanings']}")

#-----Word with No Definitions:------:
#Input: "asdfghjkl"
#Expected Output: Ensure that the response indicates that the word is not found or handle the case of no definitions.
#-----------------------------#
#print(f"Definition: {get_data(url,'asdfghjkl')}")

#-----Case Insensitivity:------:
#Input: "Hello"
#Expected Output: Ensure that the API handles case-insensitive word searches and returns the definition for "hello".
#-----------------------------#
#print(get_data(url,'Hello'))

#-----Special Characters:------:
#Input: "c++"
#Expected Output: Validate that the API can handle special characters and return definitions for programming-related terms.
#-----------------------------#
#print(get_data(url,'c++'))

#-----URI Encoding:------:
#Input: "space%20bar"
#Expected Output: Verify that the API correctly handles URI-encoded input and returns the definition for the corresponding word.
#-----------------------------#
#print(get_data(url,'space%20bar'))

#-----Language Parameter:------:
#Input: "book", language="es" (Spanish)
#Expected Output: Confirm that the API supports language parameter and returns the definition in the specified language.
#-----------------------------#
#print(get_data(url,'book','es'))

#-----Empty Input:------:
#Input: ""
#Expected Output: Check that the API handles empty input gracefully and returns an appropriate error response.
#-----------------------------#
#print(get_data(url,''))

#-----Rate Limiting:------:
#Execute a large number of requests in a short time to test the API's rate limiting mechanism. Verify that the API returns an error response when the rate limit is exceeded.
#-----------------------------#
#print(get_data(url,'word'))

#-----Invalid Endpoint:------:
#Input: "/invalid"
#Expected Output: Ensure that the API returns a proper error response for an invalid endpoint.
#-----------------------------#
#print(get_data(url,'/invalid'))

#-----Network Errors:------:
#Simulate network errors by temporarily disconnecting from the internet during a request and ensure that the API gracefully handles the error.
#-----------------------------#
#print(get_data(url,'word'))

#-----Long Word Input:------:
#Input: "supercalifragilisticexpialidocious"
#Expected Output: Verify that the API can handle long input words and returns relevant definitions.
#-----------------------------#
#print(f"Definition: {get_data(url,'supercalifragilisticexpialidocious')}")


print(get_data(url,'word'))
