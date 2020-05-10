# journal_electron_libre

#Syntaxe général du HTML dans les fichiers
Au lieu d'utiliser { } pour fermer un segment de code, on utilise plutôt pour ouvrir <> et fermer </>. 
On commence en général par séparé notre page en différentes section que l'on nomme avec la commande 
:	<section id="One" class="wrapper style3">, la classe wrapper style3 ? à déterminé.
  
Afin d'écrire dans le fichier, il y a différente manière de le faire. Pour créer un titre on utilise la fonction <header>,
il existe 5 types de header qui vont fonctionner avec tous les navigateurs de différentes grandeurs.
On peut y accéder avec : <h1> - <h5>, en les fermant et ouvrant avec la manière décrite précédemment.
On peut alors écrire des paragraphes en utilisant <p> </p>. 


#Syntaxe pour insérer un lien dans une page HTML

#Procédure pour ajouter des images et du texte aux différentes pages
Dans le template qui a été importé en css style file,dans la classe .image on peut regarder toutes 
les caractéristiques que l'on veut appliquer à l'image. 
Par caractéristique, on veut dire taille de l'image, position dans le site web.Pour choisir la classe que l'on veut,
On doit respecter la syntaxe suivante :

<div class="image.image.right"> où (image.right) est la sous-classe de image. 

On peut alors insérer l'image avec la ligne suivante :
<img src="images/we_want_you.jpg" alt="Fiche de recrutement" style="width:300px;height:400px"> 
où we_want_you.jpg est une image ajouté sur github au dossier images. 
  
Alt: représente le mot qui s'affichera si la vitesse de l'internet n'est pas assez grande pour téléchargé l'image.
Style: défini la taille de l'image en nombre de pixel, la position de l'image étant définie par notre classe image.right.
On doit ensuite refermé la classe div à moins que l'on veut ajouter d'autres images à la suite de l'autre. 
Pour ce faire on ajoute simplement la commande : </div>

La majorité de tout ce qui est dit est tiré de ce site web: https://www.w3schools.com/tags/default.asp



