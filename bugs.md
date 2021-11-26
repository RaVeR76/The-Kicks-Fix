# Bugs

## Overview
I know that most of the ***BUGS*** or ***ISSUES*** I found were relatively simple and probably downright stupidity, on my part, in some cases but for this project I had created an Excel spreadsheet to help me log them. It also had a diary of my work on a day to day basis and a page for ALL my bugs I encountered no matter how big or small. It also hand some project tips, comments as I went along, any credits for code, images, etc and ALL my Django model data as regards my Products and associated info like Brands, Colours, Types and so on.


## **[Bug 1](https://github.com/RaVeR76/The-Kicks-Fix/issues/1)**   

### **Dropdowns wouldn't work on any navbar menus**

* **Issue**  
I had labelled each dropdown-item as another dropdown-menu …. D'OH !

* **Fix**  
Just correct the error above by labelling correctly, as drop-down items

* **Verdict**  
Simple bug to start off


## **[Bug 2](https://github.com/RaVeR76/The-Kicks-Fix/issues/2)**  

### **Dropdown item hover custom CSS doesn't change the colour**

* **Issue**  
Couldn't get my dropdown item hover colour to change from the default white

* **Fix**  
No fix found and the bug is still *open* in my Github page

* **Verdict**  
I tried my best for a few hours looking through Bootstrap documentation & within the Slack Community but no joy. You could do it in previous versions but BS4 is a No No unfortunately. I think you can override it in the SCSS of BS but I don't want to mess things up as it's not that important. Just would've been a nice wee touch !

## **[Bug 3](https://github.com/RaVeR76/The-Kicks-Fix/issues/3)**  

### **Navbar Toggle Icon Not Displaying**

* **Issue** 
My navbar toggle icon would not display at all when on mobile view

* **Fix**  
I added the 'navbar-light' class to my navbar in base.html which enabled the burger icon to appear & changed the background colour of the ```navbar-toggler``` in the CSS to my Minion Yellow

* **Verdict**  
I think it all looks and works well for the overall view on smaller screens


## **[Bug 4](https://github.com/RaVeR76/The-Kicks-Fix/issues/4)**   

### **UPPERCASE CSS Wouldn't Work !**

* **Issue**    
I tried to add my own CSS to change the titles of my project to UPPERCASE but it wouldn't work

* **Fix**  
Realised that my version of Bootstrap 4 used it's own Text Transform - ```text-uppercase``` within the HTML

* **Verdict**  
Another simple fix, thankfully


## **[Bug 5](https://github.com/RaVeR76/The-Kicks-Fix/issues/5)** 

### **Model Errors At First Attempt**

* **Issue**  
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


## **[Bug 6](https://github.com/RaVeR76/The-Kicks-Fix/issues/6)**  

### **More Model Errors**

* **Issue** 
Still had similar issues to previous bug, **Bug 5**, when I did a dry run on my Kicks App even though I had made my Common App first & imported the three models from my Common App.

* **Fix**  
This was due to the fact I needed to add *common*, i.e. ```common.Category```, instead of just *Category* to my ForeignKeys for all three imports. Plus I needed to install Pillow for my imageField to work. You can see this change in the secong image above.

* **Verdict**  
Once I fixed the above issues, I was error free :)

![My Kicks Migration](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/kicks-migration.png)


## **[Bug 7](https://github.com/RaVeR76/The-Kicks-Fix/issues/7)**  

### **Adding An Extra Field To Kicks Model Error**

* **Issue**   
Forgot to add 'Price' to my Kicks model & when I tried to do it, it came up with an error saying I needed a 'Default' value.

* **Fix**  
Added 'default=0.00' to my price field which solved the issue

* **Verdict**  
Simple enough fix but I just panic when I see migration errors ha ha


## **[Bug 8](https://github.com/RaVeR76/The-Kicks-Fix/issues/8)**  

### **CSS Stopped Working !**

* **Issue**    
My CSS just stopped working all of a sudden or maybe it didn't even work when I started my laptop to be honest but when I came to add some new CSS, it just wouldn't work. I tried 'Hard Refreshes' over & over again. I rebooted my laptop twice but still no joy. I trawled through my code to see if I had made a mistake but found nothing. I then tried another different project but this was the same so I knew it was a common CSS problem.  
At first I thought it was a Gitpod update or something but could not find any online info about it. Next I thought it was due to the installation of my new webcam & the driver had messed sh!t up ..... believe me I was clutching at straws & my head was severely melted.

* **Fix**  
This BUG near killed me tonight as I have wasted a whole evening trying to fix it. In the end I needed to clear my Chrome browsing data which included 'Browsing History', 'Cookies and other site data' & 'Cached images and files'. I did this for the last 24 hrs as I wasn't sure how far I needed to go back. In the end this killed the BUG instead of me but I am still so annoyed about it. I guess I know that it won't take as long to solve it next time as this BUG is imprinted in my wee Coding Brain now :)

* **Verdict**  
Rough evening was had by all, well me just, but I got there in the end and another hard lesson learnt

![CSS - Clear Everything](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/css-not-working.png)


## **[Bug 9](https://github.com/RaVeR76/The-Kicks-Fix/issues/9)**  

### **Image Wouldn't Display**

* **Issue**  
Couldn't get my first image to work when I was testing. It worked perfectly until I added an if / else statement so that if there was no image, it would display 'No Image'

* **Fix**  
After an hour or so, and much trawling through my code. I realised I had used the wrong description of ```{% if kicks.image %}``` instead of ```{% if kicks.image1 %}``` !!!  
I was using three images for my individual product details page so the first image was used on my main products pages (aka Kicks or Accessories), as I only required one image here.

* **Verdict**  
Super annoying issue as it was a simple fix but took me a while to detect the error, as the only difference was the number 1


## **[Bug 10](https://github.com/RaVeR76/The-Kicks-Fix/issues/10)**  

### **Card Border Issue**

* **Issue**  
Tried adding a border to each card image to separate the image from the name & price but it wouldn't work or display.

* **Fix**  
I guessed that the image was hiding the border so tried adding a 'border-top' to the Card Body & it worked

* **Verdict**  
Simple enough fix to be fair


## **[Bug 11](https://github.com/RaVeR76/The-Kicks-Fix/issues/11)**  

### **Image Carousel Indicators Glitching**

* **Issue**    
I made ALL images, apart from a few I missed unfortunately, 400px x 400px just for simplification and site display purposes. 
I have only loading twelve images until I am sure everything is working properly throughout my project then I will add the rest at the end.

When images 3.jpg & 6.jpg scrolled along in their image carousels .... the Carousel Indicators glitched very slightly, for some reason.

* **Fix**  
If you added the images again to the Django Kicks DB manually (which I did for all images and data), so they change names they worked okay although 6.jpg still has a slight glitch. 
So weird and this issue occurred on the 26/10/21. I checked today 18/11/21 and they are working fine so not sure what has happened but it's fixed itself :)
I closed the issue on my Github too, as I had left this open for future investigation.

* **Verdict**  
All images look well on their main product pages respectively but more so on their individual detail pages, where the magic happens within my carousels


## **[Bug 12](https://github.com/RaVeR76/The-Kicks-Fix/issues/12)**  

### **Django Admin Issue**

* **Issue**   
I was trying to organise my Accessories Admin and it threw up an Attribute Error saying 'type' is ***not callable***

![Wee Admin Issue](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/accessory-admin-issue.png)

* **Fix**  
In my Accessories model I had simply labelled it as accessory_type so once I changed it to this in Admin it worked fine

* **Verdict**  
Another easy fix and an oversight on my part


## **[Bug 13](https://github.com/RaVeR76/The-Kicks-Fix/issues/13)**  

### **Template Wouldn't Open**

* **Issue**   
Created my accessory_detail views, urls & template but when I clicked on an accessory image it wouldn't open the accessory_detail page for that particular accessory.
Checked the views & urls over again & again. When I added ```accessories/1``` onto the end of my project address, it would open my template no problem.

* **Fix**  
Found that the issue was I hadn't added my href to the images in my accessories.html !!!  
Simple solution & I'm glad to say it didn't take too long to solve but still, it had to be resolved :)

* **Verdict**  
Another easy fix and another oversight on my part


## **[Bug 14](https://github.com/RaVeR76/The-Kicks-Fix/issues/14)**  

### **Queries Not Working**

* **Issue**   
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


## **[Bug 15](https://github.com/RaVeR76/The-Kicks-Fix/issues/15)**  

### **Brands Wouldn't Display In Navbar Dropdown**  

* **Issue**  
I wanted to display ALL my available Brands in each submenu under Men (just for starters) but couldn't get it working.
I created a FOR LOOP in my large-nav to iterate through all the Brands but it just wouldn't work.
The submenu was just blank.

* **Fix**  
I realised I needed to Import Brand to my home view, create a context dict with the Brands & pass it through to the home page. It worked so I could use the list to filter Kicks by Brands. I also needed to do this in my Kicks view too to make it work there.

* **Verdict**  
It took a wee while to figure it out but I have to say it looks so good and I am super happy with the end product


## **[Bug 16](https://github.com/RaVeR76/The-Kicks-Fix/issues/16)**  

### **JavaScript Wouldn't Work When Moved From Template Page**  

* **Issue**    
I made a JavaScript file in a JS folder in the main Static folder and I moved my JavaScript code for my Brands submenu into it but I could not get it to work so I had to move it back. This happened me before in a previous project and I had to keep it on the actual page that was using it and if another page required the same code, I would've had to copy it to that page too.

* **Fix**  
No fix for this bug but at least the JavaScript still works.


* **Verdict**  
Maybe later I look at it again (It works where it is, anyway)


## **[Bug 17](https://github.com/RaVeR76/The-Kicks-Fix/issues/17)**  

### **Types Disappeared After First Selection**  

* **Issue**    
When I chose a Type from the Accessory menu, it displayed ALL the accessories of that type but when I went to the submenu again to choose another type my list of types had vanished. I checked my code & found the issue quite quickly thankfully !

* **Fix**  
In my accessories views, I had created a Type filter for when the user had selected a type from the navbar submenu. I had called my ```GET``` variable ```types``` so when I put this in the *context* it override my initial ```types``` variable, for **ALL** types. I simply changed my ```GET``` variable to ```chosen_type``` and this solved the issue.

* **Verdict**  
Simple fix for for a simple problem


## **[Bug 18](https://github.com/RaVeR76/The-Kicks-Fix/issues/18)**  

### **Sex Filter Overriding Everything**  

* **Issue**    
My Kicks pages titles code ```{{ kicks_title }}``` worked no problem for New In and Sales but when I tried adding it to the Sex filter, this override the New In and Sales ones. It would only display titles like *'All Male Kicks'* instead of *'All New In Male Kicks'* like before

* **Fix**  
I added ```if 'category' not in request.GET:``` which allowed me to stop my sex queries overriding my Category Kicks title.
I did encounter more issues with these filters down the line though and **Sex** was always at the center of it, see next bug too.

* **Verdict**  
I had to do trial and error to get this part right which I did in the end but when I added the filter bar .... a whole new level of pain was opened ha ha !


## **[Bug 19](https://github.com/RaVeR76/The-Kicks-Fix/issues/19)**  

### **Sex Filtering Again Causing An Issue**  

* **Issue**    
SEX and 'BRAND OR STYLE' won't filter to display the images & title for the Navbar Sex only selection i.e. All Mens Kicks or All Womens Kicks.
The title kept saying ALL Kicks & displayed All the Kicks images, it wouldn't filter as per chosen Sex on the Nav

* **Fix**  
I added a **PASS** for each of the 'Category', 'Brand' & 'Style' when ```not in request.Get```'s consecutively so eventually it gets to Sex and forgets about the rest allowing me to display my ALL ```chosen_sex``` Kicks title & the chosen 'Sex' kicks images. This bug tormented me as I wanted all my titles to display depending on what the user selected by nav or filter bar :)
I added an image of what I mean below so you can understand, plus I have added Colours now too within my filters.

![Sex Query Issue](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/sex-query-issue.png)

* **Verdict**  
I did have to mess about with my query code to try and get this right. It took a while but again I am super happy with how it turned out and displays on the page. 
You can click on any of the Nav options, like Mens -> Brand -> Adidas, and it displays all the men's Adidas Kicks with the title changing to whatever the user has selected.
This works for all options for Kicks and Accesories but there is no sex option for accessories though, as they are pretty much all unisex.  
P.S. I know there is probably one line of code out there that can do this in one go but I made this work for me so I am happy.


## **[Bug 20](https://github.com/RaVeR76/The-Kicks-Fix/issues/20)**  

### **Two Different Products With Same PKs**  

* **Issue**    
When I add an item from Kicks and an item from Accessories that have the same *id* number then the quantity adds together for that *id* number.
I needed to formulate some way of separating these items or it was game over.

* **Fix**  
I changed my original **item_id** for Kicks from ```kicks.id``` to ```kicks.sku``` and for Accessories from ```accessories.id``` to ```accessories.sku```. This works so far and I can see the different items in my terminal accumulating :)

* **Verdict**  
I'm glad I got passed this issue at this moment in time but I knew similar issues would pop up later into this project. I think I maybe started off with not the greatest Schema by having two products in different apps but then a again there has to be some way around it. I'll look into this after my project is complete as this did cause me a lot of grief throughout my project.


## **[Bug 21](https://github.com/RaVeR76/The-Kicks-Fix/issues/21)**  

### **Adding To Bag Problems**  

* **Issue**    
I couldn't get the bag to add both Kicks and Accessories. I couldn't work it out as I was using SKU for both products when added to bag but it was causing all sorts of errors when I was checking an Accessory SKU within the Kicks database and vice versa. In the end I figured a method out which might not be right or the best way but it works for now.

* **Fix**  
Within ```bag_contents``` in the ```contexts.py```, as I was using SKU because of the bug, *Bug20* above where the two different products had many of the same PKs, I needed to differentiate between the two SKUs for this bug. By luck I didn't have any proper SKUs for my Accessories that I found online so made these up and they all started with **RAVE** ha ha. So I just added a wee bit of code to check if the ```item_id``` in the bag had the word 'RAVE' in it. If it didn't have 'RAVE' it was a Kicks item so I get the object from my Kicks db and if it did have 'RAVE' it was an Accessory item so I get the object from my Accessories db. Talk about a stroke of luck tbh as my head was about to explode on this bug !!!

* **Verdict**  
I the end this solve this bug at this time so I was happy again, although this piece of ingenious code was removed at a later date, as I utilised the fact that my Kicks would have sizes and my Accessories would not which made it a little easier to work with. Plus I used this fundamental difference on various occasions through my project to differentiate  between the two products.


## **[Bug 22](https://github.com/RaVeR76/The-Kicks-Fix/issues/22)**  

### **JSONField Issues**  

* **Issue**    
Just had a few issues trying to get my JSONfield data to split into the proper lists for UK, EU and US

* **Fix**  
This Django field is fairly new so there wasn't a lot of info online but I persevered and figured it out so I am so happy to utilise this method within my project.  

Below is my jsonField in Django Admin for Kids Sizes where Mens and Womens are similar but obviously different sizes  
![Django Kids Sizes jsonField](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/kids-sizes-json.png)  

And here is my code for splitting them up so I could give the user the three different size options per sex, for selection on the Kicks details page and therefore be able add them to the bag for purchase.  
![Django Kids Sizes jsonField](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/kids-sizes-view.png)  

* **Verdict**  
To be honest maybe sizes wasn't the best option to use it for, as realistically the sizes won't change but at least I got it working and may be handier used in future projects.
This was probably my proudest part of the whole project, getting this working on the Kicks details page and I did have to mess about with the JavaScript, see Bug 23 below, to get it to work but I got there and personally, I think it's an amazing wee touch !!!


## **[Bug 23](https://github.com/RaVeR76/The-Kicks-Fix/issues/23)**  

### **JavaScript For Differentiating Between Sexes**  

* **Issue**    
Had an absolute nightmare trying to get the JavaScript logic working for displaying Kids and Female sizes on the Kicks_detail page depending on whether the Kicks is for kids or for females. It would only work for Kids but not Female and vice versa. I hadn't even introduced Mens Sizes at this point ha ha ! 

* **Fix**  
To be honest I am not sure what the issue was as I spent a whole evening (approx. 5 hours) trying to get it working but I am one that never gives up so I kept going and eventually got it working. It was either the fact that my 'if' statements within my click functions where comparing 'ID' elements that weren't there because I had them looking to see if it was kids kicks or female kicks. Or it could've been simple '=' or '==' stupidity within my ```if``` statements too.

* **Verdict**  
In the end I stripped it all back and got rid of a lot of code that may have been causing the problem and to be honest it looks a lot better and **IT WORKS !!!!**  
I know my code isn't the best but I was so happy to get this part of my project working, as it just adds that little ***je ne sais quoi*** to it, in my opinion. Below is an example of my code for UK sizes with EU sizes and US sizes similar. 

![Sex Differentiation](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/sex-differentiation.png) 


## **[Bug 24](https://github.com/RaVeR76/The-Kicks-Fix/issues/24)**  

### **I Forgot About Unisex Option In My Kicks**  

* **Issue**    
After being so HAPPY to get my JavaScript working for the previous bug, Bug 23, for displaying ALL the different sizes for Kids, Females & Males depending on UK, EU or US being selected …... ANOTHER BUG arises ha ha !!!
I could curl up and die right now to be honest but hey, this is the coding life ain't it lol !!!
I only went and forgot about my Kicks SEX option of UNISEX ..... so not sure how to go about that at this point as I love my Size Options for the others.
I had some Kicks set out as Unisex so they would be displayed either within the Mens pages or the Females pages, as a lot of Kicks are Unisex. This worked really well for my navbar filters but when I came to this point, I needed to make a decision.

* **Fix**  
No fix for this issue at the moment  

* **Verdict**  
I have left ALL unisex options out for my Kicks in the database and I am only using Male, Female or Kids as the selected options.
