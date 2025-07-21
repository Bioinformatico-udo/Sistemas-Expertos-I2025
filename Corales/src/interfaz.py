import os
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
from millepora_expert import MilleporaExpert, CoralCharacteristic

class CoralApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Identificación de Corales Millepora del Atlántico")
        self.geometry("1100x800")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.historial = []
        self._setup_ui()

    def _setup_ui(self):
        self.configure(bg="#021F3F")

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(pady=20)

        base_path = os.path.dirname(__file__)
        img_path = os.path.join(base_path, "assets", "iconos", "coral_icon.jpg")
        img = Image.open(img_path).resize((80, 80))
        self.logo = ImageTk.PhotoImage(img)

        ctk.CTkLabel(header, image=self.logo, text="", fg_color="transparent").pack(side="left", padx=10)
        ctk.CTkLabel(
            header,
            text="Sistema Experto: Millepora del Atlántico",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(side="left", padx=10)

        self.tabs = ctk.CTkTabview(self, width=1000, height=650)
        self.tabs.pack(pady=10)

        self.tabs.add("Inicio")
        self.tabs.add("Identificación")
        self.tabs.add("Resultados")
        self.tabs.add("Historial")

        self._setup_inicio_tab()
        self._setup_identificacion_tab()
        self._setup_resultados_tab()
        self._setup_historial_tab()

        self.expert = MilleporaExpert()

    def _setup_inicio_tab(self):
        tab = self.tabs.tab("Inicio")
        main_frame = ctk.CTkFrame(tab, fg_color="transparent")
        main_frame.pack(expand=True, fill="both", padx=50, pady=50)

        ctk.CTkLabel(
            main_frame,
            text="Bienvenido al Sistema Experto para Identificación de Corales Millepora",
            font=ctk.CTkFont(size=22, weight="bold"),
            wraplength=700,
            justify="center"
        ).pack(pady=20)

        img_path = os.path.join(os.path.dirname(__file__), "assets", "iconos", "ejemplo.jpeg")
        img = Image.open(img_path).resize((400, 250))
        self.ejemplo_img = ImageTk.PhotoImage(img)
        ctk.CTkLabel(main_frame, image=self.ejemplo_img, text="").pack(pady=20)

        ctk.CTkLabel(
            main_frame,
            text="Para comenzar, navega a la pestaña 'Identificación' y sigue los pasos.\n\n"
                 "El sistema te guiará a través de las características observables del coral\n"
                 "para determinar a qué especie pertenece.",
            font=ctk.CTkFont(size=16),
            wraplength=600,
            justify="center"
        ).pack(pady=20)

    def _setup_identificacion_tab(self):
        tab = self.tabs.tab("Identificación")

        self.ident_tabs = ctk.CTkTabview(tab, width=950, height=550)
        self.ident_tabs.pack(pady=10)

        self.ident_tabs.add("Forma")
        self.ident_tabs.add("Color")
        self.ident_tabs.add("Oleaje")
        self.ident_tabs.add("Detalles")

        self.forma_var = ctk.StringVar(value="")
        self.color_var = ctk.StringVar(value="")
        self.oleaje_var = ctk.StringVar(value="")
        self.extra_var = ctk.StringVar(value="")

        self._setup_forma_tab()
        self._setup_color_tab()
        self._setup_oleaje_tab()
        self._setup_detalles_tab()

        ctk.CTkButton(
            tab,
            text="Identificar Especie",
            command=self.run_inference,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=40,
            width=200
        ).pack(pady=20)

    def _setup_forma_tab(self):
        tab = self.ident_tabs.tab("Forma")
        ctk.CTkLabel(
            tab,
            text="Seleccione la forma principal del coral:",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=10)

        img_frame = ctk.CTkFrame(tab, fg_color="transparent")
        img_frame.pack()

        formas = [
            ("ramificada", "forma/ramificada.jpg", "Forma ramificada"),
            ("laminar", "forma/laminar.jpg", "Láminas en abanico"),
            ("aplanada", "forma/aplanada.jpeg", "Estructura aplanada")
        ]

        for forma, img_file, desc in formas:
            frame = ctk.CTkFrame(img_frame)
            frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

            img_path = os.path.join(os.path.dirname(__file__), "assets", img_file)
            img = Image.open(img_path).resize((200, 200))
            photo = ImageTk.PhotoImage(img)

            if not hasattr(self, 'forma_images'):
                self.forma_images = []
            self.forma_images.append(photo)

            ctk.CTkLabel(frame, image=photo, text="").pack(pady=5)
            ctk.CTkRadioButton(
                frame,
                text=desc,
                variable=self.forma_var,
                value=forma,
                font=ctk.CTkFont(size=14)
            ).pack(pady=5)

    def _setup_color_tab(self):
        tab = self.ident_tabs.tab("Color")
        ctk.CTkLabel(
            tab,
            text="Seleccione el color predominante del coral:",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=10)

        img_frame = ctk.CTkFrame(tab, fg_color="transparent")
        img_frame.pack()

        colores = [
            ("amarillo", "colores/amarillo.jpg", "Amarillo brillante"),
            ("naranja", "colores/anaranjado.png", "Naranja intenso"),
            ("marron_claro", "colores/marron.png", "Marrón claro"),
            ("beige", "colores/beige.jpg", "Beige o crema")
        ]

        for color, img_file, desc in colores:
            frame = ctk.CTkFrame(img_frame)
            frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

            img_path = os.path.join(os.path.dirname(__file__), "assets", img_file)
            img = Image.open(img_path).resize((200, 200))
            photo = ImageTk.PhotoImage(img)

            if not hasattr(self, 'color_images'):
                self.color_images = []
            self.color_images.append(photo)

            ctk.CTkLabel(frame, image=photo, text="").pack(pady=5)
            ctk.CTkRadioButton(
                frame,
                text=desc,
                variable=self.color_var,
                value=color,
                font=ctk.CTkFont(size=14)
            ).pack(pady=5)

    def _setup_oleaje_tab(self):
        tab = self.ident_tabs.tab("Oleaje")
        ctk.CTkLabel(
            tab,
            text="Seleccione las condiciones de oleaje:",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=10)

        img_frame = ctk.CTkFrame(tab, fg_color="transparent")
        img_frame.pack()

        oleajes = [
            ("fuerte", "oleaje/oleaje_fuerte.jpg", "Oleaje fuerte"),
            ("moderado", "oleaje/oleaje_moderado.jpeg", "Oleaje moderado")
        ]

        for oleaje, img_file, desc in oleajes:
            frame = ctk.CTkFrame(img_frame)
            frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

            img_path = os.path.join(os.path.dirname(__file__), "assets", img_file)
            img = Image.open(img_path).resize((200, 200))
            photo = ImageTk.PhotoImage(img)

            if not hasattr(self, 'oleaje_images'):
                self.oleaje_images = []
            self.oleaje_images.append(photo)

            ctk.CTkLabel(frame, image=photo, text="").pack(pady=5)
            ctk.CTkRadioButton(
                frame,
                text=desc,
                variable=self.oleaje_var,
                value=oleaje,
                font=ctk.CTkFont(size=14)
            ).pack(pady=5)

    def _setup_detalles_tab(self):
        tab = self.ident_tabs.tab("Detalles")
        ctk.CTkLabel(
            tab,
            text="Seleccione detalles adicionales (opcional):",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=10)

        img_frame = ctk.CTkFrame(tab, fg_color="transparent")
        img_frame.pack()

        detalles = [
            ("", "detalles/ninguno.png", "Sin detalle adicional"),
            ("cilindricas", "detalles/cilindricas.jpeg", "Ramificaciones cilíndricas"),
            ("aplanadas", "detalles/detalle_aplanada.jpeg", "Ramificaciones aplanadas"),
            ("abanico", "detalles/abanico.jpg", "Forma de abanico"),
            ("cresta", "detalles/cresta.jpeg", "Forma de cresta"),
            ("protuberancias", "detalles/protuberancia.jpg", "Protuberancias"),
            ("someras", "detalles/someras.jpeg", "Aguas someras")
        ]

        for detalle, img_file, desc in detalles:
            frame = ctk.CTkFrame(img_frame)
            frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

            img_path = os.path.join(os.path.dirname(__file__), "assets", img_file)
            img = Image.open(img_path).resize((200, 200))
            photo = ImageTk.PhotoImage(img)

            if not hasattr(self, 'detalle_images'):
                self.detalle_images = []
            self.detalle_images.append(photo)

            ctk.CTkLabel(frame, image=photo, text="").pack(pady=5)
            ctk.CTkRadioButton(
                frame,
                text=desc,
                variable=self.extra_var,
                value=detalle,
                font=ctk.CTkFont(size=14)
            ).pack(pady=5)

    def _setup_resultados_tab(self):
        tab = self.tabs.tab("Resultados")
        main_frame = ctk.CTkFrame(tab, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.img_result_frame = ctk.CTkFrame(main_frame, width=350, height=350)
        self.img_result_frame.pack(side="left", padx=20, pady=20)

        self.result_image_label = ctk.CTkLabel(
            self.img_result_frame,
            text="Imagen de resultado aquí",
            font=ctk.CTkFont(size=14)
        )
        self.result_image_label.pack(expand=True)

        text_frame = ctk.CTkFrame(main_frame)
        text_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.result_label = ctk.CTkLabel(
            text_frame,
            text="Complete la identificación para ver el resultado.",
            font=ctk.CTkFont(size=16),
            wraplength=500
        )
        self.result_label.pack(pady=20)

        ctk.CTkButton(
            text_frame,
            text="Guardar Resultado",
            command=self.guardar_resultado,
            font=ctk.CTkFont(size=14)
        ).pack(pady=10)

    def _setup_historial_tab(self):
        tab = self.tabs.tab("Historial")
        main_frame = ctk.CTkFrame(tab)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.scroll_frame = ctk.CTkScrollableFrame(main_frame)
        self.scroll_frame.pack(fill="both", expand=True)

        ctk.CTkLabel(
            self.scroll_frame,
            text="Historial de identificaciones aparecerá aquí",
            font=ctk.CTkFont(size=16)
        ).pack(pady=20)

    def run_inference(self):
        if not all([self.forma_var.get(), self.color_var.get(), self.oleaje_var.get()]):
            messagebox.showerror("Error", "Por favor complete Forma, Color y Oleaje.")
            return

        self.expert.reset()
        self.expert.declare(CoralCharacteristic(forma=self.forma_var.get()))
        self.expert.declare(CoralCharacteristic(color=self.color_var.get()))
        self.expert.declare(CoralCharacteristic(oleaje=self.oleaje_var.get()))

        if self.extra_var.get():
            self.expert.declare(CoralCharacteristic(estructura=self.extra_var.get()))
            self.expert.declare(CoralCharacteristic(ramas=self.extra_var.get()))
            self.expert.declare(CoralCharacteristic(superficie=self.extra_var.get()))
            self.expert.declare(CoralCharacteristic(habitat=self.extra_var.get()))

        self.expert.run()

        if self.expert.identified_species:
            species = self.expert.identified_species
            info = self.expert.species_info[species]
            img_file = f"{species.lower().replace(' ', '_')}.jpg"
            img_path = os.path.join(os.path.dirname(__file__), "assets", "especies", img_file)
            try:
                img = Image.open(img_path).resize((350, 350))
                photo = ImageTk.PhotoImage(img)
                self.result_image = photo
                self.result_image_label.configure(image=photo, text="")
            except Exception as e:
                self.result_image_label.configure(text="Imagen no disponible", image="")
            self.result_label.configure(
                text=f"Especie: {species}\n\nDescripción:\n{info}"
            )
            self.historial.append(f"{datetime.now()}: {species}")
            self.update_historial_tab()
            self.tabs.set("Resultados")
        else:
            messagebox.showinfo("Sin resultados", "No se pudo identificar la especie con la información proporcionada.")

    def guardar_resultado(self):
        if self.expert.identified_species:
            filename = f"identificacion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            path = os.path.join(os.path.dirname(__file__), filename)
            with open(path, "w") as f:
                f.write(f"Especie: {self.expert.identified_species}\n")
                f.write(f"Características:\n- Forma: {self.forma_var.get()}\n")
                f.write(f"- Color: {self.color_var.get()}\n")
                f.write(f"- Oleaje: {self.oleaje_var.get()}\n")
                f.write(f"- Extra: {self.extra_var.get()}\n")
            messagebox.showinfo("Guardado", f"Resultado guardado en: {path}")
        else:
            messagebox.showinfo("Sin resultados", "Identifique una especie antes de guardar.")

    def update_historial_tab(self):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()
        for entry in self.historial:
            ctk.CTkLabel(self.scroll_frame, text=entry, font=ctk.CTkFont(size=14)).pack(anchor="w", pady=2)

if __name__ == "__main__":
    app = CoralApp()
    app.mainloop()
