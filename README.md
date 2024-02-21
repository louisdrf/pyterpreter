# pyterpreter
Le sujet présente un [interpréteur](https://fr.wikipedia.org/wiki/Interpr%C3%A8te_(informatique)) construit à partir de la librairie Python : [ply](https://pypi.org/project/ply/)
### Structure
Il se sépare en 4 fichiers distincts :

#### `lexer_rules.py`
Lexique du langage créé. Sert à définir les mots-clés et symboles qui permettent de construire un programme d'instructions.

#### `parser_rules.py`
Grammaire du langage créé. Définition des assemblages de symboles distribués par le lexique. Il régit la syntaxe du langage.

#### `evals.py`
Contextes de traduction et d'exécution, des instructions et expressions renvoyées par le parser. Dans notre cas en Python.

#### `interpreter.py`
L'interpréteur. Met à disposition un prompt afin d'écrire du code dans le langage créé. À exécution, le code est lu par le parser.### Fonctionnalités
Le langage propose différentes fonctionnalités clé que l'on pourrait retrouver dans un langage classique.


### Variables
**assignation**: [nom] **=** [valeur] \
ex : `a = 5; ou b = (1+2);`

**assignation avec opérateur**: [nom] ***=** [valeur] ou [nom] **/=** [valeur] \
ex : `a *= 5; ou b /= (1+2);`

**assignation multiple**: [nom],[nom],[nom] *=* [valeur],[valeur],[valeur] \
ex : `a, b, c = 1, 2, 3;`

**incrémentation**: [nom] **+=** [valeur] **ou** [nom]**++** \
ex : `a += 5; ou b++;`

**décrémentation**: [nom] **-=** [valeur] **ou** [nom]-- \
ex : `a -= 5; ou b--;`

**utilisation**: [nom] **=** [nom] \
ex : `a = b + 1;`

### Affichage
print: **print**(valeur); \
ex : `print(12+4);`

sprint : **sprint**(string); \
ex : `sprint("hello world");`

### Conditions
**condition simple**: **if**(condition) { instructions } \
ex : `if(a == 2) { print(5); }`

**sinon**: **else** { instructions } \
ex : `else { print(5); } ou else print(5);`

**combinaison**: **if**(condition) { instructions } **else** { instructions } \
ex : 
```
if(a==2) {
        print(5);
} else {
    sprint("condition non vérifiée");
}
```
ou

```
if(a==2) {
    print(5);
} 
else if(a==3) {
    sprint("condition non vérifiée");
}
```

### Boucles
**boucle for**:  
**for**(*assignation*; *condition*; *incrémentation*) { *instructions* } \
ex : 
```
counter = 0;
for(i = 0; i < 5; i+=1) {
    counter++;
}
```
**boucle while**:  
**while**(*condition*) { *instructions* } \
ex : 
```
counter = 0;
while(counter <= 10) {
    print(counter);
    counter++;
}
```

### Tableaux
**déclaration**: [nom] **=** [valeur1, valeur2...] \
ex : `my_array = [1,2,3,4];`

**accès à une case**: nom[index] \
ex: `a = array[2];`

**ajouter une valeur**: [nom].**push**(valeur) \
ex: `array = [1,2]; array.push(3);`

**retirer la dernière valeur**: [nom].**pop**() \
ex: `array = [1,2,3]; array.pop();` \
output : array = [1, 2]

**insérer à un indice donné**: [nom].**insert**(indice, valeur) \
ex: `array = [1,2,3]; array.pop();` \
output : array = [1, 2]

**concaténer deux tableaux**: [nom].**concat**(array) \
ex: 
```
array.concat([1,2,3]);
ou
array2 = [2,3,4];
array.concat(array2);
```
output: array = [1,2,3,2,3,4]

**fusionner + trier deux tableaux**: *merge_sort*(array1, array2)
ex: 
```
array1 = [1,2,3];
array2 = [4,2,1];
merge_sort(array1, array2); 
```
output: array = [1,1,2,2,3,4]


### Fonctions: 
*Les fonctions peuvent être signées comme void, elles vont donc principalement servir à éxécuter des instructions, elles peuvent contenir un return (ou non) qui fera coupe-circuit, elles peuvent être signées comme val, auquel cas elles devront retourner une valeur à l'appelant. Une fonction peut en appeler une autre, ou s'appeler elle-même.* 

**déclaration**: \
*fonction void*: **def void [nom] (paramètres) { instructions }** \
ex: 
```
def void mafonction() {
    print(1);
    return;
}
```
ou 
```
def void mafonction(param1, param2) {
    print(param1 + param2);
}
```
appeler la fonction: 
```
mafonction(); ou mafonction(2, 5); ou mafonction(a, b);
```
*fonction valeur*: **def val [nom] (paramètres) { instructions }** \
ex: 
```
def val mafonction() {
    print(1);
    return 0; 
}
```
ou 
```
def val mafonction(param1, param2) {
    return param1 + param2;
}
```
appeler une fonction:
```
a = mafonction(5, 10);
print(mafonction(a, b)); 
if(mafonction(5, 10) == 15) {
    ...
}
```
## Pile

Pour ce projet il était nécessaire de mettre en place une [pile d'exécution](https://fr.wikipedia.org/wiki/Pile_d%27ex%C3%A9cution).

La pile, sous forme d'une liste Python, se base sur deux principes : `append()` (pour ajouter une instruction dans la pile et l'éxecuter), et `pop()` (quand l'exécution est terminée, l'enlever de la pile).

Dans notre projet, la pile se sert de deux méthodes : 

`push_and_execute()` : Est la méthode qui permet d'automatiser le principe LIFO (Last In First Out) de la pile. Elle pousse l'instruction prise en paramètres, l'exécute et la libère de la pile.

`empty_function_call()`: Est la méthode qui permet de libérer la pile des instructions d'appels de fonction quand elles rencontrent un `return`.