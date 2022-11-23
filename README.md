# TodoList Application
### TodoList Apps:
* #### core 
create, login, profile <b>USER</b> 

***
* ####goals

Create, list view, detail view, update, delete:
1. boards
2. categories
3. goals
4. comments
***
* #### bot
Telegram bot <b>@ibelousov_bot</b>

Review all goals & create new goal
***


### For run app (local):
* clone repo https://github.com/blazkowicz-pnz/todo_list
* install & activate env
* Install dependencies from requirements.txt <b>(pip install requirements.txt)</b>
* Build & launch containers from <i>todo_list</i> folder <b>(docker-compose up -d --build postgres)</b>
* Make migrations <b>(.\manage.py makemigrations)</b> 
* Apply migrations <b>(.\manage.py migrate)</b>
* Run app <b>(.\manage.py runserver)</b>
***

The application is available at http://ibelousov.ga