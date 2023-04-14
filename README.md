# Capstone Project 4: inventory manager

## Description
A Python program using OOP to handle a variety of stock-taking tasks for a warehouse of shoes.

## Installation
- Dowload both inventory.py and inventory.txt files.
- Store both files in the same folder on your device.
- Open the folder in your IDE.
- Run inventory.py

## Usage
- Upon running inventory.py you will be greeted with the following menu:

![image](https://user-images.githubusercontent.com/91968539/219885409-9e7cf2f6-e7c1-490b-9835-5593c00a9f76.png)

- Select which option you would like to perform and follow the on screen instructions:

  - cs - capture and store data about a shoe
    - Allows user to enter new data about a shoe and append it to inventory.txt
    
  - va - view table of details of all shoes
    - Dsiplays a table containg the details of the shoes stored in inventory.txt
    
  - rs - find and restock the shoe with lowest quantity
    - Finds the shoe in inventory.txt with the lowest quantity and provides an option to restock a chosen quantity to this shoe 
  
  - ss - use code to search for shoe
    - Allows user to search for a shoe in inventory.txt using it's code
    - A table of the details of this shoe will be displayed
  
  - vi - view table of details and values of all shoes
    - Displays a table containg the details of the shoes stored in inventory.txt as well as their calculated values (quantity * price)
  
  - hq - view shoe with highest quantity
    - Displays a table of details of the shoe with the highest quantity
  
  - ex - exit program
    - Allows user to exit the program
