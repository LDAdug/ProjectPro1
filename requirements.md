## <remove all of the example text and notes in < > such as this one>

## Functional Requirements
1. Login
2. Logout
3. Create new account
4. Delete account
5. User home page (user can see messages of users they follow)
6. Send message to followers
7. Search for user
8. Follow User
9. User Profiles
10. Post Image with message
11. Send/Receive Private Messages
12. Search Message

## Non-functional Requirements

1. Only expected to work on Google Chrome
2. Expected to work only on Desktop
3. Only available to English users
4. Expected to work on Mac/Windows/Linux

## Use Cases

1. Send message to followers (Lawrence)
- **Pre-condition:** <can be a list or short description> 
Followers must be following user and user must know who is following them

- **Trigger:** <can be a list or short description> 
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
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** 
Return condition where if a message has been successfully sent, return to user’s page where “send message to follower” button is offered and notify message sent successfully.


- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. User selects button to “send message to followers”
  2. Alternate Tigger #2: Saves all followers onto a list
  3. Calls for user to create a message
  4. Message saved onto a string
  5. Send button after message is ready to be sent
  6. Message is exported and imported to the followers
  7. Message is called and displayed to the follower
  8. … 

3. Follow User (Lawrence)
- **Pre-condition:** <can be a list or short description> 
Searched user must exist as a saved account on the app
User must not already be following searched user

- **Trigger:** <can be a list or short description> 
User clicks on button to initiate “Follow User”

- **Primary Sequence:**
  
  1. User searches up another user they wish to follow
  2. Brings user to other user’s profile page
  3. Next to username, provides button to “Follow User”
  4. After clicking “Follow User” “following” counter increases by 1
  5. Followed user’s “followed” count increases by 1
  6. Change “Follow User” button to “Unfollow User”
  7. Proceed to postcondition
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 
If following and follower count when incremented returns true, return a notification message to follower and followee confirming changes to their respected lists

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. User searches up user they wish to follow
  2. Brings user to other user’s profile page
  3. Display “Follow User” button
  4. If User is already followed, display “Unfollow User” button instead
  5. If searcher selects button, decrement searched user’s follower count by 1
  6. Decrement user’s following count by 1
  7. Change “Unfollow User” button to “Follow User” button
  8. Proceed to post condition


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