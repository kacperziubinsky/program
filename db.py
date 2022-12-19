import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="firma"
)

mycursor = mydb.cursor()

def data():
  i=[]
  mycursor.execute("SELECT * FROM Pracownicy")
  myresult = mycursor.fetchall()
  for x in myresult:
    i.append(x)
  return i

def hour():
  z=[]
  mycursor.execute("SELECT * FROM Godziny")
  myresult=mycursor.fetchall()
  for x in myresult:
    z.append(x)
  return z

def answear(y):
  u=[]
  query="""SELECT Pracownicy.ID, Pracownicy.STAWKA_GODZ, Godziny.Godziny, Godziny.Miesiąc, (Godziny.Godziny*Pracownicy.STAWKA_GODZ) AS 'Stawka' FROM Godziny, Pracownicy WHERE Godziny.ID_PRACOWNIKA=Pracownicy.ID AND (Godziny.Miesiąc=MONTH(CURRENT_DATE) OR Godziny.Miesiąc=MONTH(CURRENT_DATE - INTERVAL 1 MONTH)) AND (Pracownicy.id=%s OR Pracownicy.ID=%s);"""
  tuple=(y,y)
  mycursor.execute(query,tuple)
  myresult=mycursor.fetchall()

  for x in myresult:
    u.append(x)
  return u

def last(y,z):
  u=[]
  query="""SELECT Pracownicy.ID, Godziny.Miesiąc, (Pracownicy.STAWKA_GODZ*Godziny.godziny) FROM Pracownicy, Godziny WHERE Pracownicy.ID=Godziny.ID_PRACOWNIKA AND Pracownicy.ID=%s AND Godziny.Miesiąc=%s"""
  tuple=(y,z)
  mycursor.execute(query,tuple)
  myresult=mycursor.fetchall()

  for x in myresult:
    u.append(x)
  return u

