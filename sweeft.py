# --------------------------------------------------------------------------------
#1
# --------------------------------------------------------------------------------
def palindrome(text):
	# length = len(text)
	# middle = int((length - 1) / 2)

	# if length % 2 == 1:
	# 	if text[0:middle] == text[middle + 1:][::-1]:
	# 		return 'String is palindrome'

	# 	else:
	# 		return 'String is not palindrome'

	# else:
	# 	return 'String is not palindrome'    This commented way was so stupid even though it worked :Dd


	if text == text[::-1]:
		return True
	else:
		return False




# print(palindrome('level'))

# --------------------------------------------------------------------------------
#2
# --------------------------------------------------------------------------------


# we have 1, 5, 10, 20, 50 coins
def coin_count(x):

	if x < 5:
		return x

	elif x < 10:
		return (x // 5) + x % 5

	elif x < 20:
		return (x // 10) + ((x % 10 ) // 5) + x % 5

	elif x < 50:
		return (x // 20) + ((x % 20) // 10) + ((x % 20) % 10 // 5) + x % 5

	elif x > 50:
		return (x // 50) + ((x % 50) // 20 ) + (((x % 50) % 20) // 10) + ((((x % 50) % 20) % 10) // 5) + (x % 5)

# print(coin_count(152))
# print(coin_count(46))

#---------------------------------------------------------------------------------
#3
# --------------------------------------------------------------------------------

def bracket(x):

	open_bracket = 0
	close_bracket = 0

	list1 = []

	for each in x:
		if each == ')' or each == '(':
			list1.append(each)
		if each == '(':
			open_bracket += 1
		elif each == ')':
			close_bracket += 1


	wrong_allert = 'Somethin is wrong!'	

	if list1[0] == ')':
		return wrong_allert

	elif list1[-1] == '(':
		return wrong_allert

	elif open_bracket != close_bracket:
		return wrong_allert

	else:
		return 'Everything is correct'


# print(bracket('(())'))

# print(bracket(')()'))

#---------------------------------------------------------------------------------
#4
# --------------------------------------------------------------------------------

"""
 ვიპოვე კანონზომიერება, მაგალითად 2 საფეხურზე შეიძლება ახვიდე 2 კომბინაციით 2; 1 1;
 ხოლო 3 საფეხურზე შეიძლება ახვიდე საფეხურების 3 კომბინაციით, 1 1 1; 1 2; 2 1. ყოველი მომდევნო
 კომბინაციათა რაოდენობა წინა ორის ჯამის ტოლია.
"""

def count_step_variates(x):
	list1 = [1, 2, ]
	
	for i in range(x):
		y = list1[-1] + list1[-2]
		list1.append(y)

	return list1[x-1]

# print(count_step_variates(5))


#---------------------------------------------------------------------------------
#5
#---------------------------------------------------------------------------------

import sqlite3


try:
    connection = sqlite3.connect("school.db")
    cursor = connection.cursor()

    #აქ შევქმენი მასწავლებლების ცხრილი, სადაც მათი პირადი ინფორმაციაა
    cursor.execute("""CREATE TABLE IF NOT EXISTS teacher(
                        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR NOT NULL,
                        surname VARCHAR,
                        gender VARCHAR,
                        subject VARCHAR )""")



    #აქ შევქმენი მოსწავლეების ცხრილი სადაც მათი პირადი ინფორმაციაა
    cursor.execute("""CREATE TABLE IF NOT EXISTS pupil(
                        pid INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR NOT NULL,
                        surname VARCHAR,
                        gender VARCHAR,
                        class INTEGER )""")


    #აქ შევქმენი ცხრილი, სადაც ჩამოწერილია მასწავლებლის აიდები და მათი მოსწავლეების აიდები
    cursor.execute("""CREATE TABLE IF NOT EXISTS teaching(
    							teacher_id INTEGER, 
    							pupil_id INTEGER )""")

    #ამ უკანასკნელ ცხრილში ჩაიყრება მასწავლებლების და მოსწავლეების აიდები და ასე დამყარდება ამ ორ ცხრილს შორის კავშირი,


    #რახან გვაინტერესებდა ყველა ის მასწავლებელი რომელიც გიორგის ასწავლიდა ჯერ ვიგებთ გიორგის აიდს
    cursor.execute('SELECT pid FROM pupil WHERE name = "გიორგი"')
    giorgis_id = cursor.fetchone()

    #გიორგის აიდის გაგების შემდეგ ვიგებთ ყველა იმ მასწავლებელთა აიდს რომელიც გიორგის ასწავლის
    cursor.execute('SELECT teacher_id FROM teaching WHERE pupil_id = ?', (giorgis_id, ))
    giorgis_teachers_id = cursor.fetchall()

    for item in giorgis_teachers_id:
        
        teacher_of_giorgi = cursor.execute('SELECT * FROM teacher WHERE teacher_id = ?', (int(item)))

    

    # cursor.execute('INSERT INTO teacher(name, surname, gender, subject) VALUES(?, ?, ?, ?)', ('Malkhaz', 'Dadvani', 'Male', 'PHP'))
    # connection.commit()



# except sqlite3.Error as error:
#     print(error)

finally:
	cursor.close()
	connection.close()





# --------------------------------------------------------------------------------
#6
# --------------------------------------------------------------------------------


"""
მეექვსე დავალება გავაკეთე და ავტვირთე pythonanywheres.com-ზე, კერძოდ: https://sweeft.pythonanywhere.com/
ჩაკნორისის ხუმრობების url: http://sweeft.pythonanywhere.com/random_joke
ხოლო მომხმარებლების მიერ ნანახი ხუმრობების url: http://sweeft.pythonanywhere.com/saved_joks
ბაზისთვის გამოვიყემე MySQL რომელის სტრუქტურაც შეგიძლიათ ნახოთ Console განყოფილებაში MySQL:sweeft$joke_list არჩევით
ამ სავარჯიშოს კოდი შეგიძლიათ თვითონ ჩემს პროფილზე ნახოთ,რომლის მონაცემებიც მითითებული მაქვს ვებსაიტზე, 
იმედი მაქვს ყველა სავარჯიშო სწორი იქნება :დ
"""




		


