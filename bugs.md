# Bugs

## Overview
I know that most of the ***BUGS*** I found were relatively simple but for this project I had created an Excel spreadsheet which had a Diary of my work on a day to day basis and a page for ALL my bugs I encountered no matter how big or small. It also hand some project tips, comments as I went along, any credits for code, images, etc and ALL my Django model data as regards my Products and associated info like Brands, Colours, Types and so on.

### **Dropdowns wouldn't work on any navbar menus**

* [Bug 1](https://github.com/RaVeR76/The-Kicks-Fix/issues/1)  
I had labelled each dropdown-item as another dropdown-menu …. D'OH !

* **Fix**  
Just correct the error above by labelling correctly, as drop-down items

* **Verdict**  
Simple bug to start off


### **Dropdown item hover custom CSS doesn't change the colour**

* [Bug 2](https://github.com/RaVeR76/The-Kicks-Fix/issues/2)  
Couldn't get my dropdown item hover colour to change from the default white

* **Fix**  
No fix found and the bug is still *open* in my Github page

* **Verdict**  
I tried my best for a few hours looking through Bootstrap documentation & within the Slack Community but no joy. You could do it in previous versions but BS4 is a No No unfortunately. I think you can override it in the SCSS of BS but I don't want to mess things up as it's not that important. Just would've been a nice wee touch !


### **Navbar Toggle Icon Not Displaying**

* [Bug 3](https://github.com/RaVeR76/The-Kicks-Fix/issues/3)  
My navbar toggle icon would not display at all when on mobile view

* **Fix**  
I added the 'navbar-light' class to my navbar in base.html which enabled the burger icon to appear & changed the background colour of the 'navbar-toggler' in the CSS to my Minion Yellow

* **Verdict**  
I think it all looks and works well for the overall view on smaller screens


### **UPPERCASE CSS Wouldn't Work !**

* [Bug 4](https://github.com/RaVeR76/The-Kicks-Fix/issues/4)  
I tried to add my own CSS to change the titles of my project to UPPERCASE but it wouldn't work

* **Fix**  
Realised that my version of Bootstrap 4 used it's own Text Transform - 'text-uppercase' within the HTML

* **Verdict**  
Another simple fix, thankfully


### **Model Errors At First Attempt**

* [Bug 5](https://github.com/RaVeR76/The-Kicks-Fix/issues/5)  
Tried my first model & loads of errors appeared !  
I was going to split my apps into a Kicks app, an Accessories app & a Common app then link them all together.

![My First Migration](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/my-first-migration.png)

* **Fix**  
I had tried to add my Kicks app first but I needed to add my Common App first, as this had 3 ForeignKey fields that were linked to my Kicks App.
Schoolboy error but I now know the craic now.

![My First Migration Fixed](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/my-first-migration-fix.png)

* **Verdict**  
Not going to lie all them red errors scared the life out of me but after I figured the structure out and as the project went along, I got think I got better at it.  
I'm not a Django wizard by all means but I think it's an awesome framework and one I will deffo be looking to use again ..... only more organised.

![My Kicks Migration](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/kicks-migration.png)


### **More Model Errors**

* [Bug 6](https://github.com/RaVeR76/The-Kicks-Fix/issues/6)  
Still had similar issues to previous bug, **Bug 5**, when I did a dry run on my Kicks App even though I had made my Common App first & imported the three models from my Common App

* **Fix**  
This was due to the fact I needed to add 'common' (i.e. 'common.Category') instead of just 'Category' to my ForeignKeys for all three imports. Plus I needed to install Pillow for my imageField to work. You can see this change in the secong image above.

* **Verdict**  
Once I fixed the above issues, I was error free :)

