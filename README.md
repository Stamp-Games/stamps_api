#Mission Statement:  
To provide a way to educate young people of various ages about the world of stamps through an interactive digital experience. 

#Project Overview: 
We will build web based games/ interactive media to support the education goals of the convention, and provide a collection point for those projects to be easily sought out by users. This collection point/ landing page will also contain links to 3rd party interactive media, as well as links to learn more about the process/ hobby/ postal system. As part of the project, we will be developing an open source API that will resolve to be a digital source for stamp factoids and images, so the developers of the media don’t have to source their own content.

###API Specific  
The API is to return the stamp information in a JSON blob/object.  
GET requests are working with pre-populated data.

###Usage
Currenty this is LHO (Local Host Only). To use please follow these steps.  
* clone this repository  
* assure that you are in the same directory you cloned this project to  
* launch the API by typing `python stamps.api`  
* navigate your web-browser to `http://127.0.0.1:5000/api/stamps/`  

####TODOS: 
** Add POST/PUT methods to add new stamps  
** Add UPDATE method to return updated stamp info  
** Add DELETE method to remove stamps  
** Create database to store stamp info to allow for filtering  