#create table if you are playing for the first time
#create table user_info(user_id varchar(40),password varchar(40),win_no int,loss_no int,win_loss float);
import random
import pymysql as ms
conn=ms.connect(host='localhost',user='root',passwd='Ninthjuly0@',database='hangman')
cur=conn.cursor()
def login():
    def create():
        f=0
        while(True):
            print("Do You Know How To Play Hangman ? \n \n 1.Yes \n 2. No \n")
            how=input("Enter The Number Of Your Respective Choice. \n")
            if(how=="2"):
                print("Hangman Is Guessing Game For Two Or More Players. \n One Player Thinks Of A Word,\n Phrase Or Sentence And The Other(s) Tries To Guess It By Suggesting Letters Or Numbers,\n Within A Certain Number Of Guesses.")
                break
            elif(how=="1"):
                break
            else:
                print("Invalid choice")
        while(True): 
            global user_id
            user_id=input("Enter your username.")
            cur.execute('select user_id from user_info;')
            un=cur.fetchall()
            if(len(un)==0):
                f=1
            for k in un:
                if(user_id in k):
                    print("User name already taken,Try again")
                    break
                else:
                    f=1
            if(f==1):
                password=input("Enter your password")
                cur.execute('insert into user_info values(%s,%s,%s,%s,%s)',[user_id,password,0,0,0])
                conn.commit()
                break
    print("===============LOG IN===============\nDo you have an existing Login ID?\n1)Login \n2)Create ID")
    while(True):
        choice=input("Enter your choice")
        if(choice=="1" or choice=="2"):
            break
        else:
            print("Invalid choice")
    while(True):
        flag,flag5,flag1,b,c=0,0,0,0,0
        if(choice=="1"):
            while(True):
                global user_id
                user_id=input("Enter your username.")
                cur.execute('select user_id from user_info;')
                u=cur.fetchall()
                for i in u:
                    if(user_id in i):
                        flag=1
                        flag1=1
                        break
                    if(flag==0):
                        print("Your username is incorrect.\n Do you want to:- \n 1)Try again\n 2)Create Login ID")
                        choice1=input("Enter your choice")
                        if(choice1=="2"):
                            create()
                            flag,flag5,flag1=0,1,1
                            break
                        else:
                            print("Invalid option")
                if(flag1==1):
                    if(flag5==1):
                        b=1
                    break
            if(b==0):
                passwd=input("Enter your password")
                cur.execute('select password from user_info;')
                p=cur.fetchall()
                flag2,flag3=0,0
                while(True):
                    for j in p:
                        if(passwd in j):
                            flag2,flag3,c=1,1,1
                            break
                        if(flag2==0):
                            print("Your password is incorrect.")
                            passwd=input("Enter your password")
                    if(flag3==1):
                        break
                if(flag3==1):
                    break
            if(c==1):
                break
        if(choice=="2"):
            create()
            break
def hangman():
    hangman=("")
    hangman0=("___________________\n|\n|\n|\n|\n|\n|\n| ")
    hangman1=("___________________\n|             |\n|             O\n|\n|\n|\n|\n|")
    hangman2=("___________________\n|             |\n|             O\n|             |\n|             |\n|             |\n|\n|")
    hangman3=("___________________\n|             |\n|             O\n|             |\n|            /|\n|           / |\n|\n|")
    hangman4=("___________________\n|             |\n|             O\n|             |\n|            /|\ \n|           / | \ \n| \n|")
    hangman5=("___________________\n|             |\n|             O\n|             |\n|            /|\ \n|           / | \ \n|            /  \n|           /")
    hangman6=("___________________\n|             |\n|             O\n|             |\n|            /|\ \n|           / | \ \n|            / \ \n|           /   \ ")
    while(True):
        print("Choose One Of The Following Topics. \n \n 1.Animals \n 2.Seasons \n 3.Popular Games \n 4.Music Genres \n 5.Brand Names \n")        
        while(True):
            topic=int(input("Enter The Number Of Your Respective Choice."))
            if(topic not in range(1,6)):
                print("Choice Out Of Range.")
                topic=int(input("Enter Your Respective Choice."))
            if(topic in range(1,6)):
                break
        print("You Chose",topic)
        f=open("word.txt","r")
        for i in range(0,topic):
            a=f.readline()
        word=a.split()
        def words(words):
            used=[]
            k=[]
            fail=0
            word=random.choice(words)
            for g in word:
                k.append("_ ")
            while(True):
                if(fail==0):
                    hangman=hangman0
                elif(fail==1):
                    hangman=hangman1
                elif(fail==2):
                    hangman=hangman2
                elif(fail==3):
                    hangman=hangman3
                elif(fail==4):
                    hangman=hangman4
                elif(fail==5):
                    hangman=hangman5
                elif(fail==6):
                    hangman=hangman6
                i=0
                print(hangman)
                print(k)
                while(True):
                    guess1=str(input("Enter Your Guess"))
                    if(guess1 in used):
                        print("You Have Already Used This Letter")
                    else:
                        break
                guess=guess1.lower() 
                used.append(guess)
                for t in word:
                    if(guess==t):
                       k.pop(i),k.insert(i,guess)
                    i+=1
                if(guess not in word):
                    fail+=1
                if("_ " not in k):
                    print(hangman)
                    print(k)
                    print("You Won!")
                    cur.execute('update user_info set win_no=win_no+1 where user_id like %s;',[user_id])
                    conn.commit()
                    cur.execute('select loss_no from user_info where user_id like %s;',[user_id])
                    g=cur.fetchall()
                    if(g==0):
                        cursor.execute('update user_info set win_loss=100 where user_id like %s;',[user_id])
                    else:
                        cur.execute('update user_info set win_loss=(win_no/loss_no) where user_id like %s;',[user_id])
                    conn.commit()
                    break
                elif(fail==6):
                    print(hangman6)
                    print(k)
                    print("You have Run Out Of Chances,You Lose. \n The Word Was",word)
                    cur.execute('update user_info set loss_no=loss_no+1 where user_id like %s;',[user_id])
                    conn.commit()
                    cur.execute('update user_info set win_loss=(win_no/loss_no) where user_id like %s;',[user_id])
                    conn.commit()
                    break
            word=random.choice(words)    
        words(word)
        break
login()
while(True):
    hangman()
    while(True):
        z=0
        print("DO YOU WANT \n 1.YOUR SCORE \n 2.ALL SCORES \n 3.PLAY AGAIN \n 4.QUIT GAME")
        q=(input("Enter The Number Of The Respective Choice    \n"))
        while(q!="1" and q!="2" and q!="3" and q!="4"):
            q=str(input("Choice Out Of Range,Try Again"))
            if(q in ["1","2","3","4"]):
                break
        if(q=="4"):
            z=1
            break
        elif(q=="1"):
            cur.execute('select user_id,win_no,loss_no,win_loss from user_info where user_id like %s;',[user_id])
            ldetails=cur.fetchall()
            print("USER_ID|WIN_NO|LOSS_NO|WIN-LOSS RATIO")
            print(ldetails)
        elif(q=="2"):
            cur.execute('select user_id,win_no,loss_no,win_loss from user_info;')
            print("USER_ID|WIN_NO|LOSS_NO|WIN-LOSS RATIO")
            alldetails=cur.fetchall()
            for y in alldetails:
                print(y)
        elif(q=="3"):
            break
    if(z==1):
        break
