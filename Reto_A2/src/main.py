import flet as ft

def main(page: ft.Page):
    page.title = "Reto: Decisiones Interactivas"
    page.window_width = 420
    page.window_height = 720

    estado = {"actual": "inicio"}  # cambia con tus propios estados

    titulo = ft.Text("🌟 Decisiones Interactivas", size=22, weight="bold")
    texto  = ft.Text("", size=18)
    imagen = ft.Image(src="", width=280, height=180, fit=ft.ImageFit.CONTAIN, visible=False)

    btn_si   = ft.ElevatedButton("Sí")
    btn_no   = ft.ElevatedButton("No")
    btn_reset= ft.TextButton("Reiniciar", icon=ft.Icons.REFRESH)  # ✅ corregido
    botones  = ft.Row([btn_si, btn_no], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    def mostrar_inicio():
        estado["actual"] = "inicio"
        page.bgcolor = None
        texto.value = "🤖 ¿Ayudas al robot a reciclar hoy?"
        imagen.visible = False
        btn_si.visible = True
        btn_no.visible = True
        page.update()

    def a_pregunta2_si():
        estado["actual"] = "p2_si"
        texto.value = "♻️ Tienes papel y plástico. ¿Empiezas por separar el papel?"
        imagen.visible = False
        page.update()

    def final_bueno():
        estado["actual"] = "final_bueno"
        texto.value = "✅ ¡Excelente! Separaste correctamente."
        page.bgcolor = ft.Colors.GREEN_50   # ✅ corregido
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    def final_medio():
        estado["actual"] = "final_medio"
        texto.value = "🟡 Casi… te faltó ordenar. ¡Inténtalo otra vez!"
        page.bgcolor = ft.Colors.AMBER_50   # ✅ corregido
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    def final_malo():
        estado["actual"] = "final_malo"
        texto.value = "❌ No participaste. El robot se quedó solo…"
        page.bgcolor = ft.Colors.RED_50     # ✅ corregido
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    def on_si(e):
        if estado["actual"] == "inicio":
            a_pregunta2_si()
        elif estado["actual"] == "p2_si":
            final_bueno()
        # agrega más elif para crecer tu historia

    def on_no(e):
        if estado["actual"] == "inicio":
            final_malo()
        elif estado["actual"] == "p2_si":
            final_medio()
        # agrega más elif para crecer tu historia

    def on_reset(e):
        mostrar_inicio()

    btn_si.on_click = on_si
    btn_no.on_click = on_no
    btn_reset.on_click = on_reset

    page.add(ft.Column([titulo, texto, imagen, botones, btn_reset],
                       alignment=ft.MainAxisAlignment.START,
                       horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                       spacing=16, expand=True))
    mostrar_inicio()

ft.app(target=main)
