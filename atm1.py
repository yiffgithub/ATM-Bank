# # ATM example - fan yang
#
# Define global variables
# Define global variables
# Ask the customer to enter a name
# Define the query function #
# Define deposit function
# Define the deposit function #
# Define the withdrawal function #
#  Define main menu functions #
#
# Set up an infinite loop to make sure the program doesn't exit #
# //定义全局变量
money = 0;
name = None;



# 要求客户输入姓名和初始存款
name = input("what is your name?\n")
money = input("what is your primary deposit?\n")
#
# 定义查询函数
#
def query(show_header):
    if show_header:
        print("------------your balance-------------")
    print(f"{name}, your current balance is ${money} ")
# 定义存款函数
def saving (num):
    global money;
    money = int(money);
    num = int (num)
    money += num
  #  num = input("how much money you want to save?\n")
    print("------------your deposit-------------")
    print(name + " deposit " + str(num) + " successfully")


#调用查询函数

query(show_header= False);
#query(show_header= True);

# 定义取款函数
#
def get_money(num):
    global money;
    num = int(num)
    money = int(money);
    if num > money:
        print("you don't have enough deposit")
    else:
        money -= num;
        print("------------your withdrawal-------------")
        print(f"{name} withdraw {num} successfully")
        query(False)
#定义汇率转换函数
def exchange_currency():
    money = input("How much Chinese yuan do you have?\n")
    print("calculating")
    money = int(money)
    new_money = money / 5.3
    print("¥" + str(money) + " = " +"$"+ str(new_money))

# 定义主菜单函数
#

def main():
    #这里是用了制表符来强制对齐
    print("------------main menu-------------")
    print(name+", welcome to ATM bank system")
    print("check balance\t \t \t \t type 1")
    print("make a deposit\t \t \t \t type 2")
    print("make a withdrawal\t \t \t type 3")
    print("currency conversion(¥\u2192$)\t type 4")
    print("exit\t \t\t \t  \t \t type 5")
    return input("what is your decision?\n")
# 设置无限循环，确保程序不会退出
while(True):
    customer_decision = main();
    if customer_decision == "1":
        query(True)
        continue;
    elif customer_decision == "2":
        num = input("how much money you want to save?\n");
        saving(num);
        continue
    elif customer_decision == "3":
         num = input("how much money you want to withdraw\n")
         get_money(num)
         continue
    elif customer_decision == "4":
        exchange_currency()
        continue
    elif customer_decision == "5":
        print("exiting")
        print("see u next week")
        break;
    else:
        print("invalid input, try again!")







