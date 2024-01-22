## 2 different solutons to a JSONPlaceholder code challenge

**Challenge**:
"You will be working with the JSONPlaceholder API, a fake online REST
API used for testing and prototyping.

Your task is to integrate two endpoints from this API. The first
endpoint is the 'Todos' API (https://jsonplaceholder.typicode.com/todos), and the second is the 'Users' API (https://jsonplaceholder.typicode.com/users). For each todo
item, you need to identify the associated user and retrieve details about both the user and the todo.

To accomplish this, you will be querying the 'Todos' endpoint to get a
list of todo items.

For each todo item, use the 'userId' to query the 'Users' endpoint and
retrieve the corresponding user details.

Your goal is to combine the information from these two sources and
format the output as a JSON object like the example below:

{"userName": "Bret", "email": "Sincere@april.biz", "todoTitle":
"delectus aut autem", "completed": false}

Note: For this exercise, please refrain from using AI tools. However,
feel free to use Google for syntax reference or any other
programming-related queries.

Useful URLs:

Todos API: https://jsonplaceholder.typicode.com/todos 

Users API: https://jsonplaceholder.typicode.com/users 

Specific User API (example): https://jsonplaceholder.typicode.com/users/1

The focus of this task is on your ability to work with APIs, process JSON data, and effectively combine information from multiple sources."



### Approach 1
  -follows the guidance provided by the challenge
  
  -uses userId from /todos to query /users in 205 API calls
    
### Approach 2
  -uses published and easily found API endpoint
  
  -uses /users and todos data /users/1/todos in 12 API calls
