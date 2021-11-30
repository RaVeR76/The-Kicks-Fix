# **Testing**

## Table of contents
---

- [**Testing**](#testing)
  - [Manual Testing](#manual-testing)
    - [Responsiveness](#responsiveness)
    - [Navigation & Search Functions](#navigation--search-functions)
    - [Home Page](#home-page)
    - [Registration](#registration)
    - [Login / Logout](#login--logout)
    - [Main Products Pages](#main-products-pages)
    - [Products Details Page](#products-details-page)
    - [The Bag Area](#the-bag-area)
    - [The Checkout](#the-checkout)
    - [Profile](#profile)
    - [Order History](#order-history)
    - [Admin Functions](#admin-functions)
    - [Contact Us and the KFC - Kicks Fix Club](#contact-us-and-the-kfc---kicks-fix-club)
    - [Overall Website Navigation, Functionality & Visual Experience](#overall-website-navigation-functionality--visual-experience)
  - [Validators](#validators)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
    - [Debug = True](#debug---true)

## Manual Testing

### Responsiveness

#### User Goals : The website will have to work well on all devices

#### **Test**
I utilised my own laptop connected to a large screen, my work laptop which has a fairly small screen, my tablet, my mobile phone and of course Chrome DevTools to test responsiveness across various platforms.  
Firstly I noticed that my ```{{ kicks_title }}``` were still large on smaller screens so were wrapping round a lot so I added some CSS to reduce the size on smaller screens. I had to settle for a happy medium here so the larger titles in length may wrap a little on smaller screens but it means the smaller titles are not super small on the largest small screens, if you get what I mean. Below is the small piece of CSS code I used to fix this issue.

```
h2.text-uppercase.product-title {
    font-size: 1.2rem;
}
```

Secondly, I noticed on mobile that my navbar dropdown submenus were only showing the top options whilst the rest were cut off at the bottom of the screen.
I added a submenu-wrapper class to each submenu and added some CSS to combat this. This is the problem when you build your project on a large screen but also the benefits of doing testing and really getting into your project on the smallest screens in DevTools.

```
ul.dropdown-menu.submenu-wrapper {
    height: 200px;
    overflow: auto;
}
```

I set my "Sorry, no Kicks available" text to center, on smaller screens, for when there are no kicks or accessories available because it looks much better in my opinion.  

I also noticed that my Profile link was not working and there was NO order history on small screens. I had just left my href link blank for Profile and I hadn't even added the code for my order history in my small-nav.html. I have made the additions and everything looks well.  

#### **Results**
The joys of testing really comes to fruition when you are manually testing your website and trying it on all different sizes. I found minor issue after minor issue when I tried the smallest screen available but nothing that made me panic. I just applied a little CSS to adjust various sizes of titles or text. The biggest one was my dropdown menu submenus for kicks Brand, Style, Colour & Types within accessories. Again, I used the smallest screen approximately 320px x 568px for the iphone5 and added the CSS as mentioned above. I think it works well across ALL portrait modes now but it's hard to get it exactly perfect for ALL screens no matter how good you are. It's definitely a lot better than my first project when I hadn't even taken screen sizes into account building my website for HTML and CSS .... that was a shock to the system but a good learning point.

#### **Verdict**
After throughily going through my website with a fine tooth comb, I did find some issues with the responsiveness as logged above but overall, I think it looks well and works well on all devices. 


### Navigation & Search Functions

#### User Goal : Navigate around the website with ease and pleasure
#### User Story : I want be able to search / filter the products by various options like male, female, kids, brands, styles and so on

#### **Test**
The various tests I carried out for the navigation and search functions are listed below:

- Click on the **Shop Now** button and make sure it takes the user to the ALL Kicks page
- Click on each navigation link to make sure it directs the user to the correct page
- Check that when the user clicks on any dropdown submenu link that it takes them to the correct page
- Check that when the user arrives on the selected page that the associated Title is displayed, i.e Women's Adidas Kicks or Kid's Running Kicks
- Check ALL navigation is functioning through my 'hamburger button' on tablets and mobile devices
- Hover over dropdown navigation links to see if hover style has been applied
- Check if the dropdown navigation link has applied style when clicked and directed to a page
- Check that my *Back To Top* button is working
- Check that the *Go To Secure Checkout* on the Success Toast, for updating the bag, takes the user to the checkout page
- Check ALL buttons do what they are designed to do
- Check that the search bar will search for any query as regards a set of Kicks (Accessories wasn't added at to this)
- Click on the The Kicks Fix logo from anywhere in the site on, on large screens, to make sure it navigates the user to Home Page

#### **Results**
Everything looks good apart from my quantity buttons on large screens, I had a go at trying to fix this last night but I was wasting too much time with so little of it left. I'm pretty sure this is similar to the bug I logged on Github and in my bug section **BUG 26** where because I am using IDs for the two buttons, they will only disable the button in the first instance. And because I am using the Products ID which is SKU in my case, if I added two Kicks but of different sizes, the second set of quantity buttons don't work.  I still haven't a fix for this as of yet but I haven't closed my Bug Issue on it yet so I will leave it open.  
That saying, this bug is similar and because I was utilising the CI code, I checked it out on Slack and it's because of a similar reason. On the smaller screens the buttons become disabled but on the larger screen it won't because the IDs are used in the same places. Like I said before I wasted a good 2 hours last night when I really need to invest that in the testing so I will just put it down to an annoying bug but deffo look at it after I get my result.  

Also, I noticed that when testing the overall navigation and search functions that I had created a silly bug whilst fixing an issue within the Responsiveness testing and it took me a few minutes to notice how to fix it ha ha.  

Lets see if you can notice it before scrolling on:  
![Account Dropdown Issue](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/account-dropdown-issue1.png)

Here is is how it looked with the issue:  
![Account Dropdown Issue](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/account-dropdown-issue1a.png)

#### **Verdict**
All in all, I am very happy with everything apart from the quantity button issue but I will have a look at it at a later date and find a solution that works for it all. I know adding classes instead of IDs is the way but when I tried last night I was disabling them **ALL** or disabling **NOTHING** ! but I will solve it, don't you worry :)

### Home Page

#### User Goal : An enticing landing page that will make any user enthralled to delve deeper into my website

#### **Test**
To be honest there is nothing really to test here as the majority of the testing was done previously with ALL the navigation links tested. Realistically, there is only a Hero Image, Slogan and an Enter the Shop button. These all test perfectly. The navbar and all links were tested above. 
I tested the logo so that it would return the user to this homepage as well. I can change the slogan in Django admin and it will change on screen. I really wanted some site Admin to be able to make all these changes but again I have added this to future upgrades, as time is of the essence. 

#### **Results**
I had quite a few hero images downloaded from the internet for testing out on my homepage and I'm sure everyone of them would've looked good here.   
But once I utilised two of my chosen colours from the start for this project, ***Eerie Black*** and ***Minion Yellow*** as my main navbar colours, I knew straight away that this was the image, that was to be my Hero ! It's simple, it's dark and mysterious and it says I need new pair of Kicks right now because let's face facts, we all have a few pairs of ropey, well used Kicks floating about the house .... just like the pair in the image !  
I only had to adjust the hero image to make it smaller so it would display better but this was way at the start of the project.
Although last night when I started looking at everything on the smaller screens, I noticed that the Kicks in the image were nowhere to be seen which kind of annoyed me. So I added a bit of CSS to fix this for the smaller screens and, I'll be honest, for such a small change it just makes the Homepage look so much better. I used CSS to position the Kicks part of the image as centrally as I could on smaller screens.  

The code I used is below:  
![Hero Image Positioning On Smaller Screens](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/hero-image-centrally.png)

#### **Verdict**
Overall, I love The Kicks Fix homepage and as the User Story says, I am enthralled to delve deeper to see what is behind this dark and wonderful image .... and buy me some Kicks of course !

### Registration

#### User Story : I want to be able to register for an account so that I can have access to unique promotions and discounts

#### **Test**
The following tests are listed below that I complied and carried out :

- Click on the *sign in* link and make sure it takes the user to login page (so that if the user has registered before)
- Click on the Register link in Account dropdown
- Try to Register with empty input fields
- Try to register with two different passwords
- Try to register with a password less than 8 characters
- Try to register with a password that is common word, like ***qwerty12***
- Try to register with the same existing username
- Try to Register with a wrong email address, by leaving out the @ or using a comma instead of a dot
- Check that an Alert Message appears after registration has been successful to say an email has been sent to the email address used at registration
- Check that the confirmation email has a link to confirm registration and that when he link is clicked ... the user is directed to The Kicks Fix confirmation page
- Check that when the user confirms their email on The Kicks Fix confirmation page that they are navigated to the login page

#### **Results**
 All tests passed that were tried above. When errors where input, Allauth displayed an error message stipulating what the issue was like *Password too common* or you need to use 8 characters for the password. I tired everything to get passed Allauth but Allauth says NO .... well, without properly registering for The Kicks Fix. I did add a few wee changes to the email confirmation message as it needed a little touch up in areas, once I read it through but apart from that everything else was excellent.

#### **Verdict**
Tests passed, works as expected, no bugs were found during the testing. Functionality covered.


### Login / Logout

#### User Story : I want to be able to login and logout with ease

#### **Test**
The following tests are listed below that I complied and carried out :  

- Click on the *sign up* link and make sure it takes the user to registration page (so if the user has NOT registered before)
- Click on the Login link in Account dropdown
- Click on Logout link in Account dropdown
- Try to Login in with empty input fields
- Click on Forgot Password link
- Try to Login in with incorrect credentials
- Try to Login in with an incorrect password
- Try to Login in with the wrong email address

#### **Results**
For some reason the **reset password** isn't working. I can follow the reset password instructions but NO EMAIL arrives with a link for the user to reset the password.
I've tried looking into it briefly but I will if I have time at the end, if not it will have to be put down as a BUG at this late stage.   
Everything else works but this has annoyed me a little.

#### **Verdict**
All in all, everything works well apart from the Allauth reset password logic isn't sending an email, for the user to reset their password by clicking the link.



### Main Products Pages

#### User Story : I want to be able to see all products with ease as I scroll down the items

#### **Test**
When I refer to products in this section, it means either a Kicks product or an Accessory product as the functionality is pretty much the same apart from Kicks have size options to choose from but that will be explained in the details pages.

- Click on *SHOP NOW* and it should take the user to the main Kicks page where ALL Kicks within the shop will be displayed
- Title should display what products are being displayed on the page depending on whatever option a user has selected from the navbar or Sort Box
- If a user clicks on one of the products cards they should be navigated to the details page for the chosen product
- When the user clicks any of the navigation options in the navbar then the products should filter down by their selection as mentioned in Navigation and Filtering Testing Section previously
- Number of products available should be displayed in top left section of main screen
- When a user hovers over a product the card will increase in scale by 1.02, to make it stand out a litltle
- If a user clicks on either the Brand or Style located under the price on one of the Kicks cards, this should navigate the user to ALL the Kicks from this Brand or Style respectively. The page title should also change to confirm this
- If a user clicks on the Type located under the price on the one of the Accessories cards, this should navigate the user to ALL the Accessories from this Type. The page title should also change to confirm this
- When the user selects **Price (low to high)** from the Sort Box then ALL the Products on the page will display from the lowest price to the highest price
- When the user selects **Price (high to low)** from the Sort Box then ALL the Products on the page will display from the highest price to the lowest price
- When the user selects **Name (A to Z)** from the Sort Box then ALL the Products on the page will display from the lowest letter of the alphabet to the highest letter in the alphabet by, their **Name**
- When the user selects **Name (Z to A)** from the Sort Box then ALL the Products on the page will display from the highest letter of the alphabet to the lowest letter in the alphabet, by their **Name**
- When the user selects **Brand (A to Z)** from the Sort Box then ALL the Kicks on the page will display from the lowest letter of the alphabet to the highest letter in the alphabet, by their **Brand**
- When the user selects **Brand (Z to A)** from the Sort Box then ALL the Kicks on the page will display from the highest letter of the alphabet to the lowest letter in the alphabet, by their **Brand**
- When the user selects **Style (A to Z)** from the Sort Box then ALL the Kicks on the page will display from the lowest letter of the alphabet to the highest letter in the alphabet, by their **Style**
- When the user selects **Style (Z to A)** from the Sort Box then ALL the Kicks on the page will display from the highest letter of the alphabet to the lowest letter in the alphabet, by their **Style**
- When the user selects **Type (A to Z)** from the Sort Box then ALL the Accessories on the page will display from the lowest letter of the alphabet to the highest letter in the alphabet, by their **Type**
- When the user selects **Type (Z to A)** from the Sort Box then ALL the Accessories on the page will display from the highest letter of the alphabet to the lowest letter in the alphabet, by their **Type**

#### **Results**
Everything works well as tested above with no issues which was pretty awesome. Maybe that's because I had a fair few issues building my code and getting my querying perfected but now I can see the benefits of all that time fine tuning them all :)  

#### **Verdict**
I know that some of the descriptions aren't the best ( I haven't even read half of them tbh) and the prices look ridiculous but I had to go with the images I got from Kaggle and there were only two sets of images available under the Sneakers tag. One was a small set and only had one image per set of Kicks. The set I used was massive and some Kicks had 30 or 40 images a set so I stil had to filter these down to three…. It was seriously monotonous, I sh1t you not.  
I know that some of the images I edited aren't the best but I spent a lot of time filtering through Kicks image after Kicks image just to get the selected three per Kicks set. I then had to edit these until the were a square shape and then resize them all until they were ALL 400px x 400px. In between that I located each Kick online and found a SKU, description and what style they are. The majority of these Kicks if not them all aren't available anymore which made even harder to locate any info on them at all. I'm sure I spent the guts of the first week of starting this project getting ALL that right before I even started into the coding part.  
As regards the Accessories, I got a lot of them from Etsy and Ebay but still had a lot of editing to do as well.  
I'm hoping you can see that within my website as there are 91 sets of Kicks and 22 accessories to select from …. so that’s 339 images I had to edit and 113 descriptions / SKUs / prices / Styles I had to find on the internet but you know what when I look through my wee website that pain was totally worth it.    
Overall I am so so happy with each of the two main products pages and the way they look and feel. It actually looks like a proper Kicks site where me personally, I could spend a lot of money as I am such a Kicks fanatic to be honest.


### Products Details Page

#### User Story : I want to be able purchase any product I desire
#### User Story : I want to be able to see individual products with one click and their various unique details like description, price, available sizes and so on

#### **Test**

- There should be three images displayed one at a time and there should be no glitching or weirdness as I made ALL images the same size
- The images should automatically scroll right to left displaying the 3 images per product and the carousel indicators should move left to right
- If a user clicks on the left or right arrows then they will be able to move the images themselves in any direction (obviously either left or right only ha ha)
- The carousel indicators should move left to right as the images auto scroll
- The user can click in the indicators too, to move to the image they want
- If the user clicks on an image, that it opens up that image in a new tab
- If a user clicks on either the Brand or Style located under the price, this should navigate the user to ALL the Kicks from this Brand or Style respectively. The page title should also change to confirm this
- If a user clicks on the Sex located under the price, this should navigate the user to ALL the Kicks available for this sex. The page title should also change to confirm this (I added this whilst typing this up by the way so I hope it looks okay)
- If a user clicks on the Type located under the price on the one of the Accessories cards, this should navigate the user to ALL the Accessories from this Type. The page title should also change to confirm this
- Depending on whether the Kicks are for Male , Female or Children the size options will change to suit on page load (there will only be one size range available but for the three regions)
- The user can select UK, EU or US by pressing the select button and the dropdown menu options will switch to that size range for the sex that the Kicks is for 
- The user can select what size they want by selecting an option from the dropdown
- The CSS will highlight the options *blue* as they hover over them in the dropdown menu
- The users chosen size will remain in the selector box until they choose a different size, region or add to bag
- The user will be able to choose their quantity by adding or taking away using the quantity buttons available
- The user will not be able to select a quantity less than one or higher than 99
- The quantity buttons will become disabled when the user reaches 1 or 99
- Validation will show an error if the user types quantity outside this range
- Apon the user having selected what they require, if they click on the *ADD TO BAG* button the Kicks with their size and quantity will be added to the bag
- Apon Adding To Bag a success message will pop up and display a message but also the items just selected in the Success Toast
- If the user decides to click the *Secure Checkout* button within this success message then they will be navigated to the Secure Checkout page
- The *BAG TOTAL* in the top right, will also update with the total if nothing was originally in the bag or add to the total, if there was a total already there
- The user can either add the same Kicks again either with the same size, different sizes from different regions or just click on the *Keep Shopping* button and return to the *All Kicks* page


#### **Results**
When I was testing all my products and when I tried Carol Christian kicks it threw up an error, nearly fainted again as I was thinking oh no not now, I figured it out that the SKU was AM/2684 BIUS-PTC/03 which must have been causing the issue because it had back slashes in it so I changed it to AM-2684 BIUS-PTC-03 which solved the issue

![Kicks SKU Issue](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/kicks-sku-issue.png)

Anyway, everything working well and looking super cool. I'm glad I added the Sex icons and code, on the fly, as now the user knows who the Kicks are for. Like I say and keep repeating myself, this wouldn't be required in a proper E-commerce shop as there would be the same Kicks available for ALL sexes generally but for this project, I needed to add it in so the user will know before they click on the Kicks. It would be worse if they loved a set of Kicks and when they went to select their size, it was only available in another sex size, other than their own. It may not be the best but at least it helps the user see before they select the Kicks.

#### **Verdict**
I love this page the most if the truth be told, here and my homepage anyway. The image carousel really brings the page alive and this is were all my hard work editing the images pays off. Also the size selector is so cool and I'm glad I stuck at the JavaScript to get it working. I know it's not the prettiest code but after a fair few hours trying to get it working and I did, I wasn't going to touch it or move it again lol.
I know it's probably missing the fact that it doesn't tell you if it's for a male, female or child, let's say if you click from the New In pages as I only assumed they would be clicking from Mens, Womens or Kids. So they user will only know by the sizes on show. This is were my unisex option fell down but in future upgrades I will add this in and make it even better. 

Just so you know as I was typing this up I thought just show what sex the Kicks are for .... so spontaniously, I have. I know in reality there should generally be the same Kicks available for ALL sexes in a proper shop and I would have made this happen if I had more time but I don't so for now I added this little bit of code below so at least the user will know what sex the Kicks are for from the main Kicks page and the details page when they have clicked on an Kicks card. It's not perfect by any means but at least the user knows before they get to the size selection options whether the Kicks are for Male, Female or Children !

![Kicks Sex Displaying Now](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/show-sex-for-kicks.png)


### The Bag Area

#### User Story : I want to see my total spend as I continue my shopping spree within the site
#### User Goal : Free delivery once a certain amount has been spent, depending on location

#### **Test**

- Products images are displayed clearly within the bag area for the user to see
- Products SKU's for ALL Products will be displayed and Products Sizes if that Product is a pair of Kicks
- The Products individual price will be displayed before the quantity
- The Products quantity will be displayed within the quantity box
- The user will be able to adjust the quantity and click on the update link which in turn will update everything including the totals
- The user will be able to remove a product by clicking the remove link and therefore remove the costs from the totals
- The user will be able to see their current total under the bag icon in the top right hand of the navbar
- The user will be able to see their bag total and grand total including delivery (if any) just above the *Secure Checkout* button
- If the total is less than the ```free_delivery_threshold``` set in Django Admin then the delivery cost will be calculated and displayed within the delivery (set at 10% at the minute)
- If the total is less than the ```free_delivery_threshold``` set in Django Admin then a red warning will display under the Grand Total telling them to spend X amount for free delivery
- The user should see not success messages for updating products within the bag area as I removed these because they were not required in my opinion
- If the user clicks on the *Continue Shopping* button they will be returned to the ALL Kicks page but their current total will continue to be on display under the bag icon
- If the user clicks on the *Secure Checkout* button they will be taken to the Checkout page to continue with their purchase

#### **Results**
I know the quantity buttons don't disable on large screens and I still have the issue with them not disabling if the user has added the same Kicks but different sizes because I am using SKU as my ID for the bag code but I will just have to put these down as unsolved bugs at the minute as I have no time to rectify these. I did try my best but couldn't come up with a solution in the time I allowed myself to have a go. I will look at it after I get my final result as it's annoying me so hang fire on this one.  
I did have some issues getting my code right for passing either product to the bag hence why I used SKU to begin with and sizes too, instead of the products PKs as this caused me major headaches at the start due to the fact I had two different products.

Apart from the quantity button issues, everything else passed the above tests and it all works really well. I maybe could have had small buttons instead of links for the *update* and *remove* options but these come as the projects get updated. It looks well on small screens after some refactoring at the end but overall I am happy with the functionality 


#### **Verdict**
All tests worked above so I am super happy again with the overall functionality of my bag page and it looks good on all devices. I did want to have Discount codes working so the user could input the special code at the bag area and a discount would be applied offering more reductions on the overall costs. I will have this option available for future implementation but for now I had to let it go !


### The Checkout

#### User Goal : Be able to make a purchase with ease
#### User Story : I want to be able to add my payment details with ease and possibly store them safely, for future usage (only as a registered user obviously)
#### User Story : I want confirmation of my order by an instant pop up and a follow up email

#### **Test**

- The user will be able to see an Order Summary of their products before they finalise their purchase
- The user wil be able to input their details as in full name and email address if they are not a registered user
- The user will have their email address populated if they are a registered user and also logged in
- The user will be able to add their delivery details even if they are not a registered user
- The user will be able to purchase products even if they are not a registered user
- The user will have the option to to Create an account or Login, on the checkout page if they are not registered or logged in
- The user if registered and logged in will have the option to save their default delivery details for future usage
- The user will also be able to return to bag to make adjustments if needed by clicking on the *Adjust Bag* button
- The form has to be filled out as per the validation and will throw up validation errors if not
- The card image will change depending on what their card is, like Visa or Mastercard
- The user will get an error message if their is any issues with their card details (Stripe Validation)
- The user will see the amount their card is going to be charged in RED directly below the *Complete Order* button so they know one final time before proceeding with payment
- The user, once all details and card details have been validated will be able to click *Complete Order* button and make the purchase
- The user should see The Kicks Fix loader as the purchase process is being carried out
- The user will see a Success message depicting that the order was successful and an email has been sent
- The user will be navigated to a checkout success page whether they are registered or not
- The user will see an overview of their order on the checkout success page
- The user will get a confirmation email whether they are registered or not
- The user will be able to return to the Kicks Sales page from the checkout success page after the purchase has been made, by clicking the large button

#### **Results**
All tests passed with no issues.

#### **Verdict**
Very happy with how the checkout page looks and its overall functionality, although I would have liked the users name to have been added at Registration process so their name would be pre-populated here or at least the users full name to be saved at this point. I did look into this functionality but I would have to had changed the registration page to make this happen and preferably at the start of the project so for now the user will have to manually input their Full Name.  
I have added names in Django Admin for some of my test user profiles so it deffo adds a little personal touch when it can be seen at checkout.


### Profile

#### User Story : I want my own personal space after registering by means of a profile page
#### User Story : I want to be able to create a wishlist of products for future purchasing


#### **Test**
Nothing here to test really as it's just a Profile page. I wanted to do so much more to this but I never got round to it.
At the minute there is the username and their email address. If the Django Admin can add their First Name and Last name then this will be populated as well.
As I mentioned above, I wanted to add these but it says online that it's better to add these at the start of the build within the UserProfile models. I was going to add them in towards the end but I was scared in case I messed the UserProfiles up. In future Django projects I will deffo add this feature so that my projects can add that personal touch by using their first names through the project.  
The users wishlist is my biggest let down by not getting it done. I never even got time to even start it if the truth be told but I have added this also to Features to be Implemented in the future. I would had this showing on the users profile page or added a heart onto the navbar that would have taken the user to their personal Wishlist page where their selected wishlist products would be displayed. Obviously, the wishlist heart would only appear if the user was authenticated but look, this is one for the future.   
I also wanted to add the users Date of Birth because at the design part of my project, I really wanted to be able to offer registered users a Birthday treat every year on their birthday or in the weeks coming up to their birthdays. A simple automatic email would be sent out to the user, say 2 weeks before their birthdays, with a 10% discount code that they could use before their birthday date had passed. The email would be personal to them as would the discount code and they could have input it at the Bag or Checkout page and after my code validates the discount code, the discount would be calculated on their current total and subtracted from it .... giving them a special Birthday Treat.  
I also wanted the user to be able to add a profile pic like in my last project but again this can be done at a later time.

#### **Results**
No results as there are no tests :(


#### **Verdict**
Profile page needs some work to it and I did try to add AdditionalUserInfoProfile and a form so they could make changes on their Profile pages but it was beginning to get messy in my code and looked even worse on the screen, so in the end I just scrapped the idea and deleted my test code. I still have a fake DOB displayed which I will remove shortly and as long as you add the users name in Django Admin then it will be displayed here too.  
I wish I had've made this happen as it would have been perfect for the user to check their profile and request changes if required :)

Below is an image of the way it should've looked after full registration:

![Profile Page](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/profile-image.png)



### Order History

#### **Test**

- Check that the user can not see their order order history if they are not logged in
- Check that a new registered user has no order history and that there is no default delivery information
- Check that when a new user makes an order and if the *"Save default delivery info"* box **is not** ticked that their details are not saved
- Check that when a new user makes an order and if the *"Save default delivery info"* box **is** ticked that their details are saved
- Check that when a new user makes an order that their order is located in their Order History
- Check that the basic elements of their order are displayed like order number (first few characters), date, items and order total
- Check that if a user amends their delivery information that this updates correctly
- Check that when a user updates their Delivery Information that a Success message appears informing them of this
- Check that the users orders are listed by oldest first and descending to newest
- Check that if a user clicks on an order by Order Number that it navigates them to their previous orders page and displays the orders details
- Check that when a user clicks on an order by Order Number that an Alert message appears informing of this process
- Check that all details can be removed and this will be saved on update

#### **Results**
All tests passed with no bugs which is always a good thing

#### **Verdict**
Order history works well and does what it was designed to. It allows users to access and update their personal Delivery Information for a quicker checkout and more importantly the user can see basic details of ALL previous orders and then access their previous orders in more detail by clicking the Order Numbers.


### Admin Functions

#### Admin Story : I want to be able to ADD products easily
#### Admin Story : I want to be able to EDIT products and prices
#### Admin Story : I want be able to DELETE products as and when required
#### Admin Story : I want be able to add offers and promotions as and when required like Christmas or personal Birthday Treats for example

#### **Test**

- See if a user can access admin functions through the url, if they are not logged in (should redirect them to login page)
- See if a logged in user can type the appropiate url to access add / edit functions
- See if an Error message appears saying "Sorry, only store admin can do that", if the user tries to access these functions through the url
- See if a superuser / admin can access these functions through the urls
- See if a superuser / admin has the options available to edit or remove any product on either their main page or individual details page
- See if a superuser / admin can access the Add Kicks or Add Accessory forms from their Account dropdown in the navbar
- See if a superuser / admin can add a product using the forms available
- See if a Success message appears on completion of Adding a new product and redirects them to the new products details page
- Check that everything has been added to that new product and all looks well
- See if the superuser / admin can edit this new product by clicking on the edit link
- See if an Alert message appears confirming to them that they are editing a product
- See if the superuser / admin can edit that product and click the *Update Product* button
- See if a Success message appears after successfully updating a product
- Make sure that product appears within the main products page
- Check that if *Cancel* button is clicked on either the Add or Edit pages that the superuser / admin is returned to the main page for that specific product
- Check that when a product had been removed by deletion that it does not exist within the database
- Check that a Success message appears on completion of the product deletion
- Check ALL forms validation for both Adding and Editing a product by leaving out required fields and inputting a price larger than 6 digits
- Check that if no images are added, a *no image* image appears instead of a blank area
- Check that even with no image the product can be added to the bag


#### **Results**
All tests passed with flying colours ..... BUT .... there is always a BUT, I noticed that because of my carousel there has to be three images added so if I only added one then it would threw up an error. I love fixing code on the fly, it makes you feel so good .... so I did, see below.

Below is my code before the fix:

![Admin Add Products Image Issue](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/add-img-admin1.png)

Below is my code after the fix:

![Admin Add Products Image Issue](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/add-img-admin2.png)


I know it is a simple solution but I have tested it and it works. If there aren't three images then it displays the default *no image* image.
I also added this to the Kicks details page too so everything is cool. I tried adding one image to image2 and tested it too and also with image3. Unless there are 3 images the carousel will not display any images only the default one.  
I also added ```{% if accessories.image1 and accessories.image2 and accessories.image3 %}``` to the accessories page too, as I didn't want an image, as in image1, displaying here then nothing on the details page so I have unity across my website. I did this for Kicks too.  

So if there aren't three images uploaded to the products database, there will be **NO IMAGE** for this product on display .... simple as that !!! (I hope this was the right decision ha ha).

#### **Verdict**
Deffo would like to add Admin forms for slogans, promotions, logos, discount codes, discount percentages, delivery costs, etc , etc but you can still utilise this within the Django Admin so at least it saves changing code and deploying again causing major site downtime which is what we don't want ..... my mentor said try and keep as much Backend as possible as it will save you a load of pain in the future. I totally understand where he is coming from and will always use this concept in the future.  
At present the two forms for adding and editing, and the delete options work well so I am not going to beat myself up over not getting the other Admin additions not completed.
I have already added this to the Features to be implemented in my README which is getting bigger by the minute ha ha but I can only get better at planning things and I deffo spent way too much time on the images and info but sure it all looks good anyways.  
So glad I found that bug when testing today and also added a quick fix within the code. I probably should have made ALL images required in my model and then I wouldn't have had this issue but it's a learning curve and I am still learning.  

All in all I am super happy with ALL admin functions and there functionality :)


### Contact Us and the KFC - Kicks Fix Club

#### User Story : I want to be able to contact the site owner, in case I have any issues or payment queries

#### **Test**

- Check that a non-registered user can see the Contact Us link
- Check that a non-registered user cannot see the KFC link
- Check that registered user can see the Contact Us link
- Check that a registered user can see the KFC link
- Check that a superuser cannot see the Contact Us link
- Check that a superuser cannot see the KFC link
- Check that a non-registered user cannot see their name within the Contact Us page (it would say Anonymous User)
- Check that a registered user can see their name within the Contact Us page
- Check that a registered user can see their name within the KLC page
- Check that the Contact Us email link opens an New Email for the user and populates the **To** section 
- Check that the KFC membership email link opens an New Email for the user and populates the **To** section 

#### **Results**
All tests passed as expected but these were simple add-ons at the end of the project just to finalise it and complete one last User Story.  
I had made the KFC available to all users but I have changed it to registered users ONLY, as it saved some code within the kicks_club page I was using, to display certain text depending on a users status.
I also removed the KFC from superusers because they don't need to see it or join, more to the point.
I also moved the Contact Us link so non registered user could see it in the Account dropdown as the site isn't just for registered ones and everyone should have the availability to Contact Us, at The Kicks Fix with issues.
I also removed the Contact us from superusers as they do not require that either.

#### **Verdict**
I added the Contact Us page last night and it's fairly simple but at least it's there for a user to contact The Kicks Fix with any issues they have.  
As for the KFC, the Kicks Fix Club, this just came to me at the end here, so bare with it as it's one of those spontanious ideas I sometimes have. It was originally going to be TLC which stood for Trainer Loving Care but with the website being called Kicks and all, I thought this would just have been like a white elephant in the room and spoil the overall feel. The TLC page was just going to have some pointers / tips about how to keep you Kicks clean, fresh and looking good. I was going to have a few links to my maintenance products in Accessories too. I just thought this would have been a bit boring hence why I've went a totally different route at the last minute.   
I then decided it was going to be Kicks Fix Care but I thought this would just be like the Contact Us page so I've let my mind go here and came up with KFC - Kicks Fix Club, which as you know is play on letters so to speak. I'm super sorry if it seems cheesy and the fact I left this to the end but I think my website deserves a club, for all the Kicks Fanatics out there like moi !  
Obviously I would have to develop this membership scenario so so much more, if the user was to accumulate points and this would be added to their profile pages, also the special offers, discount codes and everything I said on the KFC page would have to have code written for it.
This all evolved within my head in the space of about 5 minutes tonight if I am being honest but I am going to go with it just to finish the project off.  

Overall, I think this was a better option than TLC which if you look at my *Git Commits* was there in the Navbar right until tonight so you know this last minute change wasn't even on the radar at all. Given that, with the right development I beleve this would be a much better attraction for the overall site and would make users want to join the club to earn some nice savings, as they purchase Kicks or Accessories.   

***I know KFC is a trademark and I would have to call it by a different name but I just added it, for little fun to finish what has been quite an intense and stressful project***


### Overall Website Navigation, Functionality & Visual Experience

#### User Goal : An aesthetically pleasing and visually appealing website
#### User Goal : A chilled out site so that they will want to come back again and again

#### **Test**
There aren't really any tests left to do as regards this, as I have already completed these in the Responsiveness and Navigation sections.
I believe that the above User Goals have been completed because the website has good navigation, good filtering as the per navbar options, the overall functionality ALL works bar a couple of bugs with the quantity buttons bug and the Reset email bug. The visual experience works well across ALL screens after a few minor adjustments and from the homepage to the checkout page everything looks really well.

#### **Results**
Overall, very happy with the final product and I really hope the user enjoys their experience trawling through The Kicks Fix for some hidden gems. As long as the price of some of the Premier Kicks doesn't scared them off (these were genuine prices by the way and in fact I had to reduce them, as some were unbelievably extortionate)

#### **Verdict**
Love my wee website and I super proud of my achievement in the short space of time .... I really hope you all love it too !


# Validators

### HTML

All the HTML files were validated by using online code validator [W3C HTML Validation Service](https://validator.w3.org).  
99% of the errors and *BAD Values* were as regards template variables and logic but I knew this would happen anyway because the Course material told me this.  
A lot of errors were missing ```<!DOCTYPE html>```, ```lang``` and ```html``` errors but again I knew this would happen.  
Although I did find two stupid errors which I have now corrected, see below:

A container was missing the div:  
![Missing Container Closing Tag](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/missing-closing-contain-div.png)

I had two end *p* tags instead of a start one and end one:  
![Two losing p tags](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/two-closing-p-tags.png)

Overall with a few warnings and the errors mentioned above, the code was validated HTML page by HTML page and ALL passed.  

### CSS

All CSS files were validated by using an online code validator [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).  
```profile.css``` passed fine with no warnings.   
```checkout.css``` passed fine with one ```-webkit-transition ``` warning.  
```base.css``` passed fine but with six warnings but nothing major (see images below).  

![Base CSS Passed Validation](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/css-base-validation.png)

![Base CSS Minor Warnings](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/css-base-warnings.png)


Overall, really happy with my CSS and that ALL CSS files passed validation with no major issues.


### JavaScript

All the JavaScript files were validated by using an online code validator [Beautifytools.com](http://beautifytools.com/javascript-validator.php).  
Missing semicolons were some errors and these were added at the end of functions.  
A few **'$' is not defined** errors arose but after checking online I'm assuming that's because there is no jQuery plugin which utilises '$' to declare any variable.  
Overall though, the JavaScript looks good and works well within my site.


### Python

All Python files were validated by using an online code validator [Pep8](http://pep8online.com).  
File changes were made to make the code PEP8 compliant where possible.  
I think there are about three or four lines that aren't PEP8 compliant through the whole project and these are within the *webhooks* so that's not too bad.  
Other than that, it ALL looks good.

### Debug = True

While developing an app, the local debugger: `debug=True` was on.
Every time when the application has an error, the debugger was displaying an error message page.
Thanks to that I could catch all errors and fix them straight away.
