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
main.py is the heart of our game. main keeps track of the current game state, of which there are 5: start screen, game screen before round, game screen during wave, victory screen, and defeat screen. main also has to keep track of all of the buttons on the current screen. If the player is currently on the start screen, the program checks whether a mouse click has happened, and if it has, it checks whether or not the mouse click happened within the bounds of the start button.
#### Game Screen Before Round
Once the start button has been pressed, the program changes the screen to the game screen before round. On this screen the program must keep track of the play button, the shop button, and whether or not the player has clicked on a tower. If the player has clicked on a tower then the range of the tower as well as the sell button are displayed, when the player clicks off the tower the "clicked tower" state is set to false and as a result the range and sell button disappear. If the "clicked tower" state is true and the player clicks on the sell button, then the program sets the "clicked tower" state to false and also gets rid of the tower (removes the tower from the current list of towers on the screen) as well as refunds the player half of the tower's initial cost by updating the money display. When the shop button is pressed, the screen displays the shop panel. All of the buttons within the shop panel are handled by shop.py. If the shop panel is active and the player presses the shop button again, the shop panel vanishes. When the play button is pressed the program loads the next round, (stored in round.py) and advances to the game screen during wave screen.
#### Game Screen During Wave
The game during wave screen has to keep track of a lot things. It must keep track of 1.) the enemies currently on the screen 2.) the enemies yet to be loaded onto the screen, and when to deploy them 3.) the projectiles currently on the screen 4.) the towers on the screen, telling them to shoot 5.) any collisions that may happen 6.) felled enemies and updating the players cash 7.) player's remaining lives. The collision handling is done by looping through all of the enemies and then calling the collision function in collisions.py file which loops through all of the projectiles and checks if there is a collision between the current enemy and any of the projectiles on screen. This algorithm runs in $\Theta(EP)$ where $E$ is the number of enemies on screen and $P$ is the number of projectiles on screen. This is probably the most inefficient algorithm in our code, and if we were looking to improve efficiency this would be the first place to look. To keep track of enemies on screen and enemies yet to be loaded we used two lists which we update whenever a new round is loaded, a new enemy is deployed, and whenever an enemy is defeated. To keep track of deployment we just deploy whenever the current game counter % round delay == 0. This makes it so that an enemy is deployed every round delay ticks, when an enemy is deployed it is popped from the current to be deployed list and appended to the enemies on screen list. When a collision does happen, the enemy's health is depleted by the damage of the projectile it was hit by. If the enemy's health is less than or equal to 0, then it is removed from the enemies on screen list and the player gains $x$ amount of money. Currently $x = 4$, but this could change in the future. Money gained is not dependent on the enemy type, all enemies are worth $x$ amount of money. The program also keeps track of player health. If the player health reaches 0, the defeat screen is displayed. If the player reaches the end of the round without losing all of their lives, and this is the final round, then the victory screen is displayed. Else, the screen before round screen is displayed again.
#### Defeat Screen
The defeat screen only keeps track of the "again" button. Upon being clicked the player is redirected back to the start screen.
#### Victory Screen
The victory screen is pretty much the same as the defeat screen. Again it just keeps track of the "again" button which upon being pressed redirects the player back to the start screen.

---------------------


### Enemy
The enemy class keeps track of enemy pathing, health points, status affects, and speed. There are also child classes of Enemy such as Fast Enemy, Tank Enemy, Super Fast Enemy, and Super Tank Enemy which simply adjust the speed and health points attributes of the enemy class.
#### Enemy Pathing
Enemy pathing is kept track of by simply having a list of points which represent each place where the enemy has to turn a corner. The enemy starts at the initial point and then heads either up, down, left, or right depending on the location of the next way point. This would make it easy if we wanted to add a new map as updating the enemy pathing is just a matter of changing the set of waypoints
#### Enemy Status Affects
As of now there is only one status affect in the game which is slow. To ensure that only one slow is applied at a time, we also include the id of the tower that applied the slow to the enemy. This way we can check if the current slow tower's id matches the tower that slowed the enemy to begin with, and can update the slow affect as needed.
#### Enemy Health
Each enemy stores it's current health. When this value reaches 0 the enemy has been felled.
#### Enemy Speed 
The enemy speed represents the number of pixels the enemy travels in each frame. The higher this number, the faster an enemy travels. 
#### Default Enemy
This enemy is colored blue and has 100 health and 5 speed. This means that it dies in two shots from the normal tower.
#### Tank Enemy
This enemy is colored purple and has 500 health and 2 speed. This means it is very slow and dies in two shots from a sniper tower.
#### Fast Enemy
This enemy is colored white and has 100 health and 8 speed. This means that it travels more than 50% faster than the regular enemy and also dies in two hits from a normal tower
#### Super Tank Enemy
This enemy is colored black and has 750 health and 4 speed. This means that it travels at nearly the same speed as a regular enemy, but has 7.5x the health making this a formidable foe.
#### Super Fast Enemy
This enemy is colored gray and has 150 health and 12 speed. This means that it has 50% more health than the regular enemy and more than double the speed, making this possibly the toughest enemy in the game.

---------------------


### Shop
The Shop functionality of the game is implemented with 3 classes being shop_button, Shop, and Shop_Item. These 3 classes work together to smoothly allow the player to buy towers in the shop and place them on the map.
#### shop_button
The shop_button class is used to create a button on the main screen so that the event listener for loop in main can detect when the user wants to open and close the shop and properly change the display.
#### Shop
The main purpose of the shop class is to hold the different Shop_Items which are the towers that you can buy as well as also detect when a user clicks on an item in the shop and calls the appropriate function to complete that action. The Shop class also checks to see if the user is hovering over a tower in the shop and displays the description for that item if it is.
#### Shop_Item
Shop_Item holds the information about each tower that is in the shop mainly the type of tower as well as the description and price. The main function in Shop_Item is the addtower() function which allows the user to click somewhere on the map and then returns the location of the click so that the appropriate tower can be placed in that location.

---------------------

### Tower
The Towers are your only line of defense against the enemies. They shoot, slow or burn the enemies to prevent them from escaping. They can be placed anywhere besides on another tower, out of bounds, or on the path the enemies walk. The normal and sniper tower both shoot projectiles, which aim at the furthest enemy down the path that has its centerpoint within the radius of the tower. The angle is calculated by using the centerpoint of the enemy and the tower as the two points on a right triangle

The slow tower doesn't shoot projectiles however, as it slows down all enemies within its radius. The flame tower also doesn't not "shoot" projectiles, but it still attack by burning all enemies within close proximity with its flamethrower. Each tower has its own seperate cost, radius, damage, and shot speed for projectiles. 

---------------------

### Projectile
The projectiles are also their own class, following in a straight line when shoot in whichever angle chose for it until it either hits an enemy or reached the boujndary of the game.

The projectiles are updates every frame by their shot speed by the tower class

The normal tower bullet and sniper bullet have their own classes but do similar things with differing and damage

While the flame from the flame doesn't actually travel it is considered a projectile so the flame wouldn't need to be implemented within the flame tower class

---------------------

### Art
All of the artwork in our game is made of pixel art using an online pixel art editor.

Art Credit:
* Start Screen - Will Heeney
* Map - Will Heeney
* Game Start Button - Will Heeney
* Round Start Button - Keegan Smith
* Shop Button - Will Heeney
* Win Screen - Keegan Smith
* Lose Screen - Keegan Smith