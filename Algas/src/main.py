import tkinter as tk
from PIL import Image, ImageTk # Necesario para manejar imágenes

class AlgaIdentifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Identificador de Algas Marinas")
        self.root.geometry("700x600")
        self.root.configure(bg='#e0f7fa')

        # Variables para manejar imágenes
        self.image_label = None
        self.photo = None
        self.font_title = ('Arial', 14, 'bold')
        self.font_question = ('Arial', 12)
        self.font_button = ('Arial', 10, 'bold')

        # --- Frame del Encabezado Superior ---
        self.title_label = tk.Label(root, text="Sistema Experto para Identificación de Algas Marinas", 
                                     font=self.font_title, bg='#00796b', fg='white', pady=10)
        self.title_label.pack(fill='x', side=tk.TOP)

        # --- Etiqueta de la Pregunta ---
        self.question_label = tk.Label(root, text="", font=self.font_question, 
                                        bg='#e0f7fa', wraplength=650, justify='center')
        self.question_label.pack(pady=20, padx=20, fill='x')
        
        # --- Frame para contener la imagen ---
        self.image_frame = tk.Frame(root, bg='#e0f7fa')
        self.image_frame.pack(fill='both', expand=True)

        # --- Frame para contener los botones de opciones ---
        self.button_frame = tk.Frame(root, bg='#e0f7fa')
        self.button_frame.pack(pady=10, fill='x')

        self.option_a = tk.Button(self.button_frame, text="", font=self.font_button, 
                                 command=lambda: self.select_option('a'), bg='#4db6ac', fg='white', relief="raised")
        self.option_a.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X) 
        
        self.option_b = tk.Button(self.button_frame, text="", font=self.font_button, 
                                 command=lambda: self.select_option('b'), bg='#4db6ac', fg='white', relief="raised")
        self.option_b.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        # --- Botón de Reiniciar ---
        self.restart_button = tk.Button(root, text="Reiniciar Identificación", font=self.font_button,
                                         command=self.restart, bg='#ff9800', fg='white', width=25)
        self.restart_button.pack(pady=20, side=tk.BOTTOM)
        self.restart_button.pack_forget() # Ocultar inicialmente
        
        # Iniciar el proceso
        self.current_step = 1
        self.show_question()

    def show_question(self):
        # Ocultar botón de reinicio
        self.restart_button.pack_forget()
        
        # Limpiar imagen si existe
        self.clear_image()
        
        # Mostrar botones de opciones
        self.option_a.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.option_b.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        # Mostrar pregunta según el paso actual
        if self.current_step == 1:
            self.show_step1()
        elif self.current_step == 2:
            self.show_step2()
        elif self.current_step == 3:
            self.show_step3()
        elif self.current_step == 4:
            self.show_step4()
        elif self.current_step == 5:
            self.show_step5()
        elif self.current_step == 6:
            self.show_step6()
        elif self.current_step == 7:
            self.show_step7()
        elif self.current_step == 8:
            self.show_step8()
        elif self.current_step == 9:
            self.show_step9()
        elif self.current_step == 10:
            self.show_step10()

    def show_step1(self):
        self.question_label.config(text="1. ¿Cómo es la estructura de la planta?")
        self.option_a.config(text="a) Con rizomas y frondes erectos claramente diferentes")
        self.option_b.config(text="b) Aspecto filamentoso; rizomas y frondes erectos de forma similar")

    def show_step2(self):
        self.question_label.config(text="2. ¿Cómo son los frondes erectos?")
        self.option_a.config(text="a) Planos y en forma de lámina (más de 4mm ancho x 4cm largo, ápices redondeados)")
        self.option_b.config(text="b) Divididos en distintos tipos de ramillas")

    def show_step3(self):
        self.question_label.config(text="3. ¿Cómo son las ramillas?")
        self.option_a.config(text="a) Divididas de manera regular")
        self.option_b.config(text="b) Lisas, sin espinas, redondeadas o planas")

    def show_step4(self):
        self.question_label.config(text="4. ¿Cómo están dispuestas las frondes?")
        self.option_a.config(text="a) No verticiladas")
        self.option_b.config(text="b) Verticiladas (hasta 3cm alto, ramillas 0.5-2.0mm)")

    def show_step5(self):
        self.question_label.config(text="5. ¿Cómo están dispuestas las ramillas?")
        self.option_a.config(text="a) En 2+ filas o radiales, con lóbulos/dientes")
        self.option_b.config(text="b) En 1-2 filas")

    def show_step6(self):
        self.question_label.config(text="6. ¿Cómo son los rizomas y ramillas?")
        self.option_a.config(text="a) Rizomas lisos sin ramillas filamentosas")
        self.option_b.config(text="b) Rizomas cubiertos con ramillas filamentosas")

    def show_step7(self):
        self.question_label.config(text="7. ¿Tienen las ramillas constricción en la base?")
        self.option_a.config(text="a) Sí (nervio central ovalado y comprimido)")
        self.option_b.config(text="b) No (nervio central plano, láminas planas)")

    def show_step8(self):
        self.question_label.config(text="8. ¿Cómo son las ramillas?")
        self.option_a.config(text="a) Diámetro 0.3-0.5mm, ápices nunca engrosados")
        self.option_b.config(text="b) Diámetro >0.5mm, ápices ocasionalmente engrosados")

    def show_step9(self):
        self.question_label.config(text="9. ¿Cómo son las ramillas?")
        self.option_a.config(text="a) Subsésiles, sobre tallos muy cortos; esféricas a bayiformes")
        self.option_b.config(text="b) Sobre tallos evidentes; con ápices engrosados o planos")

    def show_step10(self):
        self.question_label.config(text="10. ¿Cómo son las ramillas esféricas?")
        self.option_a.config(text="a) Constreñidas en la base con pigmentación uniforme")
        self.option_b.config(text="b) No constreñidas con pigmentación moteada")

    def select_option(self, option):
        # Lógica de identificación basada en las respuestas
        # ... (Tu lógica existente para avanzar en los pasos o mostrar resultados) ...

        if self.current_step == 1:
            if option == 'b':
                self.show_result("Caulerpa fastigiata")
            else:
                self.current_step = 2
                
        elif self.current_step == 2:
            if option == 'a':
                self.show_result("Caulerpa prolifera")
            else:
                self.current_step = 3
                
        elif self.current_step == 3:
            if option == 'b':
                self.current_step = 9
            else:
                self.current_step = 4
                
        elif self.current_step == 4:
            if option == 'b':
                self.show_result("Caulerpa verticillata")
            else:
                self.current_step = 5
                
        elif self.current_step == 5:
            if option == 'b':
                self.current_step = 7
            else:
                self.current_step = 6
                
        elif self.current_step == 6:
            if option == 'a':
                self.show_result("Caulerpa cupressoides")
            else:
                self.current_step = 8
                
        elif self.current_step == 7:
            if option == 'a':
                self.show_result("Caulerpa taxifolia")
            else:
                self.show_result("Caulerpa mexicana")
                
        elif self.current_step == 8:
            if option == 'a':
                self.show_result("Caulerpa sertularioides")
            else:
                self.show_result("Caulerpa ashmeadii")
                
        elif self.current_step == 9:
            if option == 'b':
                self.show_result("Caulerpa chemnitzia")
            else:
                self.current_step = 10
                
        elif self.current_step == 10:
            if option == 'a':
                self.show_result("Caulerpa microphysa")
            else:
                self.show_result("Caulerpa macrophysa")
        
        # Mostrar siguiente pregunta si no se llegó a un resultado
        if not hasattr(self, 'result_shown') or not self.result_shown:
            self.show_question()

    def clear_image(self):
        """Elimina la imagen actual si existe"""
        if self.image_label:
            self.image_label.destroy()
            self.image_label = None
            self.photo = None
        
        if hasattr(self, 'name_label') and self.name_label:
            self.name_label.destroy()
            self.name_label = None

    def show_result(self, species):
        self.result_shown = True # Bandera para indicar que un resultado ya ha sido mostrado
        self.question_label.config(text=f"¡Identificación completada!\n\nEspecie identificada: {species}")
        self.option_a.pack_forget() # Ocultar botones de opción
        self.option_b.pack_forget()
        self.restart_button.pack(pady=20, side=tk.BOTTOM) # Mostrar botón de reinicio en la parte inferior
        # Limpiar imagen previa
        self.clear_image()
        
        # Intentar mostrar imagen si está disponible
        try:
            # Intenta cargar la imagen
            image = Image.open(f"./assets/img/{species.lower().replace(' ', '_')}.png")
            image.thumbnail((300, 300), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            
            self.image_label = tk.Label(self.image_frame, image=self.photo, bg='#e0f7fa')
            self.image_label.pack(pady=10)
            
            # Añadir nombre científico debajo de la imagen
            self.name_label = tk.Label(self.image_frame, text=species, font=('Arial', 10, 'italic'), bg='#e0f7fa')
            self.name_label.pack()
        except Exception as e:
            # Si no se encuentra la imagen, no mostrar nada
            print(f"No se pudo cargar la imagen para {species}: {e}")

    def restart(self):
        # Resetear la aplicación al estado inicial
        self.current_step = 1
        
        # Eliminar atributo de resultado para que show_question() funcione
        if hasattr(self, 'result_shown'):
            delattr(self, 'result_shown')
        
        # Limpiar imagen
        self.clear_image()
        
        # Mostrar primera pregunta
        self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlgaIdentifierApp(root)
    root.mainloop()