import MySQLdb

csv_file = "grades.csv"

# Function to insert data into the students table
def insertData(data):
    try:
        db = MySQLdb.connect("cscdata.centre.edu", "pranjal", "DSC270F@ll2023", "pranjal_grades")
        cursor = db.cursor()

        insert_query = "INSERT INTO students (number, student_id, last_name, first_name, quiz_1, quiz_2, quiz_3, quiz_4, quiz_5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cursor.execute(insert_query, data)

        db.commit()

        print("Inserted data into the database.")

    except:
        print("There was an error!")

    cursor.close()
    db.close()


# Read data from the CSV file and insert it into the database
file = open(csv_file, 'r')
lines = file.readlines()
    
for line in lines[1:]:  # Skip the header row
    line = line.strip("\n")
    data = line.split(',')
    
    number = int(data[0])
    student_id = int(data[1])
    last_name = data[2]
    first_name = data[3]
    
    quiz_scores = []
    for i in range(4, 9):
        quiz_scores.append(int(data[i]))
    
    data_to_insert = (number, student_id, last_name, first_name, *quiz_scores)
    insertData(data_to_insert)

file.close()
