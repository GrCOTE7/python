# Flet -CheatSheet des propriétés (SafeArea, Container, Row, Column, Stack)

## Légende
- Oui : propriété directement sur le contrôle
- Indirect : possible via un parent/enfant (souvent Container)
- Non : pas prévu sur ce contrôle

## Tableau synthétique

| Contrôle | bgcolor | border | width / height | padding | margin | alignment | expand | spacing | scroll | top/left/right/bottom |
|---|---|---|---|---|---|---|---|---|---|---|
| SafeArea | Indirect | Indirect | Indirect | Oui (minimum_padding) | Non | Non | Indirect | Non | Non | Non |
| Container | Oui | Oui | Oui | Oui | Oui | Oui | Oui | Non | Non | Non |
| Row | Indirect | Indirect | Oui | Non | Non | Oui (alignement des enfants) | Oui | Oui | Oui | Non |
| Column | Indirect | Indirect | Oui | Non | Non | Oui (alignement des enfants) | Oui | Oui | Oui | Non |
| Stack | Indirect | Indirect | Oui | Non | Non | Oui | Oui | Non | Non | Oui (sur les enfants du Stack) |

## Propriétés clés par contrôle

### SafeArea
- Sert à éviter les zones système (encoche, barres)
- Propriété utile : minimum_padding
- Pour le style visuel (fond, bordure), envelopper avec un Container

### Container
- Contrôle de style principal
- Accepte notamment : bgcolor, border, border_radius, padding, margin, width, height, alignment, shadow, gradient
- Le plus pratique pour habiller un bloc

### Row
- Dispose les enfants horizontalement
- Accepte notamment : controls, alignment, vertical_alignment, spacing, wrap, run_spacing, scroll
- Pour colorer/faire une bordure : mettre Row dans un Container

### Column
- Dispose les enfants verticalement
- Accepte notamment : controls, alignment, horizontal_alignment, spacing, scroll
- Pour colorer/faire une bordure : mettre Column dans un Container

### Stack
- Superpose des enfants
- Accepte notamment : controls, fit, clip_behavior, alignment
- Le positionnement absolu se fait sur les enfants (top, left, right, bottom)

## Règle pratique (à retenir)
- Mise en page : Row / Column / Stack / SafeArea
- Habillage visuel : Container

## Pattern recommandé

SafeArea  
-> Container (bgcolor, border, padding, etc.)  
-> Row ou Column ou Stack

## Mini exemples

### Row stylée (via Container)

    ft.Container(
        bgcolor=ft.Colors.BLUE_GREY_50,
        border=ft.border.all(1, ft.Colors.BLUE_GREY_200),
        padding=10,
        content=ft.Row(
            spacing=8,
            controls=[...],
        ),
    )

### Column scrollable

    ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        controls=[...],
    )

### Stack avec position absolue

    ft.Stack(
        width=300,
        height=200,
        controls=[
            ft.Container(width=300, height=200, bgcolor=ft.Colors.BLUE_100),
            ft.Container(width=80, height=80, bgcolor=ft.Colors.RED_200, top=20, left=20),
        ],
    )
