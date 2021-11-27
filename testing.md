# **Testing**

## Table of contents
---

** Table here once finished **


### Responsiveness

#### User Goals : The website will have to work well on all devices

#### **Test**
I utilised my own laptop connected to a large screen, my work laptop which has a failry small screen, my tablet, my mobile phone and of course Chrome DevTools to test reponsiveness across various platforms.  
Firstly I noticed that my ```{{ kicks_title }}``` were still large on on smaller screens so were wrapping round a lot so I added some CSS to reduce the size on smaller screens. I had to settle for a happy medium here so the larger titles in length may wrap a little on smaller screens but it means the smaller titles are not super small on the largest small screens, if you get what I mean. Below is the small piece of CSS code I used to fix this issue.

```
h2.text-uppercase.product-title {
    font-size: 1.2rem;
}
```

Secondly, I noticed on mobile that my navbar dropdown submenus were only showing the top options whilst the rest were cut off at the bottom of the screen.
I added a submenu-scroll class to each submenu and added some CSS to combat this. This is the problem when you build your project on a large screen but also the benefits of doing testing and really getting into your project on the smallest screens in DevTools.

```
ul.dropdown-menu.submenu-scroll {
    height: 200px;
    overflow: auto;
}
```

I set my "Sorry, no Kicks available" text to center, on smaller screens, for when there are no kicks or accessories available because it looks much better in my opinion.  

I also noticed that my Profile link was not working and there was NO order history on small screens. I had just left my href link blank for Profile and I hadn't even added the code for my order history in my small-nav.html. I have made the additions and everything looks well.  

#### **Results**
The joys of testing really comes to fruition when you are manually testing your website and trying it on all different sizes. I found minor issue after minor issue when Itried the smallest screen available but nothing that made me panic. I just applied a little CSS to adjust various sizes of titles or text. I biggest one was my dropdown menu submenus for kicks Brand, Style, Colour & Types within accessories. Again, I used the smallest screen approximately 320px x 568px for the iphone5 and added the CSS as mentioned above. I think it works well across ALL portrait modes now but it's hard to get it exactly perfect for ALL screens no matter how good you are. It's definitely a lot better than my first project when I hadn't even taken screen sizes into account building my website for HTML and CSS .... that was a shock to the system but a good learning point.

#### **Verdict**
After throughly going through my website with a fine tooth comb, I did find some issues with the responsiveness as logged above but overall, I think it looks well and works well on all devices. 


### Navigation & Search Functions

#### User Goal : Navigate around the website with ease and pleasure
#### User Story : I want be able to search / filter the products by various options like male, female, kids, brands, styles and so on

#### **Test**
The various tests I carried out for the navaigation and search functions are listed below:

- Click on the **Shop Now** button and make sure it takes the user to the ALL Kicks page
- Click on each navigation link to make sure it directs the user to the correct page
- Check that when the user clicks on any dropdown submenu links that it takes them to the correct page
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
Evrything looks good apart from my quantity buttons on large screens, I had a go at trying to fix this last night but I was wasting too much time with so little of it left. I'm pretty sure this is similar to the bug I logged on Github and in my bug section **BUG 26** where because I am using IDs for the two buttons, they will only disable the button in the first instance. And because I am using the Products ID which is SKU in my case, if I added two Kicks but of different sizes, the second set of quntity buttons don't work.  I still haven't a fix for this as of yet but I haven't closed my Bug Issue on it yet so I will leave it open.  
That saying, this bug is similar and because I was utilising the CI code, I checled it out on Slack and it's because of a similar reason. On the smaller screens the buttons become disabled but on the larger screen it won't because the IDs are used in the same places. Like I said before I wasted a good 2 hours last night when I really need to invest that in the testing so I will just put it down to an annoting bug but deffo look at it after I get my result.  

Also, I noticed that when testing the overall navigation and search functions that I had created a silly bug whilst fixing an issue within the Responsiveness testing and it took me a few minutes to notice how to fix it ha ha.  

Lets see if you can notice it before scrolling on:
![Account Dropdown Issue](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/account-dropdown-issue1.png)

Here is is how it looked with the issue:
![Account Dropdown Issue](https://github.com/RaVeR76/The-Kicks-Fix/raw/main/docs/screenshots/account-dropdown-issue1a.png)

#### **Verdict**
All in all, I am very happy with everything apart from the qunatity button issue but I will have a look at it at a later date and find a solution that works for it all. I know adding classes instead of IDs is the way but when I tried last night I was disabling them **ALL** or disabling ***NOTHING** ! but I will solve it, don't you worry :)

### Home Page

#### User Goal : An enticing landing page that will make any user enthralled to delve deeper into my website

#### **Test**
To be honest there is nothing really to test here as the majorty of the testing was done previously with ALL the navigation links tested. Realistically, there is only a Hero image, slogan and enter the shop button. These all test perfectly. The navbar and all links were tested above. 
I tested the logo so that it would return the user to this homepage as well. I can change the slogan in Django admin and it will change on screen. I really wanted some site Admin to be able to make all these changes but again I have added this to future upgrades, as time is of the essence. 

#### **Results**
I had quite a few hero images downloaded from the internet for testing out on my homepage and I'm sure evreyone of them would've looked good here.   
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
The folowing tests are listed below that I complied and carried out :

- Click on the *sign in* link and make sure it takes the user to login page (so that if the user has registered before)
- Click on the Register link in Account dropdown
- Try to Register with empty input fields
- Try to register with two different passwords
- Try to register with a password less than 8 characters
- Try to register with a password that is common word, like ***qwerty12***
- Try to register with the same existing username
- Try to Register with a wrong email address, by leaving out the @ or using a comma instead of a dot
- Chaeck that an ALert Message appears after registration has been successful to say an email has been sent to the email address used at registration
- Check that the confirmation email has a link to confirm registration and that when he link is clicked ... the user is directed to The Kicks Fix confirmation page
- Check that when the user confirms their email on The Kicks Fix confirmation page that they are navigated to the login page

#### **Results**
 All tests passed that were tried above. When errors where input, Allauth displayed an error message stipulating what the issue was like *Password too common* or you need to use 8 characters for the passord. I tired everything to get passed Allauth but Allauth says NO .... well, without properly registering for The Kicks Fix. I did add a few wee changes to the email confirmation message as it needed a little touch up in areas, once I read it through but apart from that everything else was excellent.

#### **Verdict**
Tests passed, works as expected, no bugs were found during the testing. Functionality covered.


### Login / Logout

#### User Story : I want to be able to login and logout with ease

#### **Test**
The folowing tests are listed below that I complied and carried out :  

- Click on the *sign up* link and make sure it takes the user to registration page (so if the user has NOT registered before)
- Click on the Login link in Account dropdown
- Click on Logout link in Account dropdown
- Try to Login in with empty input fields
- Click on Forgot Password link
- Try to Login in with incorrect credentials
- Try to Login in with an incorrect password
- Try to Lggin in with the wrong email address

#### **Results**
For some reason the **reset password** isn't working. I can follow the reset password instructions but NO EMAIL arrives with a link for the user to reset the password.
I've tried looking into it breifly but I will if I have time at the end, if not it will have to be put down as a BUG at this late stage.   
Everything else works but this has annoyed me a little.

#### **Verdict**
All in all, everything works well apart from the Allauth reset password logic isn't sending an email, for the user to reset their password by clicking the link.



### Main Products Pages

#### User Story : I want to be able to see all products with ease as I scroll down the items

#### **Test**
When I refer to products in this section, it means either a Kicks product or an Accessory products the functionality is pretty much the same apart from Kicks have a sizes option to chooses from but that will be explained in the details pages.

- Click on SHOP NOW and it should take the user to the main Kicks page where ALL Kicks within the shop will be displayed
- Title should display what products are being displayed on the page depending on whatever option a user has selected from the navbar or Filter Box
- If a user clicks on one of the product cards they should be navigated to the details page for the chosen product
- When the uses any of the navigation options in the navbar then the products should filter down by their selection as mentioned in Navagtion and Filering Testing Section previously
- Number of products available should be displayed in top left section of main screen
- When a user hovers over a product the card will increase in scale by 1.02, to make it stand out a litltle
- If a user clicks on either the Brand or Style located under the price on the one of the Kicks cards, this should navigate the user to ALL the Kicks from this Brand or Style respectively. The page title should also change to confirm this
- If a user clicks on the Type located under the price on the one of the Accessories cards, this should navigate the user to ALL the Accessories from this Type. The page title should also change to confirm this
- When the user selects **Price (low to high)** from the Filter Box then ALL the Products on the page will display from the lowest price to the highest price
- When the user selects **Price (high to low)** from the Filter Box then ALL the Products on the page will display from the highest price to the lowest price
- When the user selects **Name (A to Z)** from the Filter Box then ALL the Products on the page will display from the lowest letter of the alphabet to the highest letter in the alphabet by, their **Name**
- When the user selects **Name (Z to A)** from the Filter Box then ALL the Products on the page will display from the highest letter of the alphabet to the lowest letter in the alphabet, by their **Name**
- When the user selects **Brand (A to Z)** from the Filter Box then ALL the Kicks on the page will display from the lowest letter of the alphabet to the highest letter in the alphabet, by their **Brand**
- When the user selects **Brand (Z to A)** from the Filter Box then ALL the Kicks on the page will display from the highest letter of the alphabet to the lowest letter in the alphabet, by their **Brand**
- When the user selects **Style (A to Z)** from the Filter Box then ALL the Kicks on the page will display from the lowest letter of the alphabet to the highest letter in the alphabet, by their **Style**
- When the user selects **Style (Z to A)** from the Filter Box then ALL the Kicks on the page will display from the highest letter of the alphabet to the lowest letter in the alphabet, by their **Style**
- When the user selects **Type (A to Z)** from the Filter Box then ALL the Accessories on the page will display from the lowest letter of the alphabet to the highest letter in the alphabet, by their **Type**
- When the user selects **Type (Z to A)** from the Filter Box then ALL the Accessories on the page will display from the highest letter of the alphabet to the lowest letter in the alphabet, by their **Type**

#### **Results**
Everything works well as tested above with no issues which was pretty awesome. Maybe that's because I had a fair few issues building my code and getting my querying perfected but now I can see the benefits of all that time fine tuning them all :)  

#### **Verdict**
I know that some of the descriptions aren't the best ( I haven't even read half of them tbh) and the prices look ridiculous but I had to go with the images I got from Kaggle and there were only two sets of images available under the Sneakers tag. One was a small set and only had one image per set of Kicks. The set I used was massive and some Kicks had 30 or 40 images a set so I stil had to filter these down to three…. It was seriously monotonous, I sh1t you not.  
I know that some of the images I edited aren't the best but I spent a lot of time filtering through Kicks image after Kicks image just to get the selected three per Kicks set. I then had to edit these until the were a square shape and then resize them all until they were ALL 400px x 400 px. In between that I located each Kick online and found a SKU, description and what style they are. The majority of these Kicks if not them all aren't available anymore which made even harder to locate any info on them at all. I'm sure I spent the guts of the first week of starting this project getting ALL that right before I even started into the coding part.  
As regards the Accessories, I got a lot of them from Etsy and Ebay but still had a lot of editing to do as well.  
I'm hoping you can see that within my website as there are 91 sets of Kicks and 22 accessories to select from …. so that’s 339 images I had to edit and 113 descriptions / SKUs / prices / Styles I had to find on the internet but you know what when I look through my wee website that pain was totally worth it.    
Overall I am so so happy with each of the two main products page and the way they look and feel. It actually looks like a proper Kicks site where me personnally, I could spend a lot of money as I am such a Kicks fanatic to be honest.







### Products Details Page

#### User Story : I want to be able purchase any product I desire
#### User Story : I want to be able to see individual products with one click and their various unique details like description, price, available sizes and so on

#### **Test**

#### **Results**
I was testing all my products and when I tried Carol Christian kicks it threw up an error, I figured it out that the SKU was AM/2684 BIUS-PTC/03 which must have been causing the issue because it had back slashes in it so I changed it to AM-2684 BIUS-PTC-03 which solved the issue

#### **Verdict**







### The Bag Area

#### User Story : I want to see my total spend as I continue my shopping spree within the site

#### **Test**

#### **Results**

#### **Verdict**




### The Checkout

#### User Goal : Be able to make a purchase with ease
#### User Goal : Free delivery once a certain amount has been spent, depending on location
#### User Story : I want to be able to add my payment details with ease and possibly store them safely, for future usage (only as a registered user obviously)
#### User Story : I want confirmation of my order by an instant pop up and a follow up email

#### **Test**

#### **Results**

#### **Verdict**



### Profile

#### User Story : I want my own personal space after registering by means of a profile page
#### User Story : I want to be able to create a wishlist of products for future purchasing
#### User Story : I want to be able to contact the site owner, in case I have any issues or payment queries


#### **Test**

#### **Results**

#### **Verdict**



### Admin Functions

#### Admin Story : I want to be able to ADD products easily
#### Admin Story : I want to be able to EDIT products and prices
#### Admin Story : I want be able to DELETE products as and when required
#### Admin Story : I want be able to add offers and promotions as and when required like Christmas or personal Birthday Treats for example

#### **Test**

#### **Results**

#### **Verdict**



### Overall Website Navigation, Functionality & Visual Experience

#### User Goal : An aesthetically pleasing and visually appealing website
#### User Goal : A chilled out site so that they will want to come back again and again

#### **Test**

#### **Results**

#### **Verdict**



# Validators
