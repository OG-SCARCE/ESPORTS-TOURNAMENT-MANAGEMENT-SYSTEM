import mysql.connector as con
#global variables
dbcon=con.connect(host='localhost',user='root', password='SCARCE', database='ESPORTS',auth_plugin='mysql_native_password')
cur=dbcon.cursor()


#This function is used to generate the PLAYER'S ID automatically !
def auto_PLAYERID():
    cmd="select * from PLAYERS"
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        pi=8563498
    else:
        pi=record[len(record)-1][0]
        pi=pi+3456
    return pi

#This function is used to generate TEAM'S ID automatically !
def auto_TEAMID():
    cmd="select * from teams"
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        ti=245672468
    else:
        ti=record[len(record)-1][0]
        ti=ti+84543
    return ti
    
#This function is used to generate GAME'S ID automatically !
def auto_GAMEID():
    cmd="select * from games"
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        gi=283579
    else:
        gi=record[len(record)-1][0]
        gi=gi+9653
    return gi

#This function is used to generate the REGISTRATION ID automatically !
def auto_RGID():
    cmd="select * from REGISTRATION"
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        ri=7895628
    else:
        ri=record[len(record)-1][0]
        ri=ri+3774
    return ri

#This function is used to insert record in the table "TEAMS" !
def insert_record1():
    while True:
        ti=auto_TEAMID()
        print(" TEAM IDENTITY VERIFICATION NUMBER :",ti)
        tt=int(input("➤ENTER THE TEAM TAG :"))
        tnm=input("➤ENTER TEAM NAME :")
        ct=input("➤ENTER YOUR COUNTRY :")
        tc=input("➤ENTER YOUR TEAM CAPTAIN'S NAME :")
        em=input("➤ENTER YOUR OFFICIAL E-MAIL ADDRESS :")
        gm=input("➤ENTER THE NAME OF THE GAME IN WHICH YOU WANT TO PARTICIPATE :")
        cmd1="select * from GAMES where GAME_NAME='{}'".format(gm)
        cur.execute(cmd1)
        record=cur.fetchall()
        if len(record)==0:
            print("!!! INVALID GAME NAME ENTER DETAILS AGAIN !!!")
        else:
            cmd="insert into TEAMS values({},{},'{}','{}','{}','{}','{}')".format(ti,tt,tnm,ct,tc,em,gm)
            cur.execute(cmd)
            dbcon.commit()
            ch=input("ADD MORE RECORDS ?(y/n):")
            if ch in "nN":
                break

#This function is used to show all records of the "TEAMS" table !
def show_records1():
    cmd="select * from TEAMS"
    cur.execute(cmd)
    record=cur.fetchall()
    for rec in record:
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("TEAM'S IDENTITY NUMBER :",rec[0])
        print("TEAM'S TAG :",rec[1])
        print("TEAM'S NAME :",rec[2])
        print("TEAM'S COUNTRY :",rec[3])
        print("TEAM'S CAPTAIN :",rec[4])
        print("TEAM'S E-MAIL ADDRESS :",rec[5])
        print("TEAM'S GAME :",rec[6])
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

#This function is used to search details of a "TEAM" w.r.t the "TEAM_TAG" !
def search_record1():
    tt=int(input("➤ENTER THE TEAM TAG TO SEARCH :"))
    cmd="select * from TEAMS where TEAM_TAG={}".format(tt)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID TEAM_TAG !!! ")
    else:
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("TEAM'S IDENTITY NUMBER :",record[0][0])
        print("TEAM'S TAG :",record[0][1])
        print("TEAM'S NAME :",record[0][2])
        print("TEAM'S COUNTRY :",record[0][3])
        print("TEAM'S CAPTAIN :",record[0][4])
        print("TEAM'S E-MAIL ADDRESS :",record[0][5])
        print("TEAM'S GAME :",record[0][6])
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

#This function is used to delete a record from table "TEAMS" !
def del_record1():
    ti=int(input("➤ENTER TEAM ID TO DELETE TEAM :"))
    cmd="select * from TEAMS where TEAMID={}".format(ti)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID TEAM ID !!!")
    else:
        print("TEAM ID TO BE DELETED")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("TEAM'S IDENTITY NUMBER :",record[0][0])
        print("TEAM'S TAG :",record[0][1])
        print("TEAM'S NAME :",record[0][2])
        print("TEAM'S COUNTRY :",record[0][3])
        print("TEAM'S CAPTAIN :",record[0][4])
        print("TEAM'S E-MAIL ADDRESS :",record[0][5])
        print("TEAM'S GAME :",record[0][6])
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        cmd="delete from TEAMS where TEAMID={}".format(ti)
        cur.execute(cmd)
        dbcon.commit()
        print("TEAM RECORD DELETED SUCCESSFULLY")

#This function is used to update the "TEAM TAG" of given GAME !
def update_TEAM_TAG():
    ti=int(input("➤ENTER THE TEAM ID TO UPDATE THE TEAM TAG :"))
    cmd="select * from TEAMS where TEAMID={}".format(ti)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID TEAM ID !!!")
    else:
        tt=int(input("➤ENTER NEW TEAM TAG :"))
        cmd="update TEAMS set TEAM_TAG={} where TEAMID={}".format(tt,ti)
        cur.execute(cmd)
        dbcon.commit()
        print("TEAM TAG UPDATED SUCCESSFULLY !!!")

#This function is used to update the "TEAM NAME" of given GAME !
def update_TEAM_NAME():
    ti=input("➤ENTER THE TEAM ID TO UPDATE THE TEAM NAME :")
    cmd="select * from TEAMS where TEAMID={}".format(ti)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID TEAM ID !!!")
    else:
        tnm=input("➤ENTER NEW TEAM NAME :")
        cmd="update TEAMS set TEAM_NAME='{}' where TEAMID={}".format(tnm,ti)
        cur.execute(cmd)
        dbcon.commit()
        print("TEAM NAME UPDATED SUCCESSFULLY !!!")

#This function is used to update the "COUNTRY" of given GAME !
def update_COUNTRY():
    ti=input("➤ENTER THE TEAM ID TO UPDATE THE COUNTRY :")
    cmd="select * from TEAMS where TEAMID={}".format(ti)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID TEAM ID !!!")
    else:
        ct=input("➤ENTER NEW COUNTRY :")
        cmd="update TEAMS set COUNTRY='{}' where TEAMID={}".format(ct,ti)
        cur.execute(cmd)
        dbcon.commit()
        print("COUNTRY UPDATED SUCCESSFULLY !!!")

#This function is used to update the "TEAM_CAPTAIN" of given GAME !
def update_TEAM_CAPTAIN():
    ti=input("➤ENTER THE TEAM ID TO UPDATE THE TEAM CAPTAIN :")
    cmd="select * from TEAMS where TEAMID={}".format(ti)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID TEAM ID !!!")
    else:
        tc=input("➤ENTER NEW TEAM CAPTAIN :")
        cmd="update TEAMS set TEAM_CAPTAIN='{}' where TEAMID={}".format(tc,ti)
        cur.execute(cmd)
        dbcon.commit()
        print("TEAM CAPTAIN UPDATED SUCCESSFULLY !!!")

#This function is used to update the "EMAIL" of given GAME !
def update_EMAIL():
    ti=input("➤ENTER THE TEAM ID TO UPDATE THE EMAIL :")
    cmd="select * from TEAMS where TEAMID={}".format(ti)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID TEAM ID !!!")
    else:
        em=input("➤ENTER NEW EMAIL :")
        cmd="update TEAMS set EMAIL='{}' where TEAMID={}".format(em,ti)
        cur.execute(cmd)
        dbcon.commit()
        print("EMAIL UPDATED SUCCESSFULLY !!!")

#This function is used to update the "GAME" of given TEAM DETAILS !
def update_GAME():
    ti=int(input("➤ENTER THE TEAM ID TO UPDATE THE GAME :"))
    cmd="select * from TEAMS where TEAMID={}".format(ti)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID TEAM ID !!!")
    else:
        gm=input("➤ENTER NEW GAME :")
        cmd="update TEAMS set GAME='{}' where TEAMID={}".format(gm,ti)
        cur.execute(cmd)
        dbcon.commit()
        print("GAME UPDATED SUCCESSFULLY !!!")

#This function is used to insert record in the table "GAMES" !
def insert_record2():
    while True:
        gi=auto_GAMEID()
        print(" GAME'S IDENTITY VERIFICATION NUMBER :",gi)
        gnm=input("➤ENTER GAME'S NAME :")
        on=input("➤ENTER GAME'S DEVELOPER :")
        gv=input("➤ENTER GAME'S VERSION :")
        cg=int(input("➤ENTER CHARGES OF THE GAME IN RUPEES : Rs "))
        pz=int(input("➤ENTER PRIZE MONEY IN RUPEES : Rs "))
        cmd="insert into GAMES values({},'{}','{}','{}',{},{})".format(gi,gnm,on,gv,cg,pz)
        cur.execute(cmd)
        dbcon.commit()
        ch=input("ADD MORE RECORDS ?(y/n):")
        if ch in "nN":
            break

#This function is used to show all records of the "GAMES" table !
def show_records2():
    cmd="select * from GAMES"
    cur.execute(cmd)
    record=cur.fetchall()
    for rec in record:
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("GAMES'S IDENTITY NUMBER :",rec[0])
        print("GAMES'S NAME :",rec[1])
        print("GAMES'S DEVELOPER :",rec[2])
        print("GAMES'S VERSION :",rec[3])
        print("GAMES'S CHARGES :",rec[4])
        print("GAMES'S PRIZE AMOUNT :",rec[5])
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

#This function is used to search details of a "GAME" w.r.t the "GAMEID" !
def search_record2():
    gi=int(input("➤ENTER THE GAME ID TO SEARCH :"))
    cmd="select * from GAMES where GAMEID={}".format(gi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID GAME ID !!! ")
    else:
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("GAMES'S IDENTITY NUMBER :",record[0][0])
        print("GAMES'S NAME :",record[0][1])
        print("GAMES'S DEVELOPER :",record[0][2])
        print("GAMES'S VERSION :",record[0][3])
        print("GAMES'S CHARGES :",record[0][4])
        print("GAMES'S PRIZE AMOUNT :",record[0][5])
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

#This function is used to delete a record from table "GAMES" !
def del_record2():
    gi=int(input("➤ENTER GAME ID TO DELETE GAME :"))
    cmd="select * from GAMES where GAMEID={}".format(gi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID GAME ID !!!")
    else:
        print("GAME ID TO BE DELETED")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("GAMES'S IDENTITY NUMBER :",record[0][0])
        print("GAMES'S NAME :",record[0][1])
        print("GAMES'S DEVELOPER :",record[0][2])
        print("GAMES'S VERSION :",record[0][3])
        print("GAMES'S CHARGES :",record[0][4])
        print("GAMES'S PRIZE AMOUNT :",record[0][5])
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        cmd="delete from GAMES where GAMEID={}".format(gi)
        cur.execute(cmd)
        dbcon.commit()
        print("GAME RECORD DELETED SUCCESSFULLY")

#This function is used to update the "GAME NAME" of given GAME !
def update_GAME_NAME():
    gi=int(input("➤ENTER THE GAME ID TO UPDATE THE NAME :"))
    cmd="select * from GAMES where GAMEID={}".format(gi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID GAME ID !!!")
    else:
        gn=input("➤ENTER NEW GAME'S NAME :")
        cmd="update GAMES set GAME_NAME='{}' where GAMEID={}".format(gn,gi)
        cur.execute(cmd)
        dbcon.commit()
        print("GAME'S NAME UPDATED SUCCESSFULLY !!!")

#This function is used to update the "ORIGIN" of given GAME !
def update_DEVELOPER():
    gi=int(input("➤ENTER THE GAME ID TO UPDATE THE DEVELOPER :"))
    cmd="select * from GAMES where GAMEID={}".format(gi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID GAME ID !!!")
    else:
        on=input("➤ENTER NEW GAME DEVELOPER :")
        cmd="update GAMES set GAME_DEVELOPER='{}' where GAMEID={}".format(on,gi)
        cur.execute(cmd)
        dbcon.commit()
        print("DEVELOPER UPDATED SUCCESSFULLY !!!")

#This function is used to update the "VERSION" of given GAME !
def update_VERSION():
    gi=int(input("➤ENTER THE GAME ID TO UPDATE THE VERSION :"))
    cmd="select * from GAMES where GAMEID={}".format(gi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID GAME ID !!!")
    else:
        gv=input("➤ENTER NEW GAME VERSION :")
        cmd="update GAMES set GAME_VERSION='{}' where GAMEID={}".format(gv,gi)
        cur.execute(cmd)
        dbcon.commit()
        print("VERSION UPDATED SUCCESSFULLY !!!")

#This function is used to update the "CHARGES" of given GAME !
def update_CHARGES():
    gi=int(input("➤ENTER THE GAME ID TO UPDATE THE CHARGES :"))
    cmd="select * from GAMES where GAMEID={}".format(gi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID GAME ID !!!")
    else:
        cg=int(input("➤ENTER NEW CHARGES : "))
        cmd="update GAMES set CHARGES={} where GAMEID={}".format(cg,gi)
        cur.execute(cmd)
        dbcon.commit()
        print("CHARGES UPDATED SUCCESSFULLY !!!")

#This function is used to update the "PRIZE AMOUNT" of given GAME !
def update_PRIZE_AMOUNT():
    gi=int(input("➤ENTER THE GAME ID TO UPDATE THE PRIZE AMOUNT :"))
    cmd="select * from GAMES where GAMEID={}".format(gi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID GAME ID !!!")
    else:
        pz=int(input("➤ENTER NEW PRIZE AMOUNT : "))
        cmd="update GAMES set PRIZE_AMOUNT={} where GAMEID={}".format(pz,gi)
        cur.execute(cmd)
        dbcon.commit()
        print("PRIZE AMOUNT UPDATED SUCCESSFULLY !!!")

#This function is used to insert record in the table "PLAYERS" !
def insert_record3():
    while True:
        pi=auto_PLAYERID()
        print(" PLAYERS'S IDENTITY VERIFICATION NUMBER :",pi)
        pn=input("➤ENTER PLAYER'S NAME :")
        pa=int(input("➤ENTER PLAYER'S AGE :"))
        jn=int(input("➤ENTER JERSEY NUMBER :"))
        ti=int(input("➤ENTER TEAM ID :"))
        gm=input("➤ENTER GAME'S NAME YOU ARE PLAYING :")
        cmd1="select * from TEAMS where TEAMID={} and GAME='{}'".format(ti,gm)
        cur.execute(cmd1)
        record=cur.fetchall()
        if len(record)==0:
            print("!!! INVALID TEAM ID OR GAME NAME ENTER DETAILS AGAIN !!!")
            continue
        else:
            cmd="insert into PLAYERS values({},'{}',{},{},{},'{}')".format(pi,pn,pa,jn,ti,gm)
            cur.execute(cmd)
            dbcon.commit()
        ch=input("ADD MORE RECORDS ?(y/n):")
        if ch in "nN":
            break
#This function is used to show all records of the "PLAYERS" table !
def show_records3():
    cmd="select * from PLAYERS"
    cur.execute(cmd)
    record=cur.fetchall()
    for rec in record:
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("PLAYER'S IDENTITY NUMBER :",rec[0])
        print("PLAYER'S NAME :",rec[1])
        print("PLAYER'S AGE :",rec[2])
        print("PLAYER'S JERSEY NUMBER :",rec[3])
        print("PLAYER'S TEAM ID :",rec[4])
        print("PLAYER'S GAME :",rec[5])
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

#This function is used to search details of a "PLAYER" w.r.t the "PLAYER ID" !
def search_record3():
    pi=int(input("➤ENTER PLAYER ID TO SEARCH :"))
    cmd="select * from PLAYERS where PLAYERID={}".format(pi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID PLAYER ID !!! ")
    else:
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("PLAYER'S IDENTITY NUMBER :",record[0][0])
        print("PLAYER'S NAME :",record[0][1])
        print("PLAYER'S AGE :",record[0][2])
        print("PLAYER'S JERSEY NUMBER :",record[0][3])
        print("PLAYER'S TEAM ID :",record[0][4])
        print("PLAYER'S GAME :",record[0][5])
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

#This function is used to delete a record from table "PLAYERS" !
def del_record3():
    pi=int(input("➤ENTER PLAYER ID TO DELETE PLAYER :"))
    cmd="select * from PLAYERS where PLAYERID={}".format(pi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID PLAYER ID !!!")
    else:
        print("PLAYER ID TO BE DELETED")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("PLAYER'S IDENTITY NUMBER :",record[0][0])
        print("PLAYER'S NAME :",record[0][1])
        print("PLAYER'S AGE :",record[0][2])
        print("PLAYER'S JERSEY NUMBER :",record[0][3])
        print("PLAYER'S TEAM ID :",record[0][4])
        print("PLAYER'S GAME :",record[0][5])
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        cmd="delete from PLAYERS where PLAYERID={}".format(pi)
        cur.execute(cmd)
        dbcon.commit()
        print("PLAYER RECORD DELETED SUCCESSFULLY")

#This function is used to update the "NAME" of given PLAYER DETAILS !
def update_PLAYER_NAME():
    pi=input("➤ENTER THE PLAYER ID TO UPDATE THE PLAYER NAME :")
    cmd="select * from PLAYERS where PLAYERID={}".format(pi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID PLAYER ID !!!")
    else:
        pn=input("➤ENTER NEW PLAYER NAME :")
        cmd="update PLAYERS set PLAYER_NAME='{}' where PLAYERID={}".format(pn,pi)
        cur.execute(cmd)
        dbcon.commit()
        print("PLAYER NAME UPDATED SUCCESSFULLY !!!")

#This function is used to update the "PLAYER AGE" of given PLAYER DETAILS !
def update_PLAYER_AGE():
    pi=int(input("➤ENTER THE PLAYER ID TO UPDATE THE PLAYER AGE :"))
    cmd="select * from PLAYERS where PLAYERID={}".format(pi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID PLAYER ID !!!")
    else:
        pa=int(input("➤ENTER NEW PLAYER AGE :"))
        cmd="update PLAYERS set PLAYER_AGE={} where PLAYERID={}".format(pa,pi)
        cur.execute(cmd)
        dbcon.commit()
        print("PLAYER AGE UPDATED SUCCESSFULLY !!!")

#This function is used to update the "JERSEY NUMBER" of given PLAYER DETAILS !
def update_JERSEY_NUMBER():
    pi=int(input("➤ENTER THE PLAYER ID TO UPDATE THE JERSEY NUMBER :"))
    cmd="select * from PLAYERS where PLAYERID={}".format(pi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID PLAYER ID !!!")
    else:
        jn=int(input("➤ENTER NEW JERSEY NUMBER :"))
        cmd="update PLAYERS set JERSEY_NUMBER={} where PLAYERID={}".format(jn,pi)
        cur.execute(cmd)
        dbcon.commit()
        print("JERSEY NUMBER UPDATED SUCCESSFULLY !!!")

#This function is used to update the "TEAMID" of given PLAYER DETAILS !
def update_TEAMID():
    pi=int(input("➤ENTER THE PLAYER ID TO UPDATE THE TEAMID :"))
    cmd="select * from PLAYERS where PLAYERID={}".format(pi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID PLAYER ID !!!")
    else:
        ti=int(input("➤ENTER NEW TEAMID :"))
        cmd="update PLAYERS set TEAMID={} where PLAYERID={}".format(ti,pi)
        cur.execute(cmd)
        dbcon.commit()
        print("TEAMID UPDATED SUCCESSFULLY !!!")

#This function is used to update the "GAME" of given PLAYER DETAILS !
def update_GAME2():
    pi=input("➤ENTER THE PLAYER ID TO UPDATE THE GAME :")
    cmd="select * from PLAYERS where PLAYERID={}".format(pi)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID PLAYER ID !!!")
    else:
        gm=input("➤ENTER NEW GAME :")
        cmd="update PLAYERS set GAME='{}' where PLAYERID={}".format(gm,pi)
        cur.execute(cmd)
        dbcon.commit()
        print("GAME UPDATED SUCCESSFULLY !!!")

#This function is used to update the "REGISTRANT_NAME" of given DETAILS !
def update_REGISTRANT_NAME():
    ri=input("➤ENTER THE REGISTRATION ID TO UPDATE THE PLAYER NAME :")
    cmd="select * from REGISTRATION where REGISTRATION_ID={}".format(ri)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID REGISTRATION ID !!!")
    else:
        rn=input("➤ENTER NEW REGISTRANT NAME :")
        cmd="update REGISTRATION set REGISTRANT_NAME='{}' where REGISTRATION_ID={}".format(rn,ri)
        cur.execute(cmd)
        dbcon.commit()
        print("REGISTRANT NAME UPDATED SUCCESSFULLY !!!")

#This function is used to update the "TEAM_NAME" of given DETAILS !
def update_TEAM_NAME2():
    ri=input("➤ENTER THE REGISTRATION ID TO UPDATE THE TEAM NAME :")
    cmd="select * from REGISTRATION where REGISTRATION_ID={}".format(ri)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID REGISTRATION ID !!!")
    else:
        while True:
            tn=input("➤ENTER NEW TEAM NAME :")
            cmd1="select * from TEAMS where TEAM_NAME='{}'".format(tn)
            cur.execute(cmd1)
            record=cur.fetchall()
            if len(record)==0:
                print("!!! INVALID TEAM NAME ENTER NAME AGAIN !!!")
                continue
            else:
                cmd="update REGISTRATION set TEAM_NAME='{}' where REGISTRATION_ID={}".format(tn,ri)
                cur.execute(cmd)
                dbcon.commit()
                print("TEAM NAME UPDATED SUCCESSFULLY !!!")

#This function is used to update the "REGISTRANT_EMAIL" of given DETAILS !
def update_REGISTRANT_EMAIL():
    ri=input("➤ENTER THE REGISTRATION ID TO UPDATE THE PLAYER NAME :")
    cmd="select * from REGISTRATION where REGISTRATION_ID={}".format(ri)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID REGISTRATION ID !!!")
    else:
        re=input("➤ENTER NEW REGISTRANT EMAIL :")
        cmd="update REGISTRATION set REGISTRANT_EMAIL='{}' where REGISTRATION_ID={}".format(re,ri)
        cur.execute(cmd)
        dbcon.commit()
        print("REGISTRANT EMAIL UPDATED SUCCESSFULLY !!!")

#This function is used to update the "GAME_NAME" of given DETAILS !
def update_GAME_NAME2():
    ri=input("➤ENTER THE REGISTRATION ID TO UPDATE THE PLAYER NAME :")
    cmd="select * from REGISTRATION where REGISTRATION_ID={}".format(ri)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID REGISTRATION ID !!!")
    else:
        while True:
            gn=input("➤ENTER NEW GAME NAME :")
            cmd1="select * from GAMES where GAME_NAME='{}'".format(gn)
            cur.execute(cmd1)
            record=cur.fetchall()
            
            if len(record)==0:
                print("!!! INVALID GAME NAME ENTER DETAILS AGAIN !!!")
                continue
            else:
                cmd2="update REGISTRATION set GAME_NAME='{}' where REGISTRATION_ID={}".format(gn,ri)
                cur.execute(cmd2)
                dbcon.commit()
                print("GAME NAME UPDATED SUCCESSFULLY !!!")

#This function is used to update the "TEAM_CAPTAIN" of given DETAILS !
def update_TEAM_CAPTAIN2():
    ri=input("➤ENTER THE REGISTRATION ID TO UPDATE THE PLAYER NAME :")
    cmd="select * from REGISTRATION where REGISTRATION_ID={}".format(ri)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("!!! INVALID REGISTRATION ID !!!")
    else:
        while True:
            tc=input("➤ENTER NEW TEAM CAPTAIN :")
            cmd1="select * from TEAMS where TEAM_NAME='{}'".format(tn)
            cur.execute(cmd1)
            record=cur.fetchall()
            if len(record)==0:
                print("!!! INVALID TEAM NAME ENTER NAME AGAIN !!!")
                continue
            else:
                cmd="update REGISTRATION set TEAM_CAPTAIN='{}' where REGISTRATION_ID={}".format(tc,ri)
                cur.execute(cmd)
                dbcon.commit()
                print(" TEAM CAPTAIN UPDATED SUCCESSFULLY !!!")
        
# This function is used to prepare the "REGISTRATION BILL" of the "REGISTRANT" !
def make_bill():
    rgid=auto_RGID()
    print("REGISTRATION IDENTITY NUMBER :",rgid)
    rnm=input("➤ENTER REGISTRANT NAME :")
    rem=input("➤ENTER REGISTRANT EMAIL :")
    s=0
    while True:
        gi=int(input("➤ENTER GAME IDENTITY NUMBER :"))
        cmd="select * from GAMES where GAMEID={}".format(gi)
        cur.execute(cmd)
        record1=cur.fetchall()
        tnm=input("➤ENTER YOUR TEAM_NAME :")
        cmd="select * from TEAMS where TEAM_NAME='{}'".format(tnm)
        cur.execute(cmd)
        record2=cur.fetchall()
        if len(record1)==0:
            print("!!! INVALID GAME ID !!!")
        else:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("GAME'S NAME :",record1[0][1])
            print("GAME'S IDENTITY NUMBER :",record1[0][0])
            print("GAME'S GAME DEVELOPER :",record1[0][2])
            print("GAME'S VERSION :",record1[0][3])
            print("GAME'S CHARGES :",record1[0][4])
            print("GAME'S PRIZE AMOUNT :",record1[0][5])
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            gn=record1[0][1]
            gid=record1[0][0]
            gcy=record1[0][2]
            gv=record1[0][3]
            gc=record1[0][4]
            gp=record1[0][5]
        if len(record2)==0:
            print("!!! INVALID TEAM NAME !!!")
        else:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("TEAM'S IDENTITY NUMBER :",record2[0][0])
            print("TEAM'S TAG :",record2[0][1])
            print("TEAM'S NAME :",record2[0][2])
            print("TEAM'S COUNTRY :",record2[0][3])
            print("TEAM'S CAPTAIN :",record2[0][4])
            print("TEAM'S E-MAIL ADDRESS :",record2[0][5])
            print("TEAM'S GAME :",record2[0][6])
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            tin=record2[0][0]
            tt=record2[0][1]
            tnm=record2[0][2]
            cn=record2[0][3]
            tc=record2[0][4]
            te=record2[0][5]
            tg=record2[0][6]
            print("NUMBER OF PLAYERS ALLOWED : 5 (FIVE)")
            amt=gc*5
            print("CHARGES TO BE PAID FOR REGISTRATION :",amt)
            s=s+amt
            cmd="insert into REGISTRATION values({},'{}','{}','{}','{}','{}',{})".format(rgid,rnm,rem,gn,tnm,tc,amt)
            cur.execute(cmd)
            dbcon.commit()
            break
    print("PAYMANT FOR REGISTRATION OF TEAMS : Rs ",s)
    tax=s*15/100
    net=s+tax
    print("G.S.T AND OTHER CHARGES :Rs ",tax)
    print("TOTAL AMOUNT TO PAY : Rs ",net)
    A=int(input("CHOOSE A PAYMENT OPTION : \n1)DEBIT/CREDIT CARD \n2)UPI \n ➤ENTER YOUR CHOICE : "))
    if A==1:
        B=int(input("➤ENTER YOUR CVV NUMBER : "))
        b=str(B)
        while len(b)==0:
            print ("➤ENTER YOUR CVV FIRST TO PROCEED")
            continue
    else:
        C=int(input("➤ENTER YOUR PIN : "))
        c=str(C)
        while len(c)==0:
            print ("➤ENTER YOUR PIN FIRST TO PROCEED")
            continue
    if A==2:
        B=int(input("➤ENTER YOUR ACCOUNT NUMBER : "))
        b=str(B)
        while len(b)==0:
            print ("➤ENTER YOUR ACCOUNT NUMBER FIRST TO PROCEED")
            continue
    else:
        C=int(input("➤ENTER YOUR PASSWORD : "))
        c=str(C)
        while len(c)==0:
            print ("➤ENTER YOUR PASSWORD FIRST TO PROCEED")
            continue

    cmd="insert into RG_DETAILS values({},'{}','{}',{},{},{})".format(rgid,rnm,tnm,s,tax,net)
    cur.execute(cmd)
    dbcon.commit()
    print ("================================================================================================================")
    print ("                        !!! YOUR REGISTRATION WAS COMPLETED SUCCESSFULLY !!!                                                                            ")
    print ("================================================================================================================")

def search_bill():
    rgid=int(input("➤ENTER REGISTRATION ID TO SEARCH : "))
    cmd="select * from REGISTRATION where REGISTRATION_ID={}".format(rgid)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("INVALID REGISTRATION ID")
    else:
        cmd="select * from RG_DETAILS where REGISTRATION_ID={}".format(rgid)
        cur.execute(cmd)
        record1=cur.fetchall()
        print("REGISTRANT NAME :",record1[0][1])
        print("REGISTRANT E-MAIL :",record[0][2])
        print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        for rec in record:
            print("REGISTRANT NAME : ",rec[1],"\tGAME NAME : ",rec[3],"\tTEAM NAME : ",rec[4],"\tTEAM CAPTAIN : ",rec[5],"\tAMOUNT : ",rec[6])
        print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("PAYMANT FOR REGISTRATION OF TEAMS : Rs ",record1[0][3])
        print("G.S.T AND OTHER CHARGES :Rs ",record1[0][4])
        print("TOTAL AMOUNT TO PAY : Rs ",record1[0][5])
    
#----------Main Section-------
if dbcon.is_connected():
    print('''                        ⢐⣤⣼⣿⣿⣿⣿⣿⣿⣷⣶⣦⣀⠀⠀⠀⠀⠀   ⠀⠀    _____ ___________ ___________ _____ _____ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣢⣾⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣦⡀⠀⠀  ⠀ ⠀⠀ |  ___/  ___| ___ |  _  | ___ |_   _/  ___|
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡟⠛⢻⠉⡉⠍⠁⠁⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⡀ ⠀⠀⠀ ⠀⠀ | |__ \ `--.| |_/ | | | | |_/ / | | \ `--. 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢸⠏⢠⢀⡼⡄⠃⠤⠀⠀⠀⠀⠀⡐⠸⣿⣿⣿⣿⣿⣷.⠀⠀⠀⠀⠀  |  __| `--. |  __/| | | |    /  | |  `--. \         
                  ⡜⢰⣸⡎⣀⣷⣤⣶⣶⣶⣦⡀⠀⠈⠓⢿⣿⣿⣿⣿⣿⡆         | |___/\__/ | |   \ \_/ | |\ \  | | /\__/ /
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣇⣤⣯⣿⣿⣿⣿⣿⣿⣿⣭⣯⡆⠀⠀⠘⣿⣿⣿⣿⣿⠇⠀  ⠀⠀   \____/\____/\_|    \___/\_| \_| \_/ \____/
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⣻⣿⣿⣼⠀⢹⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⢘⣿⠙⠡⢽⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣛⣿⣯⠏⠀⢀⣿⣿⣿⣯⣠⡀⠀⠀⠀⢀⣾⡏⠒⢻⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡟⢘⣏⣺⣤⣬⣭⣼⣿⣿⣯⡉⢻⣦⣌⣦⣾⣿⣿⡚⠾⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢹⡼⣿⣿⢼⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡿⣿⢿⡟⢳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣿⣧⡞⣻⣩⣽⡽⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⣇⣬⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⡿⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡛⣿⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡃⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⡟⠻⢿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣍⠓⠲⠤⢤⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠈⣿⡏⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠈⢯⡁⠀⠀⠀⠉⠹⠶⢤⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⢀⠹⣿⡆⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⣤⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⢩⠀⢸⡄⢹⣿⣦⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣤⡄⠀⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠋⡀⣀⣰⣿⠀⠄⠹⣾⣿⣿⡿⣿⠀⢠⣤⣀⣴⣤⣤⡴⠶⠶⠿⠿⠛⠛⠋⠉⠉⣠⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⢀⡱⠏⠉⡟⠃⠀⠀⠀⢸⣿⣿⠇⣿⡴⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠖⢋⣡⣶⣿⣂⡼⠁⠉⠙⠋⠙⠿⠟⣢⣄⢿⡟⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠈⠀⠀
⠀⠀⠀⢀⣠⠴⠚⠉⠉⠀⠀⠀⠀⠀⣸⡿⠟⠀⠀⠀⠀⠀⠀⠲⣾⡛⣿⣬⡄⠀⠀⠁⠠⣤⠆⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⡟⣿⡟⠀⠀⠂⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀
⠞⠁⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⡀⡀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠁⠆⠀⠀⠀''')
    while True:
        print('''\n 
                           ██╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗████████╗░█████╗░██████╗░██╗░░░██╗
                           ██║████╗░██║██║░░░██║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝
                           ██║██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░██║██████╔╝░╚████╔╝░
                           ██║██║╚████║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░██║██╔══██╗░░╚██╔╝░░
                           ██║██║░╚███║░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░
                           ╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
              \n
█████  █████▀███████████████████████████
█▀░██  █─▄▄▄▄██▀▄─██▄─▀█▀─▄█▄─▄▄─█─▄▄▄▄█
██░██  █─██▄─██─▀─███─█▄█─███─▄█▀█▄▄▄▄─█     
▀▄▄▄▀  ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀      
       
              1.1)INSERT GAME RECORD
              1.2)SHOW GAME RECORD
              1.3)SEARCH GAME RECORD
              1.4)DELETE GAME RECORD
              1.5)UPDATE GAME RECORD :
                        1.51)UPDATE GAME NAME
                        1.52)UPDATE GAME ORIGIN
                        1.53)UPDATE GAME VERSION
                        1.54)UPDATE GAME CHARGES
                        1.55)UPDATE GAME PRIZE
                      
              \n

██████  ██████████████████████████████████
█▀▄▄▀█  ██─▄─▄─█▄─▄▄─██▀▄─██▄─▀█▀─▄█─▄▄▄▄█
██▀▄██  ████─████─▄█▀██─▀─███─█▄█─██▄▄▄▄─█
▀▄▄▄▄▀  ▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀

              2.1)INSERT TEAM RECORD
              2.2)SHOW TEAM RECORD
              2.3)SEARCH TEAM RECORD
              2.4)DELETE TEAM RECORD
              2.5)UPDATE TEAM RECORD :
                        2.51)UPDATE TEAM TAG
                        2.52)UPDATE TEAM NAME
                        2.53)UPDATE TEAM COUNTRY
                        2.54)UPDATE TEAM CAPTAIN
                        2.55)UPDATE TEAM EMAIL
                        2.56)UPDATE TEAM GAME
              \n

██████  ████████████████████████████████████████████
█▄▄▄░█  ██▄─▄▄─█▄─▄████▀▄─██▄─█─▄█▄─▄▄─█▄─▄▄▀█─▄▄▄▄█
██▄▄░█  ███─▄▄▄██─██▀██─▀─███▄─▄███─▄█▀██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▀  ▀▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀

              3.1)INSERT PLAYER RECORD
              3.2)SHOW PLAYER RECORD
              3.3)SEARCH PLAYER RECORD
              3.4)DELETE PLAYER RECORD
              3.5)UPDATE PLAYER RECORD :
                        3.51)UPDATE PLAYER NAME
                        3.52)UPDATE PLAYER AGE
                        3.53)UPDATE PLAYER JERSEY NUMBER
                        3.54)UPDATE PLAYER TEAMID
                        3.55)UPDATE PLAYER GAME
              \n

██████  ██████████████████▀████████████████████████████████████████████████████
█░█░██  ██▄─▄▄▀█▄─▄▄─█─▄▄▄▄█▄─▄█─▄▄▄▄█─▄─▄─█▄─▄▄▀██▀▄─██─▄─▄─█▄─▄█─▄▄─█▄─▀█▄─▄█
█▄▄░██  ███─▄─▄██─▄█▀█─██▄─██─██▄▄▄▄─███─████─▄─▄██─▀─████─████─██─██─██─█▄▀─██
▀▀▄▄▄▀  ▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀

              4.1) REGISTER FOR A TOURNAMENT
              4.2) SEARCH RECORD
                        4.21) SEARCH REGISTRATION RECORD
              4.3) UPDATE RECORD
                        4.31) UPDATE REGISTRANT NAME
                        4.32) UPDATE REGISTRANT EMAIL
                        4.33) UPDATE GAME NAME
                        4.34) UPDATE TEAM NAME
                        4.35) UPDATE TEAM CAPTAIN
              \n

██████  ███████████████████████
█░▄▄▄█  █▄─▄▄─█▄─▀─▄█▄─▄█─▄─▄─█
█▄▄▄▒█  ██─▄█▀██▀─▀███─████─███
▀▄▄▄▄▀  ▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▄▄▄▀▀
 
              \n''')
        ch=eval(input("➤ENTER THE OPERATION NUMBER YOU WANT TO PERFORM : "))
        if ch==1.1:
            insert_record2()
        elif ch==1.2:
            show_records2()
        elif ch==1.3:
            search_record2()
        elif ch==1.4:
            del_record2()
        elif ch==1.51:
            update_GAME_NAME()
        elif ch==1.52:
            update_DEVELOPER()
        elif ch==1.53:
            update_VERSION()
        elif ch==1.54:
            update_CHARGES()
        elif ch==1.55:
            update_PRIZE_AMOUNT()
        elif ch==2.1:
            insert_record1()
        elif ch==2.2:
            show_records1()
        elif ch==2.3:
            search_record1()
        elif ch==2.4:
            del_record1()
        elif ch==2.51:
            update_TEAM_TAG()
        elif ch==2.52:
            update_TEAM_NAME()
        elif ch==2.53:
            update_COUNTRY()
        elif ch==2.54:
            update_TEAM_CAPTAIN()
        elif ch==2.55:
            update_EMAIL()
        elif ch==2.56:
            update_GAME()
        elif ch==3.1:
            insert_record3()
        elif ch==3.2:
            show_records3()
        elif ch==3.3:
            search_record3()
        elif ch==3.4:
            del_record3()
        elif ch==3.51:
            update_PLAYER_NAME()
        elif ch==3.52:
            update_PLAYER_AGE()
        elif ch==3.53:
            update_JERSEY_NUMBER()
        elif ch==3.54:
            update_TEAMID()
        elif ch==3.55:
            update_GAME2()
        elif ch==4.1:
            make_bill()
        elif ch==4.21:
            search_bill()
        elif ch==4.31:
            update_REGISTRANT_NAME()
        elif ch==4.32:
            update_REGISTRANT_EMAIL()
        elif ch==4.33:
            update_GAME_NAME2()
        elif ch==4.34:
            update_TEAM_NAME2()
        elif ch==4.35:
            update_TEAM_CAPTAIN2()
            
        x=input(" ▲■▼ WANT TO GO TO MAIN MENU ?(y/n):")
        if x in "nN":
            print ( '''
                                                                  ,----,            
                       ,-.----.       ,----..                   ,/   .`|            
    ,---,.  .--.--.   \    /  \     /   /   \  ,-.----.      ,`   .'  : .--.--.    
  ,'  .' | /  /    '. |   :    \   /   .     : \    /  \   ;    ;     //  /    '.  
,---.'   ||  :  /`. / |   |  .\ : .   /   ;.  \;   :    \.'___,/    ,'|  :  /`. /  
|   |   .';  |  |--`  .   :  |: |.   ;   /  ` ;|   | .\ :|    :     | ;  |  |--`   
:   :  |-,|  :  ;_    |   |   \ :;   |  ; \ ; |.   : |: |;    |.';  ; |  :  ;_     
:   |  ;/| \  \    `. |   : .   /|   :  | ; | '|   |  \ :`----'  |  |  \  \    `.  
|   :   .'  `----.   \;   | |`-' .   |  ' ' ' :|   : .  /    '   :  ;   `----.   \ 
|   |  |-,  __ \  \  ||   | ;    '   ;  \; /  |;   | |  \    |   |  '   __ \  \  | 
'   :  ;/| /  /`--'  /:   ' |     \   \  ',  / |   | ;\  \   '   :  |  /  /`--'  / 
|   |    \'--'.     / :   : :      ;   :    /  :   ' | \.'   ;   |.'  '--'.     /  
|   :   .'  `--'---'  |   | :       \   \ .'   :   : :-'     '---'      `--'---'   
|   | ,'              `---'.|        `---`     |   |.'                             
`----'                  `---`                  `---'                 ''')              
                                                                                   
            break
    
else:
    print("Connection failure")
