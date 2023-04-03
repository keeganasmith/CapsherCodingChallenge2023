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
main.py is the heart of our game. main keeps track of the current game state, of which there are 5: start screen, game screen before round, game screen during wave, victory screen, and defeat screen. main also has to keep track of all of the buttons on the current screen. If the player is currently on the start screen, the program checks whether a mouse click has happened, and if it has, it checks whether or not the mouse click happened within the bounds of the start button. \
Once the start button has been pressed, the program changes the screen to the game screen before round. On this screen the program must keep track of the play button, the shop button, and whether or not the player has clicked on a tower. If the player has clicked on a tower then the range of the tower as well as the sell button are displayed, when the player clicks off the tower the "clicked tower" state is set to false and as a result the range and sell button disappear. If the "clicked tower" state is true and the player clicks on the sell button, then the program sets the "clicked tower" state to false and also gets rid of the tower (removes the tower from the current list of towers on the screen) as well as refunds the player half of the tower's initial cost by updating the money display. When the shop button is pressed, the screen displays the shop panel. All of the buttons within the shop panel are handled by shop.py. If the shop panel is active and the player presses the shop button again, the shop panel vanishes. When the play button is pressed the program loads the next round, (stored in round.py) and advances to the game screen during wave screen. \
The game during wave screen has to keep track of a lot things. It must keep track of 1.) the enemies currently on the screen 2.) the enemies yet to be loaded onto the screen, and when to deploy them 3.) the projectiles currently on the screen 4.) the towers on the screen, telling them to shoot 5.) any collisions that may happen 6.) felled enemies and updating the players cash 7.) player's remaining lives. The collision handling is done in the collisions.py file and runs in $\Theta(EP)$ where E is the number of enemies on screen and P is the number of projectiles on screen. This is probably the most inefficient algorithm in our code, and if we were looking to improve efficiency this would be the first place to look. To keep track of enemies on screen and enemies yet to be loaded we used two lists which we update whenever a new round is loaded, a new enemy is deployed, and whenever an enemy is defeated. To keep track of deployment we just deploy whenever the current game counter % round delay == 0. This makes it so that an enemy is deployed every round delay ticks, when an enemy is deployed it is popped from the current to be deployed list and appended to the enemies on screen list. When a collision does happen, the enemies health is depleted by the damage of the projectile it was hit by. If the enemies health is less than or equal to 0, then it is removed from the enemies on screen list and the player gains $x$ amount of money. Currently $x = 4$, but this could change in the future. Money gained is not dependent on the enemy type, all enemies are worth $x$ amount of money. The program also keeps track of player health. If the player health reaches 0, the defeat screen is displayed. If the player reaches the end of the round without losing all of their lives, and this is the final round, then the victory screen is displayed. Else, the screen before round screen is displayed again. 
The defeat screen only keeps track of the "again" button. Upon being clicked the player is redirected back to the start screen \
The victory screen is pretty much the same as the defeat screen. Again it just keeps track of the "again" button which upon being pressed redirects the player back to the start screen. \


### Enemy

### Shop

### Tower

### Projectile

### Art
