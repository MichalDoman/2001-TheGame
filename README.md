# 2001-TheGame (workshop exercise)

### Starting the game:

This application works with the Flask library. It uses some functions from my DiceSimulator app. When the program is
started, the user will firstly be presented with starting screen that states the goal of the game.

![](https://github.com/MichalDoman/2001-TheGame/blob/main/images/Screenshot_1.png)

### Rules and gameplay:

The user can win if they get 2001 points before computer does. In this version of dice throwing game, there are all
available dice types shown in a list. In every turn you choose two types of dice (can be 2 different), and the throws
are generated. Computer's dice are chosen at random. Then you can see the outcome of yours and computer's throws, as
well as the dice types that computer was using. If sum of both throws was equal to 7, total score is divided by 7. On
the other hand, if the sum of both throws is equal 11, total score is multiplied by 11.

![](https://github.com/MichalDoman/2001-TheGame/blob/main/images/Screenshot_2.png)

When someone get 2001 points or more, the endgame screen is shown.

![](https://github.com/MichalDoman/2001-TheGame/blob/main/images/Screenshot_3.png)

### How to run:

To run this application, it is required to have Flask library downloaded. After you run the script, you can view the app
on your localhost:5000/2001 on your browser.
