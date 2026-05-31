import customtkinter as ctk
from app.database import init_db
from app.recolector import RecolectorFrame
from config import APP_NAME, WINDOW_SIZE

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.geometry(WINDOW_SIZE)
        self.resizable(True, True)

        # Botones principales
        self.btn_init = ctk.CTkButton(self, text="Inicializar Base de Datos", command=self.inicializar_db, fg_color="blue")
        self.btn_init.pack(pady=20)

        self.btn_registro = ctk.CTkButton(self, text="Registrar Recluta", command=self.abrir_recolector, fg_color="green")
        self.btn_registro.pack(pady=20)

        self.btn_salir = ctk.CTkButton(self, text="Salir", command=self.destroy, fg_color="red")
        self.btn_salir.pack(pady=20)

    def inicializar_db(self):
        try:
            init_db()
            ctk.CTkMessagebox.show_info("Éxito", "Base de datos inicializada correctamente")
        except Exception as e:
            ctk.CTkMessagebox.show_error("Error", f"Error al inicializar DB: {str(e)}")

    def abrir_recolector(self):
        RecolectorFrame(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()