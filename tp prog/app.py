import flet as ft

def main(page):
    tasks = []
    selected_index = None  # Variable para rastrear el índice seleccionado

    def add_clicked(e):
        if new_task.value:
            tasks.append(new_task.value)
            update_task_list()
            new_task.value = ""
            new_task.focus()
            new_task.update()

    def modify_clicked(e):
        if selected_index is not None and new_task.value:
            tasks[selected_index] = new_task.value  # Modificar la tarea en la posición seleccionada
            update_task_list()
            new_task.value = ""
            new_task.focus()
            new_task.update()

    def delete_clicked(e):
        nonlocal selected_index
        if selected_index is not None:
            tasks.pop(selected_index)  # Eliminar la tarea seleccionada
            selected_index = None  # Reiniciar el índice seleccionado
            update_task_list()
            new_task.value = ""  # Limpiar el campo de texto después de eliminar
            new_task.update()

    def update_task_list():
        task_list.controls.clear()
        for i, task in enumerate(tasks):
            checkbox = ft.Checkbox(label=task, value=False)
            checkbox.on_change = lambda e, index=i: task_list_select(index)
            task_list.controls.append(checkbox)
        task_list.update()

    def task_list_select(index):
        nonlocal selected_index
        selected_index = index  # Actualizar el índice seleccionado
        new_task.value = tasks[selected_index]  # Llenar el campo de texto con la tarea seleccionada
        new_task.update()

    new_task = ft.TextField(hint_text="¿Qué ingredientes desea?", width=400)

    logo = ft.Image(src="img/R.jpg", width=500, height=500)
    header_text = ft.Text("Bienvenido al Crustaseooo", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)
    header = ft.Column(
        controls=[logo, header_text],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    task_list = ft.Column()  

    page.add(
        ft.Column(
            controls=[
                header,
                ft.Divider(height=20),
                ft.Row(
                    controls=[new_task, ft.ElevatedButton("+", on_click=add_clicked, bgcolor=ft.colors.BLUE_600, color=ft.colors.WHITE)],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Modificar", on_click=modify_clicked, bgcolor=ft.colors.GREEN_600, color=ft.colors.WHITE),
                        ft.ElevatedButton("Eliminar", on_click=delete_clicked, bgcolor=ft.colors.RED_600, color=ft.colors.WHITE)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                task_list
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    #  amarillo claro
    page.bgcolor = ft.colors.PINK_100

    # tamaño de la página
    page.window_width = 600
    page.window_height = 400
    page.update()

    # Cambiar color de los textos en la lista de tareas a negro
    for control in task_list.controls:
        control.label.color = ft.colors.BLACK

ft.app(main)


