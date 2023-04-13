## Overview
### Project Idea
I have developed a comprehensive farm management application that is simple to use, yet packed with powerful features.
I came up with this idea after consulting it with my family members who were seeking for such solution.

### Capabilities
This application allows farmers to efficiently manage two main aspects of their farm: fields and animals.

For fields, users can add, search, delete, and update any type of information related to their land. They can also implement agrotechnical treatments and attach photos, which can be helpful for identifying specific fields on a map or documenting damages caused by weather conditions.

For animals, the application currently supports two types: cows and sheep. Users can add, delete, make notes, and create connections between specific animals, as well as search and filter animals based on various criteria.

### Used technologies
AgroProject is a web-based application built primarily using Python, SQL, and HTML.

For the backend, I utilized the Django framework, which was easy to set up and allowed for the creation of a scalable application. I used SQLite as the database for implementing CRUD operations on fields and animals instances, which proved to be sufficient for the needs of this application.

For the frontend, I used HTML and CSS, and also leveraged the Bootstrap library to streamline the development process and enhance the application's user interface.

## Presentation
### Home page
Simple page with integrated API to recive weather from https://openweathermap.org/ along with a list of commonly used links for checking daily information.

<p align="center">
  <img width="750" alt="Screen Shot 2023-04-13 at 12 03 23 PM" src="https://user-images.githubusercontent.com/62257523/231845456-4337c51f-9712-493a-b149-3a3b69174e1a.png">
 </p>


### Lists
Here is a table presenting a list of cows. The table includes options for adding notes, updating, and deleting records. At the top of the page, there is a search bar for looking up specific cows, as well as multiple sorting options.
<p align="center">
  <img width="750" alt="Screen Shot 2023-04-13 at 21 09 23 PM" src="https://user-images.githubusercontent.com/62257523/231859335-a5310e45-3eb0-4230-a619-1695647dd4f7.png">
 </p>
 
### Creating new fields
Using Django and HTML i implemented forms to easily update and create new instances.
<p align="center">
  <img width="300" alt="Screen Shot 2023-04-13 at 20 07 33 PM" src="https://user-images.githubusercontent.com/62257523/231846815-add2aac3-4941-4b78-8b2a-b6605917d5b3.png">
 </p>
 
For the rest of the project, the layout maintains a consistent design.
 
