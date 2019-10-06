# Milestone 3 Data Centric Development  

Access Project on Heroku here - https://online-cookbookms3.herokuapp.com/  
Wireframes Can be seen here - 
Database Schema Can be seen here - 

An Online Cookbook - The brief for this project was to design and build an online Recipe Book to give the site owner a way to promote their brand of cooking tools by give external users a way to share recipes with other users on the site.

# Project Requirements  
Main Technologies  
HTML,CSS,JavaScript,Python & Flask,MongoDB and can include Additional Libraries and external APIS.  

# Project Mandatory Requirments  
Data Handling: Build a MongoDB-backed Flask project for a web application that allows user to store and manipulate data records about a particular domain.  
Database Structure:Put some effore into designing a database structure well suited for your domain. Mkae sure to put some thought into the nesting relationships between records of different entities.  
User Functionality: Create functionality for users to create, locate, display, edit and delete records (CRUD functionality)  
Use of Technologies: Use HTML and customer CSS for the Websites front-end.  
Structure: Incorporate a main navigation menu and structured layout  
Documentation: Write a README.md files for your project that explains what the project dose and the value that it provides to its users.  
Version control: Use Git & GitHug for version control.  
Attribution: Maintain clear separation netween code written by you and code from external sources. Attribute any code from external sources via comments above the code and for larger dependencies in the README.  
Deployment:Deploy the final version of your code to a hosting plaform such as Heroku.  

# Project Idea  
External User Goals  
-Find and Share Recipes  

Site Owner Goals  
-Promote a Brand of Cooking Tools  

Potential Features  
-Create a web application that allows users to store and easily access cooking recipes. Recipes would include fields such as ingredients, preparation steps, required tools, cuisine, etc.  

-Create the backend code and frontend form(s) to allow users to add new recipes to the site, edit them and delete them.  

-Create the backend and frontend functionality for users to locate recipes based on the recipe's fields. You may choose to create a full search functionality, or just a directory of recipes.  

-Provide results in a manner that is visually appealing and user friendly.  

Advanced potential feature (nice-to-have)  
-Build upon the required tools field to promote your brand of kitchen tools (e.g. oven, pressure cooker, etc…).  
-Create a dashboard to provide some statistics about all the recipes.  

## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members.

The site owner advances their own goals by providing this functionality, potentially by being a regular user themselves. The site owner might also benefit from the collection of the dataset as a whole.

As a user - I want a website that is easy to navigate with a layout that is easy to read  
As a user - I want to create a user account  
As a user - I want to search for recipes that might intrest me  
As a user - I want to add my own recipes to the site  
As a user - I want to update and remove my recipes from the site  
As a user - I want to share my recipes on social media  
As a user - I want to vote for my favourite recipes on the site  
As a user - I want to see all the Alergens associated with the recipe  
As a user - I want to see a list of the top 5 recipes on the site  


This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

Index: Main Home Page Displays Top Five Recipies by Votes  
User Registration Page:  Allows the user to create a user account  
User Login Page:  Allows the user to Login to their existing account  
User Profile Page: Shows list of User created Recipies  
Search Box in Nav Bar: Allows the user to search for recipies  
Nav Bar: Quick access to Login, Logout, Search, Shop  
Vote Button: Allows user to Vote from recipe  
Add Recipe Page: Allows user to add a new recipe  
Edit Recipe Page: Allows user to edit an existing recipe  
Delete Recipe Button: Allows the user to delete a recipe from the database  
Shop Page: Shows the user a range of the site owners products currently for sale  
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- 

## Technologies Used
HTML  
CSS  
JQuery  
Bootstrap 4.0.0
Font Awesome 5.11.2
Python 3.7.4
Flask  
WT-Forms  
Mongodb    

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment  

Deployed Version
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

Development Version  
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

### Content  
Recipies for testing were taken from https://www.bbc.co.uk/food/recipes  

### Media
Favicon from https://www.freefavicon.com  
Other Images from Google Images and https://pixabay.com  Used for educational purpose only.  

### Acknowledgements

- I would like to thank my mentor Spencer Barriball for his wisdow and guidance.  
- Pretty Printed on Youtube for good tutorial on building login systems with python and flask.    
- Code institute for great content and learning experience.  