# Dream Log BackEnd
## Welcome to the Dream Log BackEnd 

### Built With
-Masonite
-Cors
-Python

### Model/Schema/
## Movies

title: String,  
description: String,
image: String,
date: String, 
 

### Route Table
## Movies
| URL | Method | Action |
|-----|--------|--------|
| / | GET | Masonite Welcome Page|
| /dream | GET | Index page of all Dreams|
| /dream | POST | Create A Dream Log |
| /dream/:id | PUT | Update Dream |
| /dream/:id | DELETE | Delete selected Dream |


### User Stories
When a user is in the backend of the application the user should be able to display all the Dreams created. If a user is using Postman, Thunder Client, or Insomnia they can go to the routes listed about to create, update, or delete Dreams. If any errors occur while trying to do so double check what kind of request, you are making to the server and verify it with what you are attempting. For reference use the table above for guidance on which route to take. 

### Challenges
When testing the create route I was getting an error wehn trying to post it. After spending a couple of hours trying to figure it out. I remembered that I needed to add "*" in the CSRF Middleware.