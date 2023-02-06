## Pràctica i Examen final UF

Consistirà en diferents fitxers, a la pràctica els que vulguem, on haurem de descarregar fitxers genbank i explotar-los. Fer algunes alineacions.


### Enunciat Practica

      1. Escollir organisme i gen (o gens) a comparar entre espècies.
      2. Descarregar Genbanks utilitzant Biopython Entrez.
      3. Extreure informació del GenBank, extreure alguna informació utilitzant Regexps.
      4. Alinear sequències.
      5. Mostrar resultats amb format de taula Pandas.
   
**Enunciat complet --> [Enunciat complet](./omics-pt.pdf "Enunciat complet")**

### Pe Òmiques

      1. El mateix que a la pràctica.
      2. Saber navegar entre fitxers genBanks.
      3. Saber extreure informació amb Regexps.
      4. Saber alinear.
      5. Posar la informació a  taules de Pandas.


Exemples:

Partint d'aquest, busqueu a la taxonomia, si es carnívor.
O busqueu els **autors d'aquest àrticle amb expressions regulars**


###### Incís aclaratori

**API** - Application Program Interface

    1. Una llista de funcions que controla el programa.
    2. Exemples : 
       1. Android: ShowNotification(...,..,...)
       2. Colection de rutes: HTTP d'una aplicació web.
       3. Com es crida a una API 
    ![API](API.jpg "API")
       5. [Link metodos](https://developer.mozilla.org/es/docs/Web/HTTP/Methods "Link metodos")
       6. [github public apis](https://github.com/public-apis/public-apis "public apis")
   
   [Proves crida Api animechan](./3-apis/1-requests/animechan.py "crida animechan")


   ## NCBI BioPython

   Seguirem el tutorial de biopython, al capítol 9:

   1. [Biopython Tutorial oficial](http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec143 "biopython")
   
   Les instruccions que veurem seran

      **EInfo** Les instruccions 
      
   
- [Prova 1 einfo](./3-apis/2-entrez/1-einfo/einfo-e1/einfo.py "einfo-e1")

- [Prova 2 einfo](./3-apis/2-entrez/1-einfo/einfo-e2/einfo.py "einfo-e1")
    
      **ESearch** és un mètode tipus (GET)
   
- [Prova 1 esearch](./3-apis/2-entrez/2-esearch/esearch-e1/esearch.py "esearch-e1")
   
- [Prova 2 esearch](./3-apis/2-entrez/2-esearch/esearch-e2/esearch.py "esearch-e2")
   
      **EPost** és un mètode tipus (POST)
   
      **EFetch** recull les dades

- [Prova 1 efetch](./3-apis/2-entrez/3-efetch/efetch-e1/efetch.py "efetch-e1")

- [Prova 2 efetch](./3-apis/2-entrez/3-efetch/efetch-e2/efetch.py "efetch-e2")

- [Prova 3 efetch](./3-apis/2-entrez/3-efetch/efetch-e3/efetch.py "efetch-e3")

   ### Aligment (alineament)

    Aquest apartat, explicació teòrica de aligment i les diferents instruccions per treballar amb aligment, ho seguirem al document [pairwise.py](./4-alignments/pairwise.py "pairwise")