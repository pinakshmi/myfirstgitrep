from tkinter import *

import mysql.connector #functionality to connect to a database but not directly

import sys

class Tinder:




    def __init__(self):

        self.conn=mysql.connector.connect(host='localhost', user='root', password='', database='tinder2')
        self.mycursor=self.conn.cursor()#this is a sticker variable for identification

        self.root2 = Tk()#first window... the tinder page

        #self.root2.iconbitmap(r'C:\Python34\DLLs\tinder_new.ico')

        self.root2.title('Welcome!Find friends,dates,relationships and everything in between!')

        self.root2.minsize(250, 150)
        self.root2.maxsize(650, 450)

        self.photo=PhotoImage(file='tinder_small.png')
        self.pic=Label(self.root2, image=self.photo).pack()


        self.message1=Label(self.root2, text='What would you like to do?', fg='Red')
        self.message1.pack()

        self.btn1=Button(self.root2, text='Register', command=lambda: self.registration())
        self.btn1.pack()

        self.btn2=Button(self.root2, text='Login', command=lambda: self.login_gui())
        self.btn2.pack()

        self.btn3=Button(self.root2, text='Exit', command=lambda: self.exit_gui())
        self.btn3.pack()

        self.result2=Label(self.root2, text='', fg='Red')
        self.result2.pack()



        self.root2.mainloop() #end of window 1


    def login_gui(self):

        self.root = Tk()#the login window starts here

        self.root.title('Login')

        self.root.minsize(250, 350)
        self.root.maxsize(250, 350)

        self.email_label = Label(self.root, text='Enter Email')
        self.email_label.pack()

        self.email_input = Entry(self.root)
        self.email_input.pack()

        self.password_label = Label(self.root, text='Enter password')
        self.password_label.pack()

        self.password_input = Entry(self.root)
        self.password_input.pack()

        self.button = Button(self.root, text='Login', command=lambda: self.perform())
        self.button.pack()

        self.result = Label(self.root, text='', fg='Red')
        self.result.pack()

        self.message = Label(self.root, text='not a member?', fg='Red')
        self.message.pack()

        self.button = Button(self.root, text='Register', command=lambda: self.registration())
        self.button.pack()

        self.root.mainloop() #end of login window

    def perform(self):

        email = self.email_input.get()
        password = self.password_input.get()

        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))#database interaction to avoid unregistered users to access facilities

        user_list = self.mycursor.fetchall()

        if len(user_list) > 0:
            self.result.configure(text='Welcome')

            self.current_user_id=user_list[0][0]
            if self.current_user_id!=0:

                self.root3 = Tk()#the account window of the concerned user

                self.root3.title('Your account')
                self.root3.minsize(450, 350)
                self.root3.maxsize(1250, 1250)

                self.messge = Label(self.root3, text='How would you like to proceed?', fg='Red')
                self.messge.grid(row=0, column=3)

                self.btn4 = Button(self.root3, text='View all users', fg='Blue', command=lambda: self.view_users()).grid(row=1, column=0)

                self.btn5=Button(self.root3, text='View all proposals', fg='Red', command=lambda: self.view_proposals()).grid(row=1, column=1)
                self.btn6=Button(self.root3, text='View all requests', fg='Blue', command=lambda: self.view_requests()).grid(row=1, column=2)
                self.btn7=Button(self.root3, text='View all matches', fg='Red', command=lambda: self.view_matches()).grid(row=1, column=3)

                self.btn8=Button(self.root3, text='Logout', fg='Blue', command=lambda: self.logout()).grid(row=1, column=4)



                self.root3.mainloop()#end of the account window

            else:
                self.result.configure('you are not logged in')
        else:
            self.result.configure(text='Incorrect credentials')



    def registration(self):

        self.root1 = Tk()#registration window
        self.root1.title('Registration process')
        self.root1.minsize(250, 350)
        self.root1.maxsize(250, 350)

        self.name_label = Label(self.root1, text='Enter Name')
        self.name_label.pack()

        self.name_input = Entry(self.root1)
        self.name_input.pack()

        self.email_label = Label(self.root1, text='Enter email')
        self.email_label.pack()

        self.email_input = Entry(self.root1)
        self.email_input.pack()

        self.password_label = Label(self.root1, text='Enter password')
        self.password_label.pack()

        self.password_input = Entry(self.root1)
        self.password_input.pack()

        self.gender_label = Label(self.root1, text='Enter gender')
        self.gender_label.pack()

        self.gender_input = Entry(self.root1)
        self.gender_input.pack()

        self.age_label = Label(self.root1, text='Enter age')
        self.age_label.pack()

        self.age_input = Entry(self.root1)
        self.age_input.pack()

        self.city_label = Label(self.root1, text='Enter city')
        self.city_label.pack()

        self.city_input = Entry(self.root1)
        self.city_input.pack()

        self.button = Button(self.root1, text='Go', command=lambda: self.entrydatabase())
        self.button.pack()

        self.result1 = Label(self.root1, text='', fg='Red')
        self.result1.pack()

        self.root1.mainloop()#end of registration window

    def entrydatabase(self):

        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        gender = self.gender_input.get()
        age = self.age_input.get()
        city = self.city_input.get()

        self.mycursor.execute(
            """INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `gender`, `age`, `city`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}', '{}')""".format(
                name, email, password, gender, age, city))#database interaction to store registered feilds
        self.conn.commit()

        self.result1.configure(text='Registration successful')



    def view_users(self):


        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}'""".format(self.current_user_id))

        all_users_list=self.mycursor.fetchall()

        j=2
        for i in all_users_list:
            str1='---------------------------------------------\n'
            str1=str1+str(i[0])+'   '+str(i[1])+'   '+str(i[4])+'   '+str(i[5])+'   '+str(i[6])
            str1=str1+'\n---------------------------------------'
            self.show_users=Label(self.root3, text=str1).grid(row=j, column=0)
            j+=1


        self.root4=Tk()#proposing window
        self.root4.title('Proposing....')
        self.root4.minsize(550, 250)
        self.root4.maxsize(650, 350)

        self.questin=Label(self.root4, text='enter the user id of the user whom you want to propose', fg='Red').pack()
        self.juliet_id=Entry(self.root4)
        self.juliet_id.pack()

        self.btnpro = Button(self.root4, text='propose', fg='Red', command=lambda: self.check()).pack()

        self.resultp=Label(self.root4, text='', fg='Red')
        self.resultp.pack()
        self.root4.mainloop()#it closes on the users wish


    def check(self):

        jjuliet_id=self.juliet_id.get()

        self.mycursor.execute("""SELECT * FROM `proposals` WHERE `romeo_id` LIKE '{}' AND `juliet_id` LIKE '{}'""".format(self.current_user_id,jjuliet_id))#checking whether the person has already proposed or not

        proposed_already=self.mycursor.fetchall()

        if len(proposed_already)>0:

            self.resultp.configure(text='sabr kar!fal meetha hi hotha hai')

        else:
            self.propose(self.current_user_id, jjuliet_id)



    def propose(self, romeo_id, juliet_id):

        self.mycursor.execute("""INSERT INTO `proposals` (`proposal_id`, `romeo_id`, `juliet_id`) VALUES (NULL, '{}', '{}')""".format(romeo_id,juliet_id))#proposing

        self.conn.commit()

        self.resultp.configure(text='proposal succesfully sent.Fingers crossed!')


    def view_proposals(self):

        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE p.`romeo_id` LIKE '{}'""".format(self.current_user_id))

        self.proposed_user_list=self.mycursor.fetchall()

        j=2
        for i in self.proposed_user_list:
            str2='-----------------\n'
            str2=str2+str(i[4])+'  '+str(i[7])+'  '+str(i[8])+'  '+str(i[9])
            str2=str2+'\n--------------------'
            self.view_pro=Label(self.root3, text=str2).grid(row=j, column=1)
            j+=1



    def view_requests(self):

        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`romeo_id` WHERE p.`juliet_id` LIKE '{}'""".format(self.current_user_id))

        self.requested_user_list=self.mycursor.fetchall()

        j=2
        for i in self.requested_user_list:
            str3 = '-----------------\n'
            str3 = str3 + str(i[4]) + '  ' + str(i[7]) + '  ' + str(i[8]) + '  ' + str(i[9])
            str3 = str3 + '\n--------------------'
            self.view_pro = Label(self.root3, text=str3).grid(row=j, column=2)
            j+=1



    def view_matches(self):


            self.mycursor.execute(
                """SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE `juliet_id` IN (SELECT `romeo_id` FROM `proposals` WHERE `juliet_id` LIKE '{}') AND `romeo_id` LIKE '{}'""".format(self.current_user_id,self.current_user_id))

            match_list = self.mycursor.fetchall()

            j=2
            for i in match_list:
                str4 = '-----------------\n'
                str4 = str4 + str(i[4]) + '  ' + str(i[7]) + '  ' + str(i[8]) + '  ' + str(i[9])
                str4 = str4 + '\n--------------------'
                self.view_pro = Label(self.root3, text=str4).grid(row=j, column=3)
                j+=1





    def logout(self):

        self.current_user_id=0

        self.root3.destroy()
        self.root.destroy()



    def exit_gui(self):

        self.result2.configure(text='Bye')
        sys.exit()



user=Tinder()

