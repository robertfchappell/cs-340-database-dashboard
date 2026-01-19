This project is a dashboard app powered by MongoDB that was made for Grazioso Salvare, an international group that trains animals to save lives. Based on age, breed, and area, the dashboard's job is to help find dogs that would be good for search and rescue training.

The data model for the app is a MongoDB database, the CRUD module is written in Python to handle database interactions, and the Dash framework is used to make a dynamic web dashboard. Users can sort animal data, see the results in a table, and see charts and a geolocation map to better understand the information.

CRUD is a Python module that was made to keep database code separate from the dashboard interface. This made it easy to read, maintain, and use the code again. In the future, the same feature could be used for projects like inventory systems, reporting tools, or other data-driven apps that need access to MongoDB.

To finish this job, I first put the dataset from the Austin Animal Center into MongoDB. Then I made and tried the CRUD functions that let you add, read, change, and delete records. After that, I used Dash to build the dashboard display and connect it to the database. To make it easier for the client to use, interactive filters, charts, and a map were added.

Making sure that the database queries gave the right results for each filter option was hard for this job. This was fixed by trying queries in MongoDB first, then linking them to the dashboard.

This project shows how Python, database systems, and web-based tools can all work together to meet the needs of real organizations. Companies like Grazioso Salvare can make better choices and run their businesses better by organizing and visualizing data well.
