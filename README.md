# sanctuary_django_app


## Project Overview 

The purpose of this application is to provide a way for those that like farming simulation games to try out a demo of the game.  It will also provide a discussion section similar to Twitter where users can share images, short video clips and write short messages.  This will help create a community based around the game while giving the users the ability to try it.  

## Libraries nd Frameworks

### Frontend
- Vue.js
- Vuex
- Bootstrap

### Backend
- Django 
- DjangoRestFramework
- JWT
- Pillow
- Postgresql

## User Stories


#### Story 
As a player, I want to be able to share my thoughts to the development team and other players.  Along with commenting on other players comments because I want to be able to share my thoughts and opinions.  
#### Tasks
- Provide a social communication platform that allows user to post images and short messages
    - This will include a database object for each post.  
- Each post will be allow replies to be connected to it
#### Story 
As a player, I want to be able to find other posts about similar topics, and customize my feed so that I can easily find content that interests me.   
#### Tasks 
- Allow for the use of hastags in a post for sorting through the database objects 
- Allow search by sorting
- Use selected hashtags for sorting initial feed upon page load
#### Story 
As a player, I want to be able to try out the game and save my progress, because I like farming simulators and want to continue where I left off.  
#### Tasks
- Link the user object to save game data
#### Story 
As an admin, I want to be able to remove inappropriate posts and provide temporary bans for users so that we can keep the community healthy and family friendly.
#### Tasks 
- All users to report inappropriate posts
- Provide administrators the ability to investigate reports posts and provide temporary bans if necessary


## Schema 

Players
- Extends BaseUser model
- UserID (string)
- Display Name (string)
- Name (string)
- Email Address (string)
- Phone Number (string)
- Bio (string)
- Suspended (boolean)

Posts
- ID (string)
- Date (datetime)
- Text Content (string)
- Image Content (img)
- Hashtags (string)

Replies
- ID (Foreign Key to Post)
- Date (datetime)
- Text Content (string)
- Image Content (img)

GameData
- JSON Save file (JSON)
- UserID (foreign key to Player)

## Features 

#### Must Haves
- Make account - to save game info, create and reply to posts
- Create posts 
- Reply to posts 
- See post feed

#### Should Haves 
- Search posts' content
- Create and save feed filters

#### Can Haves 
- Create admins roles
- Allow admins to enforce community guidelines

#### Won't Haves
- Share short video clips 

## Schedule 
#### Week 1 
- Create Models
- Create Serializers
- Create views for creating and reading posts
- Create view for reply to posts

#### Week 2 
- Create view for deleting and updating posts
- Create Vue api with fetch to connect django and frontend
- Create feed sorting algorithm (simple by date, filtered by perferred topics)
- Work on CSS

#### Week 3 
- Connect game WebGL application to Django 
- Connect save file to model
- Work on CSS 

#### Week 4 
- Create admin role 
- Work on CSS 
- Create Dynamic Landing Page (stretch goal)