# Pykemon
This is a project done by a Swedish student studying python programming.

Pykemon is a project where I Theo Esberg is trying to create an simple copy of pokemon.
This project started as an endproject for my python programming class in school.
I will try to accomplish some simple tasks and functions in the game. 

# This is what I have planed.
* I Will try to get a map system working with collition based on a TMX map file generated from the map editor Tiled.
    - The map system needs to load tiles from a tilesheet
    - It also needs to get "walls" in aka collision boxes from the TMX file
    - Should be able to change between different maps mid run
* I want to implement a "camera system"
    - If the current map is larger than the cameras view than make the camera follow the player on that axis.
    - aka if the width of the map is larger than the width of the camera then make the camera follow the player on the x-axis.
    - do the samke on the y-axis.
    - If the map width and height is smaller than the screen width and height, then dont follow the player.
* I want to implement some type of GUI to create dialouges and menys and such.
    - Has to use small amount of resources.
* I want to get a starter pokemon from "professor oak", where you can choose from 3 different gen 5 starters.
    - Use the GUI for a small dialouge
    - Choose pokemon from gui
* I wanted to create a save feature so you dont have to restart all again from start.
    - Will be created with .json files. 
    - One for all pokemons in the game to read from.
    - One for your caught pokemons.
    - Add pokemon to caught pokemon when getting a starter or new pokemon
* Then I want to implement pokemon that follows the player. 
    - Choose which one to follow you from GUI
    - Press "r" to summon pokemon.
    - Follow player in the same path the player has allready walked. 
* I also wants to implement a Battle system where you can fight wild pokemons.
    - Will use the GUI a lot
    - Will read pokemons from .json files
    - Add fight moves and end battle if pokemon does not have any health left.
    - Add run feature.
      
# What are my goals with this project? 
My goals with this project is simpel. I will try to learn more about python programming and use what I 
have learned in the python programming class to try to create a little copy of the game pokemon.
I know that this will be lots and lots of reasearch to get to know new things about python programming.
I have never worked with classes and that is mostly what I belive I have to use to get this working properly
while still maintaining readable code. (But I think the risk of creating spaghetti code is high)
Even tho this is a project of mine, I want to share it with anyone that wants to use the code. That is why 
the source code is here for anyone to take and use yourself. Build more on the project yourself or wants 
to start learning how classes work or other python things work. You can just take the code and try to understand
how my thaught procces went and borrow some code for your own project. (For example the code for the tiled TMX file rendering)

# How was my progress going? 
So my progress has been a rollercoaster. Sometimes it went well while sometimes it felt like nothing was working right
and I just wanted to give up. But I managed to complete most of the functionality I wanted in the game. 
I have worked a lot outside of school to get the progress going forward. But in the end of the day it was fun
and I completed the key fetures that I wanted to add in the game.

# Did I need to learn anything new?
I have learnt sooo much in this project and probably googled a thousend questions but boy am I glad I did this.
Because I now know more than I did in the start about Python programming and how it is working with classes,
json files, tmx files and much much more. 
Here are some of the things I have learnt in this project.
    * How to read and write to JSON files correctly
    * How to create basic classes
    * How to inherit a class from another class, (such as entity is the base class for player and pokemon)
    * How to read tmx files
    * How to blit tiles to the screen from tmx files
    * The struggle of starting something then a week or two later realizing that the code is spaghetti and redo EVERYTHING!
    * How to handle images and getting subsurfaces of images
    * How to use the pylint library

# Discussion
To summerize this project I want to say that Im proud of what I managed to accomplish in the time that I had.
It would have been fun to add a way to catch and heal pokemons and much much more but for the time beeing I belive that
I'm done with this project. It was realy fun to work on and I belive that this is an amazing way to learn to code in pygame.
To anyone that wants to try to do anything like this please do, it is tons of fun!

# Sources
Since I want to give cred where cred is due, here are my sorces.
* Firsty I got the GUI textures from a project called Tuxemon here on GitHub.
    * https://github.com/Tuxemon/Tuxemon/
* All of my non GUI textures is taken from the website Pokefans
    * https://fanart.pokefans.net/tutorials/mapping/tilesets
* I have also used the website Stack Overflow to get some answers.
    * https://stackoverflow.com/
    

 
