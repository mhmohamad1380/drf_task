<div  align="center">
<h1  align="center">Dockerized Django Rest Framework task</h1>
</div>

## Installation

1. first, You should clone this Repository.<br/>
2. delete the txt file exists in db folder
3. at the third step, go to the Cloned Directory, then Open in Terminal(CMD). <br/>
4. then, type ```docker-compose up --build ``` and Press Enter. (tip: make sure that Docker and Docker-Compose are Installed on Your Machine)
5. tip: username and password are ``` admin ```

## Routes

1. ```api/register``` to Register with DRF <br/>
2. ```api/login``` to Login <br/>
3. ```api/logout``` to logout <br/>
4. ```api/users/profile/<pk>``` to see user's profile <br/>
5. ```api/notes/create/``` to create a note <br/>
6. ```api/notes/list/``` to see notes list <br/>
7. ```api/notes/edit/<pk>``` to edit your note with pk=pk <br/>
8. ```api/notes/like?note=<pk>``` to like a note with pk=pk <br/>
9. ```api/notes/dislike?note=<pk>``` to take like back from note with pk=pk <br/>


### Good Luck