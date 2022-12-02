
## Functional Requirements
1. Login (Lawrence)
2. Logout (Lawrence)
3. Create new account (Michael)
4. Delete account (Hai)
5. User home page (user can see messages of users they follow) (Michael)
6. Send message to followers (lawrence)
7. Search for user (Michael)
8. Follow User (Hai)
9. User Profiles (Michael)
10. Post Image with message (Hai)
11. Send/Receive Private Messages (Hai)
12. Search Message (Hai)

## Non-functional Requirements

1. Only expected to work on Google Chrome
2. Expected to work only on Desktop
3. Only available to English users
4. Expected to work on Mac/Windows/Linux

## Use Cases

1. Send message to followers (Lawrence)
- **Pre-condition:**  
Followers must be following user and user must know who is following them

- **Trigger:**  
Button that initiates form to select followers and create a message that will be sent to selected followers

Button automatically saves followers onto a list and present user with call to create a message

- **Primary Sequence:**
  
  1. Press button that initiates trigger #1
  2. Window appears showing followers list
  3. Selected followers is saved onto a list 
  4. Call to user to create a message
  5. Saves message onto a string
  6. Button appears to send message
  7. Message is exported and imported to the followers
  8. Message is called and displayed to the follower
 

- **Primary Postconditions:** 
Return condition where if a message has been successfully sent, return to user’s page where “send message to follower” button is offered and notify message sent successfully.


- **Alternate Sequence:** 
  
  1. User selects button to “send message to followers”
  2. Alternate Tigger #2: Saves all followers onto a list
  3. Calls for user to create a message
  4. Message saved onto a string
  5. Send button after message is ready to be sent
  6. Message is exported and imported to the followers
  7. Message is called and displayed to the follower
  8. … 

2. Search for User (Michael)
- **Pre-condition:** The user must exist and have an account registered with the website. The search bar will also only find the username of the user and not their associated name for privacy. 

- **Trigger:** User clicks on search bar in dedicated area on the website where they can enter the desired user's username for searching.

- **Primary Sequence:**
  
  1. User locates the search bar at the home page and the user clicks the search bar. The search bar then opens for user to type
  2. User enters username of desired user in the search bar
  3. After user types username of desired user in the search bar, they must click enter
  4. After pressing enter, user is redirected to a page with usernames related to their previously types and entered username
  5. User locates username in page of related usernames and clicks on their name 
  6. User is then redirected to clicked on usernames page

- **Primary Postconditions:**  User is redirected to the usernames page if they exist and are a registered user. The search bar will be on the homepage only and if user wants to use search bar again, they must redirect to the homepage where they can utilize the search bar

- **Alternate Sequence:** 
  
  1. User types the desired username in non english characters
  2. When they press enter, tell the user that types username with non english letters that the username contains characters that are invalid.
  3. Specify to user that usernames are only standard english keyboard characters 


3. Follow User (Lawrence)
- **Pre-condition:** 
Searched user must exist as a saved account on the app
User must not already be following searched user

- **Trigger:** 
User clicks on button to initiate “Follow User”

- **Primary Sequence:**
  
  1. User searches up another user they wish to follow
  2. Brings user to other user’s profile page
  3. Next to username, provides button to “Follow User”
  4. After clicking “Follow User” “following” counter increases by 1
  5. Followed user’s “followed” count increases by 1
  6. Change “Follow User” button to “Unfollow User”
  7. Proceed to postcondition


- **Primary Postconditions:**  
If following and follower count when incremented returns true, return a notification message to follower and followee confirming changes to their respected lists

- **Alternate Sequence:** 
  
  1. User searches up user they wish to follow
  2. Brings user to other user’s profile page
  3. Display “Follow User” button
  4. If User is already followed, display “Unfollow User” button instead
  5. If searcher selects button, decrement searched user’s follower count by 1
  6. Decrement user’s following count by 1
  7. Change “Unfollow User” button to “Follow User” button
  8. Proceed to post condition

4. User profiles (Michael)
- **Pre-condition:**  The user must exist and have an account registered with the website.

- **Trigger:**  The username is clicked on and the user is redirected to the users page

- **Primary Sequence:**
  
  1. User types in a username in the search bar and clicks on desired username
  2. System then redirects the user to the usernames profile page

- **Primary Postconditions:**  If users homepage exists, then their profile page will appear when clicked on at search or on homepage. 

- **Alternate Sequence 1:** 

1. User sees post of alternate user on their homepage that they are following
2. User then clicks on alternate users username on their post and is redirected to their profile page


- **Alternate Sequence 2:** 

1. User clicks on username from search bar or on homepage from alternate users post
2. Username that is clicked on is a user that has been previously deleted
3. When a user clicks on the username that is deleted, redirect them to a page that tells them the user has been deleted.

5. Send/Recieve Private Messages (Hai)
- **Pre-condition:** User has a profile, is logged in and can search for a specific user(must exist).

- **Trigger:** Press “send private message” button on another user’s profile

- **Primary Sequence:**
  
  1. User searches for a specific user
  2. System opens their user profile
  3. User presses the “Send private message” button on their user profile (Trigger)
  4. System opens a private chat window between the user and the recipient 
  5. User types a message in a chat box and hits enter
  6. System sends the message to the recipient and only the user and recipient can see the messages displayed in chat

- **Primary Postconditions:** 
Either the recipient or the user receives a notification

- **Alternate Sequence:** 
  
  1. If the user receives a private message from another user, the user receives a notification
  2. Do steps 1-6 in primary sequence to view the new messages sent by another user

6. Search Message (Hai)
- **Pre-condition:**  User must have a user profile and is logged in

- **Trigger:** Press the “Search message” button on user profile

- **Primary Sequence:**
  
  1. User presses the “search message” button on user profile (Trigger
  2. System opens a list of all messages that the user sent
  3. User types in a specific message in the search message bar
  4. System responds by displaying all messages with the exact message
  5. User presses the specific message
  6. System displays the message 

- **Primary Postconditions:** 
User is logged in and list of messages is still displayed

- **Alternate Sequence:** 
  
  1. If the number of messages is greater than 10, System only displays 10 messages and user can scroll down for more users
  2. Do steps 2-6 in primary sequence