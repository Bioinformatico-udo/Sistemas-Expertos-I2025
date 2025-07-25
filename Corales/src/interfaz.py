import os
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import subprocess
from millepora_expert import MilleporaExpert, CoralCharacteristic

class CoralApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Identificación de Corales Millepora del Atlántico")
        self.geometry("1100x800")
        self.resizable(False, False)

        icon_path = os.path.join(os.path.dirname(__file__), "assets", "iconos", "icono.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.historial = []
        self._setup_ui()
        self.expert = MilleporaExpert()

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
        self.tabs.add("Acerca de")

        self._setup_inicio_tab()
        self._setup_identificacion_tab()
        self._setup_resultados_tab()
        self._setup_historial_tab()
        self._setup_acerca_tab()

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
            text="Para comenzar, navega a la pestaña 'Identificación' y sigue los pasos.",
            font=ctk.CTkFont(size=16),
            wraplength=600,
            justify="center"
        ).pack(pady=20)

    def _setup_identificacion_tab(self):
        tab = self.tabs.tab("Identificación")
        self.ident_tabs = ctk.CTkTabview(tab, width=950, height=550)
        self.ident_tabs.pack(pady=(20, 10))

        self.ident_tabs.add("Forma")
        self.ident_tabs.add("Color")
        self.ident_tabs.add("Oleaje")
        self.ident_tabs.add("Detalles")

        self.forma_var = ctk.StringVar()
        self.color_var = ctk.StringVar()
        self.oleaje_var = ctk.StringVar()
        self.detalle_var = ctk.StringVar()

        self._setup_radio_tab(self.ident_tabs.tab("Forma"), [
            ("ramificada", "ramificada.jpg", "Ramificada"),
            ("laminar", "laminar.jpg", "Laminar"),
            ("aplanada", "aplanada.jpeg", "Aplanada")
        ], self.forma_var, "forma")

        self._setup_radio_tab(self.ident_tabs.tab("Color"), [
            ("amarillo", "amarillo.jpg", "Amarillo"),
            ("naranja", "anaranjado.png", "Naranja"),
            ("marron_claro", "marron.png", "Marrón Claro"),
            ("beige", "beige.jpg", "Beige")
        ], self.color_var, "colores")

        self._setup_radio_tab(self.ident_tabs.tab("Oleaje"), [
            ("fuerte", "oleaje_fuerte.jpg", "Fuerte"),
            ("moderado", "oleaje_moderado.jpeg", "Moderado")
        ], self.oleaje_var, "oleaje")

        self._setup_radio_tab(self.ident_tabs.tab("Detalles"), [
            ("cilindricas", "cilindricas.jpeg", "Cilíndricas"),
            ("aplanadas", "aplanados .jpeg", "Aplanadas"),
            ("abanico", "abanico.jpg", "Abanico"),
            ("cresta", "cresta.jpeg", "Cresta"),
            ("protuberancias", "protuberancia.jpg", "Protuberancias"),
            ("someras", "someras.jpeg", "Aguas someras")
        ], self.detalle_var, "detalles")

        button_container = ctk.CTkFrame(master=tab, fg_color="transparent")
        button_container.pack(pady=(30, 20))

        self.ident_button = ctk.CTkButton(
            master=button_container,
            text="🔍 IDENTIFICAR ESPECIE",
            command=self.run_inference,
            font=ctk.CTkFont(size=32, weight="bold"),
            height=80,
            width=400,
            fg_color="#0077cc",
            hover_color="#005f99",
            text_color="white",
            corner_radius=10
        )
        self.ident_button.pack()

    def _setup_radio_tab(self, tab, items, variable, folder):
        ctk.CTkLabel(tab, text="Seleccione una opción:", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
        frame = ctk.CTkFrame(tab, fg_color="transparent")
        frame.pack()
        for item, img_file, desc in items:
            box = ctk.CTkFrame(frame)
            box.pack(side="left", padx=10, pady=10)
            path = os.path.join(os.path.dirname(__file__), "assets", folder, img_file)
            img = Image.open(path).resize((200, 200))
            photo = ImageTk.PhotoImage(img)
            if not hasattr(self, f'{folder}_images'):
                setattr(self, f'{folder}_images', [])
            getattr(self, f'{folder}_images').append(photo)
            ctk.CTkLabel(box, image=photo, text="").pack(pady=5)
            ctk.CTkRadioButton(box, text=desc, variable=variable, value=item).pack()

    def run_inference(self):
        self.expert = MilleporaExpert()

        if self.forma_var.get():
            self.expert.declare(CoralCharacteristic(forma=self.forma_var.get()))
        if self.color_var.get():
            self.expert.declare(CoralCharacteristic(color=self.color_var.get()))
        if self.oleaje_var.get():
            self.expert.declare(CoralCharacteristic(oleaje=self.oleaje_var.get()))
        if self.detalle_var.get():
            d = self.detalle_var.get()
            self.expert.declare(CoralCharacteristic(estructura=d))
            self.expert.declare(CoralCharacteristic(ramas=d))
            self.expert.declare(CoralCharacteristic(superficie=d))
            self.expert.declare(CoralCharacteristic(habitat=d))

        try:
            self.expert.run()
            result = self.expert.get_result_info()
            if result:
                resumen = self.expert.get_diagnosis_summary()
                self.update_resultados_tab(
                    result["nombre"],
                    result["confianza"],
                    result["descripcion"],
                    resumen,
                    result["imagen"]
                )
                self.historial.append(f"{datetime.now()}: {result['nombre']} ({result['confianza']}%)")
                self.update_historial_tab()
                self.tabs.set("Resultados")
            else:
                messagebox.showwarning("Sin resultados", "❌ No se pudo identificar la especie con la información proporcionada.")
        except Exception as e:
            messagebox.showerror("Error del sistema experto", f"Ocurrió un error durante la inferencia:\n\n{e}")

    def _setup_resultados_tab(self):
        tab = self.tabs.tab("Resultados")
        self.resultado_frame = ctk.CTkFrame(tab)
        self.resultado_frame.pack(padx=10, pady=10)

    def update_resultados_tab(self, species, confianza, descripcion, resumen, img_path):
        for widget in self.resultado_frame.winfo_children():
            widget.destroy()
        if img_path and os.path.exists(img_path):
            img = Image.open(img_path).resize((300, 200))
            self.result_img = ImageTk.PhotoImage(img)
            ctk.CTkLabel(self.resultado_frame, image=self.result_img, text="").pack(pady=10)

        texto = f"✅ Especie identificada: {species}\nConfianza: {confianza}%\n\n{descripcion}\n\n{resumen}"
        ctk.CTkLabel(self.resultado_frame, text=texto, font=ctk.CTkFont(size=16), wraplength=800, justify="left").pack(pady=10)

    def _setup_historial_tab(self):
        tab = self.tabs.tab("Historial")
        self.scroll_frame = ctk.CTkScrollableFrame(tab)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def update_historial_tab(self):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()
        for entry in reversed(self.historial):
            ctk.CTkLabel(self.scroll_frame, text=entry, font=ctk.CTkFont(size=14)).pack(anchor="w", pady=2)

    def _setup_acerca_tab(self):
        tab = self.tabs.tab("Acerca de")
        main_frame = ctk.CTkFrame(tab, fg_color="transparent")
        main_frame.pack(expand=True, fill="both", padx=50, pady=50)

        ctk.CTkLabel(
            main_frame,
            text="Acerca del Sistema Experto Millepora",
            font=ctk.CTkFont(size=22, weight="bold"),
            wraplength=700,
            justify="center"
        ).pack(pady=20)

        ctk.CTkLabel(
            main_frame,
            text=(
                "Este sistema experto identifica especies de corales del género *Millepora* "
                "presentes en el Atlántico, utilizando características morfológicas y ambientales. "
                "Su propósito es apoyar investigaciones y prácticas educativas."
            ),
            font=ctk.CTkFont(size=16),
            wraplength=800,
            justify="center"
        ).pack(pady=20)

        # 📘 BOTÓN PARA ABRIR EL MANUAL DE USUARIO
        manual_btn = ctk.CTkButton(
            main_frame,
            text="📘 Ver Manual de Usuario",
            command=self.abrir_manual_pdf,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#4A90E2",
            hover_color="#2F6DB5",
            text_color="white"
        )
        manual_btn.pack(pady=20)

        autores_texto = (
            "Autores:\n"
            "• Aaron Ortiz– Estudiante de Informática\n"
            "• Fabian Quijada– Estudiante de Informática\n"
            "• Eduardo Gonzales – Estudiante de Informática\n\n"
            "Colaboradores Expertos:\n"
            "• Dr. Martin Rada– Especialista en Coralología\n"
            "• Jose Morillo – Investigador Marino y Licenciado en Informática\n"
        )

        ctk.CTkLabel(
            main_frame,
            text=autores_texto,
            font=ctk.CTkFont(size=14),
            wraplength=800,
            justify="left"
        ).pack(pady=10)

    def abrir_manual_pdf(self):
        pdf_path = os.path.join(os.path.dirname(__file__), "manual_usuario.pdf")
        try:
            if os.name == 'nt':  # Windows
                os.startfile(pdf_path)
            elif os.name == 'posix':  # macOS or Linux
                subprocess.call(('open' if sys.platform == 'darwin' else 'xdg-open', pdf_path))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el manual:\n{e}")


if __name__ == "__main__":
    app = CoralApp()
    app.mainloop()
