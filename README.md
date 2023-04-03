# Block TD

## Overview
Block TD is a simple Tower Defense game developed by Keegan Smith, Michael Morris, and Will Heeney for the 2023 Capsher ACC Coding Challenge.


## Dependencies:  
``` 
python -m pip install -U pygame --user 
```
## How to Play
Download the "[temp] Clock TD.zip" file and extract it's contents. Then simply run the executable. 
In the game you will buy towers and place them around the map to stop each wave of blocks from reaching the end of the track!
## Design
### Main
main.py is the heart of our game. main keeps track of the current game state, of which there are 5: start screen, game screen before round, game screen during round, victory screen, and defeat screen. main also has to keep track of all of the buttons on the current screen. If the player is currently on the start screen, the program checks whether a mouse click has happened, and if it has, it checks whether or not the mouse click happened within the bounds of the start button. 
Once the start button has been pressed, the program changes the screen to the game screen before round. On this screen the program must keep track of the play button, the start button, and whether or not the player has clicked on a tower. If the player has clicked on a tower then the range of the tower as well as the sell button are displayed, when the player clicks off the tower the "clicked tower" state is set to false and as a result the range and sell button disappear. If the "clicked tower" state is true and the player clicks on the sell button, then the program sets the "clicked tower" state to false and also gets rid of the tower as well as refunds the player half of the tower's initial cost. 
### Enemies

### Shop
The Shop functionality of the game is implemented with 3 classes being shop_button, Shop, and Shop_Item. These 3 classes work together to smoothly allow the player to buy towers in the shop and place them on the map.
#### shop_button
The shop_button class is used to create a button on the main screen so that the event listener for loop in main can detect when the user wants to open and close the shop and properly change the display.
#### Shop
The main purpose of the shop class is to hold the different Shop_Items which are the towers that you can buy as well as also detect when a user clicks on an item in the shop and calls the appropriate function to complete that action. The Shop class also checks to see if the user is hovering over a tower in the shop and displays the description for that item if it is.
#### Shop_Item
Shop_Item holds the information about each tower that is in the shop mainly the type of tower as well as the description and price. The main function in Shop_Item is the addtower() function which allows the user to click somewhere on the map and then returns the location of the click so that the appropriate tower can be placed in that location.

### Towers

### Art
