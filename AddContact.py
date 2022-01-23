

=== Module description ===
This module contains two sample classes Tweet and User that we developed
as way to introd
uce the major concepts of object-oriented programming.
"""
# Allows forward references in type annotations.
from __future__ import annotations
from datetime import date  # Python library for working with dates (and times)


class Person:
    """add a person for contact

    === Attributes ===
    name: the name of the person
    number: the phone number
    birthday: the date the person was born in
    email: the email of this person

    """
    # Attribute types
    name: str
    number: str
    birthday: date
    email: str

    def __init__(self, name: str, number: str, birthday: date, email: str) -> None:
        """
        Initialize a new contact.
        """
        self.name = name
        self.number = number
        self.birthday = birthday
        self.email = email

    def edit(self) -> None:
        """
        Replace the contents of this contact with new information
        """
        n = input ("What would you like to change: name, email, birthday, or number: ")
        try:
            if (n.lower() == "name" ):
                change = input("Please enter what to change it to: ")
                self.name = change

            if (n.lower() == "email" ):
                change = input("Please enter what to change it to: ")
                self.email = change

            if (n.lower() == "birthday" ):
                year = int (input("Please enter the birth year: "))
                month = int (input("Please enter the birth month: "))
                day = int(input("Please enter the birth day: "))
                self.birthday = date(year, month, day)

            if (n.lower == "number"):
                change = input("Please enter what to change it to: ")
                self.number = change
        except:
            print ("Invalid entry, contact not changed")



    def get_something(self, n: str) :
        if (n.lower() == "name" ):
            return self.name

        if (n.lower() == "email" ):
            return self.email

        if (n.lower() == "birthday" ):
            return self.birthday

        if (n.lower == "number"):
            return self.number

    def __str__(self):
        print ("Name:" , self.name, "/n Number: " ,self.number,  "/n birthday: ", self.birthday,
               "/n email: ", self.email  )


class Contact:
    """THe contact list

    === Attributes ===
    contacts: a list of the tweets that this user has made.
    """
    # Attribute types
    contacts: list[Person]


    def __init__(self) -> None:
        """Initialize this User contacts

        """
        self.contacts = []
        self.deleted = []

    def add_contact(self) -> None:
        """Record that this User made a tweet with the given content.

        Use date.today() to get the current date for the newly created tweet.

        """

        name = input ("Please enter the contacts name: ")
        email = input ("Please enter the contacts email: ")
        number = input ("Please enter the contacts number: ")
        try:
            year = int (input("Please enter the birth year: "))
            month = int (input("Please enter the birth month: "))
            day = int(input("Please enter the birth day: "))
            self.contacts.append(Person(name, number, date(year, month, day), email ))
            print ("The contact was added. ")
        except:
            print ("invalid entry, contact not added. ")



    def remove_contact(self) -> None:
        """
        Remove the given contact
        """
        n = input("Please enter the contacts name to be removed")
        for contact in self.contacts:
            if (contact.name == n):
                self.deleted.append(self.contacts.remove(contact))
                print ("The contact has been removed. ")



    def recover_contact(self) -> None:
        """
        recover the given contact if it was deleted
        """
        n = input("Please enter the contacts name to be added back")
        for contact in self.deleted:
            if (contact.name == n):
                self.contacts.append(self.deleted.remove(n))
                print ("This contact has been added back to your contact list.")


    def get_contact(self, n: str):
        thing = input("What would you like to get: Email, Birthday, or Number")
        for contact in self.contacts:
            if n == contact.name:
                print (contact.get_something(thing))
                return contact


    def print_all_contacts(self):
        for contact in self.contacts:
            print (contact.name)
            print ("\n")

    def edit_contact(self):
        print ('Printing all contacts...')
        self.print_all_contacts()
        name = input ("Please enter the name of the contact you want to edit")
        name = self.get_contact(name)
        name.edit()


    def options_menu(self):

        while True:

            h = int(input("What would you like to do: Please Enter a number: \n "
                          "1. Add a new contact \n"
                          "2. Delete a contact \n"
                          "3. Recover a deleted contact \n"
                          "4. Get information about a contact \n"
                          "5. Edit an exisiting contact \n "
                          "6. Show all your contacts: \n "
                          "7.  quit"))
            if (h == 1):
                self.add_contact()
            if (h == 2):
                self.remove_contact()
            if (h == 3):
                self.recover_contact()
            if (h == 4):
                name = input ("Please enter the name of the contact you want to edit")
                self.get_contact(name)
            if (h == 5):
                self.edit_contact()
            if (h ==6):
                self.print_all_contacts()
            if (h ==7):
                break
