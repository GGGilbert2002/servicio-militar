import customtkinter as ctk
from .database import get_session
from .modelos import Recluta
from config import PARROQUIAS

class RecolectorFrame(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registrar Recluta")
        self.geometry("600x700")
        self.resizable(False, False)

        # Variables de formulario
        self.cedula_var = ctk.StringVar()
        self.nombre_var = ctk.StringVar()
        self.apellido_var = ctk.StringVar()
        self.edad_var = ctk.StringVar()
        self.parroquia_var = ctk.StringVar(value=PARROQUIAS[0] if PARROQUIAS else "")
        self.direccion_var = ctk.StringVar()
        self.telefono_var = ctk.StringVar()
        self.apto_var = ctk.BooleanVar(value=True)
        self.estatura_var = ctk.StringVar()
        self.peso_var = ctk.StringVar()
        self.observaciones_var = ctk.StringVar()

        self._crear_widgets()

    def _crear_widgets(self):
        # Título
        ctk.CTkLabel(self, text="Formulario de Registro", font=("Arial", 20, "bold")).pack(pady=10)

        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Campos
        campos = [
            ("Cédula (*):", self.cedula_var),
            ("Nombre (*):", self.nombre_var),
            ("Apellido (*):", self.apellido_var),
            ("Edad (*):", self.edad_var),
            ("Parroquia (*):", self.parroquia_var, "optionmenu", PARROQUIAS),
            ("Dirección:", self.direccion_var),
            ("Teléfono:", self.telefono_var),
            ("Estatura (m):", self.estatura_var),
            ("Peso (kg):", self.peso_var),
            ("Observaciones:", self.observaciones_var)
        ]

        for campo in campos:
            if len(campo) == 2:
                label, var = campo
                ctk.CTkLabel(frame, text=label).pack(anchor="w", pady=(10,0))
                ctk.CTkEntry(frame, textvariable=var, width=400).pack(fill="x", pady=(0,5))
            elif campo[2] == "optionmenu":
                label, var, _, opciones = campo
                ctk.CTkLabel(frame, text=label).pack(anchor="w", pady=(10,0))
                ctk.CTkOptionMenu(frame, values=opciones, variable=var).pack(fill="x", pady=(0,5))

        # Checkbox para "Apto"
        ctk.CTkCheckBox(frame, text="Apto para el servicio militar", variable=self.apto_var).pack(anchor="w", pady=10)

        # Botón guardar
        ctk.CTkButton(self, text="Guardar Recluta", command=self._guardar, fg_color="green").pack(pady=20)

    def _guardar(self):
        # Validaciones básicas
        if not all([self.cedula_var.get(), self.nombre_var.get(), self.apellido_var.get(), self.edad_var.get()]):
            ctk.CTkMessagebox.show_error("Error", "Complete los campos obligatorios (*)")
            return

        try:
            edad = int(self.edad_var.get())
            if edad < 18 or edad > 50:
                ctk.CTkMessagebox.show_error("Error", "La edad debe estar entre 18 y 50 años")
                return
        except ValueError:
            ctk.CTkMessagebox.show_error("Error", "Edad debe ser un número entero")
            return

        estatura = float(self.estatura_var.get()) if self.estatura_var.get() else None
        peso = float(self.peso_var.get()) if self.peso_var.get() else None

        session = get_session()
        try:
            recluta = Recluta(
                cedula=self.cedula_var.get(),
                nombre=self.nombre_var.get(),
                apellido=self.apellido_var.get(),
                edad=edad,
                parroquia=self.parroquia_var.get(),
                direccion=self.direccion_var.get(),
                telefono=self.telefono_var.get(),
                apto=self.apto_var.get(),
                estatura=estatura,
                peso=peso,
                observaciones=self.observaciones_var.get()
            )
            session.add(recluta)
            session.commit()
            ctk.CTkMessagebox.show_info("Éxito", "Recluta registrado correctamente")
            self.destroy()
        except Exception as e:
            session.rollback()
            ctk.CTkMessagebox.show_error("Error", f"No se pudo guardar: {str(e)}")
        finally:
            session.close()