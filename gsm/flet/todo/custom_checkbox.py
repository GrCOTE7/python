from flet import *


class CustomCheckBox(Container):
    """
    Une classe simple pour créer une case à cocher personnalisée avec un cercle rouge.
    """

    def __init__(
        self,
        color="#FF0000",  # Rouge par défaut
        stroke_width=3,
        size=25,
        checked=False,
        label="",
        pressed=None,
    ):
        # Initialiser le conteneur parent
        super().__init__()

        # Stocker les propriétés
        self.color = color
        self.stroke_width = stroke_width
        self.size = size
        self.checked = checked
        self.label = label
        self.pressed = pressed
        self.check_color = "#183588"  # Couleur quand coché

        # Créer le cercle
        self.circle = Container(
            width=self.size,
            height=self.size,
            border_radius=self.size / 2,  # Cercle parfait
            bgcolor="transparent",  # Fond transparent
            border=border.all(color=self.color, width=self.stroke_width),
            content=Container(),  # Contenu vide par défaut
            animate=300,  # Animation de 300ms
        )

        # Configurer le conteneur principal
        self.content = self.circle
        self.on_click = self.toggle
        self.tooltip = "Cliquez pour cocher/décocher"

        # Mettre à jour l'état initial
        self._update_state()

        print(
            f"CustomCheckBox créée avec couleur: {self.color}, épaisseur: {self.stroke_width}"
        )

    def _update_state(self):
        """Met à jour l'apparence selon l'état coché/décoché"""
        if self.checked:
            self.circle.bgcolor = self.check_color
            self.circle.content = Icon(Icons.CHECK, color="white", size=self.size * 0.6)
        else:
            self.circle.bgcolor = "transparent"
            self.circle.content = Container()
            # S'assurer que la bordure est visible
            self.circle.border = border.all(color=self.color, width=self.stroke_width)

    def toggle(self, e):
        """Bascule l'état coché/décoché"""
        self.checked = not self.checked
        print(f"Case à cocher basculée: {self.checked}")
        self._update_state()
        self.update()

        # Appeler le callback si fourni
        if self.pressed:
            self.pressed(self)

    def is_checked(self):
        """Renvoie l'état actuel"""
        return self.checked
