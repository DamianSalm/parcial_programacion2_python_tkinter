import os
from tkinter import messagebox
from conexion import conexBD

os.system('cls')

class Personal():
  def __init__(self, id=0, nombre="", apellido="", email="", antiguedad="", curso="", modalidad="") -> None:
    self.id=id
    self.nombre=nombre
    self.apellido=apellido
    self.email=email
    self.antiguedad=antiguedad
    self.curso=curso
    self.modalidad=modalidad

  def Read():
    conex=conexBD()
    query='''select * from capacitacion order by id desc'''
    conex.cur.execute(query)
    data = conex.cur.fetchall()
    conex.close()
    return data

  def Agregar(self):
    conex=conexBD()
    query="insert into capacitacion (nombre, apellido, email, antig, curso, modalidad) values ('%s', '%s', '%s', '%s', '%s', '%s')"
    conex.cur.execute(query %(self.nombre, self.apellido, self.email, self.antiguedad, self.curso, self.modalidad))
    conex.con.commit
    messagebox.showinfo("Agregar", "Personal agregado satisfactoriamente")
    conex.close()

  def Update(self):
    conex = conexBD()
    query = '''update capacitacion set nombre='%s', apellido='%s', email='%s', antig='%s', curso='%s', modalidad='%s' where id=%s'''
    conex.cur.execute(query %(self.nombre, self.apellido, self.email, self.antiguedad, self.curso, self.modalidad, self.id))
    conex.close()
    messagebox.showinfo("Editar", "Entrada editada satisfactoriamente")

  def Delete(self):
    conex = conexBD()
    try: 
      query = "delete from capacitacion where id=%s"
      conex.cur.execute(query %self.id)
      conex.close()
      messagebox.showinfo("Eliminar", "Entrada borrada satisfactoriamente")

    except:
      conex.close()
      messagebox.showerror("Eliminar", "Hubo un problema, quizá no seleccionaste ninguna entrada?")