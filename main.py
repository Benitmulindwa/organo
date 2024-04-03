import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.bgcolor = "white"
    page.theme_mode = "light"

    def hovered(e):
        e.control.opacity = 0.7 if e.control.opacity == 1.0 else 1.0
        e.control.update()

    def display_image(e):
        result_image.content=ft.Text("Processing...")
        result_image.update()
        result_image.content = ft.Image(
            src=f"https://opsin.ch.cam.ac.uk/opsin/{mol_name.value}.png",
            error_content=ft.Text(
                "There was an error with the IUPAC name you provided",
                size=25,
                color="red",
                weight=ft.FontWeight.BOLD,
            ),
            width=200,
            height=200,
        )

        structure_name.content.value = mol_name.value
        structure_name.content.update()
        result_image.update()

    structure_name = ft.Container(
        ft.Text(size=15, weight=ft.FontWeight.W_500, selectable=True), alignment=ft.alignment.center
    )
    mol_name = ft.TextField(
        hint_text="Substance name...",
        width=300,
        height=40,
        adaptive=True,
        expand=True,
        content_padding=ft.padding.only(left=8, bottom=8),
        on_submit=display_image,
    )
    result_image = ft.Container(alignment=ft.alignment.center, margin=ft.margin.all(0))
    page.add(
        ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Image(src="logo.png", width=100, height=100),
                                        ft.Text(
                                            "ORGANO", size=35, weight=ft.FontWeight.BOLD
                                        ),
                                    ],
                                    spacing=0,
                                ),
                                ft.Text(
                                    "Convert IUPAC name to organic structure",
                                    size=13,
                                    opacity=0.7,
                                ),
                            ],
                            spacing=0,
                        ),
                        padding=ft.padding.only(bottom=10),
                    ),
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    mol_name,
                                    ft.Container(
                                        ft.Text(
                                            "Submit", size=15, weight=ft.FontWeight.BOLD
                                        ),
                                        opacity=1.0,
                                        bgcolor="#546ee5",
                                        width=60,
                                        height=40,
                                        border_radius=5,
                                        alignment=ft.alignment.center,
                                        on_hover=hovered,
                                        on_click=display_image,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Container(
                                ft.Text(
                                    "The molecule structure will be displayed down here: ",
                                    size=25,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                alignment=ft.alignment.center,
                                margin=ft.margin.only(top=5)
                            ),
                            result_image,
                            structure_name,
                        ],
                        spacing=0,
                    ),
                ],
                scroll=ft.ScrollMode.ALWAYS,
            ),
            expand=True,
            # alignment=alignment.top_right,
        ),
        ft.Divider(color="#546ee5", height=8),
        ft.Text(f"© {datetime.now().date().strftime("%Y")} by Benit MULINDWA", opacity=0.7,size=12),
    )


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
