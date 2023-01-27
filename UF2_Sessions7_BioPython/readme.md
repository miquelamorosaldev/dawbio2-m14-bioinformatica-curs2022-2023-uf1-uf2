# Sessió 7 - Biopython. Tractament del fitxer Genbank del Sars-Cov-2 i altres (2) (2022-01-23)

## Resum SeqIO

**.read()** --> Llegeix fitxers (.fasta i .genbank) que tenen només UNA (seqüència o fitxa)

Resultat = SeqRecord

**.parse()** --> Llegeix fitxers (.fasta i .genbank) que tenen només MOLTES (seqüències o fitxes)

Resultat = Llista SeqRecord's

**.write()** Escriu.


## Escriptura fitxers Genbank i Fasta.

Mirem el que posa a les linies 125 - 143

```sh
    # We can create SeqRecords, modify them and write them to disk.
    # Minimum requirements:
    # 1. seq must be of class Seq
    # 2. annotations must have a key 'molecule_type'
    seq:         Seq        = Seq('GATAGATA')
    annotations: dict       = { 'molecule_type' : 'DNA' }
    record:      SeqRecord  = SeqRecord( seq = seq,
                                         id  = '12345',
                                         description = 'GATA seq',
                                         annotations = annotations )

    # Inspect Python objects with our own explore() function
    print('SeqRecord to be written to disk:')
    pp(explore(record))
    print()

    # SeqRecords can be written to .fasta or .genbank files
    SeqIO.write(record, EXAMPLE_FASTA, 'fasta')
    SeqIO.write(record, EXAMPLE_GENBANK, 'genbank')
```

### Sobre les extensions dels fitxers Genbank

NCBI posa .gb i .gbk per defecta al baixar-nos els Genbank.
Millor canviar a .genbank per a què Ubuntu no es confongui.


## Exercicis que hem fet a classe amb el nostre Genbank.

- Mostrar quantes features y annotations hi ha.
- Quina longitud tiene la secuencia ?
- Obtenim el type i la location de totes les features del genbank. És la part 2 del fitxer.
- Analitzem la seqüencia.
- Comparem la seqüència del genbank amb la del fasta.

Si voleu consultar directament les solucions del Pablo les podeu trobar a ex1.py
[ex1.py](./code/ex1.py)

Les solucions que el Miquel ha extret a classe estan al fitxer [test.py](./code/test.py)

Alguns dels exercicis els ha fet sobre Genbank i el Fasta del Cannabis.

https://www.ncbi.nlm.nih.gov/nuccore/?term=Cannabis+sativa

El Pablo també ha trobat, dins del genbank, l'article PubMed que parla del Sars-Cov-2:

[PubMedSarsCov2.pdf](./s41586-020-2008-3.pdf)

<hr/>
<hr/>


## Esquema erarquia de clases a la lectura de fitxers FASTA i GENBANK

![[SeqRecord_Jerarquia]](jerarquia-seqrecord.png "SeqRecord_Jerarquia")


## Link següent sessió

[Sessió 8 - Regexp](./UF2_Sessions8_IntroRegexp/readme.md)