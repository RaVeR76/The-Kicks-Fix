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
#### User Story : I want be able to search / filter the products by various options like male, female, kids, sizes, brands and so on

#### **Test**
The various tests I carried out for the navaigation and search functions are listed below:

- Click on the **Shop Now** button and make sure it takes the user to the ALL Kicks page
- Click on each navigation link to make sure it directs the user to the correct page
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

Hero image adjusted for smaller screens

#### **Results**

#### **Verdict**


### Registration

#### User Story : I want to be able to register for an account so that I can have access to unique promotions and discounts

#### **Test**

#### **Results**

### **Verdict**



### Login / Logout

#### User Story : I want to be able to login and logout with ease

#### **Test**

#### **Results**

#### **Verdict**




### Products 

#### User Story : I want to be able to see all products with ease as I scroll down the items
#### User Story : I want to be able purchase any product I desire
#### User Story : I want to be able to see individual products with one click and their various unique details like description, price, available sizes and so on

#### **Test**

I was testing all my products and when I tried Carol Christian kicks it threw up an error, I figured it out that the SKU was AM/2684 BIUS-PTC/03 which must have been causing the issue because it had back slashes in it so I changed it to AM-2684 BIUS-PTC-03 which solved the issue

#### **Results**

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
