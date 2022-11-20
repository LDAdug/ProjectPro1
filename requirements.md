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
