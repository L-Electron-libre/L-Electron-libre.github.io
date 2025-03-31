# NOUVELLES CLASSES CSS POUR LE STYLE DES ÉLÉMENTS DU SITE WEB.

# Étant donné que les choses ont changés, il y a eu de légères modifications bonnes pour rendre le site plus sobre pour l'utilisateur moyen, pour cette raison les classes suivantes
css ont été rajoutés pour l'instant:

    "img_opacity_transition" -> Cette classe ajoute un effet d'opacité qui transitionne sur 0.2 secondes lorsque l'utilisateur passe sa souris sur un élément qui est clickable (i.e. images)

---------------------------------------------------
Lorsque vous voudrez ajouter un effet de style parmis ceux ci-haut sur un nouvel élément vous devriez y procéder de la sorte:

    1. L'élément HTML a-t-il déjà un `class=" (...) " dans sa balise html?

        Rajoutez le nom de la classe ci-haut dedans en mettant un espace entre les autres noms de classes. Exemple:

        class="nomDeClasseDejaLa" ---> class="nomDeClasseDejaLa img_opacity_transition"     *Ainsi vous rajouterez img_opacity_transition à la classe de la balise html de l'objet.

    2. L'élément HTML ne possède pas de `class=" (...) " dans sa balise html?

        Vous n'avez qu'à la créer! Exemple:`

        <div> Salut </div> ---> <div class="img_opacity_transition"> Salut </div>           *Ainsi vous rajouterez cette classe à la balise html de l'objet, dorénavant, ajouter une autre classe demandera de faire comme à l'étape 1.
---------------------------------------------------

