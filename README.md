# Parking ticket vending machine map 

This project is a :ticket: **ticket machine map** for places to :parking: park your :blue_car: car in the :de: german city **"cologne"**. 

It also has a map for :bus: **bus parking stations** in the same city. 

The map uses google maps and if you click on a ticket machine mark you can get more informations about it.

The **Flask web app** is made in Python, JS, CSS and HTML5.


## Getting started

To start and use the Flask Application follow these steps: 

1. download and install **Python 2.7**

2. download the project

3. start the terminal and type:

   ```
   pip install Flask
   pip install Flask-Babel
   pip install Flask-Login
   pip install Flask-WTF
   ```
   
4. run python in the terminal and type:

   ```
   >>> from database import init_db
   >>> init_db()
   ```
   
5. start Flask with: 

   ```
   >>> python parkautomaten.py
   ```
   
6. visit  [http://localhost:5000/](http://localhost:5000/)  in your browser to run it


## usage

A login interface is visible now. 

Userdetails are: **admin** and **dedefault**

The :parking: parking ticket vending machine map will show up and additional links are there, too. 

One of the links is for the :bus: bus parking station map and the other link is for the :ticket: ticket machines. 

Clicking on one of the links will display another map.

