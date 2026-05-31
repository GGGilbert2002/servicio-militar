# Plataforma de Análisis Estadístico y Territorial – Servicio Militar Coro

Sistema de escritorio para el registro, análisis estadístico y mapeo territorial del reclutamiento del servicio militar en la ciudad de Coro, Estado Falcón, Venezuela.

## 📐 Arquitectura del Sistema (Doc-as-Code)

### 1. Arquitectura de Componentes y Flujo de Datos
```mermaid  
graph TD
    A[Usuario] -->|Interacción| B[Interfaz CustomTkinter]
    B -->|Solicitudes| C[Controlador main.py]
    C -->|ORM SQLAlchemy| D[Base de Datos SQLite]
    C -->|Lectura/Escritura| E[Modelos: Recluta]
    B -->|Datos para análisis| F[Pandas / Matplotlib / Seaborn]
    F -->|Gráficos| G[Dashboard Estadístico]
    B -->|Coordenadas geográficas| H[Folium]
    H -->|Mapa interactivo| I[HTML / Leaflet]

    subgraph "CI/CD Pipeline (GitHub Actions)"
        J[Push / PR] --> K[Linter Ruff]
        K --> L[Pytest]
        L --> M[Resultado OK]
        L --> N[Resultado FALLo]
        M --> O[Aprobación para merge]
        N --> P[Mostrar log y diagnosticar]
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333
    style I fill:#9f9,stroke:#333
```

### 2. Diagrama Entidad-Relación (Base de Datos)
```mermaid
erDiagram
    RECLUTA {
        INT id PK "Autoincremental"
        VARCHAR cedula "12, Unique, Not Null"
        VARCHAR nombre "100, Not Null"
        VARCHAR apellido "100, Not Null"
        INT edad "Not Null"
        VARCHAR direccion "200"
        VARCHAR telefono "15"
        DATE fecha_registro "Not Null"
        BOOLEAN apto "Default True"
        FLOAT estatura
        FLOAT peso
        VARCHAR observaciones "300"
    }
    PARROQUIA {
        INT id_parroquia PK "Autoincremental"
        VARCHAR nombre "50, Unique"
    }
    PARROQUIA ||--o{ RECLUTA : "pertenece"
```
### 3.Diagrama de Secuencia (Registro de Recluta)
```mermaid
sequenceDiagram
    actor Usuario
    participant GUI as Interfaz (CustomTkinter)
    participant Ctrl as recolector.py
    participant DB as SQLAlchemy / SQLite

    Usuario ->> GUI: Clic en "Registrar Recluta"
    GUI ->> GUI: Abre formulario
    Usuario ->> GUI: Completa campos y clic en "Guardar"
    GUI ->> GUI: Validación local (campos vacíos)
    
    alt Validación fallida
        GUI ->> Usuario: messagebox.showerror("Campos obligatorios")
    else Validación OK
        GUI ->> Ctrl: guardar(datos_formulario)
        Ctrl ->> DB: session.add(nuevo_recluta)
        DB -->> DB: Verifica unicidad de cédula
        
        alt Cédula duplicada
            DB -->> Ctrl: Excepción
            Ctrl ->> GUI: Error
            GUI ->> Usuario: messagebox.showerror("Cédula ya existe")
        else OK
            DB -->> Ctrl: Commit exitoso
            Ctrl ->> GUI: Éxito
            GUI ->> Usuario: messagebox.showinfo("Registrado correctamente")
        end
    end
```
### 4. Casos de uso de Sistema
```mermaid
flowchart LR
    Actor((Operador))

    subgraph "Sistema SMAC"
        UC1([Inicializar Base de Datos])
        UC2([Registrar Recluta])
        UC3([Visualizar Dashboard])
        UC4([Generar Mapa Territorial])
    end

    Actor --> UC1
    Actor --> UC2
    Actor --> UC3
    Actor --> UC4

    UC4 -. "<<include>>" .-> UC3
```
### 5. Diagrama de Flujo (Lógica de Registro)
```mermaid
flowchart TD
    A[Inicio] --> B[Clic en 'Registrar Recluta']
    B --> C[Abrir formulario]
    C --> D[Usuario completa campos]
    D --> E[Clic en 'Guardar']
    E --> F{¿Campos obligatorios\nvacios?}
    
    F -->|Sí| G[Mostrar error: Campos obligatorios]
    G --> D
    
    F -->|No| H[Crear objeto Recluta con datos]
    H --> I[Ejecutar session.add]
    I --> J{¿Cédula duplicada?}
    
    J -->|Sí| K[Mostrar error: Cédula ya existe]
    K --> D
    
    J -->|No| L[session.commit]
    L --> M[Mostrar éxito: Registro guardado]
    M --> N[Limpiar formulario]
    N --> O[Fin]
```