import os
import numpy as np
import tensorflow as tf
import json
from tkinter import *
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk


# Cargar modelo y clases desde la misma carpeta
base_dir = os.path.dirname(os.path.abspath(__file__))
modelo_path = os.path.join(base_dir, "modelo_crustaceos.h5")
clases_path = os.path.join(base_dir, "clases.npy")

modelo = tf.keras.models.load_model(modelo_path)
clases = np.load(clases_path, allow_pickle=True)
# cargar archivo del glosario
ruta_glosario= os.path.join("../assets","data", "glosario.json")
with open(ruta_glosario,"r",encoding="utf-8") as archivo:
        glosario = json.load(archivo)


#imagenes
lista_imagenes={
    "Marino":"../assets/images/agua_salada.png",
    "Dulceacuicolas":"../assets/images/agua_dulce.png",
    "Tamaño pequeño (2.0cm a 3.0cm)":"../assets/images/cangrejo_pequeno.png",
    "Tamaño mediano (3.1cm a 4.0cm)":"../assets/images/cangrejo_mediano.png",
    "Tamaño grande (mas de 4.0cm)":"../assets/images/cangrejo_grande.png",
    "Caparazon Redondo":"../assets/images/caparazon_redondo.png",
    "Caparazon Ovalado":"../assets/images/caparazon_ovalado.png",
    "Caparazon Alargado":"../assets/images/caparazon_alargado.png",
    "Color Rojo":"../assets/images/cangrejo_rojo.png",
    "Color Verde":"../assets/images/cangrejo_verde.png",
    "Color Marron":"../assets/images/cangrejo_marron.png",
    "Si":"../assets/images/cangrejo_transparente.png",
    "No":"../assets/images/cangrejo_no_transparente.png",
    "Pinzas Grandes":"../assets/images/cangrejo_pinzas_grandes.png",
    "Pinzas Pequeñas":"../assets/images/cangrejo_pinzas_pequenas.png",
    "Patas nadadoras":"../assets/images/patas_caminadoras.png",
    "Patas caminadoras":"../assets/images/patas_nadadoras.png",
    "Antenas Cortas":"../assets/images/antenas_cortas.png",
    "Antenas Largas":"../assets/images/antenas_largas.png",
    "Litoral Rocosas":"../assets/images/playa_rocosa.png",
    "Litoral Arenosa":"../assets/images/playa_arenosa.png",
    "Zona de fuertes energias":"../assets/images/corrientes_fuertes.png",
    "Zona de bajas energias":"../assets/images/corrientes_suaves.png",
    "Con huevos":"../assets/images/con_huevos.png",
    "Sin huevos":"../assets/images/sin_huevos.png",
}
# Preguntas
matriz_pregunta=[
    ["¿En que ambiente habita? ",
        "Marino",
        "Dulceacuicolas"],
    ["¿Cual es su altura? ",
        "Tamaño pequeño (2.0cm a 3.0cm)",
        "Tamaño mediano (3.1cm a 4.0cm)",
        "Tamaño grande (mas de 4.0cm)"],
    ["¿Como es su caparazon? ",
        "Caparazon Redondo",
        "Caparazon Ovalado",
        "Caparazon Alargado"],
    ["¿De que color es?",
        "Color Rojo",
        "Color Verde",
        "Color Marron"],
    ["¿Su cuerpo es transparente? ",
        "Si",
        "No"],
    ["¿Como son sus pinzas?",
        "Pinzas Grandes",
        "Pinzas Pequeñas"],
    ["¿Como son sus patas? ",
        "Patas nadadoras",
        "Patas caminadoras"],
    ["¿De que tamaño son sus antenas? ",
        "Antenas Cortas",
        "Antenas Largas"],
    ["¿En que tipo de habitat se encuentra? ",
        "Litoral Rocosas",
        "Litoral Arenosa"],
    ["¿Como son las corrientes de agua de donde se encuentra?",
        "Zona de fuertes energias",
        "Zona de bajas energias"],
    ["¿Esta ovigera(Con huevos)?",
        "Con huevos",
        "Sin huevos"]
]
#caracteristicas de petrolisthes
lista_cangrejos={
    "Petrolisthes_Tridentatus":{
        "property1":"* Caparazón subcuadrado(ligeramente más largo que ancho) con gránulos bajos y pliegues posterolaterals",
        "property2":"* Región frontal tridentada (lóbulo medio triangular, al menos 2 veces más ancho que los laterales)",
        "property3":"* Artejo basal de la anténula con cresta transversal aserrada en la superficie expuesta",
        "property4":"* Tercer maxilípedo con surco longitudinal submarginal en el isquio",
        "imagen":"../assets/images/tridentatus.png"
    },
    "Petrolisthes_Tonsorius":{
        "property1":"* Caparazón subcuadrado (tan largo como ancho) casi liso, con pliegues cortos en la región posterolateral",
        "property2":"* Región frontal con surco medio profundo que se extiende hasta los lóbulos protogástricos",
        "property3":"* Flagelo de las antenas más largo que el caparazón, con setas escasas proximalmente",
        "property4":"* Carpo de los quelípedos con gránulos diagonales en el margen extensor",
        "imagen":"../assets/images/tonsorius.png"
    },
    "Petrolisthes_Jugosus":{
        "property1":"* Caparazón subcircular (más ancho que largo en hembras, más largo en machos)",
        "property2":"* Telson con 5 placas (vs. 7 en otras especies)",
        "property3":"* Región frontal trilobulada con surco medio profundo",
        "property4":"* Carpo de los quelípedos con margen extensor aserrado (gránulos en forma de espínulas)",
        "imagen":"../assets/images/jugosus.png"
    },
    "Petrolisthes_Puelitus":{
        "property1":"* Caparazón subcircular con gránulos pequeños y surcos transversales",
        "property2":"* Flagelo de las antenas desarmado (sin setas) y más largo que el caparazón",
        "property3":"* Propodio de las patas caminadoras con 4 espinas móviles en el margen flexor (vs. 5 en otras especies)",
        "property4":"* Tercer maxilípedo con surco longitudinal en el isquio y 4 surcos en el carpo",
        "imagen":"../assets/images/puelitus.png"
    },
    "Petrolisthes_Lewesi":{
        "property1":"* Caparazón subcuadrado con superficie irregular y pliegues dorsolaterales",
        "property2":"* Carpo de los quelípedos con 2–4 dientes triangulares en el margen flexor",
        "property3":"* Primer par de patas caminadoras con 5 espinas en el propodio; otros pares con 4",
        "property4":"* Región frontal ligeramente pubescente (setas aisladas)",
        "imagen":"../assets/images/lewisi.png"
    },
    "Petrolisthes_Armatus":{
        "property1":"* Caparazón ligeramente más largo que ancho, con pliegues posterolaterales",
        "property2":"* Espina epibranquial presente (ausente en otras especies)",
        "property3":"* Carpo de los quelípedos con 3 dientes en el margen flexor y gránulos en el extensor",
        "property4":"* Mero de las patas caminadoras con 2–6 espinas en el margen extensor (vs. 0–4 en otras)",
        "imagen":"../assets/images/armatus.png"
    },
    "Petrolisthes_Gallatinus":{
        "property1":"* Caparazón más largo que ancho, con pliegues transversales setosos",
        "property2":"* Región frontal con depresión media en la superficie dorsal",
        "property3":"* Espina supraorbital presente (ausente en otras especies)",
        "property4":"* Mero de los quelípedos con estrías transversales setosas",
        "imagen":"../assets/images/gallatinus.png"
    },
    "Petrolisthes_Marginatus":{
        "property1":"* Caparazón casi liso (sin gránulos pronunciados), con surcos poco profundos",
        "property2":"* Espina exorbital presente (formando un ángulo orbital externo aserrado)",
        "property3":"* Carpo de los quelípedos con tubérculos espiniformes en el margen extensor",
        "property4":"* Tercer maxilípedo con estrías y gránulos en isquio, mero, carpo y propodio",
        "imagen":"../assets/images/marginatus.png"
    },
}

total_preguntas=23
respuesta_vector = []
indice_pregunta = 0 #Llevar el contrl de las preguntas
max_preguntas= 10 #Maximo de preguntas
min_preguntas= 0 #Minimo de pregunta

#ventana principal
ventana = Tk()
ventana.title("Crustaceos Expertos")
ventana.geometry("800x600")
ventana.configure(bg="#dbe4f0")
ventana.resizable(False, False)
#panel donde se va a poner los botones y textos
panel_principal=Frame(ventana,width=200,height=600, bg="white")
panel_principal.pack(fill=BOTH, expand=True)

#Control de los radio button
opcion_elegida=StringVar()
opcion_elegida.set("opcion1")

# ================= FUNCIONES =================

#GabrielRosas
def regresar_menu():
   limpiar_panel_principal()
   global indice_pregunta
   indice_pregunta=0
   mostrar_panel_principal()

#GabrielRosas
def registrar_respuesta():
    global indice_pregunta
    if indice_pregunta==0:# ¿En que ambiente habita?
        if opcion_elegida.get()=="opcion1":
            respuesta_vector[0] = 1
            respuesta_vector[1] = 0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion2":
            respuesta_vector[0] = 0
            respuesta_vector[1] = 1
            print("Se guardo la:", opcion_elegida.get())
        print(f"Indice pregunta: {indice_pregunta} opcion elegida: {opcion_elegida.get()}")
    elif indice_pregunta==1:#  ¿Cual es su altura?
        if opcion_elegida.get()=="opcion1":
            respuesta_vector[2]=1
            respuesta_vector[3]=0
            respuesta_vector[4]=0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion2":
            respuesta_vector[2]=0
            respuesta_vector[3]=1
            respuesta_vector[4]=0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion3":
            respuesta_vector[2]=0
            respuesta_vector[3]=0
            respuesta_vector[4]=1
            print("Se guardo la:", opcion_elegida.get())
    elif indice_pregunta==2:#  ¿Como es su caparazon?
        if opcion_elegida.get()=="opcion1":
            respuesta_vector[5]=1
            respuesta_vector[6]=0
            respuesta_vector[7]=0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion2":
            respuesta_vector[5]=0
            respuesta_vector[6]=1
            respuesta_vector[7]=0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion3":
            respuesta_vector[5]=0
            respuesta_vector[6]=0
            respuesta_vector[7]=1
            print("Se guardo la:", opcion_elegida.get())
    elif indice_pregunta==3:# ¿De que color es?
        if opcion_elegida.get()=="opcion1":
            respuesta_vector[8]=1
            respuesta_vector[9]=0
            respuesta_vector[10]=0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion2":
            respuesta_vector[8]=0
            respuesta_vector[9]=1
            respuesta_vector[10]=0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion3":
            respuesta_vector[8]=0
            respuesta_vector[9]=0
            respuesta_vector[10]=1
            print("Se guardo la:", opcion_elegida.get())
    elif indice_pregunta==4:# ¿Su cuerpo es transparente?
        if opcion_elegida.get()=="opcion1":
            respuesta_vector[11]=1
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion2":
            respuesta_vector[11]=0
            print("Se guardo la:", opcion_elegida.get())
    elif indice_pregunta==5:# ¿Como son sus pinzas?
        if opcion_elegida.get()=="opcion1":
            respuesta_vector[12]=1
            respuesta_vector[13]=0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion2":
            respuesta_vector[12]=0
            respuesta_vector[13]=1
            print("Se guardo la:", opcion_elegida.get())
    elif indice_pregunta==6:# ¿Como son sus patas?
        if opcion_elegida.get()=="opcion1":
            respuesta_vector[14]=1
            respuesta_vector[15]=0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion2":
            respuesta_vector[14]=0
            respuesta_vector[15]=1
            print("Se guardo la:", opcion_elegida.get())
    elif indice_pregunta==7:# ¿De que tamaño son sus antenas?
        if opcion_elegida.get()=="opcion1":
            respuesta_vector[16]=1
            respuesta_vector[17]=0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion2":
            respuesta_vector[16]=0
            respuesta_vector[17]=1
            print("Se guardo la:", opcion_elegida.get())
    elif indice_pregunta==8:# ¿En que tipo de habitat se encuentra?
        if opcion_elegida.get()=="opcion1":
            respuesta_vector[18]=1
            respuesta_vector[19]=0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion2":
            respuesta_vector[18]=0
            respuesta_vector[19]=1
            print("Se guardo la:", opcion_elegida.get())
    elif indice_pregunta==9:# ¿Como son las corrientes de agua de donde se encuentra?
        if opcion_elegida.get()=="opcion1":
            respuesta_vector[20]=1
            respuesta_vector[21]=0
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion2":
            respuesta_vector[20]=0
            respuesta_vector[21]=1
            print("Se guardo la:", opcion_elegida.get())
    elif indice_pregunta==10:# ¿Esta ovigera(Con huevos)?
        if opcion_elegida.get()=="opcion1":
            respuesta_vector[22]=1
            print("Se guardo la:", opcion_elegida.get())
        elif opcion_elegida.get()=="opcion2":
            respuesta_vector[22]=0
            print("Se guardo la:", opcion_elegida.get())
        print(f"Indice pregunta: {indice_pregunta} opcion elegida: {opcion_elegida.get()}")

def inicializar_valores():
    global respuesta_vector
    global indice_pregunta
    global opcion_elegida
    respuesta_vector=[None]*total_preguntas
    indice_pregunta=0
    opcion_elegida.set("opcion0")

#GabrielRosas
def mostrar_resultado():
    limpiar_panel_principal()
    print("Mostrar Resultado")

    def predecir_especie():
        print("Respuesta evaluada: ",len(respuesta_vector))
        entrada = np.array([respuesta_vector])
        prediccion = modelo.predict(entrada)
        especie = clases[np.argmax(prediccion)]
        print(especie)
        nombre_especie.config(text=especie)
        for i in range(1,5):
            propiedad="property"+str(i)
            description=Label(panel_descripcion,text=lista_cangrejos[especie][propiedad], bg="white", font=("Arial",10,"bold"))
            description.pack(padx=0,pady=0, fill=BOTH)
        imagen=PhotoImage(file=lista_cangrejos[especie]["imagen"])
        imagen_reduccion=imagen.subsample(10,10)
        presentar_image=Label(panel_representacion, image=imagen_reduccion)
        presentar_image.pack(padx=0,pady=5)
        presentar_image.image=imagen_reduccion

    panel=Frame(panel_principal,width=800,height=400, bg="#6495ED")
    panel.pack(padx=0,pady=0,fill=BOTH,expand=True)

    titulo=Label(panel, text="Resultados sugerido", bg="#6495ED", font=("Arial",18,"bold"))
    titulo.pack(pady=5)
    boton_salir=Button(panel, text="Volver al menu", command=regresar_menu, bg="#FF6347", font=("Arial",12,"bold"))
    boton_salir.pack(padx=10, pady=10, side=BOTTOM)
    boton_nueva_identificacion=Button(panel, text="Nueva Identificacion", command=mostrar_ascendente, bg="#228B22", font=("Arial",12,"bold"))
    boton_nueva_identificacion.pack(padx=10, pady=10, side=BOTTOM)
    #Panel para mostrar los datos del cangrejo
    panel_resultado=Frame(panel,width=600, height=400, bg="white")
    panel_resultado.pack(padx=50,pady=10,fill=BOTH,expand=True)
    titulo_panel_descripcion=Label(panel_resultado,width=40, text="Informacion", font=("Arial",15,"bold"))
    titulo_panel_descripcion.pack()
    titulo_nombre_especie=Label(panel_resultado,width=40, text="Nombre Especie", font=("Arial",12,"bold"))
    titulo_nombre_especie.pack(pady=5, expand=False)
    nombre_especie=Label(panel_resultado,width=40, text="", bg="white", font=("Arial",15,"bold"))
    nombre_especie.pack(pady=5, expand=False)
    titulo_despcripcion_especie=Label(panel_resultado,width=40, text="Description", font=("Arial",12,"bold"))
    titulo_despcripcion_especie.pack(pady=5, expand=False)
    panel_descripcion=Frame(panel_resultado)
    panel_descripcion.pack()
    titulo_representacion=Label(panel_resultado,width=40, text="Representacion visual", font=("Arial",12,"bold"))
    titulo_representacion.pack(pady=5, expand=False)
    panel_representacion=Frame(panel_resultado)
    panel_representacion.pack()
    predecir_especie()

#JesusMarichal
def salir_programa():
    ventana.destroy()

#JesusMarichal
def mostrar_paginaweb():
    webbrowser.open("https://jesusmarichal.github.io/Landingpage_Crustaceos/")

def mostrar_paginaweb_udone():
    webbrowser.open("https://es.wikipedia.org/wiki/Universidad_de_Oriente_N%C3%BAcleo_de_Nueva_Esparta")

#GabrielRosas
def limpiar_panel_principal():
    for widget in panel_principal.winfo_children():
        widget.destroy()

def mostrar_glosario():
    limpiar_panel_principal()
    panel=Frame(panel_principal,width=800, height=600, bg="#6495ED")
    panel.pack(padx=0, pady=0, fill=BOTH, expand=True)

    titulo=Label(panel, text="Glosario", fon=("Arial",18,"bold"))
    titulo.pack(padx=0, pady=5)

    panel_glosario=Frame(panel, bg="#E6E6FA",width=600,height=400)
    panel_glosario.pack(padx=10, pady=5,fill=BOTH,expand=True)

    text=Text(panel_glosario, wrap=WORD, font=("Arial",12,""))
    text.pack(padx=2,pady=2,fill=BOTH, expand=True)

    for termino, definicion in glosario.items():
        text.insert(END, f"*{termino}: {definicion} \n"+ "-"*150+"\n\n")

    boton_salir=Button(panel, text="Volver al menu", command=regresar_menu, bg="#FF6347", font=("Arial",12,"bold"))
    boton_salir.pack(padx=100, pady=10)

#GabrielRosas
def mostrar_ascendente():
    limpiar_panel_principal()
    print(len(respuesta_vector))
    print("Panel ascendente")
    print("Respuesta listas:",len(respuesta_vector))
    inicializar_valores()
    print("Respuesta listas:",len(respuesta_vector))
    print("posicion del indice_pregunta:",indice_pregunta)
    def pregunta_siguiente():
        global indice_pregunta
        if opcion_elegida.get()!="opcion0":
            registrar_respuesta()
            if indice_pregunta >= min_preguntas and indice_pregunta+1 <= max_preguntas:
                indice_pregunta+=1
                mostrar_pregunta_respuestas()
                preguntas_completas="Pregunta Completadas:",indice_pregunta,"/",max_preguntas
                cantidad_preguntas.config(
                    text=preguntas_completas
                )
                opcion_elegida.set("opcion0")
            else:
                mostrar_resultado()
        else:
            messagebox.showwarning("Advertencia","Por favor selecciona una opcion antes de avanzar")

    def pregunta_anterior():
        global indice_pregunta
        if opcion_elegida.get()!= "opcion0":
            opcion_elegida.set("opcion0")
        if indice_pregunta-1 >= min_preguntas and indice_pregunta-1 <= max_preguntas:
            indice_pregunta-=1
            mostrar_pregunta_respuestas()
            preguntas_completas="Pregunta Completadas:",indice_pregunta,"/",max_preguntas
            cantidad_preguntas.config(
                text=preguntas_completas
            )
            opcion_elegida.set("opcion0")
        else:
            print("No puedo retroceder mas")
            messagebox.showwarning("Advertencia","Se encuentra en la primera pregunta, no puede retroceder mas")

    def limpiar_panel_respuestas():
        for widget in panel_respuestas.winfo_children():
            widget.destroy()

    def mostrar_pregunta_respuestas():
        limpiar_panel_respuestas()
        global indice_pregunta
        indice_fila=0
        if indice_pregunta>=min_preguntas and indice_pregunta<= max_preguntas:
            fila=matriz_pregunta[indice_pregunta]
            for columna in fila:
                if indice_fila==0:
                    print("-"*30)
                    print("Pregunta: ",columna,"# ",indice_pregunta)
                    titulo_preguntas.config(text=columna)
                else:
                    opcion="opcion"+ str(indice_fila)
                    print(indice_fila,": ",columna)
                    imagen_respuestas=PhotoImage(file=lista_imagenes[columna])
                    imagen_reduccion_respuesta=imagen_respuestas.subsample(10,10)#10 se muestra mejor
                    respuesta=Radiobutton(panel_respuestas, width=200, height=300,text=columna, variable=opcion_elegida, value=opcion, image=imagen_reduccion_respuesta, compound="top", relief="solid", borderwidth=1, font=("Arial",10,"bold"))
                    respuesta.pack(padx=10, pady=50, side=LEFT, fill=BOTH, expand=True)
                    respuesta.image=imagen_reduccion_respuesta
                indice_fila+=1
            print("-"*30)

    panel=Frame(panel_principal,width=800,height=600, bg="#6495ED")
    panel.pack(padx=0,pady=0,fill=BOTH,expand=True)

    titulo=Label(panel, text="Identificacion de Especies", font=("Arial",18,"bold"))
    titulo.pack(padx=0, pady=5)
    preguntas_completas="Pregunta Completadas:",indice_pregunta,"/",max_preguntas,
    cantidad_preguntas=Label(panel, text=preguntas_completas, font=("Arial",12,"bold"))
    cantidad_preguntas.pack(padx=0, pady=5)

    panel_preguntas=Frame(panel, bg="#E6E6FA",width=600,height=400)
    panel_preguntas.pack(padx=10, pady=5,fill=BOTH,expand=True)
    titulo_preguntas=Label(panel_preguntas,text="", font=("Arial",12,"bold"))
    titulo_preguntas.pack()

    panel_respuestas=Frame(panel_preguntas, bg="#FFE4C4", width=300,height=300)
    panel_respuestas.pack(side=TOP,fill=BOTH, expand=True)
    mostrar_pregunta_respuestas()

    panel_botones=Frame(panel_preguntas, bg="#FFE4C4", width=600,height=50)
    panel_botones.pack(side=BOTTOM, padx=0, pady=0, fill=X, expand=False)
    boton_anterior=Button(panel_botones, text="Anterior", command=pregunta_anterior, bg="#F0E68C", font=("Arial",12,"bold"))
    boton_anterior.pack(padx=50, pady=2, side=LEFT,fill=BOTH,expand=True)
    boton_siguiente=Button(panel_botones, text="Siguiente", command=pregunta_siguiente, bg="#228B22", font=("Arial",12,"bold"))
    boton_siguiente.pack(padx=50, pady=2, side=RIGHT,fill=BOTH,expand=True)

    boton_salir=Button(panel, text="Volver al menu", command=regresar_menu, bg="#FF6347", font=("Arial",12,"bold"))
    boton_salir.pack(padx=100, pady=10)

#GabrielRosas
def mostrar_descendente():

    def limpiar_panel_mostrar_resultado():
        for widget in panel_mostrar_resultado.winfo_children():
            widget.destroy()

    def mostrar_datos(nombre):
        for i in range(1,5):
            propiedad="property"+str(i)
            print(nombre)
            print(lista_cangrejos[nombre][propiedad])
            resultado=Label(panel_mostrar_resultado,text=lista_cangrejos[nombre][propiedad], bg="white", font=("Arial",10,"bold"))
            resultado.pack(padx=0,pady=0,fill=BOTH, expand=True)
        imagen=PhotoImage(file=lista_cangrejos[nombre]["imagen"])
        imagen_reduccion=imagen.subsample(10,10)
        presentar_image=Label(panel_mostrar_resultado, image=imagen_reduccion)
        presentar_image.pack(padx=0,pady=5)
        presentar_image.image=imagen_reduccion

    def buscar_especie():
        encontrado=""
        limpiar_panel_mostrar_resultado()
        if entrada_busqueda.get()!="":
            print("Buscando...")
            for cangrejo in lista_cangrejos:
                if entrada_busqueda.get().lower() != cangrejo.lower():
                    print("No hay similar")
                else:
                    print("Se encontro algo")
                    encontrado=cangrejo
            if encontrado!="":
                mostrar_datos(encontrado)
            else:
                print("no hubo considencias")
                sin_resultado=Label(panel_mostrar_resultado,text="No hubo considencia, intente a volver a escribir el nombre", bg="#FFA500", font=("Arial",15,"bold"))
                sin_resultado.pack(padx=0,pady=0,fill=NONE, expand=True)
        else:
            messagebox.showwarning("Advertencia","Debe llenar el campo para poder realizar la busqueda")

    print("Panel descendente")
    limpiar_panel_principal()
    panel=Frame(panel_principal,width=800,height=600, bg="#6495ED")
    panel.pack(padx=0, pady=0, fill=BOTH, expand=True)

    titulo=Label(panel, text="Verificar una Especie:", bg="#6495ED",font=("Arial",18,"bold"))
    titulo.pack(padx=5, pady=5)

    panel_verificacion=Frame(panel,bg="white", width=600, height=400)
    panel_verificacion.pack(padx=50,pady=10,fill=BOTH, expand=True)

    panel_busqueda=Frame(panel_verificacion, bg="white",width=600,height=100)
    panel_busqueda.pack(padx=0,pady=10, fill=NONE, expand=False)
    titulo_busqueda=Label(panel_busqueda, text="Seccion para identificar una especie segun su nombre:", font=("Arial",12,"bold"))
    titulo_busqueda.grid(row=0, columnspan=3,padx=2,pady=2)
    nombre_especie=Label(panel_busqueda,text="Nombre: ", width=10, font=("Arial",12,"bold"))
    nombre_especie.grid(row=2 ,column=0, padx=5, pady=5,)
    entrada_busqueda=Entry(panel_busqueda, width=20 , font=("Arial",15,"bold"))
    entrada_busqueda.grid(row=2 ,column=1, padx=5, pady=5)
    boton_buscar=Button(panel_busqueda, text="Buscar", width=10, bg="#6495ED", command=buscar_especie, font=("Arial",12,"bold"))
    boton_buscar.grid(row=2 ,column=2, padx=5, pady=5)

    panel_resultado=Frame(panel_verificacion, bg="white",width=600,height=300)
    panel_resultado.pack(padx=0,pady=0, fill=BOTH, expand=True)
    titulo_resultado=Label(panel_resultado,text="Resultados de la especie identificada:", font=("Arial",12,"bold"))
    titulo_resultado.pack(padx=0, pady=5, fill=NONE,expand=False)
    panel_mostrar_resultado=Frame(panel_resultado, bg="white")
    panel_mostrar_resultado.pack(padx=0,pady=0, fill=BOTH, expand=True)

    boton_salir=Button(panel, text="Volver al menu", command=regresar_menu, bg="#FF6347", font=("Arial",12,"bold"))
    boton_salir.pack(padx=100, pady=10)

#GabrielRosas
def mostrar_panel_principal():
    panel_menu=Frame(panel_principal,width=200,height=600, bg="#B0C4DE")
    panel_menu.pack(side=LEFT,fill=Y, expand=True)

    panel_fondo=Frame(panel_principal,width=600,height=600)
    panel_fondo.pack(side=RIGHT,fill=BOTH, expand=True)
    imagen_fondo=PhotoImage(file="../assets/images/fondo.png")
    imagen_reduccion_fondo=imagen_fondo.subsample(3,3)
    fondo=Label(panel_fondo, bg="pink",image=imagen_reduccion_fondo,width=600,height=600)
    fondo.pack(padx=0,pady=0,fill=BOTH,expand=True)
    fondo.image = imagen_reduccion_fondo
    nombre_programa=Label(fondo, text="Identificacion y Verificacion de Petrolisthes",width=600,font=("Arial",15,"bold"))
    nombre_programa.pack(padx=0,pady=0,side=TOP,fill=NONE,expand=False)
    materia_cursada=Label(fondo, text="Sistemas-Expertos-I2025",width=60,font=("Arial",15,"bold"))
    materia_cursada.pack(padx=0,pady=0,side=BOTTOM,fill=NONE,expand=False)

    imagen_logo=PhotoImage(file="../assets/images/logo_UDO.png")
    imagen_reduccion_logo=imagen_logo.subsample(12,12)
    titulo_panel=Button(panel_menu, image=imagen_reduccion_logo,height=20, bg="#E0FFFF", command=mostrar_paginaweb_udone)
    titulo_panel.pack(padx=0,pady=0,fill=BOTH, expand=True)
    titulo_panel.image=imagen_reduccion_logo

    boton=Button(panel_menu, text="IDENTIFICAR ESPECIE", bg="#4682B4", bd=2, command=mostrar_ascendente, font=("Arial",12,"bold"))
    boton.pack(padx=0,pady=0,fill=BOTH, expand=True)

    boton2=Button(panel_menu, text="VERIFICAR ESPECIE", bg="#4682B4", bd=2,command=mostrar_descendente, font=("Arial",12,"bold"))
    boton2.pack(padx=0,pady=0,fill=BOTH, expand=True)

    boton2=Button(panel_menu, text="GLOSARIO ESPECIE", bg="#4682B4", bd=2,command=mostrar_glosario, font=("Arial",12,"bold"))
    boton2.pack(padx=0,pady=0,fill=BOTH, expand=True)

    boton3=Button(panel_menu, text="PAGINA WEB", bg="#4682B4", bd=2,command=mostrar_paginaweb, font=("Arial",12,"bold"))
    boton3.pack(padx=0,pady=0,fill=BOTH, expand=True)

    boton4=Button(panel_menu, text="CERRAR APLICACAION", bg="#FF6347", bd=2,command=salir_programa, font=("Arial",12,"bold"))
    boton4.pack(padx=0,pady=0,fill=BOTH, expand=True)

# ================ Programa principal ==================

mostrar_panel_principal()

'''
for termino, definicion in glosario.items():
    print(f"**{termino}**: {definicion} \n"+ "-"*50)
'''
ventana.mainloop()
