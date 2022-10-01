<?php
class DatabaseHelper{
    private $db;

    public function __construct($servername, $username, $password, $dbname, $port){
        $this->db = new mysqli($servername, $username, $password, $dbname, $port);
        if ($this->db->connect_error) {
            die("Connection failed: " . $db->connect_error);
        }        
    }

    //TUTTI I QUADRI (quadri.html)
    public function getQuadri(){
        $query = "SELECT * FROM quadro WHERE eliminato=0";
        $stmt = $this->db->prepare($query);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getQuadriNonEliminati(){
        $query = "SELECT * FROM quadro WHERE eliminato=0";
        $stmt = $this->db->prepare($query);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    //TUTTI GLI ARTISTI (artisti.html)
    public function getArtisti(){
        $query = "SELECT * FROM artista";
        $stmt = $this->db->prepare($query);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    //TUTTE LE CATEGORIE (categorie.html)
    public function getCategories(){
        $stmt = $this->db->prepare("SELECT * FROM correnteartistica");
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getAdmins(){
        $stmt = $this->db->prepare("SELECT * FROM utente WHERE venditore=1");
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }


    //N QUADRI RANDOM (home.html)
    public function getRandomQuadri($n){
        $stmt = $this->db->prepare("SELECT titolo, immagine, artista FROM quadro WHERE eliminato=0 ORDER BY RAND() LIMIT ?");
        $stmt->bind_param('i',$n);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

     //N ARTISTI RANDOM (home.html)
     public function getRandomArtisti($n){
        $stmt = $this->db->prepare("SELECT nome, cognome, immagine FROM artista ORDER BY RAND() LIMIT ?");
        $stmt->bind_param('i',$n);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

         //N ARTISTI RANDOM (home.html)
    public function getRandomCategorie($n){
        $stmt = $this->db->prepare("SELECT nomeCorrArt, immagine FROM correnteartistica ORDER BY RAND() LIMIT ?");
        $stmt->bind_param('i',$n);
        $stmt->execute();
        $result = $stmt->get_result();
    
        return $result->fetch_all(MYSQLI_ASSOC);
    }

    //TUTTE LE INFO DEL QUADRO DAL TITOLO (quadro.html)
    public function getQuadroByTitolo($id){
        $query = "SELECT * FROM quadro WHERE titolo=?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$id);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getQuadritByCategoria($categoryName){
        $query = "SELECT titolo, immagine, dimensione, artista, prezzo, nomeCorrArt FROM quadro WHERE nomeCorrArt = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$categoryName);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getQuadriByArtista($artista){
        $query = "SELECT titolo, immagine, dimensione, artista, prezzo, nomeCorrArt FROM quadro WHERE artista = ? AND eliminato=0";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$artista);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    //tutti i quadri di un carrello specifico
    public function getCarrello($email){
        $query = "SELECT titolo, quantita FROM carrello WHERE email = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }


    public function getNumberOfPortrait($email){
        $query = "SELECT COUNT(codCarrello) as numquadri FROM carrello WHERE email = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getQuadroInCarrello($email, $titolo){
        $query = "SELECT quantita FROM carrello WHERE email = ? AND titolo=?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ss',$email, $titolo);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function updateQuantitaInCarrello($email, $titolo, $quantita){
        $query ="UPDATE carrello SET quantita=? WHERE email=? AND titolo=?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('iss',$quantita, $email, $titolo);
        $stmt->execute();
        //$result = $stmt->get_result();

        //return $stmt->execute();
    }

    public function getUtente($email){
        $query = "SELECT * FROM utente WHERE email = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getArtista($cognome){
        $query = "SELECT * FROM artista WHERE cognome = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$cognome);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }


       //TUTTE LE NOTIFICHE
    public function getNotifiche($email){
        $query ="SELECT * FROM notifica WHERE email=?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getNotifica($codNotifica){
        $query ="SELECT * FROM notifica WHERE codNotifica=?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$codNotifica);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getOrders($email){
        $query ="SELECT quadro_ordinato.titoloQuaOrd, quadro_ordinato.quantita, quadro.immagine, quadro.prezzo, ordine.dataOrdine, ordine.dataConsegna FROM quadro_ordinato, quadro, utente, ordine WHERE quadro_ordinato.titoloQuaOrd = quadro.titolo AND quadro_ordinato.codOrdine = ordine.codOrdine AND ordine.email = utente.email AND ordine.arrivato = 0 AND utente.email = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getSpecificOrders($email, $codOrdine){
        $query ="SELECT quadro_ordinato.titoloQuaOrd, quadro_ordinato.quantita, quadro.immagine, quadro.prezzo, ordine.dataOrdine, ordine.dataConsegna FROM quadro_ordinato, quadro, utente, ordine WHERE quadro_ordinato.titoloQuaOrd = quadro.titolo AND quadro_ordinato.codOrdine = ordine.codOrdine AND ordine.email = utente.email AND utente.email = ? AND ordine.codOrdine = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('si',$email, $codOrdine);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getAllOrders(){
        $query ="SELECT * From ordine, utente where ordine.email = utente.email ORDER BY codOrdine DESC";
        $stmt = $this->db->prepare($query);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getAllOrdersFromUser($email){
        $query ="SELECT * From ordine WHERE email = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getShipOrdersFromUser($email){
        $query ="SELECT * From ordine WHERE email = ? AND arrivato = 0";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getDeliveredOrders($email){
        $query ="SELECT quadro_ordinato.titoloQuaOrd, quadro_ordinato.quantita, quadro.immagine, quadro.prezzo, ordine.dataOrdine, ordine.dataConsegna FROM quadro_ordinato, quadro, utente, ordine WHERE quadro_ordinato.titoloQuaOrd = quadro.titolo AND quadro_ordinato.codOrdine = ordine.codOrdine AND ordine.email = utente.email AND ordine.arrivato = 1 AND utente.email = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getSpecifiedPaintingFromOrders($email, $titoloquadro){
        $query ="SELECT quadro_ordinato.titoloQuaOrd, quadro_ordinato.codOrdine, quadro_ordinato.quantita, quadro.immagine, quadro.prezzo, ordine.dataOrdine, ordine.dataConsegna FROM quadro_ordinato, quadro, utente, ordine WHERE quadro_ordinato.titoloQuaOrd = quadro.titolo AND quadro_ordinato.codOrdine = ordine.codOrdine AND ordine.email = utente.email AND ordine.arrivato = 0 AND utente.email = ? AND quadro_ordinato.titoloQuaOrd = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ss',$email, $titoloquadro);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getSpecificCategory($category){
        $query = "SELECT * FROM correnteartistica WHERE nomeCorrArt = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$category);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    
    public function insertQuadro($titolo, $immagine, $dimensione, $artista, $prezzo, $nomeCorrArt, $quantita, $eliminato, $codQuadro){
        $query= "INSERT INTO quadro(titolo, immagine, dimensione, artista, prezzo, nomeCorrArt, quantita, eliminato, codQuadro) VALUES (?,?,?,?,?,?,?,?,?)";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ssssdsiii', $titolo, $immagine, $dimensione, $artista, $prezzo, $nomeCorrArt, $quantita, $eliminato, $codQuadro);
        $stmt->execute();
    }

    public function insertArtista($cognome, $nome, $immagine, $descrizione){
        $query= "INSERT INTO artista(cognome, nome, immagine, descrizione) VALUES (?,?,?,?)";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ssss', $cognome, $nome, $immagine, $descrizione);
        $stmt->execute();
    }

    public function insertCategoria($nome, $immagine, $descrizione){
        $query= "INSERT INTO correnteartistica(nomeCorrArt, immagine, descrizione) VALUES (?,?,?)";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('sss', $nome, $immagine, $descrizione);
        $stmt->execute();
    }

    public function insertInCarrello($email, $titolo, $quantita){
        $query= "INSERT INTO carrello(email, titolo, quantita) VALUES (?,?,?)";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ssi', $email, $titolo, $quantita);
        $stmt->execute();
    }

    public function insertUser($email, $password, $nome, $cognome, $venditore, $indirizzo, $città, $paese, $cap){
        $query= "INSERT INTO utente(email, passwordd, nome, cognome, venditore, indirizzo, citta, paese, cap) VALUES (?,?,?,?,?,?,?,?,?)";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ssssisssi', $email, $password, $nome, $cognome, $venditore, $indirizzo, $città, $paese, $cap);
        $stmt->execute();
    }

    public function insertNotifica($titolo, $testo, $link, $dataeora, $visualizzato, $email){
        $query= "INSERT INTO notifica(titolo, testo, link, dataeora, visualizzato, email) VALUES (?,?,?,?,?,?)";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ssssis', $titolo, $testo, $link, $dataeora, $visualizzato, $email);
        $stmt->execute();
    }

    public function checkLogin($email, $password){
        $query = "SELECT email, cognome FROM utente WHERE email = ? AND passwordd = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ss',$email, $password);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }    

    public function countNotifiche($email){
        $query ="SELECT COUNT(*) AS num FROM notifica WHERE email=? AND visualizzato = 0";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s',$email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function statoNotifica($codNotifica){
        $stmt = $this->db->prepare("SELECT Visualizzato FROM Notifica  WHERE codNotifica = ?");
        $stmt->bind_param("i",$codNotifica);
        $stmt->execute();
        $result = $stmt->get_result();
        return $result->fetch_all(MYSQLI_ASSOC)[0]["Visualizzato"];
    }

    public function leggiNotifica($codNotifica){
        $query ="UPDATE notifica SET visualizzato=1 WHERE codNotifica=?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('i', $codNotifica);
        $stmt->execute();
        $result = $stmt->get_result();

        return $stmt->execute();
    }

    public function leggiTutteNotifiche($email){
        $query ="UPDATE notifica SET visualizzato=1 where email=? AND visualizzato=0";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s', $email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $stmt->execute();
    }

    public function updateIndirizzo($email, $indirizzo){
        $query ="UPDATE utente SET indirizzo=? WHERE email=?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ss', $indirizzo, $email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $stmt->execute();
    }

    public function updateCitta($email, $citta){
        $query ="UPDATE utente SET citta=? WHERE email=?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ss', $citta, $email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $stmt->execute();
    }

    public function updatePaese($email, $paese){
        $query ="UPDATE utente SET paese=? WHERE email=?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ss', $paese, $email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $stmt->execute();
    }
    
    public function updateCap($email, $cap){
        $query ="UPDATE utente SET cap=? WHERE email=?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('is', $cap, $email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $stmt->execute();
    }

    public function updatePassword($email, $password){
        $query ="UPDATE utente SET passwordd=? WHERE email=?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ss', $password, $email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $stmt->execute();
    }

    public function deleteCart($email){
        $query ="DELETE FROM carrello WHERE email = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('s', $email);
        $stmt->execute();
    }

    public function deletePaintingInCart($email, $titolo){
        $query ="DELETE FROM carrello WHERE email = ? AND titolo = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('ss', $email, $titolo);
        $stmt->execute();
    }

    public function insertOrder($email, $dataOrdine, $dataConsegna, $arrivato, $importo){
        $query= "INSERT INTO ordine(email, dataOrdine, dataConsegna, arrivato, importo) VALUES (?,?,?,?,?)";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('sssid', $email, $dataOrdine, $dataConsegna, $arrivato, $importo);
        $stmt->execute();
    }

    public function insertOrderedPainting($codOrdine, $titoloQuaOrd, $quantita){
        $query= "INSERT INTO quadro_ordinato(codOrdine, titoloQuaOrd, quantita) VALUES (?,?,?)";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param('isi', $codOrdine, $titoloQuaOrd, $quantita);
        $stmt->execute();
    }

    public function getLastOrder($email){
        $stmt = $this->db->prepare("SELECT codOrdine FROM ordine WHERE email = ? ORDER BY codOrdine DESC LIMIT 1");
        $stmt->bind_param('s',$email);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function deleteQuadro($titolo){
        $stmt = $this->db->prepare("UPDATE quadro
                                    SET eliminato = 1
                                    WHERE titolo = ?");
        $stmt->bind_param("s",$titolo);
        $stmt->execute();
    }

    public function updatePrezzo($prezzo, $titolo){
        $stmt = $this->db->prepare("UPDATE quadro
                                    SET prezzo = ?
                                    WHERE titolo = ?");
        $stmt->bind_param("ds",$prezzo, $titolo);
        $stmt->execute();
    }

    public function updatequantita($quantita, $titolo){
        $stmt = $this->db->prepare("UPDATE quadro
                                    SET quantita = ?
                                    WHERE titolo = ?");
        $stmt->bind_param("is",$quantita, $titolo);
        $stmt->execute();
    }

    public function decreasequantita($quantita2, $titolo){
        $stmt = $this->db->prepare("UPDATE quadro
                                    SET quantita = quantita - ?
                                    WHERE titolo = ?");
        $stmt->bind_param("is", $quantita2, $titolo);
        $stmt->execute();
    }

        public function removeQuadroFromAllCart($titolo){
            $stmt = $this->db->prepare("DELETE FROM carrello
                                        WHERE titolo = ?");
            $stmt->bind_param("s", $titolo);
            return $stmt->execute();
        }

        public function getMaxCodQuadro(){
            $stmt = $this->db->prepare("SELECT codQuadro FROM quadro ORDER by codQuadro DESC ");
            $stmt->execute();
            $result = $stmt->get_result();
    
            return $result->fetch_all(MYSQLI_ASSOC);
        }

        public function setOrderDelivered($codOrdine){
            $stmt = $this->db->prepare("UPDATE ordine
                                        SET arrivato = 1
                                        where codOrdine = ?");
            $stmt->bind_param("i",$codOrdine);
            $stmt->execute();
        }
}
?>