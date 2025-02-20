# Resolução do TPC2

### **Data:** 16 de Fevereiro de 2025  
### **Autor:**  
![Foto do Autor](https://avatars.githubusercontent.com/u/140913282?v=4)  
- **Nome:** Pedro Miguel Araújo Gomes 
- **Número de Aluno:** A104540

---

## Resumo
Este trabalho prático (TPC2) consistiu na leitura de um ficheiro CSV com informações de obras musicais, **`obras.csv`**, e processamento do mesmo sem fazer recurso ao módulo CSV do Python. Depois da leitura do dataset são esperados os seguintes resultados: 

- Lista ordenada alfabeticamente dos compositores musicais;
- Distribuição das obras por período: quantas obras catalogadas em cada período;
- Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
desse período.

---

## Resultados
Todos o conteúdo resultante deste TPC foi organizado e guardado no ficheiro **`resultados.json`** gerado posterior à execução do programa. Para além disso, os resultados foram ainda "imprimidos" no terminal:

1. **`Lista ordenada alfabeticamente dos compositores musicais`**  
```bash
Foi extraída a informação de 174 linhas 'csv'.

Lista de Compositores Ordenada:
1. Alessandro Stradella
2. Antonio Maria Abbatini
3. Bach, Johann Christoph
4. Bach, Johann Michael
5. Bach, Wilhelm Friedemann
6. Balbastre, Claude
7. Baldassare Galuppi
8. Barbara of Portugal
9. Benda, Franz
10. Bernardo Pasquini
11. Biber, Heinrich Ignaz Franz
12. Bononcini, Giovanni Battista
13. Boyvin, Jacques
14. Bull, John
15. Cabanilles, Juan Bautista
16. Caldara, Antonio
17. Carissimi, Giacomo
18. Cavalli, Francesco
19. Cristofaro Caresana
20. David Perez
21. Dieterich Buxtehude
22. Domenico Scarlatti
23. Duarte Lobo
24. Duarte Lôbo
25. Durante, Francesco
26. Elisabeth Sophie of Mecklenburg
27. Emanuele d'Astorga
28. Estevao de Brito
29. Fernandes, Gaspar
30. Filipe De Magalhaes
31. Friederike Sophie Wilhelmine
32. Froberger, Johann Jakob
33. Georg Bohm
34. Georg Muffat
35. Gibbons, Orlando
36. Gibbs, Joseph
37. Giovanni Battista Bassani
38. Giovanni Gabrieli
39. Giovanni Legrenzi
40. Giuseppe Tartini
41. Gregor Aichinger
42. Gregorio Allegri
43. Handel, George Frideric
44. Hans Leo Haßler
45. Hasse, Johann Adolph
46. Haym, Nicola Francesco
47. Heinrich Scheidemann
48. Henri Desmarets
49. Jan Pieterszoon Sweelinck
50. Jean-Joseph Mouret
51. Jean-Marie Leclair
52. Jeremiah Clarke
53. Johann Christoph(er) Pepusch
54. Johann David Heinichen
55. Johann Ernst Eberlin
56. Johann Hermann Schein
57. Johann Joachim Quantz
58. Johann Krieger
59. Johann Nicolaus Bach
60. John Blow
61. John Dowland
62. John Eccles
63. John IV
64. Krebs, Johann Ludwig
65. Leopold I
66. Louis Couperin
67. Lully, Jean-Baptiste
68. Lôbo, Duarte
69. Machado, Manuel
70. Madre De Deus, Filpe Da
71. Manuel Cardoso
72. Manuel Correia
73. Manuel Rodriguez Coelho
74. Marais, Marin
75. Marc-Antoine Charpentier
76. Martini, Giovanni Battista
77. Mattheson, Johann
78. Melchior Schildt
79. Michael Praetorius
80. Mondonville, Jean-Joseph
81. Monsieur de Sainte-Colombe
82. Monteverdi, Claudio
83. Neander, Joachim
84. Nicolas Siret
85. Nicolaus Bruhns
86. Nivers, Guillaume-Gabriel
87. Paolo Agostino
88. Pedro de Araujo
89. Pergolesi, Giovanni Battista
90. Peri, Jacopo
91. Peter Philips
92. Pierre Beauchamp
93. Pietro Della Valle
94. Rameau, Jean-Philippe
95. Reincken, Johann Adam
96. Robert Cambert
97. Rousseau, Jean-Jacques
98. Sammartini, Giovanni Battista
99. Sammartini, Giuseppe
100. Samuel Scheidt
101. Sanz, Gaspar
102. Schenck, Johannes
103. Seixas, Carlos
104. Stefano Landi
105. Strozzi, Barbara
106. Titelouze, Jean
107. Tomaso Albinoni
108. Viadana, Lodovico Grossi da
109. Weldon, John
110. Wilhelmine of Prussia
```

2. **`Distribuição das obras por período`**
```bash
Distribuição das Obras por Período:
Barroco: 26 obras
Clássico: 15 obras
Medieval: 48 obras
Renascimento: 41 obras
Século XX: 18 obras
Romântico: 19 obras
Contemporâneo: 7 obras
```

3. **`Dicionário Período -> Lista alfabética dos títulos das Obras`**
```bash
Títulos das Obras por Período (Ordenados):

Barroco:
- Ab Irato
- Die Ideale, S.106
- Fantasy No. 2
- Hungarian Rhapsody No. 16
- Hungarian Rhapsody No. 5
- Hungarian Rhapsody No. 8
- Impromptu Op.51
- In the Steppes of Central Asia
- Mazurkas, Op. 50
- Military Band No. 1
- Nocturne in C minor
- Paganini Variations, Book I
- Polonaise Op. 44
- Polonaise-Fantasie
- Polonaises Op.71
- Preludes Op. 11
- Preludes Op. 49
- Prince Rostislav
- Rage Over a Lost Penny
- Rondo Op. 5
- Shéhérazade, ouverture de féerie
- Symphonies de Beethoven
- The Rondo
- Transcendental Études
- Études Op. 25
- Études Op.10

Clássico:
- Bamboula, Op. 2
- Capriccio Italien
- Czech Suite
- French Overture
- Hungarian Rhapsody No. 14
- Hungarian Rhapsody No. 18
- Händelgesellschaft volume 50
- In Nature's Realm
- Mass in C major
- Scherzo No.3
- Serenade for Strings in G minor
- Serenata Notturna
- Stabat Mater
- Suite for Orchestra in B minor
- Zärtliche Liebe

Medieval:
- Adagio in B minor
- Ballade No.1
- Ballades, Op. 10
- Barcarole Op. 60
- Coriolan Overture
- Dixit Dominus
- Eroica Variations
- Fantasia and Fugue, BWV 542, G minor
- Fantasia in D minor
- Fantasy on Hungarian Folk Themes
- Faust Overture
- Gigue in G major, K. 574
- Grande valse brillante
- Hungarian Rhapsody No. 11
- Hungarian Rhapsody No. 13
- Hungarian Rhapsody No. 15
- Hungarian Rhapsody No. 3
- Hungarian Rhapsody No. 4
- Hungarian Rhapsody No. 7
- Impromptu, Op. 29
- La Savane
- Mazurkas, Op. 30
- Mazurkas, Op. 63
- Mazurkas, Op. 67
- Mazurkas, Op. 68
- Morceau de salon
- Preludes Op. 11 No. 4
- Preludes Op. 74
- Première rhapsodie
- Prélude, Choral et Fugue
- Rhapsodie Espagnole
- Romance in F major
- Rondo for Piano No. 3
- Serenade for Strings
- Serenade for Wind Instruments
- Suite No. 1 for two pianos
- Suite No. 2 for two pianos
- Suite in D minor, HWV 437
- Tapiola
- The Noon Witch
- Three Pieces for Orchestra
- Tragic Overture
- Transcendental Études
- Tönet, ihr Pauken! Erschallet, Trompeten!, BWV 214
- Valses Sentimentales
- Variations in F minor
- Variations on a Theme of Corelli, Op. 42
- Wedding day at Troldhaugen

Renascimento:
- Bagatelles, Opus 119
- Bagatelles, Opus 33
- Cantatas, BWV 141-150
- Carnival Overture
- Estampes
- Fantaisie brillante, Op. 22
- Festklänge, S.101
- Funeral March in Memory of Rikard Nordraak
- Hamlet, S.104
- Hungarian Rhapsody No. 10
- Hungarian Rhapsody No. 12
- Hungarian Rhapsody No.1
- Komm, Jesu, komm!
- L'Art de varier
- Le Mancenillier
- Legends, Op.59
- Liturgy of St. John Chrysostom
- Marie-Magdeleine
- Mazurkas, Op. 56
- Morceaux de Salon, Op. 10
- Nocturne in A-flat
- Othello
- Polonaises, Op.26
- Preludes Op. 11
- Preludes, Op. 32
- Romance in G major
- Rondo Op. 1
- Scans of the Bach Gesellschaft edition of the Eight Short Preludes and Fugues
- Scherzo No.4
- Schubert's Valses Nobles
- Shéhérazade
- Six Pieces for Piano, Op. 118
- St. Paul's Suite
- Symphonic Dances, Op. 64
- The Creatures of Prometheus
- Transcendental Études
- Transcendental Études
- Valse romantique
- Variation on a Waltz by Diabelli
- Vers la flamme
- Études Op. 25

Século XX:
- Berceuse
- Eleven Chorale Preludes, Op. 122
- Fürchte dich nicht
- Hungarian Rhapsody No. 17
- Hungarian Rhapsody No. 9
- Nocturnes Op. Posth. 72
- Papillons
- Peer Gynt Suite Suite No. 1
- Serenade for Strings
- Sigurd Jorsalfar
- Singet dem Herrn ein neues Lied
- Sonatas and Partitas for Solo Violin
- Sonatina in F major
- Sonatina in G
- Symphonic Poem No.1, Ce qu'on entend sur la montagne
- The Storm, Op.76
- Variations on a Theme of Chopin, Op. 22
- Études Op. 25

Romântico:
- Book II
- Fantasy No. 4
- Feu d'artifice
- Feuilles d'Album
- Grande Tarantelle
- Jeux d'enfants
- Lobet den Herrn, alle Heiden
- Moments musicaux
- Overture, Scherzo and Finale
- Preludes Op. 11
- Preludes Op. 59
- Präludium und Fuge über das Thema B-A-C-H
- Psalm 42 , Op. 42
- Salve Regina
- Scherzo No. 2
- Syrinx
- Waltzes, Op. 34
- Études Op. 25
- Études Op.10

Contemporâneo:
- Impromptu, Op. 36
- Les cinq doigts
- Polonaises, Op.40
- Preludes Opus 51
- Rhapsodies, Op. 79
- Sonnerie de Ste-Geneviève du Mont-de-Paris
- Études Op. 25
```

---

### Como Executar o Código
1. Certifica-te de que tens Python 3.12 (ou superior) instalado.
2. Executa o programa
```bash
python organizer.py
```
Podes aceder ao **`resultados.json`** e observar os resultados da execução.
