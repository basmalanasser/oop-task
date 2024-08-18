#class MagicalContact:
    #def __init__(self):
#n=input("enter:")
#e=input("enter:")
#pn=int(input ("enter:"))
class MagicalContact:
    def __init__(self,name,email,phonenum):
        self.__name=name
        self.__email=email
        self.__phonenum=phonenum

    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_phonenum(self):
        return self.__phonenum
    def set_email(self,new_email):
        self.__email=new_email
    def set_phonenum(self,new_phonenum):
        self.__phonenum=new_phonenum
    def describe(self):
        print(f"Name:{self.__name},Email:{self.__email},Phone number:{self.__phonenum}")

class WizardOrWitch(MagicalContact):
    def __init__(self,name,email,phonenum,wand,house):
        super().__init__(name,email,phonenum)
        self.__wand=wand
        self.__house=house

    def get_wand(self):
        return self.__wand
    
    def get_house(self):
        return self.__house
    
    def describe(self):
        super().describe()
        print(f"Wand:{self.__wand},House:{self.__house}")

class MagicalCreature(MagicalContact):
    def __init__(self, name, email, phonenum,species,is_tame):
        super().__init__(name, email, phonenum)
        self.__species=species
        self.__is_tame=is_tame

    def get_species(self):
        return self.__species
    
    def is_tame(self):
        return self.__is_tame
    
    def describe(self):
        super().describe()
        print(f"Species:{self.__species},Tame:{self.__is_tame}")

class MagicalContactBook:
    def __init__(self):
        self.__contacts=[]

    def add_contact(self,contact):
        self.__contacts.append(contact)

    def show_contacts(self):
        for contact in self.__contacts:
            contact.describe()

    def search_contact(self,name):
        for contact in self.__contacts:
            if contact.get_name()==name:
                return contact
        else:print("not found")

contact_book=MagicalContactBook()
harry=WizardOrWitch("Harry Potter","harry@hogwarts.com","+44 1987654320","wards","gryffindor")
dobby=MagicalCreature("Dobby","dobby_2806@free_elfmail.elf","+44 01234567890","gr",True)
draco=WizardOrWitch("Draco","draco@hogwarts.com","+44 1044567800","holly","slytherin")
contact_book.add_contact(harry)
contact_book.add_contact(dobby)
contact_book.add_contact(draco)

#contact_book.show_contacts()
name=input("enter the name ur searching for:")
found_contact=contact_book.search_contact(name)
if found_contact:
    print(found_contact.describe())
else:print("not found")
new_phonenum=input("enter phone:")
new_email=input("enter the new email:")
harry.set_phonenum(new_phonenum)
harry.set_email(new_email)
print(harry.describe())

#harry.get_email()
#print(f"Name:{harry.get_name()}")
#print(f"Email:{harry.get_email()}")
#print(f"phone number:{harry.get_phonenum()}")
#print(f"wand:{harry.get_wand()}")
#print(f"house:{harry.get_house()}")
#print(harry.get_house())
#print(dobby.get_name())
#print(dobby.get_email())
#print(dobby.get_phonenum())
#print(dobby.get_species())
#print(dobby.is_tame())
#print(contact_book.search_contact("Dobby"))



