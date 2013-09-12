__author__ = 'vagrant'
# -*- coding: utf-8 -*-

from CourseConfiguration import courseConfiguration

projectName = "supplementalVocabCoursesESLSPAco"
languageDict = [
    ["x for Spanish speakers", "English"],
]
unitMap = {u"Presentaciones y saludos": ["Meeting-and-Greeting-1",
                                        "Meeting-and-Greeting-2"],
           u"Recibir ayuda en tu aprendizaje de lengua": ["Communication-Facilitation-1",
                                                         "Communication-Facilitation-2",
                                                         "Communication-Facilitation-3",
                                                         "Communication-Facilitation-4",
                                                         "Communication-Facilitation-5",
                                                         "Communication-Facilitation-6",
                                                         "Communication-Facilitation-7"],
           u"Recibir más ayuda en tu aprendizaje de lengua": ["Language-Learning-Facilitation-1",
                                                             "Language-Learning-Facilitation-2",
                                                             "Translation-Facilitation"],
           u"La conversación cortés": ["Polite-Conversation-1",
                                      "Polite-Conversation-2",
                                      "Polite-Conversation-3",
                                      "Useful-Expressions-1",
                                      "Useful-Expressions-2"],
           u"Las formas geométricas y los colores": ["Shapes",
                                                    "Colors"],
           u"La ropa": ["Clothing-1",
                       "Clothing-2",
                       "Clothing-3"],
           u"Las compras y las tiendas": ["Shopping-Stores",
                                         "Shopping-1",
                                         "Shopping-2",
                                         "Shopping-3",
                                         "Shopping-4",
                                         "Shopping-5"],
           u"La casa y el apartamento": ["House-Apartment-1",
                                        "House-Apartment-2"],
           u"Habitaciones de la casa": ["Living-Room",
                                       "Dining-Room",
                                       "Kitchen",
                                       "Bathroom-1",
                                       "Bathroom-2",
                                       "Bedroom"],
           u"La familia": ["Family-1",
                          "Family-2",
                          "Family-3",
                          "Family-4"],
           u"La oficina y las profesiones": ["Office-1",
                                            "Office-2",
                                            "Professions-1",
                                            "Professions-2"],
           u"Las partes del cuerpo": ["Parts-of-the-Body-1",
                                     "Parts-of-the-Body-2"],
           u"Emergencias": ["Emergencies-1",
                           "Emergencies-2",
                           "Emergencies-3",
                           "Emergencies-4",
                           "Emergencies-5"],
           u"Los lugares y preguntar el camino": ["Places-1",
                                                 "Places-2",
                                                 "Asking-for-Directions-1",
                                                 "Asking-for-Directions-2"],
           u"La escuela": ["School-1",
                          "School-2",
                          "School-3"],
           u"Los instrumentos musicales": ["Musical-Instruments-1",
                                          "Musical-Instruments-2"],
           u"Los deportes": ["Recreation-1",
                            "Recreation-2",
                            "Recreation-3"],
           u"La naturaleza": ["Nature-1",
                             "Nature-2"],
           u"Los animales": ["Animals-1",
                            "Animals-2"],
           u"La comida 1": ["Meals",
                           "Beverages",
                           "Fruit",
                           "Vegetables",
                           "Grains"],
           u"La comida 2": ["Dairy",
                           "Meat",
                           "Seafood",
                           "Spices-Condiments",
                           "Dessert"],
           u"Ir a un restaurante": ["At-the-Restaurant-1",
                                   "At-the-Restaurant-2",
                                   "At-the-Restaurant-3",
                                   "At-the-Restaurant-4",
                                   "At-the-Restaurant-5"],
           u"Los idiomas": ["Languages-1",
                           "Languages-2",
                           "Languages-3",
                           "Languages-4"],
           u"Los países": ["Continents",
                          "Countries-1",
                          "Countries-2",
                          "Countries-3"],
           u"Viajar": ["Travel-1",
                      "Travel-2",
                      "Travel-3",
                      "Travel-4",
                      "Travel-5"],
           u"Comprar billetes": ["Buying-Tickets-1",
                                "Buying-Tickets-2",
                                "Buying-Tickets-3"],
           u"Tomar un taxi": ["Taking-a-Taxi-1",
                             "Taking-a-Taxi-2",
                             "Taking-a-Taxi-3"],
           u"Alojarse en un hotel": ["At-the-Hotel-1",
                                    "At-the-Hotel-2",
                                    "At-the-Hotel-3",
                                    "At-the-Hotel-4"],
           u"Ir al banco": ["Going-to-the-Bank-1",
                           "Going-to-the-Bank-2",
                           "Going-to-the-Bank-3",
                           "Going-to-the-Bank-4"],
           u"Los números": ["Numbers-Cardinal-1",
                           "Numbers-Cardinal-2",
                           "Numbers-Cardinal-3",
                           "Numbers-Cardinal-4",
                           "Numbers-Ordinal",
                           "Numbers-Other"],
           u"Los días de la semana": ["Days-of-the-Week-1",
                                     "Days-of-the-Week-2",
                                     "Time-1",
                                     "Time-2",
                                     "Asking-the-Time"],
           u"Las estaciones y el tiempo": ["Months",
                                          "Seasons",
                                          "Weather-1",
                                          "Weather-2"],
           u"Pronombres personales y  adjetivos posesivos": ["Personal-Pronouns",
                                                            "Possessive-Adjectives",
                                                            "Conjunctions"],
           u"Los adjetivos y los adverbios": ["Adjectives-1",
                                             "Adjectives-2",
                                             "Adjectives-3",
                                             "Adverbs"],
           u"Los verbos": ["Verbs-1",
                          "Verbs-2",
                          "Verbs-3",
                          "Verbs-4",
                          "Verbs-5",
                          "Verbs-6",
                          "Verbs-7",
                          "Verbs-8"],
           u"Preposiciones": ["Prepositions-1",
                             "Prepositions-2",
                             "Prepositions-3",
                             "Prepositions-4"],
}
unitNameList = [
    u"Presentaciones y saludos",
    u"Recibir ayuda en tu aprendizaje de lengua",
    u"Recibir más ayuda en tu aprendizaje de lengua",
    u"La conversación cortés",
    u"Las formas geométricas y los colores",
    u"La ropa",
    u"Las compras y las tiendas",
    u"La casa y el apartamento",
    u"Habitaciones de la casa",
    u"La familia",
    u"La oficina y las profesiones",
    u"Las partes del cuerpo",
    u"Emergencias",
    u"Los lugares y preguntar el camino",
    u"La escuela",
    u"Los instrumentos musicales",
    u"Los deportes",
    u"La naturaleza",
    u"Los animales",
    u"La comida 1",
    u"La comida 2",
    u"Ir a un restaurante",
    u"Los idiomas",
    u"Los países",
    u"Viajar",
    u"Comprar billetes",
    u"Tomar un taxi",
    u"Alojarse en un hotel",
    u"Ir al banco",
    u"Los números",
    u"Los días de la semana",
    u"Las estaciones y el tiempo",
    u"Pronombres personales y  adjetivos posesivos",
    u"Los adjetivos y los adverbios",
    u"Los verbos",
    u"Preposiciones",
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
    u"Recibir ayuda en tu aprendizaje de lengua": u"""Esta unidad enseña palabras y frases útiles relacionadas con recibir ayuda en tu aprendizaje de lengua.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Recibir más ayuda en tu aprendizaje de lengua": u"""Esta unidad enseña palabras y frases útiles relacionadas con recibir más ayuda en tu aprendizaje de lengua.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"La conversación cortés": u"""Esta unidad enseña palabras y frases útiles relacionadas con la conversación cortés.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Las formas geométricas y los colores": u"""Esta unidad enseña palabras y frases útiles relacionadas con las formas geométricas y los colores.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"La ropa": u"""Esta unidad enseña palabras y frases útiles relacionadas con la ropa.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Las compras y las tiendas": u"""Esta unidad enseña palabras y frases útiles relacionadas con las compras y las tiendas.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"La casa y el apartamento": u"""Esta unidad enseña palabras y frases útiles relacionadas con la casa y el apartamento.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Habitaciones de la casa": u"""Esta unidad enseña palabras y frases útiles relacionadas con habitaciones de la casa.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"La familia": u"""Esta unidad enseña palabras y frases útiles relacionadas con la familia.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"La oficina y las profesiones": u"""Esta unidad enseña palabras y frases útiles relacionadas con la oficina y las profesiones.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Las partes del cuerpo": u"""Esta unidad enseña palabras y frases útiles relacionadas con las partes del cuerpo.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Emergencias": u"""Esta unidad enseña palabras y frases útiles relacionadas con emergencias.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Los lugares y preguntar el camino": u"""Esta unidad enseña palabras y frases útiles relacionadas con los lugares y preguntar el camino.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"La escuela": u"""Esta unidad enseña palabras y frases útiles relacionadas con la escuela.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Los instrumentos musicales": u"""Esta unidad enseña palabras y frases útiles relacionadas con los instrumentos musicales.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Los deportes": u"""Esta unidad enseña palabras y frases útiles relacionadas con los deportes.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"La naturaleza": u"""Esta unidad enseña palabras y frases útiles relacionadas con la naturaleza.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Los animales": u"""Esta unidad enseña palabras y frases útiles relacionadas con los animales.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"La comida 1": u"""Esta unidad enseña palabras y frases útiles relacionadas con la comida.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"La comida 2": u"""Esta unidad enseña palabras y frases útiles relacionadas con la comida.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Ir a un restaurante": u"""Esta unidad enseña palabras y frases útiles relacionadas con ir a un restaurante.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Los idiomas": u"""Esta unidad enseña palabras y frases útiles relacionadas con los idiomas.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Los países": u"""Esta unidad enseña palabras y frases útiles relacionadas con los países.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Viajar": u"""Esta unidad enseña palabras y frases útiles relacionadas con viajar.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Comprar billetes": u"""Esta unidad enseña palabras y frases útiles relacionadas con comprar billetes.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Tomar un taxi": u"""Esta unidad enseña palabras y frases útiles relacionadas con tomar un taxi.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Alojarse en un hotel": u"""Esta unidad enseña palabras y frases útiles relacionadas con alojarse en un hotel.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Ir al banco": u"""Esta unidad enseña palabras y frases útiles relacionadas con ir al banco.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Los números": u"""Esta unidad enseña palabras y frases útiles relacionadas con los números.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Los días de la semana": u"""Esta unidad enseña palabras y frases útiles relacionadas con los días de la semana.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Las estaciones y el tiempo": u"""Esta unidad enseña palabras y frases útiles relacionadas con las estaciones y el tiempo.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Pronombres personales y  adjetivos posesivos": u"""Esta unidad enseña palabras y frases útiles relacionadas con los pronombres personales y los adjetivos posesivos.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Los adjetivos y los adverbios": u"""Esta unidad enseña palabras y frases útiles relacionadas con los adjetivos y los adverbios.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Los verbos": u"""Esta unidad enseña palabras y frases útiles relacionadas con los verbos.

Esta unidad te ayudará a

- memorizar palabras y frases relacionadas con el tema
- aprender a leer y escribir las palabras y frases
- reconocer sonidos y a poder pronunciarlos correctamente

Empieza con actividades como Comparacion de idiomas y Practica de la pronunciacion para que te ayude a familiarizarte con el material.

Continúa con las actividades de opción múltiple activadas con la voz y las actividades de relacionar para reforzar el recuerdo de las palabras y frases.

Luego completa las actividades de dictado y de escritura para practicar la producción y la escritura en la lengua.

Finalmente, completa las actividades de asesoramiento al final de la unidad para comprobar tu conocimiento de las palabras o frases."

""",
    u"Preposiciones": u"""Esta unidad enseña palabras y frases útiles relacionadas con las preposiciones.

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
    u"Adjectives-1": u"Los adjetivos 1",
    u"Adjectives-2": u"Los adjetivos 2",
    u"Adjectives-3": u"Los adjetivos 3",
    u"Adverbs": u"Los adverbios",
    u"Animals-1": u"Los animales 1",
    u"Animals-2": u"Los animales 2",
    u"Asking-for-Directions-1": u"Preguntar el camino 1",
    u"Asking-for-Directions-2": u"Preguntar el camino 2",
    u"Asking-the-Time": u"Preguntar la hora",
    u"At-the-Hotel-1": u"En el hotel 1",
    u"At-the-Hotel-2": u"En el hotel 2",
    u"At-the-Hotel-3": u"En el hotel 3",
    u"At-the-Hotel-4": u"En el hotel 4",
    u"At-the-Restaurant-1": u"El restaurante 1",
    u"At-the-Restaurant-2": u"El restaurante 2",
    u"At-the-Restaurant-3": u"El restaurante 3",
    u"At-the-Restaurant-4": u"El restaurante 4",
    u"At-the-Restaurant-5": u"El restaurante 5",
    u"Bathroom-1": u"El baño 1",
    u"Bathroom-2": u"El baño 2",
    u"Bedroom": u"El dormitorio",
    u"Beverages": u"Las bebidas",
    u"Buying-Tickets-1": u"Comprar billetes 1",
    u"Buying-Tickets-2": u"Comprar billetes 2",
    u"Buying-Tickets-3": u"Comprar billetes 3",
    u"Clothing-1": u"La ropa 1",
    u"Clothing-2": u"La ropa 2",
    u"Clothing-3": u"La ropa 3",
    u"Colors": u"Los colores",
    u"Communication-Facilitation-1": u"Frases para facilitar la comunicación 1",
    u"Communication-Facilitation-2": u"Frases para facilitar la comunicación 2",
    u"Communication-Facilitation-3": u"Frases para facilitar la comunicación 3",
    u"Communication-Facilitation-4": u"Frases para facilitar la comunicación 4",
    u"Communication-Facilitation-5": u"Frases para facilitar la comunicación 5",
    u"Communication-Facilitation-6": u"Frases para facilitar la comunicación 6",
    u"Communication-Facilitation-7": u"Frases para facilitar la comunicación 7",
    u"Conjunctions": u"Las conjunciones",
    u"Continents": u"Los continentes",
    u"Countries-1": u"Los países 1",
    u"Countries-2": u"Los países 2",
    u"Countries-3": u"Los países 3",
    u"Dairy": u"Los productos lacteos",
    u"Days-of-the-Week-1": u"Los días de la semana 1",
    u"Days-of-the-Week-2": u"Los días de la semana 2",
    u"Dessert": u"Los postres",
    u"Dining-Room": u"El comedor",
    u"Emergencies-1": u"Emergencias 1",
    u"Emergencies-2": u"Emergencias 2",
    u"Emergencies-3": u"Emergencias 3",
    u"Emergencies-4": u"Emergencias 4",
    u"Emergencies-5": u"Emergencias 5",
    u"Family-1": u"La familia 1",
    u"Family-2": u"La familia 2",
    u"Family-3": u"La familia 3",
    u"Family-4": u"La familia 4",
    u"Fruit": u"Las frutas",
    u"Going-To-the-Bank-1": u"Ir al banco 1",
    u"Going-To-the-Bank-2": u"Ir al banco 2",
    u"Going-To-the-Bank-3": u"Ir al banco 3",
    u"Going-To-the-Bank-4": u"Ir al banco 4",
    u"Grains": u"Los cereales",
    u"House-Apartment-1": u"La casa 1",
    u"House-Apartment-2": u"La casa 2",
    u"Kitchen": u"La cocina",
    u"Language-Learning-Facilitation-1": u"Frases para facilitar el aprendizaje de un idioma 1",
    u"Language-Learning-Facilitation-2": u"Frases para facilitar el aprendizaje de un idioma 2",
    u"Languages-1": u"Los idiomas 1",
    u"Languages-2": u"Los idiomas 2",
    u"Languages-3": u"Los idiomas 3",
    u"Languages-4": u"Los idiomas 4",
    u"Living-Room": u"La sala",
    u"Meals": u"Las comidas",
    u"Meat": u"La carne",
    u"Meeting-and-Greeting-1": u"Presentaciones y Saludos 1",
    u"Meeting-and-Greeting-2": u"Presentaciones y Saludos 2",
    u"Months": u"Los meses",
    u"Musical-Instruments-1": u"Los instrumentos musicales 1",
    u"Musical-Instruments-2": u"Los instrumentos musicales 2",
    u"Nature-1": u"La naturaleza 1",
    u"Nature-2": u"La naturaleza 2",
    u"Numbers-Cardinal-1": u"Los números Cardinales 1",
    u"Numbers-Cardinal-2": u"Los números Cardinales 2",
    u"Numbers-Cardinal-3": u"Los números Cardinales 3",
    u"Numbers-Cardinal-4": u"Los números Cardinales 4",
    u"Numbers-Ordinal": u"Los números Ordinales",
    u"Numbers-Other": u"Los números Otros",
    u"Office-1": u"La oficina 1",
    u"Office-2": u"La oficina 2",
    u"Parts-of-the-Body-1": u"Las partes del cuerpo 1",
    u"Parts-of-the-Body-2": u"Las partes del cuerpo 2",
    u"Personal-Pronouns": u"Pronombres personales",
    u"Places-1": u"Los lugares 1",
    u"Places-2": u"Los lugares 2",
    u"Polite-Conversation-1": u"La conversación cortés 1",
    u"Polite-Conversation-2": u"La conversación cortés 2",
    u"Polite-Conversation-3": u"La conversación cortés 3",
    u"Possessive-Adjectives": u"Los determinantes posesivos",
    u"Prepositions-1": u"Preposiciones 1",
    u"Prepositions-2": u"Preposiciones 2",
    u"Prepositions-3": u"Preposiciones 3",
    u"Prepositions-4": u"Preposiciones 4",
    u"Professions-1": u"Las profesiones 1",
    u"Professions-2": u"Las profesiones 2",
    u"Recreation-1": u"Los deportes 1",
    u"Recreation-2": u"Los deportes 2",
    u"Recreation-3": u"Los deportes 3",
    u"School-1": u"La escuela 1",
    u"School-2": u"La escuela 2",
    u"School-3": u"La escuela 3",
    u"Seafood": u"Los mariscos",
    u"Seasons": u"Las estaciones",
    u"Shapes": u"Las formas geométricas",
    u"Shopping-1": u"Las compras 1",
    u"Shopping-2": u"Las compras 2",
    u"Shopping-3": u"Las compras 3",
    u"Shopping-4": u"Las compras 4",
    u"Shopping-5": u"Las compras 5",
    u"Shopping-Stores": u"Las compras Las tiendas",
    u"Spices-Condiments": u"Los condimentos y las especias",
    u"Taking-a-Taxi-1": u"Tomar un taxi 1",
    u"Taking-a-Taxi-2": u"Tomar un taxi 2",
    u"Taking-a-Taxi-3": u"Tomar un taxi 3",
    u"Time-1": u"La hora 1",
    u"Time-2": u"La hora 2",
    u"Translation-Facilitation": u"Frases para facilitar la traducción",
    u"Travel-1": u"Viajar 1",
    u"Travel-2": u"Viajar 2",
    u"Travel-3": u"Viajar 3",
    u"Travel-4": u"Viajar 4",
    u"Travel-5": u"Viajar 5",
    u"Useful-Expressions-1": u"Las expresiones útiles 1",
    u"Useful-Expressions-2": u"Las expresiones útiles 2",
    u"Vegetables": u"Las verduras",
    u"Verbs-1": u"Los verbos 1",
    u"Verbs-2": u"Los verbos 2",
    u"Verbs-3": u"Los verbos 3",
    u"Verbs-4": u"Los verbos 4",
    u"Verbs-5": u"Los verbos 5",
    u"Verbs-6": u"Los verbos 6",
    u"Verbs-7": u"Los verbos 7",
    u"Verbs-8": u"Los verbos 8",
    u"Weather-1": u"El tiempo 1",
    u"Weather-2": u"El tiempo 2",
}
isTranslit = False

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
    configObject.isTranslit = isTranslit

    return configObject