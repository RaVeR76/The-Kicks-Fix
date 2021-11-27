# **Testing**

## Table of contents
---

** Table here once finished **


### Responsiveness

#### User Goals : The website will have to work well on all devices

#### **Test**
I utilised my own laptop connected to a large screen, my work laptop which has a failry small screen, my tablet, my mobile phone and of course Chrome DevTools to test reponsiveness across various platforms

I noticed that my ```{{ kicks_title }}``` were still large on on smaller screens so were wrapping like mad so I added some CSS to reduce the size on smaller screens. I had to settle for a happy medium here so the lerger titles in length may wrap a little on smaller screens but it means the smaller titles are not super small on the larger small screens, if you get what I mean.

```
h2.text-uppercase.product-title {
    font-size: 1.2rem;
}
```

I noticed on mobile that my navbar submenus were only showing the top options whilst the rest were off the bottom of the screen.
I added a submenu-scroll class to each submenu and added some CSS to combat this. This is the problem when you build your project on a large screen but also the bnefits of doing testing and really getting into your project on the smallest screen in DevTools.

```
ul.dropdown-menu.submenu-scroll {
    height: 200px;
    overflow: auto;
}
```

I set my text to center, on smaller screens, for when there are no Kicks or accessories are available because it looks much better in my opinion


Profile not working and NO order history on small scrrens ffs

#### **Results**

#### **Verdict**
After throughly going through my app with a fine tooth comb, I did find some issues with the responsiveness as logged above but overall, I think it looks well and works well on all devices. 


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




### Navigation & Search Functions

#### User Goal : Navigate around the website with ease and pleasure
#### User Story : I want be able to search / filter the products by various options like male, female, kids, sizes, brands and so on

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
