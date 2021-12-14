# IntelliJ to NetBeans Project Converter
Make your Java applications created in IntelliJ easily compatible with NetBeans! 

Run the following command in terminal or command prompt

```
python convert.py

Enter Source Path: /Users/johnexample/Desktop/myproject 

```

That's all it will take to convert your project. Enjoy! 


Don't hesitate to contact me at devansh@dksources.com if you have and questions or problems. 


## Explanation
The ```nbproject``` is a required folder by NetBeans, where it keeps its project settings. 
The only neccessary project build files needed are the ```project.xml``` and ```project.properties```. 


In ```project.xml```,  line 5 is changed to reflect the accurate name of the user's project. An unmodified copy is kept in the ```template``` folder, and the working copy of the settings are duplicated in the internal ```nbproject``` folder. 
