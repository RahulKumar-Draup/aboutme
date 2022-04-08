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
            self.make_new_entry()
        elif self.num == 2:
            self.edit_details()
        elif self.num == 3:
            self.delete_data()

    '''USER ENTERS THEIR DETAILS THROUGH HERE '''

    def enter_detail(self):
        name = str(input('Enter your name:'))
        profession = str(input("Enter your profession: "))
        contact = str(input("enter your contact: "))
        skills = str(input("Enter your skills: "))
        about = str(input("Enter about yourself in detail: "))
        passion = str(input("Enter your passion : "))
        organisation = str(input("Enter your organisation : "))
        extra_skills = str(input("Enter your extra skills : "))
        secret_key = contact[::-1]
        print("your secret key is: ", secret_key)
        print("  "*30)
        print("your details are successfully submitted")

        y = {'name': name, 'profession': profession, 'contact': contact, 'skills': skills, 'about': about,
             'passion': passion, 'organisation': organisation, 'extra_skills': extra_skills, 'secret_key': secret_key}
        # with open('details.json','w') as file:
        #
        #     json.dump(y,file)
        return y

    def make_new_entry(self):
        entry = self.enter_detail()
        with open('details.json', 'r') as file:
            data = json.load(file)
            data = list(data)

        data.append(entry)
        with open('details.json', 'w') as file:
            json.dump(data, file, indent=2)

    def delete_data(self):
        key = str(input("enter your sceret key : "))
        user = self.load_data()
        new = []
        # print(data[1].get('name'))
        for person in user:
            if key == person.get('secret_key'):
                pass
            else:
                new.append(person)
        with open('details.json', 'w') as file:
            json.dump(new, file, indent=2)

    def load_data(self):
        with open('details.json') as f:
            val = json.loads(f.read())
            return val

    """printing entry by each person"""

    def view_all_entry(self):
        user = self.load_data()
        # print(user)
        print("-"*30+"ALL RECORDS"+"-"*30)
        for person in range(len(user)):
            print('name:', user[person].get('name'))
            print('profession:', user[person].get('profession'))
            print('contact:', user[person].get('contact'))
            print('skills:', user[person].get('skills'))
            print('passion:', user[person].get('passion'))
            print('organisation:', user[person].get('organisation'))
            print('extra_skills:', user[person].get('extra_skills'))
            print("-"*50)
        return 'All data are as above'

    def search_by_npc(self):

        val = input('Enter name or profession or contact to search by: ')
        print("-"*30+"RECORDS"+"-"*30)
        user = self.load_data()
        matched = []
        for person in user:
            if val == person.get('name'):
                matched.append(person)
            elif val == person.get('profession'):
                matched.append(person)
                # return person
            elif val == person.get('contact'):
                matched.append(person)
        if matched:
            for person in range(len(matched)):
                print('name:', matched[person].get('name'))
                print('profession:', matched[person].get('profession'))
                print('contact:', matched[person].get('contact'))
                print('skills:', matched[person].get('skills'))
                print('passion:', matched[person].get('passion'))
                print('organisation:', matched[person].get('organisation'))
                print('extra_skills:', matched[person].get('extra_skills'))
                print("-" * 50)
            return "All matches found are as above"
        else:
            return "No such record available"

    '''with object for this class add .search_by_NCP()'''
    def search_by_secretkey(self):
        key = str(input("enter your secret key: "))
        print("-" * 30 + "RECORDS" + "-" * 30)
        user = self.load_data()
        matched = []
        for person in user:
            if person.get('secret_key') == key:
                matched.append(person)
        if matched:
            for person in range(len(matched)):
                print('name:', matched[person].get('name'))
                print('profession:', matched[person].get('profession'))
                print('contact:', matched[person].get('contact'))
                print('skills:', matched[person].get('skills'))
                print('passion:', matched[person].get('passion'))
                print('organisation:', matched[person].get('organisation'))
                print('extra_skills:', matched[person].get('extra_skills'))
                print("-" * 50)
            return "All matches found are as above"
        else:
            return "No such record"

    def edit_details(self):
        key = str(input("To edit you detail enter your secret key: "))
        user = self.load_data()
        new = []
        for person in user:
            if key == person.get('secret_key'):
                newdata = {}
                newdata['name'] = input('Enter updated name: ')
                newdata['profession'] = input('Enter updated profession: ')
                newdata['contact'] = input('Enter updated contact : ')
                newdata['skills'] = input('Enter updated skills: ')
                newdata['passion'] = input('Enter updated passion: ')
                newdata['organisation'] = input('Enter updated organisation: ')
                newdata['extra_skills'] = input('Enter updated extra_skills: ')
                newdata['secret_key'] = newdata['contact'][::-1]
                new.append(newdata)
                print("--------details updated search your data by secret key to see updated record--------")
            else:
                newdata = {}
                newdata['name'] = person.get('name')
                newdata['profession'] = person.get('profession')
                newdata['contact'] = person.get('contact')
                newdata['skills'] = person.get('skills')
                newdata['passion'] = person.get('passion')
                newdata['organisation'] = person.get('organisation')
                newdata['extra_skills'] = person.get('extra_skills')
                newdata['secret_key'] = person.get('secret_key')
                new.append(newdata)
            with open('details.json', 'w') as f:
                json_data = json.dumps(new, indent=2)
                f.write(json_data)


num = int(input())
obj = User(num)

if num == 6:
    print(obj.search_by_secretkey())
elif num == 5:
    print(obj.search_by_npc())
elif num == 4:
    print(obj.view_all_entry())
else:
    print(obj)

    # '''A CLASS  OBJECT IS CREATED WITH ENTERED DATA'''


# def __str__(self):
#     val = input('Enter name or profession or contact to search by: ')
#     user = self.load_data()
#     for person in range(len(user)):
#         if val == user[person].get('name') or val == user[person].get('profession') or val == user[person].get(
#                 'contact'):
#             return f'{user[person]}'
#         else:
#             return "no such objects"
#
# def __repr__(self):
#     user = self.load_data()
#     key = str(input("enter your secret key: "))
#     for person in user:
#         if key == person.get('secret_key'):
#             return f"{user[person]}"
#     else:
#         return "No such record found"


# print('name:', user[person].get('name'))
# print('profession:', user[person].get('profession'))
# print('contact:', user[person].get('contact'))
# print('skills:', user[person].get('skills'))
# print('passion:', user[person].get('passion'))
# print('organisation:', user[person].get('organisation'))
# print('extra_skills:', user[person].get('extra_skills'))
