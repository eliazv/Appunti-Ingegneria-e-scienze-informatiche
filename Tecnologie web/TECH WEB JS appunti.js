/*•	Al click sul bottone “Carica Dati” si dovrà:
o	Inserire all’interno del paragrafo il testo “Caricamento dati in corso...”
o	Leggere il json sw_a.json e visualizzarlo in una tabella valida ed accessibile tenendo conto che:
	Deve essere creata una colonna per ogni attributo degli oggetti (N.B il nome deve essere una cella di intestazione).
	Come ultima colonna deve esserne inserita una con intestazione Azione e che contiene n bottoni con il testo “Modifica Riga” (1 bottone per ogni riga).
	Tutte i valori devono essere visualizzati nella tabella come testo, a parte l’attributo “colore preferito”, che verrà usato per impostare il colore di sfondo
 della relativa cella.
	Una volta caricati i dati, modificare il testo del paragrafo inserendo la stringa “Caricamento dei dati avvenuto con successo.”
•	Al click sul bottone “Modifica riga” si dovrà:
o	Sostituire i testi di ogni cella della riga con un input (accessibile!) per modificare i rispettivi valori. I campi colore preferito e email devono avere un
 input particolare, mentre per gli altri va bene un semplice input di testo.
o	Il testo del bottone cliccato dovrà essere cambiato in “Conferma”.
•	Al click sul bottone “Conferma” si dovrà:
o	Leggere i contenuti dei vari input e inserirli come testo all’interno delle rispettive celle (ad eccezione del colore preferito, che dovrà sempre essere
     usato come sfondo della cella).
o	Cambiare il testo del bottone cliccato in “Modifica Riga”.
 */

$(document).ready(function(){

    $(document).on("click",".modifica", function(){
        const tr = $(this).parent().parent();

        console.log($(this).parent().parent().index());

        let i=1;
        $(tr.children().each(function(){
            if(!$(this).children().is("button")){
                if(i==2){
                    $(this).html("<input type='email'/>");
                }else if(i==3){
                    $(this).html("<input type='color'/>");
                }else{
                    $(this).html("<input type='text'/>");
                }
                i++;
            }else{
                $(this).children().text("Conferma");
                $(this).children().removeClass("modifica");
                $(this).children().addClass("conferma");
            }
        }))
    });

    $(document).on("click",".conferma", function(){
        const tr = $(this).parent().parent();

        let i=1;
        $(tr.children().each(function(){
            if(!$(this).children().is("button")){
                const val = $(this).children().val();

                $(this).html("");
                if(i==3){
                    $(this).css("background-color", val);
                }else{
                    $(this).text(val);
                }
                i++;
            }else{
                $(this).children().text("Modifica Riga");
                $(this).children().removeClass("conferma");
                $(this).children().addClass("modifica");
            }
        }));
    })
        
    $("main > button").click(function(){
        $("table").html("");
        $("main>p").text("Caricamento dati in corso");

        $.ajax({
            url: "sw_a.json",
            dataType: "json",
            success: function(result){
                const keys = Object.keys(result[0]);

                $("table").append(`<tr></tr>`);

                keys.forEach(key => {
                    $("table tr").append(`<th id="${key.toLowerCase()}">${key}</th>`);
                });

                $("table tr").append(`<th id="azione">Azione</th>`)

                for(let i=0; i<result.length; i++){
                    $("table").append(`<tr>
                                        <th id="${result[i].nome.toLowerCase().trim()}" headers="${keys[0]}">${result[i].nome}</th>
                                        <td headers="${keys[1]} ${result[i].nome.toLowerCase()}">${result[i].email}</td>
                                        <td headers="${keys[2]} ${result[i].nome.toLowerCase()}" style="background-color:${result[i].colore_preferito}"></td>
                                        <td headers="${keys[3]} ${result[i].nome.toLowerCase()}">${result[i].colore_capelli}</td>
                                        <td headers="${keys[4]} ${result[i].nome.toLowerCase()}">${result[i].colore_occhi}</td>
                                        <td headers="${keys[5]} ${result[i].nome.toLowerCase()}">${result[i].genere}</td>
                                        <td headers="azione ${result[i].nome.toLowerCase()}"><button class="modifica">Modifica Riga</button></td>
                                        </tr>`);
                }

                $("main>p").text("Caricamento dati avvenuto con successo.");
            }
        })
    });
});


/*•	Al caricamento della pagina:
o	Il form deve essere nascosto.
o	Deve essere aggiunta una riga di intestazione alla tabella con le seguenti colonne: Name, Email, Description, Action.
•	Al click sul bottone “Insert” si dovrà:
o	Inserire come testo del bottone di submit la stringa “Add”.
o	Mostrare il form, i cui input dovranno essere vuoti.
o	Al click sul bottone “Add” si dovrà:
	Leggere le stringhe inserite nei 3 input. In caso uno o più campi siano vuoti, visualizzare un messaggio di errore in un paragrafo.
	Creare una nuova riga della tabella con i dati inseriti (il nome deve essere usato come intestazione). Nella colonna action, inserire 2 bottoni: 
“Update” e “Delete”.
	Nascondere il form.
•	Al click sul bottone “Delete” si dovrà rimuovere la corrispondente riga della tabella. 
•	Al click sul bottone “Update” si dovrà:
o	Mostrare il form (non è necessario inserire negli input i valori attuali) il cui input submit dovrà avere come testo la stringa “Update Now”.
o	Al click sul bottone “Update Now” si dovrà:
	aggiornare le colonne della riga che si sta modificando con quelli inseriti (visualizzare un messaggio di errore se uno dei campi è vuoto).
	Nascondere il form.
 */

function update(){
    $("form").show();
    $("input[type=\"submit\"]").val("Update Now");
}

$(document).ready(function(){
    $("form").hide();

    $("table").append(`<tr>
                        <th id="name">Name</th>
                        <th id="email">Email</th>
                        <th id="description">Description</th>
                        <th id="action">Action</th></tr>`);

    $("button").click(function(){
        $("input[type=\"submit\"]").val("Add");
    
        $("form").show();
    });

    $("input[type=\"submit\"]").click(function(event){
        event.preventDefault();
        $("form p").remove();
        const name = $("input[name='name']").val();
        const email = $("input[name='email']").val();
        const description = $("input[name='description']").val();
        
        if(name=="" || email == "" || description == ""){
            $("form").append(`
                            <p>Errore inserimento!</p>`);

            return;
        }
        
        $("table").append(`<tr>
                            <th id=${name.toLowerCase()}>${name}</th>
                            <td headers="email">${email}</td>
                            <td headers="description">${description}</td>
                            <td headers="action"><button onclick='update()'">Update</button> <button value="Delete">Delete</button></td>
        </tr>`);

        $("form").hide();
    });
    
});

/* •	Al click sul bottone “Aggiungi Riga” si dovrà:
o	Leggere il contenuto dell’input numerocolonne che rappresenterà il numero di colonne che comporranno la nuova riga della pagina.
 Inserire nel div successivo al bottone, un input di tipo numero per ogni colonna che si vuole inserire (che rappresenta la larghezza delle colonne, 
    usando la griglia di bootstrap 1-12) e un bottone “Genera Colonne”.
o	Al click sul bottone “Genera Colonne” si dovrà:
	Controllare che la somma dei numeri inseriti sia pari a 12.
	In caso il totale sia 12, aggiungere una riga al div con classe container-fluid che ha la stessa struttura di quella descritta dall’utente.
 Una volta creata la colonna, svuotare il div che segue il bottone “Aggiungi Riga”.
 */

 function GeneraColonne(nColonne){
    let sommaColonne = 0;

    for(let i=0; i < nColonne; i++){
        sommaColonne = sommaColonne + parseInt($("input[name=colonna"+i+"]").val());
    }

    if(sommaColonne == 12){
        $("div[class='col-12']:last-of-type").append(`
        <div class="row container-fluid"></div>
        `);

        for(let i=0; i < nColonne; i++){
            $("div[class=\"row container-fluid\"]:last-of-type").append(`
                <div class="col-${$("input[name=colonna"+i+"]").val()}"></div>
            `);
        }
        $("button+div").html("");
    }

}

$(document).ready(function (){
    $("button").click(function (){
        const nColonne = $("input[name='numerocolonne']").val();

        for(let i=0; i < nColonne; i++){
            $("button+div").append(`
            <input type="number" name="colonna${i}"/>
            `);
        }

        $("button+div").append(`
        <button onclick="GeneraColonne(${nColonne});">Genera Colonne</button>
        `);
    });
});

/*•	Al caricamento della pagina dovrà essere effettuata una richiesta GET alla pagina index.php dell’esercizio precedente, 
leggere i dati JSON e visualizzarli in una tabella (da aggiungere come ultimo elemento del body).
•	Al click sul bottone “Aggiungi” si dovrà:
o	Controllare che il contenuto degli input non siano vuoti.
o	Se non vuoti, mandarli in post alla pagina index.php dell’esercizio precedente.
o	Eseguire nuovamente una richiesta GET per ottenere i dati aggiornati
 */
$("document").ready(function (){
    $.ajax(
        {
            url:"../php/index.php",
            method:"get",
            dataType:"json",

            success: function(result){
                $("body").append(`<table></table>`);

                $("body table").append(`<tr>
                                        <th id="name">Name</th>
                                        <th id="height">Height</th>
                                        <th id="mass">Mass</th>
                                        </tr>`);

                result.forEach(character => {
                    $("body table").append(`<tr>
                                            <td headers="name">${character.name}</td>
                                            <td headers="height">${character.height}</td>
                                            <td headers="mass">${character.mass}</td>
                                            </tr>`); 
                })
            }
        }
    );

    $("input[type='submit']").click(function(){
        const name = $("input[name='name']").val();
        const height = $("input[name='height']").val();
        const mass = $("input[name='mass']").val();
        if(name != "" && height != "" && mass != ""){
            $.ajax(
                {
                    url:"../php/index.php",
                    method:"post",
                    data: {'name' : name, 'height' : height, 'mass' : mass},
                    success: function(result){
                    }
                });

            $.ajax(
                {
                    url:"../php/index.php",
                    method:"get",
                    dataType:"json",
        
                    success: function(result){
                        $("body table").append(``);
        
                        $("body table").append(`<tr>
                                                <th id="name">Name</th>
                                                <th id="height">Height</th>
                                                <th id="mass">Mass</th>
                                                </tr>`);
        
                        result.forEach(character => {
                            $("body table").append(`<tr>
                                                    <td headers="name">${character.name}</td>
                                                    <td headers="height">${character.height}</td>
                                                    <td headers="mass">${character.mass}</td>
                                                    </tr>`); 
                        })
                    }
                }
            ); 
        }
    });
});