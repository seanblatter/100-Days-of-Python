print("""                                                  ______    ____                                                                     
            ..'''' |`````````,       .'.        .~      ~. |                   |`````````, | `````````:' `````````:'       .'.       
         .''       |'''''''''      .''```.     |           |______             |'''''''''  |       ..'         ..'       .''```.     
      ..'          |             .'       `.   |           |                   |           |   ..''        ..''        .'       `.   
....''             |           .'           `.  `.______.' |___________        |           | .:,,,,,,,,, .:,,,,,,,,, .'           `. 
                                                                                                                                     

""")
import time
time.sleep(2)
print("""
 .              +   .                .   . .     .  .
                   .                    .       .     *
  .       *                        . . . .  .   .  + .
            "You Are Here"            .   .  +  . . .
.                 |             .  .   .    .    . .
                  |           .     .     . +.    +  .
                 \|/            .       .   . .
        . .       V          .    * . . .  .  +   .
           +      .           .   .      +
                            .       . +  .+. .
  .                      .     . + .  . .     .      .
           .      .    .     . .   . . .        ! /
      *             .    . .  +    .  .       - O -
          .     .    .  +   . .  *  .       . / |
               . + .  .  .  .. +  .
.      .  .  .  *   .  *  . +..  .            *
 .      .   . .   .   .   . .  +   .    .            + """)


print("Yooo, whats up little alien dude!")
time.sleep(1.25)
print("Welcome to Earth, lots of crazy stuff happens here man!")
time.sleep(1.25)

print("My names Surfer Willy, and I like to surf the cosmic waves of the universe.")
name = input("What should I call you? ")
alien_world_name = input(f"Dope name {name}, what planet do you come from?")

if alien_world_name == "Earth":
    print("Wow! Two planets named Earth? I wonder which one was called Earth first!")
else: print(f"Woah! {alien_world_name} sounds like a cool place! We should go sometime!")

time.sleep(1.25)

would_you = input("Do you want to know where I was born? Tyes Y or N ")
if would_you == "Y":
    print("How considerate! I was actually born on the planet of P1ZZ@, on the fifth millenium of the reign of the mighty pepperoni.")
else: print("You rude piece of shit, hopefully your attitude gets better. I was born on the plannet P1ZZ@!")
time.sleep(4.25)

print("Anyways! I hope that you are hungry, because these Earthlings sure know how to make a pizza!")
time.sleep(3)

print("For your first meal here, I am going to take you to the best pizza parlor in town!")

time.sleep(2.23)

pizzatype = input("Personally my favorite slice here is the Pepperoni, but the Vegetarian is also very good.\n They have every type of slice here, so if you want something else, let them know! ")
time.sleep(2.23)



if pizzatype == "Pepperoni":
    print("Good choice! Let's order two slices to go.")
elif pizzatype == "Vegetarian":
    print("I love olives and peppers on my pizza! Lets order to go.")
else:
    print(f"{pizzatype} is my second favorite slice! Right after pepperoni! ")

choice1 = input(f"Should we eat at home or the park, {name}? ")

if choice1 == "home":
    choice2 = input("Do you want to 'speed' or go the 'speedlimit' on our way home?")
    if choice2 == "speedlimit":
        choice3 = input("Now that we are in the neighborhood, is your house the red, yellow, or green one?")
        if  choice3 == "red":
            print("Why the hell did you go with red?")
        elif choice3 == "yellow":
            print ("You want to look like the sun or something?")
        elif choice3 == "green":
            print ("Yes- the shrek house is the only house.")
