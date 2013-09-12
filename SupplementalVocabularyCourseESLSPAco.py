__author__ = 'vagrant'
# -*- coding: utf-8 -*-

from CourseConfiguration import courseConfiguration

projectName = "supplementalVocabCoursesESLSPAco"
languageDict = [
    ["x for Spanish speakers", "English"],
]
unitMap = {"Presentaciones y saludos": ["Meeting-and-Greeting-1",
                                        "Meeting-and-Greeting-2"],
           "Recibir ayuda en tu aprendizaje de lengua": ["Communication-Facilitation-1",
                                                         "Communication-Facilitation-2",
                                                         "Communication-Facilitation-3",
                                                         "Communication-Facilitation-4",
                                                         "Communication-Facilitation-5",
                                                         "Communication-Facilitation-6",
                                                         "Communication-Facilitation-7"],
           "Recibir más ayuda en tu aprendizaje de lengua": ["Language-Learning-Facilitation-1",
                                                             "Language-Learning-Facilitation-2",
                                                             "Translation-Facilitation"],
           "La conversación cortés": ["Polite-Conversation-1",
                                      "Polite-Conversation-2",
                                      "Polite-Conversation-3",
                                      "Useful-Expressions-1",
                                      "Useful-Expressions-2"],
           "Las formas geométricas y los colores": ["Shapes",
                                                    "Colors"],
           "La ropa": ["Clothing-1",
                       "Clothing-2",
                       "Clothing-3"],
           "Las compras y las tiendas": ["Shopping-Stores",
                                         "Shopping-1",
                                         "Shopping-2",
                                         "Shopping-3",
                                         "Shopping-4",
                                         "Shopping-5"],
           "La casa y el apartamento": ["House-Apartment-1",
                                        "House-Apartment-2"],
           "Habitaciones de la casa": ["Living-Room",
                                       "Dining-Room",
                                       "Kitchen",
                                       "Bathroom-1",
                                       "Bathroom-2",
                                       "Bedroom"],
           "La familia": ["Family-1",
                          "Family-2",
                          "Family-3",
                          "Family-4"],
           "La oficina y las profesiones": ["Office-1",
                                            "Office-2",
                                            "Professions-1",
                                            "Professions-2"],
           "Las partes del cuerpo": ["Parts-of-the-Body-1",
                                     "Parts-of-the-Body-2"],
           "Emergencias": ["Emergencies-1",
                           "Emergencies-2",
                           "Emergencies-3",
                           "Emergencies-4",
                           "Emergencies-5"],
           "Los lugares y preguntar el camino": ["Places-1",
                                                 "Places-2",
                                                 "Asking-for-Directions-1",
                                                 "Asking-for-Directions-2"],
           "La escuela": ["School-1",
                          "School-2",
                          "School-3"],
           "Los instrumentos musicales": ["Musical-Instruments-1",
                                          "Musical-Instruments-2"],
           "Los deportes": ["Recreation-1",
                            "Recreation-2",
                            "Recreation-3"],
           "La naturaleza": ["Nature-1",
                             "Nature-2"],
           "Los animales": ["Animals-1",
                            "Animals-2"],
           "La comida 1": ["Meals",
                           "Beverages",
                           "Fruit",
                           "Vegetables",
                           "Grains"],
           "La comida 2": ["Dairy",
                           "Meat",
                           "Seafood",
                           "Spices-Condiments",
                           "Dessert"],
           "Ir a un restaurante": ["At-the-Restaurant-1",
                                   "At-the-Restaurant-2",
                                   "At-the-Restaurant-3",
                                   "At-the-Restaurant-4",
                                   "At-the-Restaurant-5"],
           "Los idiomas": ["Languages-1",
                           "Languages-2",
                           "Languages-3",
                           "Languages-4"],
           "Los países": ["Continents",
                          "Countries-1",
                          "Countries-2",
                          "Countries-3"],
           "Viajar": ["Travel-1",
                      "Travel-2",
                      "Travel-3",
                      "Travel-4",
                      "Travel-5"],
           "Comprar billetes": ["Buying-Tickets-1",
                                "Buying-Tickets-2",
                                "Buying-Tickets-3"],
           "Tomar un taxi": ["Taking-a-Taxi-1",
                             "Taking-a-Taxi-2",
                             "Taking-a-Taxi-3"],
           "Alojarse en un hotel": ["At-the-Hotel-1",
                                    "At-the-Hotel-2",
                                    "At-the-Hotel-3",
                                    "At-the-Hotel-4"],
           "Ir al banco": ["Going-to-the-Bank-1",
                           "Going-to-the-Bank-2",
                           "Going-to-the-Bank-3",
                           "Going-to-the-Bank-4"],
           "Los números": ["Numbers-Cardinal-1",
                           "Numbers-Cardinal-2",
                           "Numbers-Cardinal-3",
                           "Numbers-Cardinal-4",
                           "Numbers-Ordinal",
                           "Numbers-Other"],
           "Los días de la semana": ["Days-of-the-Week-1",
                                     "Days-of-the-Week-2",
                                     "Time-1",
                                     "Time-2",
                                     "Asking-the-Time"],
           "Las estaciones y el tiempo": ["Months",
                                          "Seasons",
                                          "Weather-1",
                                          "Weather-2"],
           "Pronombres personales y  adjetivos posesivos": ["Personal-Pronouns",
                                                            "Possessive-Adjectives",
                                                            "Conjunctions"],
           "Los adjetivos y los adverbios": ["Adjectives-1",
                                             "Adjectives-2",
                                             "Adjectives-3",
                                             "Adverbs"],
           "Los verbos": ["Verbs-1",
                          "Verbs-2",
                          "Verbs-3",
                          "Verbs-4",
                          "Verbs-5",
                          "Verbs-6",
                          "Verbs-7",
                          "Verbs-8"],
           "Preposiciones": ["Prepositions-1",
                             "Prepositions-2",
                             "Prepositions-3",
                             "Prepositions-4"],
}
unitNameList = [
    "Presentaciones y saludos",
    "Recibir ayuda en tu aprendizaje de lengua",
    "Recibir más ayuda en tu aprendizaje de lengua",
    "La conversación cortés",
    "Las formas geométricas y los colores",
    "La ropa",
    "Las compras y las tiendas",
    "La casa y el apartamento",
    "Habitaciones de la casa",
    "La familia",
    "La oficina y las profesiones",
    "Las partes del cuerpo",
    "Emergencias",
    "Los lugares y preguntar el camino",
    "La escuela",
    "Los instrumentos musicales",
    "Los deportes",
    "La naturaleza",
    "Los animales",
    "La comida 1",
    "La comida 2",
    "Ir a un restaurante",
    "Los idiomas",
    "Los países",
    "Viajar",
    "Comprar billetes",
    "Tomar un taxi",
    "Alojarse en un hotel",
    "Ir al banco",
    "Los números",
    "Los días de la semana",
    "Las estaciones y el tiempo",
    "Pronombres personales y  adjetivos posesivos",
    "Los adjetivos y los adverbios",
    "Los verbos",
    "Preposiciones",
]
unitObjectives = {
    "Presentaciones y saludos": u"""Esta unidad enseña palabras y frases útiles relacionadas con las presentaciones y los saludos.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Recibir ayuda en tu aprendizaje de lengua": u"""Esta unidad enseña palabras y frases útiles relacionadas con recibir ayuda en tu aprendizaje de lengua.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Recibir más ayuda en tu aprendizaje de lengua": u"""Esta unidad enseña palabras y frases útiles relacionadas con recibir más ayuda en tu aprendizaje de lengua.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "La conversación cortés": u"""Esta unidad enseña palabras y frases útiles relacionadas con la conversación cortés.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Las formas geométricas y los colores": u"""Esta unidad enseña palabras y frases útiles relacionadas con las formas geométricas y los colores.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "La ropa": u"""Esta unidad enseña palabras y frases útiles relacionadas con la ropa.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Las compras y las tiendas": u"""Esta unidad enseña palabras y frases útiles relacionadas con las compras y las tiendas.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "La casa y el apartamento": u"""Esta unidad enseña palabras y frases útiles relacionadas con la casa y el apartamento.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Habitaciones de la casa": u"""Esta unidad enseña palabras y frases útiles relacionadas con habitaciones de la casa.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "La familia": u"""Esta unidad enseña palabras y frases útiles relacionadas con la familia.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "La oficina y las profesiones": u"""Esta unidad enseña palabras y frases útiles relacionadas con la oficina y las profesiones.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Las partes del cuerpo": u"""Esta unidad enseña palabras y frases útiles relacionadas con las partes del cuerpo.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Emergencias": u"""Esta unidad enseña palabras y frases útiles relacionadas con emergencias.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Los lugares y preguntar el camino": u"""Esta unidad enseña palabras y frases útiles relacionadas con los lugares y preguntar el camino.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "La escuela": u"""Esta unidad enseña palabras y frases útiles relacionadas con la escuela.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Los instrumentos musicales": u"""Esta unidad enseña palabras y frases útiles relacionadas con los instrumentos musicales.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Los deportes": u"""Esta unidad enseña palabras y frases útiles relacionadas con los deportes.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "La naturaleza": u"""Esta unidad enseña palabras y frases útiles relacionadas con la naturaleza.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Los animales": u"""Esta unidad enseña palabras y frases útiles relacionadas con los animales.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "La comida 1": u"""Esta unidad enseña palabras y frases útiles relacionadas con la comida.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "La comida 2": u"""Esta unidad enseña palabras y frases útiles relacionadas con la comida.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Ir a un restaurante": u"""Esta unidad enseña palabras y frases útiles relacionadas con ir a un restaurante.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Los idiomas": u"""Esta unidad enseña palabras y frases útiles relacionadas con los idiomas.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Los países": u"""Esta unidad enseña palabras y frases útiles relacionadas con los países.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Viajar": u"""Esta unidad enseña palabras y frases útiles relacionadas con viajar.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Comprar billetes": u"""Esta unidad enseña palabras y frases útiles relacionadas con comprar billetes.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Tomar un taxi": u"""Esta unidad enseña palabras y frases útiles relacionadas con tomar un taxi.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Alojarse en un hotel": u"""Esta unidad enseña palabras y frases útiles relacionadas con alojarse en un hotel.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Ir al banco": u"""Esta unidad enseña palabras y frases útiles relacionadas con ir al banco.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Los números": u"""Esta unidad enseña palabras y frases útiles relacionadas con los números.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Los días de la semana": u"""Esta unidad enseña palabras y frases útiles relacionadas con los días de la semana.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Las estaciones y el tiempo": u"""Esta unidad enseña palabras y frases útiles relacionadas con las estaciones y el tiempo.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Pronombres personales y  adjetivos posesivos": u"""Esta unidad enseña palabras y frases útiles relacionadas con los pronombres personales y los adjetivos posesivos.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Los adjetivos y los adverbios": u"""Esta unidad enseña palabras y frases útiles relacionadas con los adjetivos y los adverbios.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Los verbos": u"""Esta unidad enseña palabras y frases útiles relacionadas con los verbos.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    "Preposiciones": u"""Esta unidad enseña palabras y frases útiles relacionadas con las preposiciones.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
}

lessonOrder = unitMap



# unitNumbers = {
#     "Presentaciones y saludos": 1,
#     "Recibir ayuda en tu aprendizaje de lengua": 2,
#     "Recibir más ayuda en tu aprendizaje de lengua": 3,
#     "La conversación cortés": 4,
#     "Las formas geométricas y los colores": 5,
#     "La ropa": 6,
#     "Las compras y las tiendas": 7,
#     "La casa y el apartamento": 8,
#     "Habitaciones de la casa": 9,
#     "La familia": 10,
#     "La oficina y las profesiones": 11,
#     "Las partes del cuerpo": 12,
#     "Emergencias": 13,
#     "Los lugares y preguntar el camino": 14,
#     "La escuela": 15,
#     "Los instrumentos musicales": 16,
#     "Los deportes": 17,
#     "La naturaleza": 18,
#     "Los animales": 19,
#     "La comida 1": 20,
#     "La comida 2": 21,
#     "Ir a un restaurante": 22,
#     "Los idiomas": 23,
#     "Los países": 24,
#     "Viajar": 25,
#     "Comprar billetes": 26,
#     "Tomar un taxi": 27,
#     "Alojarse en un hotel": 28,
#     "Ir al banco": 29,
#     "Los números": 30,
#     "Los días de la semana": 31,
#     "Las estaciones y el tiempo": 32,
#     "Pronombres personales y  adjetivos posesivos": 33,
#     "Los adjetivos y los adverbios": 34,
#     "Los verbos": 35,
#     "Preposiciones": 36,
# }
isESLTrue = True
lessonNameToListNameMap = {
    "Adjectives-1": "Los adjetivos 1",
    "Adjectives-2": "Los adjetivos 2",
    "Adjectives-3": "Los adjetivos 3",
    "Adverbs": "Los adverbios",
    "Animals-1": "Los animales 1",
    "Animals-2": "Los animales 2",
    "Asking-for-Directions-1": "Preguntar el camino 1",
    "Asking-for-Directions-2": "Preguntar el camino 2",
    "Asking-the-Time": "Preguntar la hora",
    "At-the-Hotel-1": "En el hotel 1",
    "At-the-Hotel-2": "En el hotel 2",
    "At-the-Hotel-3": "En el hotel 3",
    "At-the-Hotel-4": "En el hotel 4",
    "At-the-Restaurant-1": "El restaurante 1",
    "At-the-Restaurant-2": "El restaurante 2",
    "At-the-Restaurant-3": "El restaurante 3",
    "At-the-Restaurant-4": "El restaurante 4",
    "At-the-Restaurant-5": "El restaurante 5",
    "Bathroom-1": "El baño 1",
    "Bathroom-2": "El baño 2",
    "Bedroom": "El dormitorio",
    "Beverages": "Las bebidas",
    "Buying-Tickets-1": "Comprar billetes 1",
    "Buying-Tickets-2": "Comprar billetes 2",
    "Buying-Tickets-3": "Comprar billetes 3",
    "Clothing-1": "La ropa 1",
    "Clothing-2": "La ropa 2",
    "Clothing-3": "La ropa 3",
    "Colors": "Los colores",
    "Communication-Facilitation-1": "Frases para facilitar la comunicación 1",
    "Communication-Facilitation-2": "Frases para facilitar la comunicación 2",
    "Communication-Facilitation-3": "Frases para facilitar la comunicación 3",
    "Communication-Facilitation-4": "Frases para facilitar la comunicación 4",
    "Communication-Facilitation-5": "Frases para facilitar la comunicación 5",
    "Communication-Facilitation-6": "Frases para facilitar la comunicación 6",
    "Communication-Facilitation-7": "Frases para facilitar la comunicación 7",
    "Conjunctions": "Las conjunciones",
    "Continents": "Los continentes",
    "Countries-1": "Los países 1",
    "Countries-2": "Los países 2",
    "Countries-3": "Los países 3",
    "Dairy": "Los productos lacteos",
    "Days-of-the-Week-1": "Los días de la semana 1",
    "Days-of-the-Week-2": "Los días de la semana 2",
    "Dessert": "Los postres",
    "Dining-Room": "El comedor",
    "Emergencies-1": "Emergencias 1",
    "Emergencies-2": "Emergencias 2",
    "Emergencies-3": "Emergencias 3",
    "Emergencies-4": "Emergencias 4",
    "Emergencies-5": "Emergencias 5",
    "Family-1": "La familia 1",
    "Family-2": "La familia 2",
    "Family-3": "La familia 3",
    "Family-4": "La familia 4",
    "Fruit": "Las frutas",
    "Going-To-the-Bank-1": "Ir al banco 1",
    "Going-To-the-Bank-2": "Ir al banco 2",
    "Going-To-the-Bank-3": "Ir al banco 3",
    "Going-To-the-Bank-4": "Ir al banco 4",
    "Grains": "Los cereales",
    "House-Apartment-1": "La casa 1",
    "House-Apartment-2": "La casa 2",
    "Kitchen": "La cocina",
    "Language-Learning-Facilitation-1": "Frases para facilitar el aprendizaje de un idioma 1",
    "Language-Learning-Facilitation-2": "Frases para facilitar el aprendizaje de un idioma 2",
    "Languages-1": "Los idiomas 1",
    "Languages-2": "Los idiomas 2",
    "Languages-3": "Los idiomas 3",
    "Languages-4": "Los idiomas 4",
    "Living-Room": "La sala",
    "Meals": "Las comidas",
    "Meat": "La carne",
    "Meeting-and-Greeting-1": "Presentaciones y Saludos 1",
    "Meeting-and-Greeting-2": "Presentaciones y Saludos 2",
    "Months": "Los meses",
    "Musical-Instruments-1": "Los instrumentos musicales 1",
    "Musical-Instruments-2": "Los instrumentos musicales 2",
    "Nature-1": "La naturaleza 1",
    "Nature-2": "La naturaleza 2",
    "Numbers-Cardinal-1": "Los números Cardinales 1",
    "Numbers-Cardinal-2": "Los números Cardinales 2",
    "Numbers-Cardinal-3": "Los números Cardinales 3",
    "Numbers-Cardinal-4": "Los números Cardinales 4",
    "Numbers-Ordinal": "Los números Ordinales",
    "Numbers-Other": "Los números Otros",
    "Office-1": "La oficina 1",
    "Office-2": "La oficina 2",
    "Parts-of-the-Body-1": "Las partes del cuerpo 1",
    "Parts-of-the-Body-2": "Las partes del cuerpo 2",
    "Personal-Pronouns": "Pronombres personales",
    "Places-1": "Los lugares 1",
    "Places-2": "Los lugares 2",
    "Polite-Conversation-1": "La conversación cortés 1",
    "Polite-Conversation-2": "La conversación cortés 2",
    "Polite-Conversation-3": "La conversación cortés 3",
    "Possessive-Adjectives": "Los determinantes posesivos",
    "Prepositions-1": "Preposiciones 1",
    "Prepositions-2": "Preposiciones 2",
    "Prepositions-3": "Preposiciones 3",
    "Prepositions-4": "Preposiciones 4",
    "Professions-1": "Las profesiones 1",
    "Professions-2": "Las profesiones 2",
    "Recreation-1": "Los deportes 1",
    "Recreation-2": "Los deportes 2",
    "Recreation-3": "Los deportes 3",
    "School-1": "La escuela 1",
    "School-2": "La escuela 2",
    "School-3": "La escuela 3",
    "Seafood": "Los mariscos",
    "Seasons": "Las estaciones",
    "Shapes": "Las formas geométricas",
    "Shopping-1": "Las compras 1",
    "Shopping-2": "Las compras 2",
    "Shopping-3": "Las compras 3",
    "Shopping-4": "Las compras 4",
    "Shopping-5": "Las compras 5",
    "Shopping-Stores": "Las compras Las tiendas",
    "Spices-Condiments": "Los condimentos y las especias",
    "Taking-a-Taxi-1": "Tomar un taxi 1",
    "Taking-a-Taxi-2": "Tomar un taxi 2",
    "Taking-a-Taxi-3": "Tomar un taxi 3",
    "Time-1": "La hora 1",
    "Time-2": "La hora 2",
    "Translation-Facilitation": "Frases para facilitar la traducción",
    "Travel-1": "Viajar 1",
    "Travel-2": "Viajar 2",
    "Travel-3": "Viajar 3",
    "Travel-4": "Viajar 4",
    "Travel-5": "Viajar 5",
    "Useful-Expressions-1": "Las expresiones útiles 1",
    "Useful-Expressions-2": "Las expresiones útiles 2",
    "Vegetables": "Las verduras",
    "Verbs-1": "Los verbos 1",
    "Verbs-2": "Los verbos 2",
    "Verbs-3": "Los verbos 3",
    "Verbs-4": "Los verbos 4",
    "Verbs-5": "Los verbos 5",
    "Verbs-6": "Los verbos 6",
    "Verbs-7": "Los verbos 7",
    "Verbs-8": "Los verbos 8",
    "Weather-1": "El tiempo 1",
    "Weather-2": "El tiempo 2",
}


def createSVCConfiguration():
    """
    takes the above information and builds a course object for the rest of the scripts

    :return: a filled out course object
    """
    configObject = courseConfiguration()
    configObject.projectName = projectName
    configObject.unitNameList = unitNameList
    configObject.languageDict = languageDict
    configObject.unitMap = unitMap
    configObject.unitObjectives = unitObjectives
    configObject.lessonOrder = lessonOrder
    configObject.unitNumbers = configObject.createUnitNumbers(unitNameList)
    configObject.lessonToList = lessonNameToListNameMap
    configObject.isESLTrue = isESLTrue
    configObject.unitNumberToNames = configObject.createUnitNumberToNames(unitNameList)

    return configObject