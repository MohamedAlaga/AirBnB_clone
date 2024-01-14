<p align="center">
  <img src="./hbnb.png?raw=true" alt="HBNB logo">
</p>
<h1 align="center">HBnB console</h1>
<p align="center">An AirBnB clone.</p>
---

## Description

Hbnb - console  is a command interpreter for a web application that can manipulate a powerful storage system,
The console will be a tool to validate this storage engine it is only the back end console.

## Classes 

HolbertonBnB utilizes the following classes:

1- BaseModel\n
    PUBLIC INSTANCE ATTRIBUTES:
        <ul>
        <li>id</li>
        <li>created_at</li>
        <li>updated_at	</li>
        </ul>
    PUBLIC INSTANCE METHODS:
        <ul>
        <li>save</li>
        <li>to_dict</li>
        </ul>

2- FileStorage\n
    PUBLIC INSTANCE METHODS:
        <ul>
        <li>all</li>
        <li>new</li>
        <li>save</li>
        <li>reload</li>
        </ul>
    PRIVATE CLASS ATTRIBUTES:\n
        <ul>
        <li>file_path</li>
        <li>objects</li>
        </ul>

3-User\n
Inherits from BaseModel
    PUBLIC CLASS ATTRIBUTES:
        <ul>
        <li>email</li>
        <li>password</li>
        <li>first_name</li>
        <li>last_name</li>
        </ul>

4-State \n
Inherits from BaseModel
        <ul>
        <li>name</li>
        </ul>

5-City\n
Inherits from BaseModel
    PUBLIC CLASS ATTRIBUTES
        <ul>
        <li>state_id</li>
        <li>name</li>
        </ul>

6-Amenity\n
Inherits from BaseModel
    PUBLIC CLASS ATTRIBUTES
        <ul>
        <li>name</li>
        </ul>

7-Place\n
Inherits from BaseModel
    PUBLIC CLASS ATTRIBUTES
        <ul>
        <li>city_id</li>
        <li>user_id</li>
        <li>name</li>
        <li>description</li>
        <li>number_rooms</li>
        <li>number_bathrooms</li>
        <li>max_guest</li>
        <li>price_by_night</li>
        <li>latitude</li>
        <li>longitude</li>
        <li>amenity_ids</li>
        </ul>

8-Review\n
Inherits from BaseModel
    PUBLIC CLASS ATTRIBUTES
        <ul>
        <li>place_id</li>
        <li>user_id</li>
        <li>text</li>
        </ul>
