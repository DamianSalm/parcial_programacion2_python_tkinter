#IMPORTAR
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Personal import Personal
from conexion import conexBD
import os

#CREAR DB Y TABLAS
conexBD().crearCapacitacion()

#ROOT DIR
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

#VENTANA 
raiz=Tk()
raiz.resizable(True,True)
raiz.config(bg="lightblue")
raiz.iconbitmap(os.path.join(ROOT_DIR, "python.ico"))
raiz.title("** PARCIAL PROGRAMACIÓN 2 - ALTA CAPACITACIONES - Salmieri, Germán Damián **")

#MARCO
marco=Frame(raiz,bg="pink",width="650",height="350")
marco.pack(fill="none",expand="False")
titulo=Label(marco,text=" ** ALTA CAPACITACIONES **")
titulo.grid(row=0,column=0,columnspan=4,pady=15,padx=15)
titulo.config(bg="pink",width=40,font=("Rockwel",15,"bold"),anchor="center")

#ETIQUETAS - INGRESO DE DATOS

labnom=Label(marco,text="Nombre ")
labnom.grid(row=1, column=0, sticky="w", pady=15, padx=15)

labape=Label(marco,text="Apellido ")
labape.grid(row=1, column=2, sticky="w", pady=15, padx=15)

labmail=Label(marco,text="E-mail ")
labmail.grid(row=2, column=0, sticky="w", pady=15, padx=15)

labtel=Label(marco,text="Antiguedad ")
labtel.grid(row=2, column=2, sticky="w", pady=15, padx=15)

labcur=Label(marco,text="Curso ")
labcur.grid(row=3, column=0, sticky="w", pady=5, padx=15)

labmod=Label(marco,text="Modalidad ")
labmod.grid(row=3, column=2, sticky="w", pady=5, padx=15)

lableyenda=Label(marco,text="Aplicación creada por Germán Damián Salmieri")
lableyenda.grid(row=10, column=0, columnspan=10, sticky="s", pady=15, padx=15)
lableyenda.config(width=40)

#VARIABLES PARA LOS ENTRYS
nomvar, apevar, mailvar, antvar = StringVar(), StringVar(), StringVar(), StringVar()
curvar, modvar = IntVar(), IntVar()

#ENTRYS
txtnom=Entry(marco, textvariable=nomvar, state='disabled')
txtnom.grid(row=1,column=1,sticky="w",pady=15,padx=5)

txtape=Entry(marco, textvariable=apevar, state='disabled')
txtape.grid(row=1,column=3,sticky="w",pady=15,padx=5)

txtmail=Entry(marco, textvariable=mailvar, state='disabled')
txtmail.grid(row=2,column=1,sticky="w",pady=15,padx=5)

txtant=Entry(marco, textvariable=antvar, state='disabled')
txtant.grid(row=2,column=3,sticky="w",pady=15,padx=5)

#BOTONES DE OPCION

capac1=Radiobutton(marco, cursor='target', variable=curvar, value=1, text="Capacitacion & Desarrollo", state='disabled')
capac1.grid(row=3,column=1,sticky="w",padx=5,pady=5)

capac2=Radiobutton(marco, cursor='target', variable=curvar, value=2, text="Comunicacion eficaz", state='disabled')
capac2.grid(row=4,column=1,sticky="w",padx=5,pady=5)

capac3=Radiobutton(marco, cursor='target', variable=curvar, value=3, text="Ev. de Desempeño", state='disabled')
capac3.grid(row=5,column=1,sticky="w",padx=5,pady=5)

moda1=Radiobutton(marco, cursor='target', variable=modvar, value=1, text="Virtual", state='disabled')
moda1.grid(row=3,column=3,sticky="w",padx=5,pady=5)

moda2=Radiobutton(marco, cursor='target', variable=modvar, value=2, text="Presencial", state='disabled')
moda2.grid(row=4,column=3,sticky="w",padx=5,pady=5)

moda3=Radiobutton(marco, cursor='target', variable=modvar, value=3, text="Mixta", state='disabled')
moda3.grid(row=5,column=3,sticky="w",padx=5,pady=5)

#FUNCIONALIDAD A LOS BOTONES

def estadoEntries(estado):
    # funcion para setear el estado de todos los entry fields.
    txtnom.config(state=estado)
    txtape.config(state=estado)
    txtmail.config(state=estado)
    txtant.config(state=estado)
    capac1.config(state=estado)
    capac2.config(state=estado)
    capac3.config(state=estado)
    moda1.config(state=estado)
    moda2.config(state=estado)
    moda3.config(state=estado)

def hab_desh():
    # ¿?
    pass

def nuevo():
    # seteamos una variable global para determinar que queremos crear una entrada en la BD.
    # limpiamos las variables de entrada, y normalizamos botones y entry fields
    global isNew
    isNew = True
    cleanVars()
    estadoEntries("normal")
    botonguardar.config(state="normal")
    botoncancel.config(state="normal")
    botonnuevo.config(state="disabled")
    botoneditar.config(state="disabled")
    botoneliminar.config(state="disabled")

    # foco en txtnom field
    txtnom.focus()

    # predeterminar radiobuttons
    curvar.set(1)
    modvar.set(1)

    # advertir al usuario
    messagebox.showwarning("*ATENCIÓN","Está por ingresar una nueva entrada")

def guardar():
    # leemos la variable de control global para crear o actualizar datos
    global isNew
    # definimos el curso y modalidad de cursado dependiendo del radiobutton seleccionado
    if curvar.get() == 1:
        curso="Capacitacion & Desarrollo"
    elif curvar.get() == 2:
        curso="Comunicacion Eficaz"
    elif curvar.get() == 3:
        curso="Ev. de Desempeño"
    else:
        messagebox.showerror("Error", "Debes seleccionar un curso")
        # modalidad
    if modvar.get() == 1:
        modalidad="Virtual"
    elif modvar.get() == 2:
        modalidad="Presencial"
    elif modvar.get() == 3:
        modalidad="Mixta"
    else:
        messagebox.showerror("Error", "Debes seleccionar una modalidad")

    try: 
        # para crear instanciamos una nueva persona con los valores de los entryfields y las variables de curso y modalidad,
        # luego confirmamos la operación y agregamos la instancia a la BD
        if isNew:
            person = Personal(0, nomvar.get(), apevar.get(), mailvar.get(), antvar.get(), curso, modalidad)
            answer = messagebox.askyesno("Agregar", "Desea agregar esta entrada al registro?")
            if answer == True:
                person.Agregar()
            else:
                messagebox.showinfo("Agregar", "Operación cancelada")
        else:
        # para actualizar instanciamos una nueva persona con los valores de los entryfields, las variables de curso y modalidad,
        # esta vez, la instancia tendrá un id ya existente, y los fields se cambiarán en la funcion editar() para que
        # concuerden con los datos ya guardados.
        # Luego confirmamos la operación y agregamos la instancia a la BD
            person = Personal(lista.item(lista.selection())['text'], nomvar.get(), apevar.get(), mailvar.get(), antvar.get(), curso, modalidad)
            answer = messagebox.askyesno("Editar", "Desea editar esta entrada?")
            if answer == True:
                person.Update()
            else:
                messagebox.showinfo("Editar", "Operación cancelada")

        # limpiamos las variables de entrada, y normalizamos entryfields y botones
        cleanVars()
        estadoEntries("disabled")
        botonguardar.config(state="disabled")
        botoncancel.config(state="disabled")
        botonnuevo.config(state="normal")
        botoneliminar.config(state="normal")
        botoneditar.config(state="normal")

    except:
        # si esto falla, limpiamos variables, y normalizamos fields y botones de todos modos
        cleanVars()
        estadoEntries("disabled")
        botonguardar.config(state="disabled")
        botoncancel.config(state="disabled")
        botonnuevo.config(state="normal")
        botoneliminar.config(state="normal")
        botoneditar.config(state="normal")
        messagebox.showerror("Error", "Hubo un error al guardar la información")

    # al terminar, actualizamos el treeview
    llenar_lista()

def edit():
    # setteamos la variable de control global a false, para que guardar() funcione como update.
    global isNew
    isNew = False
    try:
        # limpiamos las variables de entorno, normalizamos entryfields. Para setear los radiobuttons, seleccionamos el
        # radiobutton que contenga texto igual al texto que tenga la DB, y le damos .select()
        # normalizamos botones e informamos al usuario que se está por editar una persona
        cleanVars()
        estadoEntries("normal")
        nomvar.set(lista.item(lista.selection())['values'][0])
        apevar.set(lista.item(lista.selection())['values'][1])
        mailvar.set(lista.item(lista.selection())['values'][2])
        antvar.set(lista.item(lista.selection())['values'][3])
            # var -> "Capacitacion & Desarrollo", "Comunicacion eficaz", "Ev. de Desempeño"
            # moda -> "Virtual", "Presencial", "Mixta"
        if lista.item(lista.selection())['values'][4] == "Capacitacion & Desarrollo":
            capac1.select()
        elif lista.item(lista.selection())['values'][4] == "Comunicacion Eficaz":
            capac2.select()
        elif lista.item(lista.selection())['values'][4] == "Ev. de Desempeño":
            capac3.select()
        if lista.item(lista.selection())['values'][5] == "Virtual":
            moda1.select()
        elif lista.item(lista.selection())['values'][5] == "Presencial":
            moda2.select()
        elif lista.item(lista.selection())['values'][5] == "Mixta":
            moda3.select()
        # estado normal de los botones
        botonguardar.config(state="normal")
        botonnuevo.config(state="disabled")
        botoneditar.config(state="disabled")
        botoneliminar.config(state="disabled")
        botoncancel.config(state="normal")
        txtnom.focus()
        messagebox.showwarning("Editar","Está por editar los datos de una entrada")
    except:
        # si esto falla, hubo un error
        messagebox.showerror("Editar","Error, no se ha seleccionado ninguna entrada")

def delete():
    # instanciamos la persona a eliminar y pedimos confirmacion para borrar,
    # limpiamos las variables de entrada, normalizamos botones y entries, luego llenamos el treeview.
    person = Personal(lista.item(lista.selection())['text'])
    answer = messagebox.askyesno("Eliminar", "Desea eliminar esta entrada del registro?")
    if answer == True:
        person.Delete()
    else:
        messagebox.showinfo("Delete", "Operación cancelada")
    cleanVars()
    estadoEntries('disabled')
    botonguardar.config(state="disabled")
    botoncancel.config(state="disabled")
    botonnuevo.config(state="normal")
    botoneditar.config(state="normal")
    botoneliminar.config(state="normal")
    llenar_lista()

def cancelar():
    # limpiamos las variables de entrada, normalizamos el estado de los botones y fields, e informamos al usuario que se canceló su operación.
    cleanVars()
    estadoEntries("disabled")
    botonnuevo.config(state="normal")
    botoneditar.config(state="normal")
    botoneliminar.config(state="normal")
    botoncancel.config(state="disabled")
    botonguardar.config(state="disabled")
    messagebox.showinfo("Cancelar", "Se canceló la operación")

def cleanVars():
    # limpiamos las variables de los entries
    nomvar.set("")
    apevar.set("")
    mailvar.set("")
    antvar.set("")
    curvar.set(0)
    modvar.set(0)

def vaciar_lista():
    # vaciamos el treeview
    data=lista.get_children()
    for i in data:
        lista.delete(i)

def llenar_lista():
    try: # habilitamos los botones e intentamos vaciar el treeview, leer los datos de la tabla, e insertarlos en el treeview ya vacio.
        botoneditar.config(state="normal")
        botoneliminar.config(state="normal")
        vaciar_lista()
        datos=Personal.Read()
        for d in datos:
            lista.insert('',0,text=d[0],values=(d[1],d[2],d[3],d[4], d[5], d[6]))
    except:
        #sino, se da un error y quedan los botones bloqueados
        messagebox.showerror("Tabla", "Hubo un error al cargar los datos en la tabla.")

def salir():
    # message box -> desea salir?
    res=messagebox.askquestion("*SALIR*","Confirma que desea salir del programa?")
    if res=="yes":
        # si? destruir raiz
        raiz.destroy()


#BOTONES
botonnuevo=Button(marco, cursor='spraycan', text="NUEVO", command=lambda:nuevo())
botonnuevo.grid(row=8, column=0)

botonguardar=Button(marco, cursor='heart', text="GUARDAR", command=lambda:guardar(), state='disabled')
botonguardar.grid(row=8, column=1)

botoneditar=Button(marco, cursor='exchange', text="EDITAR", command=lambda:edit(), state='disabled')
botoneditar.grid(row=8, column=2)

botoneliminar=Button(marco, cursor='pirate', text="ELIMINAR", command=lambda:delete(), state='disabled')
botoneliminar.grid(row=8, column=3)

botoncancel=Button(marco, cursor='sizing', text="CANCELAR", command=lambda:cancelar(), state='disabled')
botoncancel.grid(row=8, column=4)

botonsalir=Button(marco, cursor='mouse', text="SALIR", command=lambda:salir())
botonsalir.grid(row=8, column=5)

#CREAMOS EL TREEVIEW Y CANTIDAD DE COLUMNAS
lista=ttk.Treeview(marco, columns=('Nom', 'Ape', 'Mail', 'Antig', 'Curso', 'Modal'))
lista.grid(row=7, column=0, columnspan=7, sticky="w", padx=3)
# scroll
scroll=ttk.Scrollbar(marco, orient='vertical', command=lista.yview)
scroll.grid(row=7, column=6, padx=3, sticky='nse')
lista.configure(yscrollcommand=scroll.set)
# headings y columnas
lista.heading('#0',text='ID')
lista.column('#0',width=50)
lista.heading('#1',text='Nombre')
lista.column('#1',width=100)
lista.heading('#2',text='Apellido')
lista.column('#2',width=100)
lista.heading('#3',text='Email')
lista.column('#3',width=100)
lista.heading('#4',text='Antiguedad')
lista.column('#4',width=80)
lista.heading('#5',text='Curso')
lista.column('#5',width=150)
lista.heading('#6',text='Modalidad')
lista.column('#6',width=100)
llenar_lista()


#MAINLOOP
raiz.mainloop()

