# NETFLOX

The company NETFLOX wishes to have a system that allows them to manage their online business, which essentially involves renting various types of items (series, movies, and documentaries) for online viewing and managing their inventory of available rental items. Therefore, it is necessary to build a database application that allows customers, for example, to search for and rent available items and allows administrators, who are manually added to the database, to perform typical system management tasks (e.g., adding a new item or viewing statistics).

## Implemented Functions:
For better program manipulation, we have implemented various functions organized into different categories, namely:

• _Menus_

• _Opcao_

• _Registo_

• _Procura_

• _Atualiza_

• _Verifica_

• _Estatisticas_


**_Menus_:**

This was the function that served as the main foundation for our program. Here, we created the initial menu, registration menu, login menu, administrator menu, and customer menu. Additionally, we created a function that allows us to insert administrators into our database.

**_Opcao_:**

This menu is intended for the choices that the administrator and customer have within their respective menus.
The options available in the customer menu include: viewing messages sent by the administrator, viewing all items, and accessing the store where they can rent an item.
For the administrator menu, the available options include adding items, deleting items, changing the price of an item, increasing a customer's balance, sending messages to customers, and listing all available items.

**_Registo_:**

This function is used to record various pieces of information that are useful for both the administrator and the customer. This function is used to register customers, administrators, to record the rental of an item, to record the history of changes to an item. It also serves to record a message and to register whether it has been read or not.

**_Procura_:**

The _Procura_ function is used to retrieve information, including the old price of an item, the price of a specific item, the balance of a customer, the ID of an item, the name of a customer, messages, and other options.

**_Atualiza_:**

This function is used to keep the database constantly updated so that it remains up-to-date whenever there is a change in the data. We have created functions to delete an item, change the price of an item, update a customer's balance, and update the status of a message.

**_Verifica_:**

This function is used for verifying all the credentials of both administrators and customers.

**_Estatisticas_:**

This function is used to display the total number of customers, the total number of items, the total number of items by type, and the total number of items rented.



## Requirements:

• Python 3.8.5

• PostgreSQL 12

• Psycopg2 2.8.6

• PyCharm

• ONDA in https://onda.dei.uc.pt
