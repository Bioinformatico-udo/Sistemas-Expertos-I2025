import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import webbrowser
import os

class AlgaExpertSystem:
    """Clase que encapsula la lógica del sistema experto para identificación de algas"""
    def __init__(self):
        self.current_step = 1
        self.answers = []
        self.verification_species = None
    
    def reset(self):
        """Reinicia el sistema a su estado inicial"""
        self.current_step = 1
        self.answers = []
        self.verification_species = None
    
    def get_question(self):
        """Devuelve la pregunta actual y opciones"""
        if self.current_step == 1:
            return ("1. ¿Cómo es la estructura de la planta?", 
                    "a) Con rizoides y frondes erectos claramente diferentes",
                    "b) Con rizoides y frondes erectos de forma similar")
        
        elif self.current_step == 2:
            return ("2. ¿Cómo son los frondes erectos?", 
                    "a) Planos y en forma de lámina",
                    "b) Divididos en distintos tipos de ramillas")
        
        elif self.current_step == 3:
            return ("3. ¿Cómo son las ramillas?", 
                    "a) Divididas de manera regular",
                    "b) Lisas, sin espinas, redondeadas o planas")
        
        elif self.current_step == 4:
            return ("4. ¿Cómo están dispuestas las frondes?", 
                    "a) No verticiladas",
                    "b) Verticiladas")
        
        elif self.current_step == 5:
            return ("5. ¿Cómo están dispuestas las ramillas?", 
                    "a) En 2+ filas o radiales",
                    "b) En 1-2 filas")
        
        elif self.current_step == 6:
            return ("6. ¿Cómo son los rizoides y ramillas?", 
                    "a) Rizoides lisos sin ramillas filamentosas",
                    "b) Rizoides cubiertos con ramillas filamentosas")
        
        elif self.current_step == 7:
            return ("7. ¿Tienen las ramillas constricción en la base?", 
                    "a) Sí (nervio central ovalado y comprimido)",
                    "b) No (nervio central plano, láminas planas)")
        
        elif self.current_step == 8:
            return ("8. ¿Cómo son las ramillas?", 
                    "a) Diámetro 0.3-0.5mm, ápices nunca engrosados",
                    "b) Diámetro >0.5mm, ápices ocasionalmente engrosados")
        
        elif self.current_step == 9:
            return ("9. ¿Cómo son las ramillas?", 
                    "a) Sobre Estolones muy cortos; esféricas a bayiformes",
                    "b) Sobre Estolones evidentes; con ápices engrosados o planos")
        
        elif self.current_step == 10:
            return ("10. ¿Cómo son las ramillas esféricas?", 
                    "a) Constreñidas en la base con pigmentación uniforme",
                    "b) No constreñidas con pigmentación moteada")
        
        return ("Identificación completada", "", "")
    
    def answer_question(self, answer):
        """Procesa una respuesta y avanza en el sistema"""
        if self.current_step <= 10:
            self.answers.append((self.current_step, answer))
            
            if self.current_step == 1:
                if answer == 'b':
                    return "Caulerpa fastigiata"
                self.current_step = 2
                
            elif self.current_step == 2:
                if answer == 'a':
                    return "Caulerpa prolifera"
                self.current_step = 3
                
            elif self.current_step == 3:
                if answer == 'b':
                    self.current_step = 9
                else:
                    self.current_step = 4
                    
            elif self.current_step == 4:
                if answer == 'b':
                    return "Caulerpa verticillata"
                self.current_step = 5
                
            elif self.current_step == 5:
                if answer == 'b':
                    self.current_step = 7
                else:
                    self.current_step = 6
                    
            elif self.current_step == 6:
                if answer == 'a':
                    return "Caulerpa cupressoides"
                self.current_step = 8
                
            elif self.current_step == 7:
                if answer == 'a':
                    return "Caulerpa taxifolia"
                return "Caulerpa mexicana"
                
            elif self.current_step == 8:
                if answer == 'a':
                    return "Caulerpa sertularioides"
                return "Caulerpa ashmeadii"
                
            elif self.current_step == 9:
                if answer == 'b':
                    return "Caulerpa chemnitzia"
                self.current_step = 10
                
            elif self.current_step == 10:
                if answer == 'a':
                    return "Caulerpa microphysa"
                return "Caulerpa macrophysa"
        
        return None


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Experto para Algas Marinas")
        self.state('zoomed')
        self.configure(bg='#f0f8ff')

        # Inicializar el sistema experto
        self.expert_system = AlgaExpertSystem()

        self.application_path = os.path.dirname(os.path.abspath(__file__))

        self.icon_path = os.path.join(self.application_path, '../assets/icon/ico.png')
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
        self.expert_system.reset()
        self.identificar_alga_frame.pack(fill='both', expand=True)
        self.identificar_alga_frame.show_question()
    
    def show_verificar_alga(self):
        self.hide_all_frames()
        self.expert_system.reset()
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
        
        # Crear widgets
        self.create_widgets()
    
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
        self.question_frame.pack(fill='both', padx=20, pady=20)
        
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

        self.show_question()
    
    def show_question(self):
        # Resetear estado
        self.restart_button.pack_forget()
        self.clear_image()
        self.option_a.pack(side='left', padx=10)
        self.option_b.pack(side='left', padx=10)
        
        # Obtener pregunta actual
        question, option_a, option_b = self.parent.expert_system.get_question()
        
        # Mostrar pregunta
        self.question_label.config(text=question)
        self.option_a.config(text=option_a)
        self.option_b.config(text=option_b)

        # Limpiar imagen previa
        self.clear_image()

        self.image_relative_path = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(self.image_relative_path, f"../assets/img_q/partes_algas.png")
        # Intentar mostrar imagen si está disponible
        try:
            # En un entorno real, aquí cargarías la imagen desde un archivo
            image = Image.open(self.icon_path)
            image = image.resize((600, 300), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            
            # Crear etiqueta para la imagen
            self.image_label = tk.Label(self.image_frame, image=self.photo, bg='#e0f7fa')
            self.image_label.pack(pady=10)
            
        except Exception as e:
            print(f"No se pudo cargar la imagen: {e}")
    
    def clear_image(self):
        """Elimina la imagen actual si existe"""
        if hasattr(self, 'image_label'):
            self.image_label.destroy()
        if hasattr(self, 'name_label'):
            self.name_label.destroy()

    def select_option(self, option):
        # Procesar respuesta
        species = self.parent.expert_system.answer_question(option)
        clasificacion = """
        Imperio: Eukaryota
        Reino: Plantae
        Phylum: Chlorophyta
        Clase: Ulvophyceae
        Orden: Bryopsidales
        Familia: Caulerpaceae
        Género: Caulerpa"""
        
        if species:
            self.show_result(species, clasificacion)
        else:
            self.show_question()
    
    def show_result(self, species, clasificacion):
        self.question_label.config(text=f"¡Identificación completada!\n\nEspecie identificada: {species}")

        self.option_a.pack_forget() # Ocultar botones de opción
        self.option_b.pack_forget()
        self.restart_button.pack(pady=2) # Mostrar botón de reinicio en la parte inferior
        # Limpiar imagen previa
        self.clear_image()

        self.image_relative_path = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(self.image_relative_path, f"../assets/img/{species.lower().replace(' ', '_')}.png")
        # Intentar mostrar imagen si está disponible
        try:
            # En un entorno real, aquí cargarías la imagen desde un archivo
            image = Image.open(self.icon_path)
            image = image.resize((250, 150), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            
            # Crear etiqueta para la imagen
            self.image_label = tk.Label(self.image_frame, image=self.photo, bg='#e0f7fa')
            self.image_label.pack(pady=10)
            
            # Añadir nombre científico
            self.name_label = tk.Label(self.image_frame, text=f"{species}\n\nClasificación Taxonómica: {clasificacion}", font=('Arial', 10, 'italic'), bg='#e0f7fa')
            self.name_label.pack()
        except Exception as e:
            print(f"No se pudo cargar la imagen: {e}")

        
    
    def restart(self):
        self.parent.expert_system.reset()
        
        # Mostrar primera pregunta
        self.show_question()

class VerificarAlgaFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(style='TFrame')
        self.parent = parent
        
        # Crear widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Botón para volver al menú
        self.back_button = ttk.Button(self, text="Volver al Menú", 
                                   command=self.parent.show_main_menu)
        self.back_button.pack(anchor='nw', padx=10, pady=10)
        
        # Título
        title_label = tk.Label(self, text="Verificar Alga", 
                             font=('Arial', 16, 'bold'), 
                             bg='#00796b', fg='white', pady=10)
        title_label.pack(fill='x')
        
        # Contenido principal
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill='both', expand=True, padx=50, pady=30)
        
        # Descripción
        description = ("Seleccione la especie que cree que es su alga y responda las preguntas "
                      "para verificar si su identificación es correcta.")
        desc_label = tk.Label(self.main_frame, text=description, 
                            font=('Arial', 11), wraplength=600,
                            justify='left', bg='#f0f8ff')
        desc_label.pack(pady=10)
        
        # Selección de especie
        species_frame = ttk.Frame(self.main_frame)
        species_frame.pack(pady=20, fill='x')
        
        species_label = tk.Label(species_frame, text="Seleccione la especie:", 
                               anchor='w', bg='#f0f8ff')
        species_label.pack(side='left', padx=5)
        
        self.species_var = tk.StringVar()
        self.species_combobox = ttk.Combobox(species_frame, 
                                           textvariable=self.species_var,
                                           width=30)
        self.species_combobox['values'] = [
            "Caulerpa fastigiata", "Caulerpa prolifera", "Caulerpa verticillata",
            "Caulerpa cupressoides", "Caulerpa taxifolia", "Caulerpa mexicana",
            "Caulerpa sertularioides", "Caulerpa ashmeadii", "Caulerpa chemnitzia",
            "Caulerpa microphysa", "Caulerpa macrophysa"
        ]
        self.species_combobox.current(0)
        self.species_combobox.pack(side='left', padx=5)
        
        # Botón de inicio
        self.start_button = ttk.Button(self.main_frame, text="Iniciar Verificación", 
                                     command=self.start_verification, width=20)
        self.start_button.pack(pady=20)
        
        # Frame para el proceso de verificación (inicialmente oculto)
        self.verification_frame = ttk.Frame(self)
        
        # Área de pregunta
        self.question_label = tk.Label(self.verification_frame, text="", 
                                     font=('Arial', 12), bg='#f0f8ff',
                                     wraplength=550, justify='left')
        self.question_label.pack(pady=20, padx=20)
        
        # Frame para botones de opciones
        self.button_frame = ttk.Frame(self.verification_frame)
        self.button_frame.pack(pady=20)
        
        self.option_a = ttk.Button(self.button_frame, text="", width=75,
                                  command=lambda: self.answer_question('a'))
        self.option_a.pack(side='left', padx=10)
        
        self.option_b = ttk.Button(self.button_frame, text="", width=75,
                                  command=lambda: self.answer_question('b'))
        self.option_b.pack(side='left', padx=10)
        
        # Botón para cancelar verificación
        self.cancel_button = ttk.Button(self.verification_frame, text="Cancelar Verificación",
                                      command=self.cancel_verification)
        self.cancel_button.pack(pady=20)
        
        # Resultado de verificación
        self.result_frame = ttk.Frame(self.verification_frame)
        
        self.result_label = tk.Label(self.result_frame, text="", 
                                   font=('Arial', 12), bg='#f0f8ff',
                                   wraplength=550, justify='left')
        self.result_label.pack(pady=20)
        
        self.suggestion_label = tk.Label(self.result_frame, text="", 
                                       font=('Arial', 11), bg='#f0f8ff',
                                       wraplength=550, justify='left', fg='#d32f2f')
        self.suggestion_label.pack(pady=10)
        
        self.restart_button = ttk.Button(self.result_frame, text="Verificar Otra Alga",
                                       command=self.restart_verification)
        self.restart_button.pack(pady=20)
    
    def start_verification(self):
        # Obtener especie seleccionada
        selected_species = self.species_var.get()
        
        if selected_species == "":
            messagebox.showwarning("Selección requerida", "Por favor seleccione una especie")
            return
        
        # Configurar el sistema experto
        self.parent.expert_system.reset()
        self.parent.expert_system.verification_species = selected_species
        
        # Ocultar el marco principal y mostrar el marco de verificación
        self.main_frame.pack_forget()
        self.verification_frame.pack(fill='both', expand=True, padx=50, pady=30)
        
        # Mostrar la primera pregunta
        self.show_question()
    
    def show_question(self):
        # Obtener pregunta actual
        question, option_a, option_b = self.parent.expert_system.get_question()
        
        # Mostrar pregunta
        self.question_label.config(text=question)
        self.option_a.config(text=option_a)
        self.option_b.config(text=option_b)
        
        # Ocultar resultado si está visible
        self.result_frame.pack_forget()
        self.button_frame.pack(pady=20)
        self.cancel_button.pack(pady=20)
    
    def answer_question(self, option):
        # Procesar respuesta
        species = self.parent.expert_system.answer_question(option)
        
        if species:
            self.show_result(species)
        else:
            self.show_question()
    
    def show_result(self, species):
        # Ocultar botones de opciones
        self.button_frame.pack_forget()
        self.cancel_button.pack_forget()
        
        # Mostrar resultado
        self.result_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        selected_species = self.parent.expert_system.verification_species
        
        if species == selected_species:
            self.result_label.config(text=f"¡Verificación exitosa!\n\nLa especie {species} ha sido confirmada.")
            self.suggestion_label.config(text="")
        else:
            self.result_label.config(text=f"La especie seleccionada ({selected_species}) no coincide con las características.")
            self.suggestion_label.config(text=f"Basado en las respuestas, la especie parece ser: {species}")
    
    def cancel_verification(self):
        # Volver al marco principal
        self.verification_frame.pack_forget()
        self.main_frame.pack(fill='both', expand=True, padx=50, pady=30)
    
    def restart_verification(self):
        # Volver al inicio
        self.result_frame.pack_forget()
        self.main_frame.pack(fill='both', expand=True, padx=50, pady=30)
        self.verification_frame.pack_forget()

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
        title_label = tk.Label(self, text="Glosario de Términos", 
                             font=('Arial', 16, 'bold'), 
                             bg='#00796b', fg='white', pady=10)
        title_label.pack(fill='x')
        
        # Contenedor principal con scroll
        outer_content_frame = ttk.Frame(self, style='TFrame')
        outer_content_frame.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Configuración del canvas y scrollbar
        self.canvas = tk.Canvas(outer_content_frame, bg='#f0f8ff', highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(outer_content_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style='TFrame')
        
        self.canvas_window_id = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        # Configurar eventos
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.scrollable_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind('<Enter>', self._bind_mouse_wheel)
        self.canvas.bind('<Leave>', self._unbind_mouse_wheel)
        
        # Contenido del glosario
        self.create_glosario_content()
        self.after(1, self.trigger_initial_scroll_update)
    
    def create_glosario_content(self):
        """Crea y organiza el contenido del glosario"""
        # Título del glosario
        title_label = tk.Label(self.scrollable_frame, 
                             text="Glosario para el uso del Sistema Experto de Algas Marinas",
                             font=('Arial', 14, 'bold'),
                             bg='#f0f8ff')
        title_label.pack(pady=(0, 20))
        
        # Términos del glosario
        terminos = [
            ("Rizomas", "Tallos subterráneos o rastreros que pueden dar origen a nuevas plantas."),
            ("Frondes erectos", "Las partes verticales de la planta de alga que se extienden hacia arriba desde el sustrato."),
            ("Ramillas", "Pequeñas ramas o divisiones secundarias que se desprenden de los frondes principales."),
            ("Verticiladas", "Una disposición de ramillas o frondes que se organizan en forma de espiral o en círculos alrededor de un eje central."),
            ("Apices", "Las puntas o extremos de las ramillas o frondes."),
            ("Constricción basal", "Un estrechamiento o reducción en el diámetro en la base de una estructura."),
            ("Nervio central", "Una estructura similar a una nervadura que recorre el centro de una lámina o fronde, dándole soporte."),
            ("Laminar", "Describe una estructura que es plana y delgada, como una hoja."),
            ("Dicotómica", "Un patrón de ramificación en el que cada división se bifurca en dos ramas aproximadamente iguales."),
            ("Talo", "El cuerpo vegetativo de un alga, que no está diferenciado en raíz, tallo y hojas verdaderas."),
            ("Bentónico", "Organismos que viven asociados al fondo de cuerpos de agua."),
            ("Epífita", "Un organismo que crece sobre otra planta u alga, pero no es parasitario."),
            ("Uniaxial", "Talo formado por un único eje central de células."),
            ("Multiaxial", "Talo formado por múltiples ejes celulares que crecen juntos."),
            ("Vesícula gaseosa (Neumatocisto)", "Estructura llena de gas que ayuda a la flotación del alga."),
            ("Receptáculo", "Estructura reproductiva que contiene los órganos sexuales."),
            ("Conceptáculo", "Cavidad en los receptáculos que contiene las estructuras reproductivas."),
            ("Incrustante", "Que crece pegado y se adhiere fuertemente al sustrato."),
            ("Calcificado", "Que contiene depósitos de carbonato de calcio, dándole una textura dura o pétrea."),
            ("Filamentoso", "Que tiene forma de hilo o filamento."),
            ("Macroscópico", "Visible a simple vista sin necesidad de microscopio."),
            ("Microscópico", "Requiere un microscopio para ser observado."),
            ("Hábitat", "El entorno natural en el que vive una especie."),
            ("Sustrato", "La superficie sobre la cual crece un organismo (rocas, arena, otras algas)."),
            ("Mareas", "El ascenso y descenso periódico del nivel del mar."),
            ("Intermareal", "Zona de la costa que queda expuesta al aire durante la marea baja y sumergida durante la marea alta."),
            ("Submareal", "Zona del fondo marino que siempre está sumergida, incluso durante la marea baja.")
        ]
        
        # Crear un frame para los términos
        terms_frame = ttk.Frame(self.scrollable_frame, style='TFrame')
        terms_frame.pack(fill='x', padx=20, pady=10)
        
        # Agregar cada término con su definición
        for termino, definicion in terminos:
            term_frame = ttk.Frame(terms_frame, style='TFrame')
            term_frame.pack(fill='x', pady=5, anchor='w')
            
            # Término en negrita
            term_label = tk.Label(term_frame, text=f"{termino}:", 
                                font=('Arial', 11, 'bold'), 
                                bg='#f0f8ff', anchor='w')
            term_label.pack(side='left', anchor='w')
            
            # Definición
            def_label = tk.Label(term_frame, text=definicion,
                               font=('Arial', 11),
                               bg='#f0f8ff', anchor='w',
                               wraplength=600, justify='left')
            def_label.pack(side='left', padx=(5, 0), fill='x', expand=True)
            
            # Configurar el evento para actualizar el wraplength cuando cambie el tamaño
            def_label.bind('<Configure>', lambda e, lbl=def_label: lbl.config(wraplength=lbl.winfo_width()-5))
    
    def trigger_initial_scroll_update(self):
        """Actualiza el scroll al mostrar el frame"""
        self.update_idletasks()
        self._on_frame_configure()
    
    def _on_canvas_configure(self, event):
        """Ajusta el ancho del frame interno cuando cambia el tamaño del canvas"""
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window_id, width=canvas_width)
        
        # Actualizar wraplength para todas las definiciones
        for child in self.scrollable_frame.winfo_children():
            if isinstance(child, ttk.Frame):
                for subchild in child.winfo_children():
                    if isinstance(subchild, tk.Label) and 'wraplength' in subchild.config():
                        subchild.config(wraplength=canvas_width - 40)
    
    def _on_frame_configure(self, event=None):
        """Actualiza la región de scroll cuando cambia el contenido"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def _on_mouse_wheel(self, event):
        """Maneja el evento de la rueda del mouse para el scroll"""
        if event.num == 4:
            self.canvas.yview_scroll(-1, "unit")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "unit")
        else:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def _bind_mouse_wheel(self, event):
        """Vincula los eventos de la rueda del mouse cuando el cursor entra al canvas"""
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
        self.canvas.bind_all("<Button-4>", self._on_mouse_wheel)
        self.canvas.bind_all("<Button-5>", self._on_mouse_wheel)
    
    def _unbind_mouse_wheel(self, event):
        """Desvincula los eventos de la rueda del mouse cuando el cursor sale del canvas"""
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")

        

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
        self.logo_path = os.path.join(self.relative_logo_path, '../assets/icon/ico.png')

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
            "Br. Khristian Flores - Desarrollador de Software",
            "Br. Duberth Farías - Desarrollador de Software",
            "Lic. José Morillo - Guía del Proyecto",
            "Lic. Yuraima García - Experta en Algas"
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