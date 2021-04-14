import mysql.connector
import re
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",  #Enter password of your database
  database='office'
)

print(mydb)
cur = mydb.cursor()


class Person:
   'Common base class for all person'

   def __init__(self, name,money,sleepmood,healthrate):
      self.name = name
      self.salary = money
      self.sleepmood = sleepmood
      self.healthrate = healthrate
      #property betwwen 0 and 100
   def sleep(self,hourssleep):
       print ("sleeeeeeeeeeeeeeeeep ")
       #bat5od 3dd al sa3t 2li al sh5s bynha lw 7 (sleep mood)happy lw less tired
       #lw akbr lazy
       if hourssleep == 7:
           print("7 happy ")
           sleepmood="happy"
       elif hourssleep < 7:
           sleepmood="tired"
           print("tired")
       elif hourssleep > 7:
           sleepmood="lazy"
           print("lazy")
       self.sleepmood=sleepmood
   def eat(self,meals):
       print ("eat")
       #bya5od al meals lw byakol 3 yb2aa health rate b 100
       if meals == 3:
          print("3")
          healthrate=100
       # Once guessed, loop will break
       elif meals == 2:
            print("2")
            healthrate=75
       elif meals == 1:
            print("1")
            healthrate=50
       self.healthrate=healthrate

   def buy(self,items,money_value):
      print ("buy")
      #bbuy bya5od al 3dd al items w 3la asasha by7dd decreaseMoney 10LE
      #kol ma yshtri item al money y2l b one
      self.money=int(money_value) - (int(items)*10)
      # print("money after buy "+ str(emp2.money))


class Employee(Person):
   'Common base class for all employees'
   id=1
   name="ma"
   email="marwa@email.com"
   money=1000
   salary=3444
   is_manager=1
   workmood="happy"
   sleepmood="happy"
   healthrate=100


    # class Student(Person):
    #   def __init__(self, fname, lname):
    #     Person.__init__(self, fname, lname)
   def __init__(self):
     print("employee constructor called")
   def work(self,hourswork):
     print ("work ")
     #bta5od al hours
     #lw 8 (work mood)happy lw less tired
     #lw akbr lazy
     if hourswork == 8:
        print("8")
        workmood="happy" # Once guessed, loop will break
     elif hourswork < 8:
        workmood="tired"
        print("tired")
     elif hourswork > 8:
        workmood="lazy"
        print("lazy")
     self.workmood=workmood
   def SendEmail(self,tomail,subject,body):
      print("send Email")
      #b7dd to (lmen)
      #b7dd al subject
      #b7dd al body
      # bt3ml create l file yomsl al email al mb3ot
      f=open("emailfile.txt",'w')
      # for ele in li:
      #    f.write(str(ele[0])+'\n')
      f.write("to:"+tomail+'\n')
      f.write("subject:"+subject+'\n')
      f.write(body+'\n')
      f.close()

   def displayEmployee(self):
       print("Name : ", self.name,  ", Salary: ", self.salary ,"email",self.email,"money",self.money,"sleepmood",self.sleepmood)


class Office():
   'Common base class for all employees'
   name="life"
   employees="employee"

   def get_all_employee(self):
     print ("get_all_employee ")
     cur.execute('select * from employee')
     rows = cur.fetchall()
     for row in rows:
         # print(row)
         print(row[0], row[1], row[2])
     mydb.commit()
     print('operation done successfully')
     # mydb.close()

   def getEmployee(self,idemp):
      print("get Employee")
      idempp=int(idemp);
      # print(idempp)
      # print(type(idempp))
      # cur.execute('select * from employee where id=1')
      # myresult = cur.fetchall()
      # for x in myresult:
      #     print(x)
      sql_select_query ="""select * from employee where id = %s"""
      cur.execute(sql_select_query,(idempp,))
      myresult = cur.fetchall()
      for row in myresult:
          if row[8] == 1:  ##manager
             print(row[0], row[1], row[2],row[3],row[5],row[6], row[7], row[8],row[9])
          else :
              print(row)

      mydb.commit()
      # mydb.close()

   def hireEmployee(self,officename,idhire):
      print("hire Employee")
      ###insert employee in database
      sql_update_query ="""Update employee set officename = %s where id = %s"""
      input_data =(officename,idhire)
      cur.execute(sql_update_query, input_data)
      mydb.commit();
      # mydb.close()
   def fireEmployee(self,idfire):
       print("fire Employee")
       ###delete employee from database
       query = "DELETE FROM employee WHERE id = %s"
       cur.execute(query, (idfire,))
       mydb.commit();
       # mydb.close()

import csv
import sys
name="name"
age=15
flag=0
def main():
  while 1:
    # menu(flag)
    # if flag == 1:
    #     break;
# def menu(flag):
    print("************Welcome to our office **************")
    print()
    choice = input("""
                      ADD: ADD new employee
                      fire: fire employee
                      hire:hire employee
                      all: All employees
                      one: One Employee
                      sendmail: sendmail
                      Q: Quite
                      Please enter your choice: """)
    if choice.lower() == "add" :
        add()
    elif choice.lower() == "fire":
        fire()
    elif  choice.lower() == "hire":
        hire()
    elif  choice.lower() == "all":
        allemployee()
    elif  choice.lower() == "one":
        oneemployee()
    elif  choice.lower() == "sendmail":
        sendmail()
    elif choice=="Q" or choice=="q":
        # flag=1
        mydb.close()
        sys.exit
        break;

    else:
        print("You must only select either A or B")
        print("Please try again")
        # menu()
def fire():
    print("enter id of employee you want to fire")
    idfire=int(input())
    fireoffice=Office();
    fireoffice.fireEmployee(int(idfire));

def hire():
    print("hire")
   ###y7ot asm al office llid 2li 7yd5lo
    print("enter id of employee you want to hire ")
    idhire=input()
    print("enter office ")
    officename=input()
    fireoffice=Office();
    fireoffice.hireEmployee(officename,int(idhire));

def allemployee():
    fireoffice=Office();
    fireoffice.get_all_employee();
def oneemployee() :
    print("enter id of employee  ")
    idemp=input()
    fireoffice=Office();
    fireoffice.getEmployee(int(idemp));
def sendmail():
    print("enter email you want   ")
    tomail=input()
    print("enter subject you want   ")
    subject=input()
    print("enter body you want   ")
    body=input()
    empmail = Employee()
    empmail.SendEmail(tomail,subject,body)
    # f=open("emailfile.txt",'w')
    # f.write("to:"+tomail+'\n')
    # f.write("subject:"+subject+'\n')
    # f.write("to:"+body+'\n')
    # f.close()

def add():
   print("ADD new employee ")
   def emenu():
    print("************select employee position **************")
    print()
    emp = input("""
                      If manager press “mngr”
					  if normal employee press “nrml”
                      Please enter your choice: """)
    if emp.lower() == "mngr" :
        manager()
    elif emp.lower() == "nrml":
        normal()
    else:
        print("You must only select either A or B")
        print("Please try again")
        emenu()
   emenu()
def data(is_manager_value):

    emp2 = Employee()
    emp2.is_manager=is_manager_value
    print("enter id of Employee")
    id_value=input()
    emp2.id=id_value
    #############################
    print("enter name of Employee")
    name_value=input()
    emp2.name=name_value
    #############################
    print("enter email")
    email_value=input()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while (not (re.search(regex,email_value))):
            print("invalid email enter valid email")
            email_value=input()
    emp2.email=email_value
    ##############################
    print("enter salary you take")
    salary_value=input()
    minSalary=1000
    while int(salary_value) <= 1000 :
        print("invalid salary enter salary greater than 1000")
        salary_value=input()
    emp2.salary=salary_value
    ###################################
    print("enter amount of money you have")
    money_value=input()
    emp2.money=money_value
    ##7sglha b3dd al items w b3den a3ml 3lehaa update 3la 7sb 3dd al items a2ll 10
    #########
    print("enter number of items you buy")
    items=input()
    print(int(items))
    ########################
    print("enter number of hours you sleep ")
    hoursSleep=input()
    # print(hoursSleep)
    emp2.sleep(int(hoursSleep))
    # emp2.sleepmood=sleepmood
    # ###########################
    print("enter number of meals you eat ")
    meals=input()
    print(meals)
    emp2.eat(int(meals))
    # rate= input()
    # minrate=0
    # maxrate=100
    # while emp2.healthRate <= int(rate) <= maxrate:
    #     print("valid rate")
    # ##############################
    print("enter number of hours you work ")
    hoursWork=input()
    print(hoursWork)
    emp2.work(int(hoursWork))
    ############################
    # emp2.money=int(money_value) - (int(items)*10)
    emp2.buy(items,money_value)
    print("money after buy "+ str(emp2.money))
    #########################
    cur.execute(f"Insert into employee (id,name, email,salary,money,is_manager,sleepmood,healthrate,workmood) \
     values('{emp2.id}','{emp2.name}','{emp2.email}','{emp2.salary}','{emp2.money}','{emp2.is_manager}','{emp2.sleepmood}','{emp2.healthrate}','{emp2.workmood}')")
    mydb.commit()
    # mydb.close()

def manager():
   print("manager")
   is_manager_value=1
   data(is_manager_value)
def normal():
   print("normal")
   is_manager_value=0
   data(is_manager_value)
#the program is initiated, so to speak, here
main()
