import json


class User:

    """ASKING USER CHOICE"""

    print("enter 1 to submit new details:")
    print("enter 2 to edit your details:")
    print("enter 3 to delete your details:")
    print("enter 4 to  see all records:")
    print("Enter 5 to search by name, profession or contact")
    print("Enter 6 to search by secret key")

    """DIRECTING TO FUNCTIONS BASED ON USER CHOICE"""

    def __init__(self, num):
        self.num = num
        if self.num == 1:
            self.enter_detail()
        # elif self.num == 2:
        #     self.edit_details()
        # elif self.num ==3:
        #     self.delete_entry()
        # elif self.num==4:
        #     self.view_details()

    '''USER ENTERS THEIR DETAILS THROUGH HERE '''

    def enter_detail(self):
        name = str(input('Enter your name:'))
        profession = str(input("Enter your profession: "))
        contact = int(input("enter your contact: "))
        skills = str(input("Enter your skills: "))
        about = str(input("Enter about yourself in detail: "))
        passion = str(input("Enter your passion : "))
        organisation = str(input("Enter your organisation : "))
        extra_skills = str(input("Enter your extra skills : "))
        print("your secret key is")
        print("your details are successfully submitted")


'''A CLASS  OBJECT IS CREATED WITH ENTERED DATA'''

obj = User(1)
print(obj)






    #
    #     with open('details.json','w') as f:
    #         json.dump(data,f)
    #
    #     with open('details.json') as jsonfiles:
    #         data = json.load(jsonfiles)
    #         temp = data['user']
    #         y = {'name':name,'profession':profession,'contact':contact,'skills':skills,'about':about,'passion':passion,
    #              'organisation':organisation,'extra_skills':extra_skills,'secretkey':secret_key}
    #         temp.append(y)
    # enter_detail(data)
    #
    #
    # def edit_details(self):
    #
    #
    #
    #
    # def delete_entry(self):
    #
    #
    #
    #
    # def secretkey(self):
    #     return -------------
    #
    #
    #
    # def search_by_NPC(self,name,profession,contact):
    #     file = open('details.json', 'r')
    #     json_data = file.read()
    #     json_obj = json.loads(json_data)
    #     for value in json_obj['user']:
    #
    #         if name == value['name']:
    #             return ---------
    #         elif profession == value['profession']:
    #             return ----------
    #         elif contact == value['contact']:
    #             return ----------
    #
    #
    # def searchby_secretkey(self,secretkey):
    #     if secretkey ==
    #
    #
    #
    # def view_details(self):
    #
    #     file = open('details.json','r')
    #     json_data = file.read()
    #     json_obj = json.loads(json_data)
    #     for value in json_obj['user']:
    #         print('name',value['name'])
    #         print('profession',value['profession'])
    #         print('contact',value['contact'])
    #         print('skills',value['skills'])
    #         print('about',value['about'])
    #         print('passion',value['passion'])
    #         print('organisation',value['organisation'])
    #         print('extra skills',value['extra skills'])
    #
    #
    #
    #
    #


