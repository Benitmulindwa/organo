import flet as ft


def main(page: ft.Page):
    page.bgcolor = "white"
    page.theme_mode = "light"
    # page.vertical_alignment = MainAxisAlignment.CENTER

    def display_image(e):

        result_image.content = ft.Image(
            src=f"https://opsin.ch.cam.ac.uk/opsin/{mol_name.value}.png",
            error_content=ft.Text(
                "There's an error with the name you provided",
                size=25,
                weight=ft.FontWeight.BOLD,
            ),
            width=250,
            height=250,
        )
        mol_name.value = ""
        mol_name.update()
        result_image.update()

    mol_name = ft.TextField(
        width=300,
        height=40,
        adaptive=True,
        content_padding=ft.padding.only(left=8, bottom=8),
        on_submit=display_image,
    )
    result_image = ft.Container(
        ft.Text(
            "Your molecule structure will be displayed here",
            size=25,
            weight=ft.FontWeight.BOLD,
        ),
        alignment=ft.alignment.center,
    )
    page.add(
        ft.Container(
            ft.Column(
                [
                    ft.Text("ORGANO", size=35, weight=ft.FontWeight.BOLD),
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    mol_name,
                                    ft.Container(
                                        ft.Text("Submit", ft.FontWeight.BOLD),
                                        bgcolor="green",
                                        width=60,
                                        height=40,
                                        border_radius=5,
                                        alignment=ft.alignment.center,
                                        on_click=display_image,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            result_image,
                        ],
                    ),
                ],
            ),
            expand=True,
            # alignment=alignment.top_right,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
