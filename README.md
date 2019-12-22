# Milestone 3 Data Centric Development  

Access Project on Heroku here - https://online-cookbookms3.herokuapp.com/  

An Online Cookbook - The brief for this project was to design and build an online Recipe Book to give the site owner a way to promote their brand of cooking tools by give external users a way to share recipes with other users on the site.

# Technologies Used 
HTML  
CSS  
JQuery  
Bootstrap 4.0.0
Font Awesome 5.11.2
Python 3.7.4
Flask  
WT-Forms  
Mongodb    

# Outline of Project Mandatory Requirments  
Below is an Outline of the Project requirments from Code Institute Milestone 3.

Data Handling: Build a MongoDB-backed Flask project for a web application that allows user to store and manipulate data records about a particular domain.  
Database Structure:Put some effore into designing a database structure well suited for your domain. Mkae sure to put some thought into the nesting relationships between records of different entities.  
User Functionality: Create functionality for users to create, locate, display, edit and delete records (CRUD functionality)  
Use of Technologies: Use HTML and customer CSS for the Websites front-end.  
Structure: Incorporate a main navigation menu and structured layout  
Documentation: Write a README.md files for your project that explains what the project dose and the value that it provides to its users.  
Version control: Use Git & GitHub for version control.  
Attribution: Maintain clear separation between code written by you and code from external sources. Attribute any code from external sources via comments above the code and for larger dependencies in the README.  
Deployment:Deploy the final version of your code to a hosting plaform such as Heroku.  

# Project Idea 
External User Goals  
- Find and Share Recipes  

Site Owner Goals  
- Promote a Brand of Cooking Tools  

Potential Features  
- Create a web application that allows users to store and easily access cooking recipes. Recipes would include f fields such as ingredients, preparation steps, required tools, cuisine, etc.  
- Create the backend code and frontend form(s) to allow users to add new recipes to the site, edit them and delete them.  
- Create the backend and frontend functionality for users to locate recipes based on the recipe's fields. You may choose to create a full search functionality, or just a directory of recipes.  
- Provide results in a manner that is visually appealing and user friendly.  

## UX

Wireframes Can be seen here - https://github.com/jsnbly/milestone3/tree/master/wireframes
Database Schema Can be seen here - https://github.com/jsnbly/milestone3/tree/master/schema
Importance vs Viability Graph ie. Strategy Plane - https://github.com/jsnbly/milestone3/tree/master/strategygraph.jpg

The Project Scope was to create an Online Cookbook that would have all the elements of a CRUD  
Create, Read, Update, Delete Application the following are some User Stories that this version  
trys to satisfy.

As a user - I want a website that is easy to navigate with a layout that is easy to read  
As a user - I want to create a user account  
As a user - I want to search for recipes that might intrest me  
As a user - I want to add my own recipes to the site  
As a user - I want to update and remove my recipes from the site  
As a user - I want to share my recipes on social media  
As a user - I want to vote for my favourite recipes on the site   
As a user - I want to see a list of the top 5 recipes on the site  


## Features

Home Page/Index: Main Home Page Displays Top Five Recipes by Votes Jumbotron with link for Registration   
User Registration Page:  Allows the user to create a user account  
User Login Page:  Allows the user to Login to their existing account  
User Profile Page: Shows list of User created Recipies  
Pagination: Built into the Search and Recipe page to allow easier navigation
Search Box in Nav Bar: Allows the user to search for recipes  
Nav Bar: Quick access to Login, Logout, Search, Shop  
Vote Link: Allows user to Vote from recipe  
Add Recipe Page: Allows user to add a new recipe  
Edit Recipe Page: Allows user to edit an existing recipe  
Delete Recipe Button: Allows the user to delete a recipe from the database  
Shop Page: Shows the user a range of the site owners products currently for sale  
 
### Existing Features
- Home Page/Index - Provides a Landing page for the user Showing Recipes and SIgnup Options  
- When the Site opens the customer is greeted with Nav Bar, Jumbotron, A list of the top 5 Recipes and Site Footer 
- It is fully responsive regardless of the screen size it is opened in. 

- User Registration Page  
- When the customer clicks the register button they are prompted to enter their details to register an account  
- It asked for username, email, and password and then creates a user account in the database.  

- User Login Page  
- This page prompts the user to enter their user name and password to access their user profile page  

- User Profile Page  
- Once the user is logged in they will see a new jumbotron for the shop and they will see a list of their  
- Recipes in the data base here they can view, edit and delete their recipes from the database

- Pagination has been built in to search results so as not to load the full database of recipes, Pagination
  allows for seprate pages of results.  

- Nav Bar  
- Responsive Nav Bar that collapses when the site is viewed on small screen devices it is home to the search box  
- and navigation links to let the user view recipes, login/logout and access the shop.  

- Search Box  
- The user can search for any word, phrase or tag that might link to a recipe and will display the result when the search button is pushed or no results found if there is nothing in the database.  

- Recipe Page  
- Lists all Recipes on the site, User can Click into individual recipes to see full instructions of how to prepare.  

- Shop Page  
- Generic Landing page for a pretend shop that the Site owner can fill with their own information regarding Products for Sale. 


For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- A way to Admin Recipes added to the site to check for profanity etc.   
- A Comment section for the recipes  
- A better way of voting on recipes at present there is no logic to see if the user has already voted  
- Email Confirmation at time of login  


## Testing
Manual testing was used to test the user interface elements while developing this application examples processes used can be seen below  

Automated HTML Validation was achived using W3 Validators on https://validator.w3.org/ and https://jigsaw.w3.org/css-validator/ 

- Testing Search Fuction  
1. Load Webpage
2. Enter Query in Search Bar
3. Test Pass if Query equals Results

- Testing User Registration
1. Contextulize User Registration Page
2. Fill in required form information
3. Complete and port form
4. Test Passed if user logged in

- Testing Login Fuction
1. Make Sure no user settings logged in (Incognito Mode)
2. Hit Login Option
3. Enter known username and password combination
4. Test passed if know user logged in without error

- Add/Save Recipe 
1. Requires User to be logged into the site
2. Click Add Recipe
3. Enter required information in recipe fields
4. Test Passed if user redirected to profile page with recipe added flash message

- Edit Recipe
1. Requires user to be logged into the site
2. From the users profile page they can select edit button on recipe
3. Page should redirect to an edit form page with details of the recipe 
4. Test passed if Recipe can be updated and saved to show results Flash message recipe edited

- Delete Recipe
1. Requires user to be logged into the site
2. From the users profile page they can select the delete button on a recipe
3. Test passed if recipe removed and no longer displayed on profile page

As well as the above examples Manual testing was used to test the UI of the Website to check Responsiveness and reability of the site across a range of screen sizes. Chrome Developer Tools was used along with a Chromebook14" Samsung S6 and Huawei p30 to get a feel for the site across a range of screen types.


## Deployment  

### Deployed Version
The Depolyed version of this project was achived using heroku and mongodb.com the main difference with  
the deployed version is it used Heroku Config Vars for the secret key and Mongo_URI form a security point  
I chose to use this method rather than use something like an config.py file as I felt it was more secure  
To push the Project to Heroku Only requires a few steps and I initially using it for development testing  
but found it faster to run the code locally while developing. The below is a basic run down of the steps  
and gives an overview of the process without having all requirments from the start if you are trying  
to run from this repository all necessary files are included!  ie requirments.txt and Procfile. This also  
asumes you have a heroku account to push to.  
  
1. Install heroku on your local machine Link can be found in Software used section  
2. Clone this repository to your local machine  
3. We need a requirments.txt to staisfy heroku so as you are developing and adding extensions with pip   
   you need to create your requirments.txt with pip freeze --local> requirements.txt  
4. Create a simple text file named Procfile without the file extension, ie Procfile.txt is not valid  
5. Open Procfile for editing and put web: python3 app.py on the first line this tells Heroku how to run 
6. Open Heroku.com and setup a new project name for this project
7. You need to add some Config Vars to get this to run so you need to go to proect settings  
   click reveal Config Vars and add the following in upper case without quotation and in seperate boxes  
   "IP" 0.0.0.0  
   "MONGODB_URI" You will get your connection information from mongodb.com under how to connect you app  
   "PORT" 5000  
   "SECRET_KEY" This can be what ever you like!  
8. For deployment you can open a terminal or command promt and type "heroku login"  (asuming your not  
   logged in to heroku), Then run "heroku git:clone -a online-cookbookms3" (this name links the project 
   to heroku), Next run "cd online-cookbookms3" to access the folder, Next run "git add" then git commit -am "make it  better" to commit changes and finally "git push heroku master" this should hopfully build and launch the app  
   if not check the heroku logs to see what went wrong     
9. Open heroku.com and in your profile page clicj the projects title then click open app to view running application 

### Development Version  
Development for this project was tested using Python 3.7.4 on Windows 10 running through Command Line  
and linking back to MongoDB Collection hosted on mongodb.com, the Following steps will help anyone   
to achive a running version on their machine. You will need to edit the Secret_Key and MONGODB_URI to your  
specifications and setup a collection with the database schema before you can connect.  

1. Make Sure you have Latest Version of Python installed ie. Python V.3.7.4  
2. git clone this Repository into a local folder  
3. Open a command promt or terminal in this folder and run pip install -r requirments.txt to satisfy local requirments  
3. Setup a mongodb.com Database with the Schema in this Repository  
4. Uncomment and Edit SECRET_KEY and MONGODB_URI to your specifications  
5. In the command promt or terminal and run "python app.py" again in the projects main directory   
6. Comment out app.run(host=os.environ.get('IP'),  port=int(os.environ.get('PORT')), debug=True) towards the end of          app.py    
7. Replace this with app.run(debug=True) this will allow the app to diplay debugging information in the browser  
8. Open a web browser and point it to http://127.0.0.1:5000 to view running version  
    


## Credits  
I would like to credit my mentor as he helped with explaning the use of regular expressions in my search code 
as I could not find a cleaner way to achive this his code is clearly commented in the search route section and I thank him for his help. This was the line query = {'$regex': re.compile('.*{}.*'.format(search_query)), '$options': 'i'}      

The login code was built with the help of Pretty Printed video on Youtube this can be found here  
https://www.youtube.com/watch?v=vVx1737auSE  

I also took inspiration for Pagination from Pretty Printed video here:  
https://www.youtube.com/watch?v=Lnt6JqtzM7I  

Navbar and Footer Code was taken from Bootstrap 4 example Code in Bootstrap4 Documentation

### Content  
Recipes for testing were taken from https://www.bbc.co.uk/food/recipes  

### Media
Favicon from https://www.freefavicon.com  
Other Images from Google Images and https://pixabay.com  Copyright of their owners and used here for educational purpose only.  

### Acknowledgements

- I would like to thank my mentor Spencer Barriball for his wisdow and guidance.  
- Pretty Printed on Youtube for good tutorials on building login systems and pagination with python and flask.  
- Code institute for great content and learning experience.  