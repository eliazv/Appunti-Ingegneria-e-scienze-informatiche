'''
    Elaborato Programmazione di Reti
            a.a. 2020/2021
           Elia Zavatta
           Matricola: 0000921998
      Traccia 2: Python Web Server 
'''

#!/bin/env python
import sys, signal
import http.server
import socketserver
import threading 


#gestire l'attesa senza busy waiting
waiting_refresh = threading.Event()


# Legge il numero della porta dalla riga di comando, e mette default 8080
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8080


#variabili per il login
users = {}
 
#menù console del login
def displayMenuLogin():
    status = input("Are you registered user? y/n?  ")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()

#crea un nuovo utente
def newUser():
    createLogin = input("Create login name: ")
 
    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created! Now login\n")
 
#cerca di eseguire l'accesso con credenziali che se corrette fa uscire il programma dalla parte di login ed entrare nel main()    
def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")
 
    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
        main()
    else:
        print("\nUser doesn't exist or wrong password!\n")
 


# classe che mantiene le funzioni di SimpleHTTPRequestHandler e implementa il metodo get nel caso in cui si voglia fare un refresh
class ServerHandler(http.server.SimpleHTTPRequestHandler):   
    
    def do_GET(self):
        # Scrivo sul file AllRequests le richieste dei client     
        with open("AllRequests.txt", "a") as out:
          info = "GET request,\nPath: " + str(self.path) + "\nHeaders:\n" + str(self.headers) + "\n"
          out.write(str(info))
        if self.path == '/refresh':
            resfresh_contents()
            self.path = '/'
        http.server.SimpleHTTPRequestHandler.do_GET(self)

        
 
        
# ThreadingTCPServer per gestire piu' richieste
server = socketserver.ThreadingTCPServer(('127.0.0.1',port), ServerHandler)

# creo la parte iniziale della grafica di ogni pagina
header_html = """
<html>
    <head>
        <style>
            h1 {
                text-align: center;
                margin: 0;
            }
            table {width:70%;}
            img {
                max-width:300;
                max-height:200px;
                width:auto;
            }
            td {width: 33%;}
            p {text-align:justify;}
            td {
                padding: 20px;
                text-align: center;
            }
            .topnav {
  		        overflow: hidden;
  		        background-color: #00A878;
  		    }
            .topnav a {
  		        float: left;
  		        color: #f2f2f2;
  		        text-align: center;
  		        padding: 14px 16px;
  		        text-decoration: none;
  		        font-size: 21px;
  		    }        
  		    .topnav a:hover {
  		        background-color: #B4EBE9;
  		        color: black;
  		    }        
  		    .topnav a.active {
  		        background-color: #D41E16;
  		        color: white;
  		    }
        </style>
    </head>
    <body>
        <img src="https://salute.regione.emilia-romagna.it/ssr/strumenti-e-informazioni/logo-ssr/declinazioni-del-logo/bologna_aosp.JPG" alt="aziendaimg">
        <title>Azienda Ospedaliera</title>
"""

# barra di navigazione 
navigation_bar = """
        <br>
        <br>
        <br>
        <div class="topnav">
            <a class="active" href="http://127.0.0.1:{port}">Home</a>
  		    <a href="http://127.0.0.1:{port}/geriatria.html">Geriatria</a>
            <a href="http://127.0.0.1:{port}/cardiologia.html">Cardiologia</a>
            <a href="http://127.0.0.1:{port}/chirurgia.html">Chirurgia</a>
            <a href="http://127.0.0.1:{port}/farmacia.html">Farmacia</a>
            <a href="http://127.0.0.1:{port}/neurologia.html">Neurologia</a>
            <a href="http://127.0.0.1:{port}/psichiatria.html">Psichiatria</a>
  		    <a href="http://127.0.0.1:{port}/refresh" style="float: right">&#8635;</a>
  		</div>
        <br><br>
        <table align="center">
""".format(port=port)



# la parte finale di ogni pagina
footer_html= """
        </table>
    </body>
</html>
"""

  
# creo tutti le pagine
def resfresh_contents():
    print("updating all contents")
    create_page_cardiologia()
    create_page_geriatria()
    create_page_chirurgia()
    create_page_farmacia()
    create_page_neurologia()
    create_page_psichiatria()
    create_index_page()
    print("finished update")



def create_page_geriatria():
        message = header_html + "<h1>Azienda Ospedaliera</h1>" + navigation_bar + "<br><br>" 
        message = message + '<img src="https://www.centromedicoeuropa.it/wp-content/uploads/2019/09/geriatria-800x547.jpg" alt="geriatriaimg">' + "<br><br><br>"
        message = message + "<h2>Geriatria</h2>" + "La geriatria e' la branca della medicina che si occupa dei bisogni e dei problemi di salute tipici della terza eta'."
        message = message + "<h4>Di cosa si occupa il geriatra?</h4>" + "Il geriatra e' un medico in grado di valutare e gestire i bisogni tipici della terza eta' in tema di salute. Il compito spesso e' reso difficile dal fatto che non e' raro, dopo i 65 anni, riscontrare contemporaneamente piu' problemi di salute che richiederebbero l'intervento di specialisti diversi. Il geriatra evita inoltre che l'assunzione contemporanea di piu' farmaci finisca per scatenare effetti collaterali o produrre interazioni pericolose.<br><br><br>"
        message = message + "<h4>Quali sono le patologie trattate piu' spesso dal geriatra?</h4>" + "Fra le patologie con cui un geriatra si trova piu' spesso ad avere a che fare sono incluse: artrite, diabete, difficolta' nelle interazioni sociali, disturbi della memoria, inclusa la malattia di Alzheimer, ipertensione, malattie cardiovascolari, patologie cognitive."
        message = message + '<br><br><a href="https://it.wikipedia.org/wiki/Geriatria">per maggiori informazioni</a>'
        message = message +  footer_html
        f = open('geriatria.html','w', encoding="utf-8")
        f.write(message)
        f.close()    

def create_page_cardiologia():
    
        message = header_html + "<h1>Azienda Ospedaliera</h1>" + navigation_bar + "<br><br>" 
        message = message + '<img src="https://www.materdei.it/wp-content/uploads/2009/09/cardiologia-visita-2-copia-1030x617.jpg" alt="cardiologiaimg">' + "<br><br><br>"
        message = message + "<h2>Cardiologia</h2>" + "La Cardiologia si occupa dello studio, della diagnosi e della cura (farmacologica e/o invasiva) delle malattie cardiovascolari. E' un reparto cui accedono i pazienti affetti da patologie cardiache acute o crooniche, per eseguire accertamenti e/o cure." + "<br><br><br>"  
        message = message + "<h3>LABORATORIO DI EMODINAMICA</h3>"+ "Effettua prestazioni diagnostiche ed interventiche coronariche e vascolari sia in elezione che in urgenza ed emergenza.Costituisce il centro di riferimento provinciale garantendo la necessaria ricettivita' ad eseguireprocedure elettive ed urgenti su pazienti proveniennti dal territorio di Forli'-Cesena. Il laboratorio assicura il trattamento dell'infarto Miocardico Acuto mediante angioplastica primaria (reperibilita' 24/24). Innoltre svolge attivita' di diagnostica vascolare periferica ed interventistica endovascolare, in collaborazione con la Chirurgia Vascolare Interaziendale.<br><br><br>"
        message = message + "<h3>LABORATORIO DI ELETTROFISIOLOGIA</h3>"+ "Effettua prestazioni diagnostiche (studi elettrofisiologici) ed interventistiche (ablazioni transcatetere, impianti di pace-maker, impianti di defibrillatore automatico e impianti di pace-maker defibrillatore automaticocon stimolatore biventricolare) sia in elezione che in urgenza. Il laboratorio di Elettrofisiologia e' di riferimento per la provincia di Forli'-Cesena.<br>"
        message = message + '<br><br><a href="https://it.wikipedia.org/wiki/Cardiologia">per maggiori informazioni</a>'
        message = message + footer_html
        f = open('cardiologia.html','w', encoding="utf-8")
        f.write(message)
        f.close()

    
def create_page_chirurgia():
        message = header_html + "<h1>Azienda Ospedaliera</h1>" + navigation_bar + "<br><br>" 
        message = message + '<img src="http://www.cmt-firenze.it/wp-content/uploads/2017/03/chirurgia-generale-firenze.jpg" alt="chirurgiaimg">' + "<br><br><br>"
        message = message + "<h2>Chirurgia</h2>" + "Con la definizione 'chirurgia generale' si indica, differentemente da quanto suggerisce la definizione stessa, quella branca della chirurgia che si occupa di risolvere o migliorare la prognosi delle patologie che interessano gli organi della cavita' addominale (intestino, colon, fegato, stomaco, esofago, pancreas, cistifellea, fegato, dotti biliari) oltre alla mammella e alla tiroide.<br><br><br>"
        message = message + "<h4>Di cosa si occupa il chirurgo generale?</h4>" + "Il chirurgo generale e' un chirurgo specializzato in interventi chirurgici condotti su mammella, tiroide o su uno degli organi della cavita' addominale, il cui obiettivo e' curare o migliorare la prognosi delle patologie che interessano questi organi.<br><br><br>"
        message = message + "<h4>Quali sono le patologie trattate piu' spesso dal chirurgo generale?</h4>" + "Le patologie piu' spesso trattate da questo chirurgo sono le patologie a carico della mammella, della tiroide e degli organi della cavita' addominale (intestino, colon, fegato, stomaco, esofago, cistifellea, pancreas, fegato, dotti biliari). Tra queste ricordiamo in particolare: malattie funzionali e infiammatorie a carico di mammella, tiroide e degli organi della cavita' addominale;ernie (iatali e inguinali), ulcere, diverticoliti, neoplasie (gastriche, dell'esofago, dell'intestino, del pancreas, del colon-retto, del fegato, della mammella, della tiroide, dei dotti biliari);cisti, poliposi, calcolosi, sindromi dolorose da aderenze addominali post-chirurgiche.Dal punto di vista diagnostico il chirurgo generale effettua molto spesso biopsie dei linfonodi e biopsie mammarie"
        message = message + '<br><br><a href="https://it.wikipedia.org/wiki/Chirurgia">per maggiori informazioni</a>'
        message = message + footer_html
        f = open('chirurgia.html','w', encoding="utf-8")
        f.write(message)
        f.close()    


def create_page_farmacia():
        message = header_html + "<h1>Azienda Ospedaliera</h1>" + navigation_bar + "<br><br>" 
        message = message + '<img src="https://www.farmaciavincente.it/wordpress/wp-content/uploads/2015/11/reparto-vincente-in-farmacia.jpg" alt="farmaciaimg">' + "<br><br><br>"
        message = message + "<h2>Farmacia</h2>" + "La Farmacia e' uno dei reparti fondamentali, anche se praticamente 'invisibili' ai pazienti, delle strutture ospedaliere. E il farmacista ospedaliero svolge il ruolo di coniugare il miglioramento dell'assistenza al paziente con la qualita' della gestione del farmaco, occupandosi anche della razionalizzazione dei costi: una serie di compiti battezzata oggi Clinical Pharmacy, cioe' una collaborazione continua del farmacista clinico con il medico tenendo conto di vari elementi che, partendo dalla cura e dal benessere della persona-paziente e dalla sua patologia, con l'uso sicuro ed efficace del farmaco appropriato alla terapia, si occupano anche del miglioramento del complesso processo di scelta, valutazione, acquisizione di farmaci e dispositivi medici.<br><br><br>"
        message = message + '<br><br><a href="https://it.wikipedia.org/wiki/Farmacia">per maggiori informazioni</a>'
        message = message + footer_html
        f = open('farmacia.html','w', encoding="utf-8")
        f.write(message)
        f.close() 

    
def create_page_neurologia():
        message = header_html + "<h1>Azienda Ospedaliera</h1>" + navigation_bar + "<br><br>" 
        message = message + '<img src="https://www.benacuslab.com/wp-content/uploads/2019/07/Neurologia.jpg" alt="neurologiaimg" class="center">' + "<br><br><br>"
        message = message + "<h2>Neurologia</h2>" + "La neurologia e' la branca della medicina che si occupa dello studio e del trattamento dei disturbi del sistema nervoso, sia quello centrale (il cervello e il midollo spinale) che quello periferico (costituito da tutti gli altri elementi nervosi, incluse le strutture presenti negli occhi, nelle orecchie e nella pelle).<br><br><br>"
        message = message + "<h4>Di cosa si occupa il neurologo?</h4>" + "Il neurologo e' un medico specializzato in neurologia. Si occupa della diagnosi e del trattamento dei problemi che colpiscono il cervello, il midollo spinale e i nervi, senza pero' ricorrere alla chirurgia, ambito di azione del neurochirurgo. Molti neurologi sono ulteriormente specializzati in un settore della neurologia, ad esempio nel trattamento di ictus, epilessia, problemi neuromuscolari, disturbi del sonno, del dolore, dei tumori del sistema nervoso o dei problemi tipici della terza eta'.<br><br>"
        message = message + "<h4>Quali sono le patologie trattate piu' spesso dal neurologo?</h4>" + "Le patologie piu' spesso trattate dal neurologo sono: cefalee e le altre forme di mal di testa, disturbi del linguaggio, disturbi del movimento, epilessia, infezioni del cervello e del sistema nervoso periferico, come l'encefalite, la meningite e gli ascessi cerebrali, malattie cerebrovascolari, come l'ictus, malattie neurodegenerative, come l'Alzheimer, il Parkinson e la Sclerosi Laterale Amiotrofica, patologie che portano alla perdita della mielina nel sistema nervoso centrale, come la sclerosi multipla, problemi al midollo spinale, incluse le malattie infiammatorie e quelle autoimmuni. <br><br>"
        message = message + '<br><br><a href="https://it.wikipedia.org/wiki/Neurologia">per maggiori informazioni</a>'
        message = message + footer_html
        f = open('neurologia.html','w', encoding="utf-8")
        f.write(message)
        f.close() 

    
def create_page_psichiatria():
        message = header_html + "<h1>Azienda Ospedaliera</h1>" + navigation_bar + "<br><br>" 
        message = message + '<img src="https://www.cabpolidiagnostico.it/wp-content/uploads/2017/08/psichiatria.jpg" alt="psichiatriaimg">' + "<br><br><br>"
        message = message + "<h2>Psichiatria</h2>" + "La psichiatria e' un specialita' della medicina che ha per oggetto lo studio clinico e la terapia dei disturbi mentali e dei comportamenti patologici. La diagnosi psichiatrica e' un processo complesso, che si avvale di valutazioni anamnestiche, colloqui clinici, test e reattivi psicopatologici e, quando necessario, anche di altre valutazioni mediche e psicologiche (internistiche, neurologiche, psicologiche,etc...). I disturbi di competenza psichiatrica sono diversi e possono essere temporanei o cronici.<br><br><br>"
        message = message + '<br><br><a href="https://it.wikipedia.org/wiki/Psichiatria">per maggiori informazioni</a>'
        message = message + footer_html
        f = open('psichiatria.html','w', encoding="utf-8")
        f.write(message)
        f.close() 

    
    
# creazione della pagina iniziale (index.html)
def create_index_page():
    f = open('index.html','w', encoding="utf-8")
    try:
        message = header_html + "<h1>Azienda Ospedaliera</h1>" + navigation_bar
        message = message + '<th colspan="4"><h2>I Nostri Servizi</h2></th>'
        message = message + '<th><h2>Downloads</h2></th></tr>'
        message = message + '<td><h3><ul><li><a href="/geriatria.html">Geriatria</a></li><li><a href="/cardiologia.html">Cardiologia</a></li><li><a href="/chirurgia.html">Chirurgia</a></li>'
        message = message + '<li><a href="/farmacia.html">Farmacia</a></li><li><a href="/neurologia.html">Neurologia</a></li><li><a href="/psichiatria.html">Psichiatria</a></li></ul></h3></td>'
        message = message + '<th colspan="4"><h3><ul><li><a href="/info.pdf" download="info.pdf">Download file pdf</a></li></ul></h3></th>'
        message = message + '<th colspan="4"><br><br><br><br><br><i>&emsp;&emsp;realizzato da Elia Zavatta </i></th>'
        message = message + footer_html
    except:
        pass
    f.write(message)
    f.close()


#  permette terminare l'esecuzione del server tramite i tasti Ctrl+C
def signal_handler(signal, frame):
    print( 'Exiting http server (Ctrl+C pressed)')
    try:
      if(server):
        server.server_close()
    finally:
      # fermo il thread del refresh senza busy waiting
      waiting_refresh.set()
      #Termina il programma
      sys.exit(0)
      
     

#esegue la parte di login finche l'utente non esegue l'accesso    
def login_():
    while 1: 
        displayMenuLogin()
     
      
def main():
    #
    resfresh_contents()
    #Assicura che da tastiera usando la combinazione di tasti Ctrl+C termini in modo pulito tutti i thread generati
    server.daemon_threads = True 
    #il Server acconsente al riutilizzo del socket anche se ancora non e' stato rilasciato quello precedente, andandolo a sovrascrivere
    server.allow_reuse_address = True  
    #interrompe l'esecuzione se da tastiera arriva la sequenza (CTRL + C) 
    signal.signal(signal.SIGINT, signal_handler)
    # cancella i dati get ogni volta che il server viene attivato
    f = open('AllRequests.txt','w', encoding="utf-8")
    f.close()
    try:
      while True:
        server.serve_forever()
    except KeyboardInterrupt:
      pass
    #Chiude il server socket
    server.server_close() 
    

if __name__ == "__main__":  
    login_()
