# Test cases for UI - Tests

```https://api.dictionaryapi.dev/api/v2/entries/en/<word>```

### 1- Valid Word Lookup:	
```Input: "apple"```

```Expected Output: Successful response with the definition and relevant information about the word "apple".```

### 2- Word with Multiple Definitions:	
```Input: "run"```

```Expected Output: Verify that the response contains multiple definitions for the word "run".```

### 3- Word with No Definitions:	
```Input: "asdfghjkl"```

```Expected Output: Ensure that the response indicates that the word is not found or handle the case of no definitions.```

### 4- Case Insensitivity:	
```Input: "Hello"```

```Expected Output: Ensure that the API handles case-insensitive word searches and returns the definition for "hello".```

### 5- Special Characters:	
```Input: "c++"```

```Expected Output: Validate that the API can handle special characters and return definitions for programming-related terms.```

### 6- URI Encoding:	
```Input: "space%20bar"```

```Expected Output: Verify that the API correctly handles URI-encoded input and returns the definition for the corresponding word.```

### 7- Language Parameter:	
```Input: "book", language="es" (Spanish)```

```Expected Output: Confirm that the API supports language parameter and returns the definition in the specified language.```

### 8- Empty Input:	
```Input: ""```

```Expected Output: Check that the API handles empty input gracefully and returns an appropriate error response.```

### 9- Rate Limiting:	
```Execute a large number of requests in a short time to test the API's rate limiting mechanism. Verify that the API returns an error response when the rate limit is exceeded.```

### 10- Invalid Endpoint:	
```Input: "/invalid"```

```Expected Output: Ensure that the API returns a proper error response for an invalid endpoint.```

### 11- Network Errors:	
```Simulate network errors by temporarily disconnecting from the internet during a request and ensure that the API gracefully handles the error.```

### 12- Long Word Input:	
```Input: "supercalifragilisticexpialidocious"```

```Expected Output: Verify that the API can handle long input words and returns relevant definitions.```
