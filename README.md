# MINECRAFT AGENT FRAMEWORK
Aquest projecte per l'assignatura de TAP permet la integració de **BOTS INTEL·LIGENTS** en Minecraft utilitzant l'API 'mcpi'.
Els bots poden realitzar diverses accions, com insultar jugadors, col·locar TNT, respondre preguntes com un oracle i executar ordres dinàmicament.

------
## Index
- **Instal·lació**
  - **Requisits previs**
  - **Com fer que funcioni**
- **Descripció Bots**
  - **InsultBot**
  - **TNTBot**
  - **OracleBot**
-------

## Instal·lació

### **Requisits previs**
- Tenir **Minecraft Pi Edition** o Minecraft Server compatible amb el API 'mcpi'.
- Instal·lar **Python 3.x**

### **Com fer que funcioni**
- Clonar aquest repositori.
- cd AdventuresInMinecraft-Linux-master
- En el terminal executar ./StartServer
- Obrim el Minecraft i ens conectem al servidor amb el nom TAP server i la direcció localhost
- Després de conectar-nos al servidor ja podem executar els tests
- Obrim un altre terminal
- cd test
- Per provar els diferents bots podem fer:
  - python3 run_insult.py
  - python3 run_oracle.py
  - python3 run_tnt.py
- Tambe podem executar directament python3 run_bots.py, que executara tots els bots a la vegada
## Descripcio Bots
### InsultBot
El bot InsultBot insulta aleatòriament els jugadors en el xat de Minecraft. Pot iniciar i aturar-se en resposta a les comandes "start" i "stop" enviades per  l'usuari.
- **Programació Funcional**
  - La selección d'insults es fa mitjançant la funció *random.choice()*, utilutzant la programación funcional oer escollir aleatòriamente un insult de la llista.
  - Es fa servir el *filter()* per verificar si el bot ha de seguir en execució en funció de les entrades del xat.
- **Programació Reflexiva**
  - La reflexió també s'aplica a les comandes de control del bot, utilitzant *gettattr()* per invocar accions dinàmiques basades en les comandes que rep del xat.
### TNTBot
El bot TNTBot col·loca TNT a prop del jugador i el fa explotar després de ser tocat pel jugador. El bot comprova que el TNT no es col·loqui en l'aire, per garantir que estigui en una posicio vàlida per explotar.
- **Programació Funcional**
  - S'ha utilitzat *map()* per generar coordenades aleatòries on col·locar el TNT sense necessitat de bucles explícits.
  - El bot fa servir *filter()* per verificar que el lloc seleccionat per col·locar el TNT no sigui l'aire, evitant errors en la col·locació.
- **Programació Reflexiva**
  - El bot fa servir reflexió per obtenir de manera dinàmica el bloc de TNT amb *gettattr(block, "TNT")*. Això permet una extensió fàcil del bot per a altres tipus de blocs o accions en el futur.
### OracleBot
L'OracleBot escolta els missatges enviats al xat del jugadir i respon preguntes comunes com "quin és el teurgias nom?", "quin és el teu propòsit?" o "com està el temps?". Aquest bot mante actiu fins que se li indiqui que aturi la seva acciónarial.
- **Programació Funcional**
  - S'ha utilitzat un diccionario de funcions per obtenir respostes de manera eficient, evitant l'ús de múltiples condicions *if-else*.
  - Utilitza *map()* per processar els missatges del xat de forma funcional, eliminant bucles explícits.
- **Programació Reflexiva**
  - La reflexió s'aplica utilitzant *gettattr(self, "command_" + ordre, None) per cridar funcions dinàmiques segons les comandes del jugadors. Això evita la necessitat de condicions explícites i fa el codi més extensible i adaptable a nous tipus de comandes.
-----
Aquest projecte combina la potència de la programació funcional i reflexiva amb la creativitat per construir bots intel·ligents que poden interactúar amb el món de Minecraft de manera autònoma i dinàmica. Amb aquesta estructura, els bots poden adaptar-se fàcilmente a noves comandes i escenaris sense necessitat de modificacions complicades en el codi.
