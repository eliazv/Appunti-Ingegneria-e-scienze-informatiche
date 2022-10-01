<!--APPUNTI-->

<!-- 
  MySQL Connect : connesione db
  PHP MySqli: prendere result
  MySQL Prepared : bind params
  PHP String: funzioni su stringhe
  PHP variable Handing: funzioni generiche
  PHP Math: funzioni numeriche
  PHP loops: for
  PHP array: array func (print_r stampa, si trova in PHP handling)
  




  //IMPARA
  $result = $stmt->get_result()->fetch_all(MYSQLI_ASSOC)[0]["attributo"]; 

  $result = $stmt->get_result(); 
  $stmt->close();
  $db->close();
  return $result->fetch_all(MYSQLI_ASSOC); 
-->



<?php
  setcookie("notizie", $_POST["notizie"], time() + 3600);
  //query insert o update
  function insertQuadro($titolo, $codQuadro){
      $stmt = $this->db->prepare($query);
      $stmt->bind_param('ssssdsiii', $titolo, $codQuadro);
      $stmt->execute();
      //fosse get
      return  $stmt->get_result()->fetch_all(MYSQLI_ASSOC)[0]["attributo"]; 
  }

//funzioni sul DB
function readNumberss($soglia){
  //connessione DB
  $db = new mysqli("localhost", "root", "", "nomedb", 3307);
  if ($db->connect_error) {
      die("Connection failed: " . $db->connect_error);
  }

  $stmt = $db->prepare("SELECT id, numero FROM numeri  WHERE numero > ?");
  $stmt->bind_param("i", $soglia);
  $stmt->execute();
  $result = $stmt->get_result(); //IMPARA

  $stmt->close();
  $db->close();
  return $result->fetch_all(MYSQLI_ASSOC); //IMPARA
}
if(isset($_POST["soglia"]) && $_POST["soglia"] > 0){  //controlli sui valori
  //filter_var($_POST["email"], FILTER_VALIDATE_EMAIL) // email, controlla se il pattern è di una email
  //(is_numeric($_POST["contact"]) || strlen($_POST["contact"]) != 10

  //mettere tutti i risultati di una query in un array
  $numbersAssoc = readNumberss($_POST["soglia"]);
  $numbers = array();
  foreach($numbersAssoc as $n){
    array_push($numbers, $n["numero"]); //(destinaz, elemento["attributo"])
  }

}
$output = json_encode($numbers); //converte in array JSON







?>







<!-- --------------------------------------------------------------------------------------------------------------------------------------  -->


<!-- 18-07-06 -->
<?php

function readNumbers($soglia){
    $db = new mysqli("localhost", "root", "", "luglio", 3307);

    if ($db->connect_error) {
        die("Connection failed: " . $db->connect_error);
    }

    $stmt = $db->prepare("SELECT id, numero
                            FROM numeri
                            WHERE numero > ?");
    $stmt->bind_param("i", $soglia);
    $stmt->execute();
    $result = $stmt->get_result();

    $stmt->close();
    $db->close();
    return $result->fetch_all(MYSQLI_ASSOC);
}

$_POST["soglia"] = 30;

if(isset($_POST["soglia"]) && $_POST["soglia"] > 0){
    $numbersAssoc = readNumbers($_POST["soglia"]);
    
    $numbers = array();
    foreach($numbersAssoc as $n){
        array_push($numbers, $n["numero"]); //Numero??
    }

    for($i=1; $i<count($numbers); $i++){
        for($j=$i-1; $j >= 0; $j--){
            if($numbers[$j] > $numbers[$i]){
                $tmp = $numbers[$j];
                $numbers[$j] = $numbers[$i];
                $numbers[$i] = $tmp;
            }
        }
    }
    
    $output = json_encode($numbers);

    var_dump($output);
}

?>







<!--20-02-21-->
<!--1-->
<?php
  if(isset($_POST["remember"])){ //controlla se è stato premuto
    setcookie("username", $_POST["username"], time() + 3600); //nome, valore, tempo validità (cookie valido per 60 minuti)
    setcookie("notizie", $_POST["notizie"], time() + 3600);
  }
?>

<html lang="it">
  <head>
    <title>Esercizio PHP</title>
  </head>
  <body>
    <div class="header">
      <a  class="home">Esercizio PHP</a>
      <div class="products">
        <a href="index.php">Homepage</a>
        <a href="settings.php">Settings</a>
      </div>
    </div>

    <form action="settings.php" method="post" style="border: 2px dotted blue; text-align:center; width: 400px;">
	   <p>
		     <label for="username">Username </label><input name="username" type="text" value="<?php if(isset($_COOKIE["username"])){echo $_COOKIE["username"];}?>" >
	   </p>
     <p>
       <label for="notizie">Categoria notizie:</label>
       <select name="notizie">
         <option value="">--------</option>
          <option value="politica" <?php if(isset($_COOKIE["notizie"]) && $_COOKIE["notizie"] =="politica"){echo "selected";}?>>Politica</option> <!--se notizie settato e con val politica, seleziona questa opzione-->
          <option value="attualità" <?php if(isset($_COOKIE["notizie"]) && $_COOKIE["notizie"] =="attualità"){echo "selected";}?>>Attualità</option>
          <option value="sport" <?php if(isset($_COOKIE["notizie"]) && $_COOKIE["notizie"] =="sport"){echo "selected";}?> >Sport</option>
          <option value="scienze" <?php if(isset($_COOKIE["notizie"]) && $_COOKIE["notizie"] =="scienze"){echo "selected";}?> >Scienze</option>
        </select>
	   </p>
		 <p>
      <input type="checkbox" name="remember" /> Remember me
	   </p>
		<p>
      <input type="submit" value="submit"></input>
    </p>
    </form>

  </body>
</html>


<!--2-->
<?php
  function getArticles($category){  //funzione database
    $db = new mysqli("localhost", "root", "", "febbraio", 3307);  //connessione al server xamp

    // Check connection
    if ($db->connect_error) {
      die("Connection failed: " . $db->connect_error);
    }

    //DA IMPARARE A MEMORIA
    if($category == "all"){ //prende tutte
      $stmt = $db->prepare("SELECT titolo, descrizione, categoria
                            FROM articoli");
    }else{ //prende una
      $stmt = $db->prepare("SELECT titolo, descrizione, categoria
                            FROM articoli
                            WHERE categoria = ?");
      $stmt->bind_param("s", $category);  
    }
    
    $stmt->execute();
    $result = $stmt->get_result();
    return $result->fetch_all(MYSQLI_ASSOC);  
  }
?>

<html lang="it">
  <head>
    <title>Esercizio PHP</title>
  </head>
  <body>
    <div class="header">
      <a  class="home">Esercizio PHP</a>
      <div class="products">
        <a href="index.php">Homepage</a>
        <a href="settings.php">Settings</a>
      </div>
    </div>
    <article>
      <?php 
        if(isset($_COOKIE["notizie"])){
          $category = $_COOKIE["notizie"];
        }else{
          $category = "all";
        }
      ?>
      <?php foreach(getArticles($category) as $article):?> 
        <div>
          <h1><?php echo $article["titolo"]?></h1>
          <p><?php echo $article["descrizione"]?></p>
        </div>
      <?php endforeach;?>
    </article>
  </body>
</html>






<!--20-01-29-->
<!--1-->

<!DOCTYPE HTML>
<html>
 <head>
   <title>Scegli la tua nuova automobile</title>
 </head>
 <body>
   <div class="container">
     <div class="main">
     <h2>Dati personali</h2>
     <?php session_start();?> <!--inizia sessione-->
     <span id="error">
       <?php 
        if(isset($_GET["msg1"])){ //controlla se c'è un errore, quindi se la variabile msg1 è settata
          session_destroy(); //distrugge la sessione
          echo $_GET["msg1"];
          session_start();
        }else{
          echo "";
        }?>
     </span>
       <form action="page2.php" method="post"><br />
         <label>Nome e Cognome :<span>*</span></label><br />
         <input name="nome" type="text" placeholder="Thomas A. Anderson"><br />
         <label>Email:<span>*</span></label><br />
         <input name="email" type="email" placeholder="neo@matrix.com"><br />
         <label>#Tel:<span>*</span></label><br />
         <input name="contact" type="text" placeholder="10 caratteri numerici"><br />
         <input type="reset" value="Reset" />
         <input type="submit" value="Next" />
       </form>
     </div>
   </div>
 </body>
</html>


<!--2-->
<?php 
  session_start();
  if($_POST["nome"]=="" || $_POST["email"]=="" || $_POST["contact"]==""){  //controlla che i campi non siano vuoti
    header("location: index.php?msg1=Campi del primo form vuoti."); //se vuoti reindirizza a pagina precedente e da errore settando msg1
    return;
  }

  if (!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) { //"sanitizza" il campo email, controlla se il pattern è di una email
    header("location: index.php?msg1=Email errata.");
    return;
  }

  if(!is_numeric($_POST["contact"]) || strlen($_POST["contact"]) != 10){ //"sanitizza" il campo contatto, controlla se contatto è numerico e che abbia 10 caratteri
    header("location: index.php?msg1=Numero di telefono errato.");
    return;
  }

  else{ //sa va tutto bene
    $_SESSION["post"] = array($_POST["nome"], $_POST["email"], $_POST["contact"]); //salvo i dati su session post
  }
?>
<!DOCTYPE HTML>
<html>
 <head>
   <title>Scegli la tua nuova automobile</title>
 </head>
 <body>
   <div class="container">
     <div class="main">
       <h2>Allestimento</h2>
       <hr/>
       <span id="error">
        <?php 
          if(isset($_GET["msg2"])){
            session_destroy();
            echo $_GET["msg2"];
          }else{
            echo "";
          }?>
       </span>
       <form action="page3.php" method="post">
         <label>Modello :<span>*</span></label><br />
         <input name="modello" id="modello" type="text" value=""><br />
         <label>Versione :<span>*</span></label><br />
         <input name="versione" id="versione" type="text" value=""><br />
         <label>Motore :<span>*</span></label><br />
         <select name="motore"><br />
           <option value="">----Select----</options>
           <option value="1.0">1.0 VVT-i (72 CV) 5 Marce Manuale</option>
           <option value="1.5hyb">1.5 Hybrid (100 CV) E-CVT</option>
           <option value="1.5">1.5 VVT-iE (111 CV) 6 Marce Manuale</option>
           <option value="1.6">1.6 VVT-iE (131 CV) 6 Marce Manuale</option>
         </select><br />
         <label>Colore :<span>*</span></label><br />
         <select name="colore">
           <option value="">----Select----</option>
           <option value="rosso">rosso</option>
           <option value="nero">nero</option>
           <option value="giallo">giallo</option>
           <option value="verde">verde</option>
           <option value="blu">blu</option>
         </select><br />
        <input type="reset" value="Reset" />
        <input type="submit" value="Next" />
       </form>
     </div>
   </div>
 </body>
</html>

<!--3-->
<?php
session_start();
if($_POST["modello"]=="" || $_POST["versione"]=="" || $_POST["motore"]=="" || $_POST["colore"]==""){ // controlla che i campi non siano vuoti
  header("location: page2.php?msg2=Campi del secondo form vuoti.");
  return;
}
else{
  var_dump($_SESSION);
  array_push($_SESSION["post"], $_POST["modello"],$_POST["versione"],$_POST["motore"],$_POST["colore"]); //primo elemento è il vettore, gli altri sono gli elemnti da aggiungere in coda. 
                                                                                                            //Salvo altri elementi nella variabile
}
?>
<!DOCTYPE HTML>
<html>
 <head>
   <title>Scegli la tua nuova automobile</title>
 </head>
 <body>
   <div class="container">
     <div class="main">
       <h2>Optional & accessori</h2><hr/>
       <span id="error">
       </span>
       <form action="page4.php" method="post">
         <label>Cruise control:</label><br />
         <input name="cruise" id="cruise" type="checkbox"><br />
         <label>Barre portatutto:</label><br />
         <input name="portatutto" id="portatutto" type="checkbox"><br />
         <label>Radio bluetooth:</label><br />
         <input name="bluetooth" id="bluetooth" type="checkbox"><br />
         <label>Allarme:</label><br />
         <input name="allarme" id="allarme" type="checkbox"><br />
         <input type="reset" value="Reset" />
         <input name="submit" type="submit" value="Submit" />
       </form>
     </div>
   </div>
 </body>
</html>


<!--4-->
<?php
session_start();
var_dump($_SESSION);

if(isset($_POST["cruise"])){
  array_push($_SESSION["post"], "cruise");
}
if(isset($_POST["portatutto"])){
  array_push($_SESSION["post"], "portatutto");
}
if(isset($_POST["bluetooth"])){
  array_push($_SESSION["post"], "bluetooth");
}
if(isset($_POST["allarme"])){
  array_push($_SESSION["post"], "allarme");
}
?>
<!DOCTYPE HTML>
<html>
 <head>
   <title>Scegli la tua nuova automobile</title>
 </head>
 <body>
   <div class="container">
     <div class="main">
       <h2>Visualizza la tua scelta in formato JSON</h2>
       <?php 
        foreach($_SESSION["post"] as $scelta){ //scorro l'array per stampare tutte le scelte fatte
          echo "<p>$scelta</p>"; //ogni scelta in un p
        }
       ?>
	 </div>
   </div>
 </body>
</html>
<?php session_destroy();?>















<!--19-02-01      booh incomprensibile--> 
<?php

function checkCinquina($numeri, $input){
  $inputNumeri = explode('-', $input); //rompe la striga dentro un array, "-" separatore, input è la striga da rompere
  if(count($inputNumeri) != 5) {//se ci sono più di 5 lementi errore
    return false;
  }

  foreach($inputNumeri as $numero){
    if(!is_numeric($numero) || !isset($numeri[$numero])){ // questo check riassume tutti i check richiesti sull'input dei numeri, numerici e settati
      return false;
    }
  }
  return true;
}

function aggiungiNumero($db, $numeri) {
  if(count($numeri) >= 90){
    return;
  }
  $nuovo = "".rand(1, 90);
  do {
    $nuovo = "".rand(1, 90);
  } while(isset($numeri[$nuovo]));

  $db->exec('INSERT INTO partita(numero) VALUES (' . $nuovo . ')');
}

if(isset($_GET['bingo']) && !empty($_GET['bingo']) && ($_GET['bingo'] === 'cinquina' || $_GET['bingo'] === 'bingo')){
try {
  $db = new PDO('mysql:host=127.0.0.1;dbname=bingo', 'root', '');
  $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

  $numeri = [];
  $records = $db->query('SELECT numero FROM partita')->fetchAll();
  foreach($records as $record){
    $numeri[$record['numero']] = $record['numero'];
  }

  if($_GET['bingo'] === 'cinquina') {
    if(count($numeri) < 5){
      echo 'non è ancora possibile fare cinquina';
      aggiungiNumero($db, $numeri);
    } else {
      if(checkCinquina($numeri, $_GET['bingo_row1']) || checkCinquina($numeri, $_GET['bingo_row2']) || checkCinquina($numeri, $_GET['bingo_row3'])) {
        echo 'Hai fatto cinquina';
      } else {
        aggiungiNumero($db, $numeri);
      }
    }
  } else if($_GET['bingo'] === 'bingo') {
    if(count($numeri) < 15){
      echo 'non è ancora possibile fare bingo';
      aggiungiNumero($db, $numeri);
    } else {
      if(checkCinquina($numeri, $_GET['bingo_row1']) && checkCinquina($numeri, $_GET['bingo_row2']) && checkCinquina($numeri, $_GET['bingo_row3'])) {
        echo 'Hai fatto bingo';
      } else {
        aggiungiNumero($db, $numeri);
      }
    }
  }

}catch(PDOException $e) {
  echo 'errore pdo ' . $e->getMessage();
}
}
?>

 <!DOCTYPE html>
 <html>
   <head>
     <title>Bingo</title>
   </head>
   <body>
     <h1>Esercizio PHP</h1>
     <div>
       <form action="index.php">
         <h2>Bingo</h2>
         <section id="numbers">
          <label for="bingo_row1">
            Riga1: <input type="text" id="bingo_row1" name="bingo_row1">
          </label>
          <label for="bingo_row2">
            Riga2: <input type="text" id="bingo_row2" name="bingo_row2">
          </label>
          <label for="bingo_row3">
            Riga3: <input type="text" id="bingo_row3" name="bingo_row3">
          </label>
         </section>
         <section id="control">
           <input type="radio" name="bingo" value="cinquina">Controlla cinquina<br>
           <input type="radio" name="bingo" value="bingo">Controlla bingo<br>
        </section>
        <input type="submit" value="submit">
        </form>
     </div>
   </body>
 </html>








 <!--18-09-18-->
 <?php

class Hamming{ //classe

    public function isValid($str1,$str2){
        if(strlen($str1) != strlen($str2)){
            return false;
        }
        return true;
    }

    public function distance($str1,$str2){
        $str1Split = str_split($str1);
        $str2Split = str_split($str2);

        $distance = "";
        for($i = 0; $i<count($str1Split); $i++){
            if($str1Split[$i] == $str2Split[$i]){
                $distance = $distance."0";
            }else{
                $distance = $distance."1";
            }
        }
        return $distance;
    }

    public function weight($str){
        $strSplit = str_split($str);
        $weight = 0;
        for($i = 0; $i<count($strSplit); $i++){
            if($strSplit[$i] != 0){
                $weight++;
            }
        }
        return $weight;
    }
}


function getStrings(){
    $db = new mysqli("localhost", "root", "", "settembre", 3307);  //crea connessione

    if ($db->connect_error) {
        die("Connection failed: " . $db->connect_error);
    }

    $stmt = $db->prepare("SELECT id, stringa
                          FROM stringhe");

    $stmt->execute();
    $result = $stmt->get_result();

    $stmt->close();
    $db->close();
    return $result->fetch_all(MYSQLI_ASSOC);
}

$stringsAssoc = getStrings();

$strings = array();
foreach($stringsAssoc as $string){
    array_push($strings, $string["stringa"]);
}

$cognome="Ventu";
$hamming = new Hamming();

$output = array();
foreach($strings as $string){
    if($hamming->isValid($cognome, $string)){
        $distance = $hamming->distance($cognome, $string);
        $weight = $hamming->weight($distance);
        $output[$string] = array($distance, $weight);
    }
}

$jsonOutput = json_encode($output);

echo $jsonOutput;
?>

