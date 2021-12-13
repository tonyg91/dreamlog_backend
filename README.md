# Dream Log Back End
## Welcome to the Dream Log App Backend

### Built With
-React

### Model/Schema/
## Dreams

title: String,  
description: String,
image: String,
date: String, 
 

### Route Table
## Dreams
| URL | Method | Action |
|-----|--------|--------|
| / | GET | Masonite Welcome Page|
| /dream | GET | Index page of all Dreams|
| /dream/:id | GET | Show page of a single dream |
| /new | POST | Create A Dream Log |
| /edit | PUT | Update Dream |
| /dream/:id | DELETE | Delete selected Dream |


### User Stories
 When a user is in the backend of the application the user should be able to display all the Dreams created. If a user is using Postman, Thunder Client, or Insomnia they can go to the routes listed about to create, update, or delete Dreams. If any errors occur while trying to do so double check what kind of request, you are making to the server and verify it with what you are attempting. For reference use the table above for guidance on which route to take.

### Challenges
When testing the create route I was getting an error wehn trying to post it. After spending a couple of hours trying to figure it out. I remembered that I needed to add "*" in the CSRF Middleware.