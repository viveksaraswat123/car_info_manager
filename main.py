import pymysql

# Connect to DB
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='vivek',
    database='car_details',
    cursorclass=pymysql.cursors.DictCursor
)

def add_car(car_number, owner_name, model_year, service_km):
    with conn.cursor() as cursor:
        sql = "INSERT INTO car_info (car_number, owner_name, model_year, service_km) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (car_number, owner_name, model_year, service_km))
        conn.commit()

def view_all_cars():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM car_info")
        return cursor.fetchall()

def delete_car_by_number(car_number):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM car_info WHERE car_number = %s", (car_number,))
        conn.commit()

def update_service_km(car_number, new_km):
    with conn.cursor() as cursor:
        cursor.execute("UPDATE car_info SET service_km = %s WHERE car_number = %s", (new_km, car_number))
        conn.commit()
