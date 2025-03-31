<!--
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<h1>Informations saisies</h1>
<?php
   // Vérifier si le formulaire est soumis
   if ( isset( $_POST['submit'] ) ) {
     /* récupérer les données du formulaire en utilisant
        la valeur des attributs name comme clé
       */
     $email = $_POST['email'];

     // afficher le résultat
     echo '<h3>Informations récupérées en utilisant POST</h3>';
     echo 'Email : ' .$email;
     exit;
  }
?>

</body>
</html>
-->
