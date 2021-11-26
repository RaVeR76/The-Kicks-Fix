# Bugs

## Overview
I know that most of the ***BUGS*** or ***ISSUES*** I found were relatively simple and probably downright stupidity, on my part, in some cases but for this project I had created an Excel spreadsheet to help me log them. It also had a diary of my work on a day to day basis and a page for ALL my bugs I encountered no matter how big or small. It also hand some project tips, comments as I went along, any credits for code, images, etc and ALL my Django model data as regards my Products and associated info like Brands, Colours, Types and so on.

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
I added the 'navbar-light' class to my navbar in base.html which enabled the burger icon to appear & changed the background colour of the ```navbar-toggler``` in the CSS to my Minion Yellow

* **Verdict**  
I think it all looks and works well for the overall view on smaller screens


### **UPPERCASE CSS Wouldn't Work !**

* [Bug 4](https://github.com/RaVeR76/The-Kicks-Fix/issues/4)  

I tried to add my own CSS to change the titles of my project to UPPERCASE but it wouldn't work

* **Fix**  
Realised that my version of Bootstrap 4 used it's own Text Transform - ```text-uppercase``` within the HTML

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


### **More Model Errors**

* [Bug 6](https://github.com/RaVeR76/The-Kicks-Fix/issues/6)  

Still had similar issues to previous bug, **Bug 5**, when I did a dry run on my Kicks App even though I had made my Common App first & imported the three models from my Common App

* **Fix**  
This was due to the fact I needed to add *common*, i.e. ```common.Category```, instead of just *Category* to my ForeignKeys for all three imports. Plus I needed to install Pillow for my imageField to work. You can see this change in the secong image above.

* **Verdict**  
Once I fixed the above issues, I was error free :)

![My Kicks Migration](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/kicks-migration.png)


### **Adding An Extra Field To Kicks Model Error**

* [Bug 7](https://github.com/RaVeR76/The-Kicks-Fix/issues/7)  

Forgot to add 'Price' to my Kicks model & when I tried to do it, it came up with an error saying I needed a 'Default' value.

* **Fix**  
Added 'default=0.00' to my price field which solved the issue

* **Verdict**  
Simple enough fix but I just panic when I see migration errors ha ha


### **CSS Stopped Working !**

* [Bug 8](https://github.com/RaVeR76/The-Kicks-Fix/issues/8)  

My CSS just stopped working all of a sudden or maybe it didn't even work when I started my laptop to be honest but when I came to add some new CSS, it just wouldn't work. I tried 'Hard Refreshes' over & over again. I rebooted my laptop twice but still no joy. I trawled through my code to see if I had made a mistake but found nothing. I then tried another different project but this was the same so I knew it was a common CSS problem.  
At first I thought it was a Gitpod update or something but could not find any online info about it. Next I thought it was due to the installation of my new webcam & the driver had messed sh!t up ..... believe me I was clutching at straws & my head was severely melted.

* **Fix**  
This BUG near killed me tonight as I have wasted a whole evening trying to fix it. In the end I needed to clear my Chrome browsing data which included 'Browsing History', 'Cookies and other site data' & 'Cached images and files'. I did this for the last 24 hrs as I wasn't sure how far I needed to go back. In the end this killed the BUG instead of me but I am still so annoyed about it. I guess I know that it won't take as long to solve it next time as this BUG is imprinted in my wee Coding Brain now :)

* **Verdict**  
Rough evening was had by all, well me just, but I got there in the end and another hard lesson learnt

![CSS - Clear Everything](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/css-not-working.png)


### **Image Wouldn't Display**

* [Bug 9](https://github.com/RaVeR76/The-Kicks-Fix/issues/9)  

Couldn't get my first image to work when I was testing. It worked perfectly until I added an if / else statement so that if there was no image, it would display 'No Image'

* **Fix**  
After an hour or so, and much trawling through my code. I realised I had used the wrong description of ```{% if kicks.image %}``` instead of ```{% if kicks.image1 %}``` !!!  
I was using three images for my individual product details page so the first image was used on my main products pages (aka Kicks or Accessories), as I only required one image here.

* **Verdict**  
Super annoying issue as it was a simple fix but took me a while to detect the error, as the only difference was the number 1


### **Card Border Issue**

* [Bug 10](https://github.com/RaVeR76/The-Kicks-Fix/issues/10) 

Tried adding a border to each card image to separate the image from the name & price but it wouldn't work or display.

* **Fix**  
I guessed that the image was hiding the border so tried adding a 'border-top' to the Card Body & it worked

* **Verdict**  
Simple enough fix to be fair


### **Image Carousel Indicators Glitching**

* [Bug 11](https://github.com/RaVeR76/The-Kicks-Fix/issues/11)  

I made ALL images, apart from a few I missed unfortunately, 400px x 400px just for simplification and site display purposes. 
I have only loading twelve images until I am sure everything is working properly throughout my project then I will add the rest at the end.

When images 3.jpg & 6.jpg scrolled along in their image carousels .... the Carousel Indicators glitched very slightly, for some reason.

* **Fix**  
If you added the images again to the Django Kicks DB manually (which I did for all images and data), so they change names they worked okay although 6.jpg still has a slight glitch. 
So weird and this issue occurred on the 26/10/21. I checked today 18/11/21 and they are working fine so not sure what has happened but it's fixed itself :)
I closed the issue on my Github too, as I had left this open for future investigation.

* **Verdict**  
All images look well on their main product pages respectively but more so on their individual detail pages, where the magic happens within my carousels


### **Django Admin Issue**

* [Bug 12](https://github.com/RaVeR76/The-Kicks-Fix/issues/12)  

I was trying to organise my Accessories Admin and it threw up an Attribute Error saying 'type' is ***not callable***

![Wee Admin Issue](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/accessory-admin-issue.png)

* **Fix**  
In my Accessories model I had simply labelled it as accessory_type so once I changed it to this in Admin it worked fine

* **Verdict**  
Another easy fix and an oversight on my part


### **Template Wouldn't Open**

* [Bug 13](https://github.com/RaVeR76/The-Kicks-Fix/issues/13)  

Created my accessory_detail views, urls & template but when I clicked on an accessory image it wouldn't open the accessory_detail page for that particular accessory.
Checked the views & urls over again & again. When I added ```accessories/1``` onto the end of my project address, it would open my template no problem.

* **Fix**  
Found that the issue was I hadn't added my href to the images in my accessories.html !!!  
Simple solution & I'm glad to say it didn't take too long to solve but still, it had to be resolved :)

* **Verdict**  
Another easy fix and another oversight on my part


### **Queries Not Working**

* [Bug 14](https://github.com/RaVeR76/The-Kicks-Fix/issues/14)  

I could not get my queries working at all for Category=new_in & Sex=male which was really my first query I tried.
I knew once I figured this first one out then the rest would be easy.
I tried everything for hours and then I had to contact Tutor Support.
We tried for more hours to solve it between us and eventually we got there in the end :)

* **Fix**  
Firstly, I hadn't given my Sex model a name attribute so when I tried to filter this I was getting errors and I couldn't figure it out.  
Secondly, in my Kicks views I had removed the ```.split(',')``` from ```sex = request.GET['sex'].split(',')``` so the images wouldn't display.  
At the end I got there & that's all that matters even if my head was melted but sure ..... everyday is a school day !!!

* **Verdict**  
I always try my best to solve these issues myself and I generally do but I deffo neeeded help with this one and I'm glad **Tutor Support** was on hand to assist me.
I couldn't stop querying after I knew how to do it ha ha !


### **Brands Wouldn't Display In Navbar Dropdown**

* [Bug 15](https://github.com/RaVeR76/The-Kicks-Fix/issues/15)  

I wanted to display ALL my available Brands in each submenu under Men (just for starters) but couldn't get it working.
I created a FOR LOOP in my large-nav to iterate through all the Brands but it just wouldn't work.
The submenu was just blank.

* **Fix**  
I realised I needed to Import Brand to my home view, create a context dict with the Brands & pass it through to the home page. It worked so I could use the list to filter Kicks by Brands. I also needed to do this in my Kicks view too to make it work there.

* **Verdict**  
It took a wee while to figure it out but I have to say it looks so good and I was super happy with the end product
