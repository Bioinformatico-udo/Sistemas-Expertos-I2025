import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import webbrowser
import os

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Experto para Algas Marinas")
        self.geometry("800x600")
        self.state("zoomed") # Configurar para pantalla completa
        self.configure(bg='#f0f8ff')

        self.application_path = os.path.dirname(os.path.abspath(__file__))

        self.icon_path = os.path.join(self.application_path, '../ico.png')
        try:
            icon_image = Image.open(self.icon_path) 
            self.icon_photo = ImageTk.PhotoImage(icon_image)
            self.iconphoto(True, self.icon_photo)
        except FileNotFoundError:
            print(f"Advertencia: El archivo de icono '{self.icon_path}' no se encontró.")
        except Exception as e:
            print(f"Error al cargar el icono de la ventana: {e}")

        # Configurar el estilo
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f8ff')
        self.style.configure('TButton', font=('Arial', 10, 'bold'), background='#4db6ac', foreground='black')
        self.style.map('TButton', background=[('active', '#3da89a')])
        
        # Crear menú principal
        self.create_main_menu()
        
        # Inicializar las secciones
        self.identificar_alga_frame = IdentificarAlgaFrame(self)
        self.verificar_alga_frame = VerificarAlgaFrame(self)
        self.glosario_terminos_frame = GlosarioTerminosFrame(self)
        self.manual_usuario_frame = ManualUsuarioFrame(self)
        self.acerca_de_frame = AcercaDeFrame(self)
        
        # Mostrar el menú principal inicialmente
        self.show_main_menu()
        
    def create_main_menu(self):
        # Frame para el menú principal
        self.main_menu_frame = ttk.Frame(self)
        self.main_menu_frame.pack(fill='both', expand=True, padx=50, pady=50)
        
        # Título
        title_label = tk.Label(self.main_menu_frame, 
                             text="Sistema Experto para Identificación de Algas Marinas",
                             font=('Arial', 18, 'bold'),
                             bg='#00796b', fg='white', pady=20)
        title_label.pack(fill='x', pady=(0, 30))
        
        # Botones del menú
        menu_options = [
            ("Identificar Alga", self.show_identificar_alga),
            ("Verificar Alga", self.show_verificar_alga),
            ("Glosario de Terminos",self.show_glosario_terminos),
            ("Manual de Usuario", self.show_manual_usuario),
            ("Acerca de", self.show_acerca_de)
        ]
        
        for text, command in menu_options:
            btn = ttk.Button(self.main_menu_frame, text=text, command=command, width=25)
            btn.pack(pady=10, ipady=10)
        
        # Pie de página
        footer_label = tk.Label(self.main_menu_frame, 
                              text="© 2025 Sistema Experto de Algas Marinas",
                              font=('Arial', 8),
                              bg='#f0f8ff', fg='#666666')
        footer_label.pack(side='bottom', pady=10)
    
    def show_main_menu(self):
        self.hide_all_frames()
        self.main_menu_frame.pack(fill='both', expand=True, padx=50, pady=50)
    
    def show_identificar_alga(self):
        self.hide_all_frames()
        self.identificar_alga_frame.pack(fill='both', expand=True)
    
    def show_verificar_alga(self):
        self.hide_all_frames()
        self.verificar_alga_frame.pack(fill='both', expand=True)

    def show_glosario_terminos(self):
        self.hide_all_frames()
        self.glosario_terminos_frame.pack(fill='both', expand=True)
    
    def show_manual_usuario(self):
        self.hide_all_frames()
        self.manual_usuario_frame.pack(fill='both', expand=True)
    
    def show_acerca_de(self):
        self.hide_all_frames()
        self.acerca_de_frame.pack(fill='both', expand=True)
        self.acerca_de_frame.after(50, self.acerca_de_frame.trigger_initial_scroll_update)
    
    def hide_all_frames(self):
        for frame in [self.main_menu_frame, self.identificar_alga_frame, 
                     self.verificar_alga_frame, self.glosario_terminos_frame, self.manual_usuario_frame, 
                     self.acerca_de_frame]:
            frame.pack_forget()


class IdentificarAlgaFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(style='TFrame')
        self.parent = parent
        self.current_step = 1
        self.result_shown = False
        self.image_label = None
        self.photo = None
        
        # Crear widgets
        self.create_widgets()
        self.show_question()
    
    def create_widgets(self):
        # Botón para volver al menú
        self.back_button = ttk.Button(self, text="Volver al Menú", 
                                    command=self.parent.show_main_menu)
        self.back_button.pack(anchor='nw', padx=10, pady=10)
        
        # Título
        self.title_label = tk.Label(self, text="Identificación de Algas Marinas", 
                                  font=('Arial', 16, 'bold'), 
                                  bg='#00796b', fg='white', pady=10)
        self.title_label.pack(fill='x')
        
        # Área de pregunta
        self.question_frame = ttk.Frame(self)
        self.question_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.question_label = tk.Label(self.question_frame, text="", 
                                     font=('Arial', 12), bg='#f0f8ff',
                                     wraplength=550, justify='left')
        self.question_label.pack(pady=20)
        
        # Frame para contener la imagen
        self.image_frame = ttk.Frame(self.question_frame)
        self.image_frame.pack(fill='x', pady=10)
        
        # Frame para botones de opciones
        self.button_frame = ttk.Frame(self.question_frame)
        self.button_frame.pack(pady=20)
        
        self.option_a = ttk.Button(self.button_frame, text="", width=75,
                                  command=lambda: self.select_option('a'))
        self.option_a.pack(side='left', padx=10)
        
        self.option_b = ttk.Button(self.button_frame, text="", width=75,
                                  command=lambda: self.select_option('b'))
        self.option_b.pack(side='left', padx=10)
        
        # Botón de reinicio
        self.restart_button = ttk.Button(self, text="Reiniciar Identificación",
                                        command=self.restart)
        self.restart_button.pack(pady=20)
        self.restart_button.pack_forget()
    
    def show_question(self):
        # Resetear estado
        self.result_shown = False
        self.restart_button.pack_forget()
        self.clear_image()
        self.option_a.pack(side='left', padx=10)
        self.option_b.pack(side='left', padx=10)
        
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
        if self.result_shown:
            return
            
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
        
        if not self.result_shown:
            self.show_question()
    
    def clear_image(self):
        """Elimina la imagen actual si existe"""
        if self.image_label:
            self.image_label.destroy()
            self.image_label = None
            self.photo = None
            self.name_label.destroy()
    
    def show_result(self, species):
        self.result_shown = True # Bandera para indicar que un resultado ya ha sido mostrado
        self.question_label.config(text=f"¡Identificación completada!\n\nEspecie identificada: {species}")
        self.option_a.pack_forget() # Ocultar botones de opción
        self.option_b.pack_forget()
        self.restart_button.pack(pady=20, side=tk.BOTTOM) # Mostrar botón de reinicio en la parte inferior
        # Limpiar imagen previa
        self.clear_image()

        self.image_relative_path = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(self.image_relative_path, f"../assets/img/{species.lower().replace(' ', '_')}.png")
        # Intentar mostrar imagen si está disponible
        try:
            # En un entorno real, aquí cargarías la imagen desde un archivo
            image = Image.open(self.icon_path)
            image = image.resize((250, 250), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            
            # Crear etiqueta para la imagen
            self.image_label = tk.Label(self.image_frame, image=self.photo, bg='#e0f7fa')
            self.image_label.pack(pady=10)
            
            # Añadir nombre científico
            self.name_label = tk.Label(self.image_frame, text=species, font=('Arial', 10, 'italic'), bg='#e0f7fa')
            self.name_label.pack()
        except Exception as e:
            print(f"No se pudo cargar la imagen: {e}")
    
    def restart(self):
        # Resetear la aplicación al estado inicial
        self.current_step = 1
        
        # Eliminar atributo de resultado
        if hasattr(self, 'result_shown'):
            delattr(self, 'result_shown')
        
        # Limpiar imagen
        self.clear_image()
        
        # Mostrar primera pregunta
        self.show_question()

class VerificarAlgaFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(style='TFrame')
        self.parent = parent
        
        # Botón para volver al menú
        back_button = ttk.Button(self, text="Volver al Menú", 
                               command=self.parent.show_main_menu)
        back_button.pack(anchor='nw', padx=10, pady=10)
        
        # Título
        title_label = tk.Label(self, text="Verificar Alga", 
                             font=('Arial', 16, 'bold'), 
                             bg='#00796b', fg='white', pady=10)
        title_label.pack(fill='x')
        
        # Contenido
        content_frame = ttk.Frame(self)
        content_frame.pack(fill='both', expand=True, padx=50, pady=30)
        
        description = ("Esta función permite verificar si una muestra de alga pertenece "
                      "a una especie específica. Seleccione las características de su alga "
                      "y el sistema determinará si coincide con alguna especie conocida.\n\n\n\nEn desarrollo...")
        desc_label = tk.Label(content_frame, text=description, 
                            font=('Arial', 11), wraplength=600,
                            justify='left', bg='#f0f8ff')
        desc_label.pack(pady=10)
        
        # Formulario de características
        form_frame = ttk.Frame(content_frame)
        form_frame.pack(pady=20)
        
        """
        characteristics = [
            "Tipo de estructura:",
            "Forma de los frondes erectos:",
            "Disposición de las ramillas:",
            "Presencia de rizomas:",
            "Tamaño de las ramillas:"
        ]
        

        for i, char in enumerate(characteristics):
            lbl = tk.Label(form_frame, text=char, anchor='w', bg='#f0f8ff')
            lbl.grid(row=i, column=0, padx=5, pady=5, sticky='w')
            
            options = ["-- Seleccione --", "Opción 1", "Opción 2", "Opción 3"]
            cb = ttk.Combobox(form_frame, values=options, width=30)
            cb.current(0)
            cb.grid(row=i, column=1, padx=5, pady=5)
        """
        # Botón de verificación
        verify_btn = ttk.Button(content_frame, text="Verificar Alga", 
                              command=self.verify_alga, width=20)
        verify_btn.pack(pady=20)
    
    def verify_alga(self):
        messagebox.showinfo("Verificación", 
                          "La verificación de algas está en desarrollo.\n"
                          "Próximamente podrá verificar sus muestras con nuestro sistema.")

class GlosarioTerminosFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(style='TFrame')
        self.parent = parent
        
        # Botón para volver al menú
        back_button = ttk.Button(self, text="Volver al Menú", 
                               command=self.parent.show_main_menu)
        back_button.pack(anchor='nw', padx=10, pady=10)
        
        # Título
        title_label = tk.Label(self, text="Glosario de Terminos", 
                             font=('Arial', 16, 'bold'), 
                             bg='#00796b', fg='white', pady=10)
        title_label.pack(fill='x')
        
        # Contenido
        content_frame = ttk.Frame(self)
        content_frame.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Texto del manual
        manual_text = """
        Glosario para el uso del Sistema Experto de Algas Marinas\n\n
        
        Términos:\n
           - Rizomas: Tallos subterráneos o rastreros\n
           - Frondes erectos: Partes verticales de la planta\n
           - Ramillas: Pequeñas ramas o divisiones\n
           - Verticiladas: Disposición en espiral o en círculos
        """
        
        manual_label = tk.Label(content_frame, text=manual_text, 
                              font=('Arial', 11), justify='left',
                              bg='#f0f8ff', anchor='w')
        manual_label.pack(fill='both', padx=20, pady=10)

class ManualUsuarioFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(style='TFrame')
        self.parent = parent
        
        # Botón para volver al menú
        back_button = ttk.Button(self, text="Volver al Menú", 
                               command=self.parent.show_main_menu)
        back_button.pack(anchor='nw', padx=10, pady=10)
        
        # Título
        title_label = tk.Label(self, text="Manual de Usuario", 
                             font=('Arial', 16, 'bold'), 
                             bg='#00796b', fg='white', pady=10)
        title_label.pack(fill='x')
        
        # Contenido
        content_frame = ttk.Frame(self)
        content_frame.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Texto del manual
        manual_text = """
        Manual de Uso del Sistema Experto para Algas Marinas
        
        1. Identificar Alga
           Esta función le guiará a través de una serie de preguntas para identificar 
           una especie específica de alga marina. Responda cada pregunta seleccionando 
           la opción que mejor describa su muestra.
           
        2. Verificar Alga
           Si ya tiene una idea de qué especie podría ser su alga, utilice esta función 
           para verificar su hipótesis. Seleccione las características de su muestra y 
           el sistema confirmará o refutará su identificación.
           
        3. Consejos para una identificación precisa:
           - Examine su muestra con cuidado bajo buena iluminación
           - Utilice una lupa si es necesario para ver detalles pequeños
           - Consulte imágenes de referencia cuando esté disponible
           - Si no está seguro de una característica, elija la opción más probable
        
        Para más información, consulte nuestra guía completa en PDF.
        """
        
        manual_label = tk.Label(content_frame, text=manual_text, 
                              font=('Arial', 11), justify='left',
                              bg='#f0f8ff', anchor='w')
        manual_label.pack(fill='both', padx=20, pady=10)
        
        self.relative_pdf_path  = "../docs/Sistema-Experto-para-Algas-Marinas.pdf"
        online_btn = ttk.Button(content_frame, text="Abrir Guía Completa en PDF",
                                command=self.open_pdf)
        online_btn.pack(pady=20)

    def open_pdf(self):
        script_dir = os.path.dirname(__file__)
        pdf_full_path = os.path.join(script_dir, self.relative_pdf_path)

        if os.path.exists(pdf_full_path):
            pdf_url = "file:///" + os.path.normpath(pdf_full_path).replace("\\", "/")
            webbrowser.open_new(pdf_url)
        else:
            messagebox.showerror("Error", 
                                f"El archivo PDF '{self.relative_pdf_path}' no se encontró.\n"
                                f"Asegúrese de que la ruta sea correcta desde la carpeta del script."
                                f"\nRuta buscada: {pdf_full_path}")

class AcercaDeFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(style='TFrame')
        self.parent = parent
        
        # Botón para volver al menú
        back_button = ttk.Button(self, text="Volver al Menú", 
                               command=self.parent.show_main_menu)
        back_button.pack(anchor='nw', padx=10, pady=10)
        
        # Título
        title_label = tk.Label(self, text="Acerca de", 
                             font=('Arial', 16, 'bold'), 
                             bg='#00796b', fg='white', pady=10)
        title_label.pack(fill='x')

        outer_content_frame = ttk.Frame(self, style='TFrame')
        outer_content_frame.pack(fill='both', expand=True, padx=50, pady=30)

        self.canvas = tk.Canvas(outer_content_frame, bg='#f0f8ff', highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(outer_content_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style='TFrame')

        self.canvas_window_id = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas.bind("<Configure>", self._on_frame_configure)
        self.scrollable_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind('<Enter>', self._bind_mouse_wheel)
        self.canvas.bind('<Leave>', self._unbind_mouse_wheel)

        self.relative_logo_path = os.path.dirname(os.path.abspath(__file__))
        self.logo_path = os.path.join(self.relative_logo_path, '../ico.png')

        try:
            original_image = Image.open(self.logo_path)
            desired_size = (150, 150)
            
            original_width, original_height = original_image.size
            ratio = min(desired_size[0] / original_width, desired_size[1] / original_height)
            new_width = int(original_width * ratio)
            new_height = int(original_height * ratio)

            resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(resized_image)

            logo_label = tk.Label(self.scrollable_frame, image=self.logo_photo, bg='#f0f8ff')
            logo_label.pack(pady=10)
            
        except FileNotFoundError:
            print(f"Error: La imagen '{self.logo_path}' no se encontró. Asegúrate de que esté en la ruta correcta.")
            placeholder_canvas = tk.Canvas(self.scrollable_frame, width=150, height=150, bg='white', highlightthickness=0)
            placeholder_canvas.create_text(75, 75, text="LOGO NO ENCONTRADO", font=('Arial', 10), fill='red')
            placeholder_canvas.pack(pady=10)
        except Exception as e:
            print(f"Ocurrió un error al cargar o procesar la imagen: {e}")
            placeholder_canvas = tk.Canvas(self.scrollable_frame, width=150, height=150, bg='white', highlightthickness=0)
            placeholder_canvas.create_text(75, 75, text="ERROR DE IMAGEN", font=('Arial', 10), fill='red')
            placeholder_canvas.pack(pady=10)
        
        # Información de la aplicación
        app_info = """
        Sistema Experto para Identificación de Algas Marinas
        
        Versión: 1.0
        Desarrollado por: Khristian Flores y Duberth Farias
        
        Este sistema utiliza claves dicotómicas basadas en características morfológicas
        para identificar especies específicas de algas marinas. 
        
        © 2025 Universidad de Oriente. Todos los derechos reservados.

        Creditos a:
        """
        
        self.info_label = tk.Label(self.scrollable_frame, text=app_info, 
                                 font=('Arial', 11), justify='center',
                                 bg='#f0f8ff')
        self.info_label.pack(pady=10)
        
        # Créditos
        self.credits_frame = ttk.Frame(self.scrollable_frame, style='TFrame')
        self.credits_frame.pack(pady=10)
        
        credits = [
            "Br. Khristian Flores - Desarrollo de Software",
            "Br. Duberth Farías - Desarrollo de Software",
            "Lic. José Morillo - Director de Proyecto",
            "Lic. Yuraima García - Validación Experta"
        ]
        
        for credit in credits:
            lbl = tk.Label(self.credits_frame, text=credit, font=('Arial', 10), bg='#f0f8ff')
            lbl.pack(pady=2)
        
    def trigger_initial_scroll_update(self):
        self.update_idletasks() 
        self._on_frame_configure() 

    def _on_frame_configure(self, event=None):
        canvas_width = self.canvas.winfo_width()
        if canvas_width > 0:
            self.canvas.itemconfig(self.canvas_window_id, width=canvas_width)
            if self.info_label.winfo_exists():
                self.info_label.config(wraplength=max(100, canvas_width - 40))

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def _on_mouse_wheel(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "unit")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "unit")
        else:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _bind_mouse_wheel(self, event):
        self.canvas.unbind_all("<MouseWheel>") 
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")

        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
        self.canvas.bind_all("<Button-4>", self._on_mouse_wheel)
        self.canvas.bind_all("<Button-5>", self._on_mouse_wheel)

    def _unbind_mouse_wheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()