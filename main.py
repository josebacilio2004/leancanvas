import tkinter as tk


class LeanCanvasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lean Canvas: Digital Insight")
        self.root.geometry("1000x800")

        # Configuración del layout principal
        self.create_frames()
        self.populate_frames()

    def create_frames(self):
        frame_style = {"bg": "#F8F8F8", "bd": 2, "relief": "solid"}

        self.problem_frame = tk.Frame(self.root, **frame_style)
        self.value_proposition_frame = tk.Frame(self.root, **frame_style)
        self.customer_segments_frame = tk.Frame(self.root, **frame_style)
        self.solution_frame = tk.Frame(self.root, **frame_style)
        self.channels_frame = tk.Frame(self.root, **frame_style)
        self.revenue_streams_frame = tk.Frame(self.root, **frame_style)
        self.cost_structure_frame = tk.Frame(self.root, **frame_style)
        self.key_metrics_frame = tk.Frame(self.root, **frame_style)
        self.unfair_advantage_frame = tk.Frame(self.root, **frame_style)

        # Posicionamiento en la cuadrícula
        self.problem_frame.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")
        self.value_proposition_frame.grid(row=0, column=2, rowspan=2, columnspan=2, sticky="nsew")
        self.customer_segments_frame.grid(row=0, column=4, rowspan=2, columnspan=2, sticky="nsew")
        self.solution_frame.grid(row=2, column=0, rowspan=2, columnspan=2, sticky="nsew")
        self.channels_frame.grid(row=2, column=2, rowspan=2, columnspan=2, sticky="nsew")
        self.revenue_streams_frame.grid(row=2, column=4, rowspan=2, columnspan=2, sticky="nsew")
        self.cost_structure_frame.grid(row=4, column=0, rowspan=2, columnspan=3, sticky="nsew")
        self.key_metrics_frame.grid(row=4, column=3, rowspan=2, columnspan=2, sticky="nsew")
        self.unfair_advantage_frame.grid(row=4, column=5, rowspan=2, sticky="nsew")

        for i in range(6):
            self.root.columnconfigure(i, weight=1)
        for i in range(6):
            self.root.rowconfigure(i, weight=1)

    def populate_frames(self):
        # Insertar el contenido de cada sección
        self.add_content(self.problem_frame, "Problema", [
            "Las organizaciones enfrentan dificultades para tomar decisiones estratégicas debido a la sobrecarga de datos.",
            "Falta de adopción efectiva de tecnologías de inteligencia artificial y transformación digital.",
            "Ineficiencia en procesos clave que resulta en altos costos operativos."
        ])

        self.add_content(self.value_proposition_frame, "Propuesta de Valor", [
            "Toma de decisiones basada en IA: Herramientas y plataformas que proporcionan análisis y recomendaciones en tiempo real.",
            "Transformación digital integral: Servicios completos para modernizar y optimizar operaciones.",
            "Optimización de procesos: Mejora de la eficiencia operativa mediante automatización y IA.",
            "Consultoría estratégica personalizada: Planes adaptados a las necesidades específicas de cada cliente."
        ])

        self.add_content(self.customer_segments_frame, "Segmentos de Clientes", [
            "Empresas medianas y grandes.",
            "Instituciones financieras.",
            "Sector salud.",
            "Retailers y comercio electrónico."
        ])

        self.add_content(self.solution_frame, "Solución", [
            "Desarrollo de una plataforma digital que ofrezca análisis basados en IA.",
            "Servicios de consultoría personalizada para la implementación de soluciones de IA y transformación digital.",
            "Capacitaciones y formación en el uso de tecnologías digitales."
        ])

        self.add_content(self.channels_frame, "Canales", [
            "Plataforma en línea para acceso a herramientas y recursos.",
            "Consultoría directa con expertos en transformación digital.",
            "Webinars y eventos educativos."
        ])

        self.add_content(self.revenue_streams_frame, "Ingresos", [
            "Suscripciones a la plataforma de IA.",
            "Honorarios por servicios de consultoría y desarrollo de proyectos.",
            "Programas de formación y capacitación."
        ])

        self.add_content(self.cost_structure_frame, "Estructura de Costos", [
            "Desarrollo y mantenimiento de tecnología de IA.",
            "Salarios del personal especializado.",
            "Marketing y ventas.",
            "Investigación y desarrollo de nuevas tecnologías."
        ])

        self.add_content(self.key_metrics_frame, "Métricas Clave", [
            "Tasa de adopción de la plataforma digital.",
            "Incremento en la eficiencia operativa de los clientes.",
            "Retorno de inversión para los clientes a través de la implementación de IA.",
            "Crecimiento en el número de clientes y suscripciones."
        ])

        self.add_content(self.unfair_advantage_frame, "Ventaja Especial", [
            "Expertise en la intersección de IA y transformación digital.",
            "Soluciones personalizadas adaptadas a las necesidades específicas de cada industria.",
            "Red de alianzas con universidades y proveedores tecnológicos para mantenerse a la vanguardia."
        ])

    def add_content(self, frame, title, content_list):
        # Agregar el título de la sección
        title_label = tk.Label(frame, text=title, font=("Arial", 14, "bold"), bg=frame["bg"], wraplength=200)
        title_label.pack(anchor="n", pady=5)

        # Agregar cada punto de contenido
        for item in content_list:
            item_label = tk.Label(frame, text=f"• {item}", font=("Arial", 10), bg=frame["bg"], wraplength=200,
                                  justify="left")
            item_label.pack(anchor="w", padx=10, pady=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = LeanCanvasApp(root)
    root.mainloop()
