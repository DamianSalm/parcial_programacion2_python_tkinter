#IMPORTAR
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Personal import Personal
from conexion import conexBD

#CREAR DB Y TABLAS
conexBD().crearCapacitacion()

#VENTANA 
raiz=Tk()
raiz.resizable(True,True)
raiz.config(bg="lightblue")
raiz.title("** PARCIAL PROGRAMACIÓN 2 - ALTA CAPACITACIONES - Salmieri, Germán Damián **")

#MARCO
marco=Frame(raiz,bg="pink",width="650",height="350")
marco.pack(fill="none",expand="False")
titulo=Label(marco,text=" ** ALTA CAPACITACIONES **")
titulo.grid(row=0,column=0,columnspan=4,pady=15,padx=15)
titulo.config(bg="pink",width=40,font=("Rockwel",15,"bold"),anchor="center")

#ETIQUETAS - INGRESO DE DATOS

labnom=Label(marco,text="Nombre ")
labnom.grid(row=1,column=0,sticky="w",pady=15,padx=15)

labape=Label(marco,text="Apellido ")
labape.grid(row=1,column=2,sticky="w",pady=15,padx=15)

labmail=Label(marco,text="E-mail ")
labmail.grid(row=2,column=0,sticky="w",pady=15,padx=15)

labtel=Label(marco,text="Antiguedad ")
labtel.grid(row=2,column=2,sticky="w",pady=15,padx=15)

labcur=Label(marco,text="Curso ")
labcur.grid(row=3,column=0,sticky="w",pady=5,padx=15)

labmod=Label(marco,text="Modalidad ")
labmod.grid(row=3,column=2,sticky="w",pady=5,padx=15)

lableyenda=Label(marco,text="Aplicación creada por Germán Damián Salmieri")
lableyenda.grid(row=10,column=0,columnspan=4,sticky=" ",pady=15,padx=15)
lableyenda.config(width=40)


#VARIABLES PARA LOS ENTRYS
nomvar, apevar, mailvar, antvar = StringVar(), StringVar(), StringVar(), StringVar()
curvar, modvar = IntVar(), IntVar()



#ENTRYS
txtnom=Entry(marco, textvariable=nomvar)
txtnom.grid(row=1,column=1,sticky="w",pady=15,padx=5)

txtape=Entry(marco, textvariable=apevar)
txtape.grid(row=1,column=3,sticky="w",pady=15,padx=5)

txtmail=Entry(marco, textvariable=mailvar)
txtmail.grid(row=2,column=1,sticky="w",pady=15,padx=5)

txtant=Entry(marco, textvariable=antvar)
txtant.grid(row=2,column=3,sticky="w",pady=15,padx=5)

#BOTONES DE OPCION

capac1=Radiobutton(marco, variable=curvar, value=1, text="Capacitación & Desarrollo")
capac1.grid(row=3,column=1,sticky="w",padx=5,pady=5)

capac2=Radiobutton(marco, variable=curvar, value=2, text="Comunicación eficaz")
capac2.grid(row=4,column=1,sticky="w",padx=5,pady=5)

capac3=Radiobutton(marco, variable=curvar, value=3, text="Ev. de Desempeño")
capac3.grid(row=5,column=1,sticky="w",padx=5,pady=5)

moda1=Radiobutton(marco, variable=modvar, value=1, text="Virtual")
moda1.grid(row=3,column=3,sticky="w",padx=5,pady=5)

moda2=Radiobutton(marco, variable=modvar, value=2, text="Presencial")
moda2.grid(row=4,column=3,sticky="w",padx=5,pady=5)

moda3=Radiobutton(marco, variable=modvar, value=3, text="Mixta")
moda3.grid(row=5,column=3,sticky="w",padx=5,pady=5)


#FUNCIONALIDAD A LOS BOTONES

def estadotextos(estado):
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
    pass

def nuevo():    
    global isNew
    isNew = True
    cleanEntries() #limpiar la lista
    estadotextos("normal") #deshabilitar botones
    botonguardar.config(state="normal")
    botonnuevo.config(state="disabled")
    botoneditar.config(state="disabled")
    botoneliminar.config(state="disabled")
    botoncancel.config(state="normal")

    #Pongo el foco en txtnom
    txtnom.focus()

    messagebox.showwarning("*ATENCIÓN","Está por ingresar una nueva entrada")

def guardar():
    global isNew
    if curvar.get() == 1:
        curso="Capacitacion & Desarrollo"
    elif curvar.get() == 2:
        curso="Comunicación Eficaz"
    elif curvar.get() == 3:
        curso="Ev. de Desempeño"
    else:
        messagebox.showerror("Error", "Debes seleccionar un curso")
    if modvar.get() == 1:
        modalidad="Virtual"
    elif modvar.get() == 2:
        modalidad="Presencial"
    elif modvar.get() == 3:
        modalidad="Mixta"
    else:
        messagebox.showerror("Error", "Debes seleccionar una modalidad")

    try: 
        if isNew:
            person = Personal(0, nomvar.get(), apevar.get(), mailvar.get(), antvar.get(), curso, modalidad)
            answer = messagebox.askyesno("Eliminar", "Desea eliminar esta entrada del registro?")
            if answer == True:
                person.Agregar()
            else:
                messagebox.showinfo("Agregar", "Operación cancelada")
        else:
            person = Personal(lista.item(lista.selection())['text'], nomvar.get(), apevar.get(), mailvar.get(), antvar.get(), curso, modalidad)
            answer = messagebox.askyesno("Eliminar", "Desea eliminar esta entrada del registro?")
            if answer == True:
                person.Update()
            else:
                messagebox.showinfo("Editar", "Operación cancelada")

        cleanEntries()
        estadotextos("disabled")
        botonguardar.config(state="disabled")
        botoncancel.config(state="disabled")
        botonnuevo.config(state="normal")
        botoneliminar.config(state="normal")
        botoneditar.config(state="normal")
    except: 
        messagebox.showerror("Error", "Hubo un error al guardar la información")

    llenar_lista()

def edit():    
    global isNew
    isNew = False
    try:
        cleanEntries() #limpiar la lista
        estadotextos("normal") #deshabilitar botones
        nomvar.set(lista.item(lista.selection())['values'][0])
        apevar.set(lista.item(lista.selection())['values'][1])
        mailvar.set(lista.item(lista.selection())['values'][2])
        antvar.set(lista.item(lista.selection())['values'][3])
            # var -> "Capacitación & Desarrollo" "Comunicación eficaz" "Ev. de Desempeño"
            # moda ->"Virtual" "Presencial" "Mixta"
        if lista.item(lista.selection())['values'][4] == "Capacitación & Desarrollo":
            capac1.select()
        elif lista.item(lista.selection())['values'][4] == "Comunicación eficaz":
            capac2.select()
        elif lista.item(lista.selection())['values'][4] == "Ev. de Desempeño":
            capac3.select()
        if lista.item(lista.selection())['values'][5] == "Virtual":
            moda1.select()
        elif lista.item(lista.selection())['values'][5] == "Presencial":
            moda2.select()
        elif lista.item(lista.selection())['values'][5] == "Mixta":
            moda3.select()
            
        botonguardar.config(state="normal")
        botonnuevo.config(state="disabled")
        botoneditar.config(state="disabled")
        botoneliminar.config(state="disabled")
        botoncancel.config(state="normal")
        txtnom.focus()
        messagebox.showwarning("Editar","Está por editar los datos de una entrada")
    except:
        messagebox.showwarning("Editar","Error, no se ha seleccionado ninguna entrada")

def delete():
    person = Personal(lista.item(lista.selection())['text'])
    answer = messagebox.askyesno("Eliminar", "Desea eliminar esta entrada del registro?")
    if answer == True:
        person.Delete()
    else:
        messagebox.showinfo("Delete", "Operación cancelada")
    cleanEntries()
    estadotextos('disabled')
    botonguardar.config(state="disabled")
    botoncancel.config(state="disabled")
    botonnuevo.config(state="normal")
    botoneditar.config(state="normal")
    botoneliminar.config(state="normal")
    llenar_lista()

def cancelar():
    cleanEntries() #limpio los entries
    estadotextos("disabled") #deshabilito los entries
    botonnuevo.config(state="normal") #reorganizo botones #nuevo si
    botoneditar.config(state="normal") #editar si
    botoneliminar.config(state="normal") #eliminar si
    botoncancel.config(state="disabled") #cancel no
    botonguardar.config(state="disabled") #guardar no
    messagebox.showinfo("Cancelar", "Se canceló la operación")

def cleanEntries():
    nomvar.set("")
    apevar.set("")
    mailvar.set("")
    antvar.set("")
    curvar.set(0)
    modvar.set(0)

def vaciar_lista():
    botoneditar.config(state="normal")
    botoneliminar.config(state="normal")
    data=lista.get_children()
    for i in data:
        lista.delete(i)

def llenar_lista():
    botoneditar.config(state="normal")
    botoneliminar.config(state="normal")
    vaciar_lista()
    datos=Personal.Read()
    for d in datos:
        lista.insert('',0,text=d[0],values=(d[1],d[2],d[3],d[4], d[5], d[6]))

def salir():
    res=messagebox.askquestion("*SALIR*","Confirma que desea salir del programa?")
    if res=="yes":
        raiz.destroy()


#BOTONES
botonnuevo=Button(marco,text="NUEVO",command=lambda:nuevo())
botonnuevo.grid(row=8,column=0)

botonguardar=Button(marco,text="GUARDAR",command=lambda:guardar())
botonguardar.grid(row=8,column=1)

botoneditar=Button(marco,text="EDITAR",command=lambda:edit())
botoneditar.grid(row=8,column=2)

botoneliminar=Button(marco,text="ELIMINAR",command=lambda:delete())
botoneliminar.grid(row=8,column=3)

botoncancel=Button(marco,text="CANCELAR",command=lambda:cancelar())
botoncancel.grid(row=8,column=4)

botonsalir=Button(marco, text="SALIR", command=lambda:salir())
botonsalir.grid(row=8, column=5)


#CREAMOS EL TREEVIEW Y CANTIDAD DE COLUMNAS
lista=ttk.Treeview(marco, columns=('Nom', 'Ape', 'Mail', 'Antig', 'Curso', 'Modal'))
lista.grid(row=7, column=0, columnspan=6, sticky="w")
scroll=ttk.Scrollbar(marco, orient='vertical', command=lista.yview)
scroll.grid(row=7, column=6, sticky='nse')
lista.configure(yscrollcommand=scroll.set)

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
lista.column('#5',width=100)
lista.heading('#6',text='Modalidad')
lista.column('#6',width=100)
llenar_lista()



raiz.mainloop()

