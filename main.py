from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "52.2.83.96"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_seguros"  

# Get all claims
@app.get("/claims")
def get_claims():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM siniestros")
    result = cursor.fetchall()
    mydb.close()
    return {"claims": result}

# Get a claim by ID
@app.get("/claims/{id}")
def get_claim(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM siniestros WHERE id = {id}")
    result = cursor.fetchone()
    mydb.close()
    return {"claim": result}

# Add a new claim
@app.post("/claims")
def add_claim(item: schemas.Claim):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    poliza_id = item.poliza_id
    fecha = item.fecha
    descripcion = item.descripcion
    monto = item.monto
    cursor = mydb.cursor()
    sql = "INSERT INTO siniestros (poliza_id, fecha, descripcion, monto) VALUES (%s, %s, %s, %s)"
    val = (poliza_id, fecha, descripcion, monto)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Claim added successfully"}

# Modify a claim
@app.put("/claims/{id}")
def update_claim(id: int, item: schemas.Claim):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    poliza_id = item.poliza_id
    fecha = item.fecha
    descripcion = item.descripcion
    monto = item.monto
    cursor = mydb.cursor()
    sql = "UPDATE siniestros SET poliza_id=%s, fecha=%s, descripcion=%s, monto=%s WHERE id=%s"
    val = (poliza_id, fecha, descripcion, monto, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Claim modified successfully"}

# Delete a claim by ID
@app.delete("/claims/{id}")
def delete_claim(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM siniestros WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"message": "Claim deleted successfully"}
