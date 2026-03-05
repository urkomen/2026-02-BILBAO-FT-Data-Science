# Variables iniciales
vidas = 0 # Vidas de usuario (al llegar a 6 muere)
lista_letras = [] # Lista de letras usadas

titulo = [
" ███████╗ █████╗      ██████╗  █████╗ ███╗   ███╗███████╗███████╗",
" ██╔════╝██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝",
" █████╗  ███████║    ██║  ███╗███████║██╔████╔██║█████╗  ███████╗",
" ██╔══╝  ██╔══██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║",
" ███████╗██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║",
" ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝",
"                                                                  ",
"                         EL AHORCADO                              "
]

victoria = [
"██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗ ",
"██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗",
"██║   ██║██║██║        ██║   ██║   ██║██████╔╝██║███████║",
"╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║",
" ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║",
"  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝",
    ]

derrota = [
"███████╗ ███████╗██████╗ ██████╗ ██████╗  ██████╗ ████████╗ █████╗ ",
"██╔═══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗",
"██║   ██║█████╗  ██████╔╝██████╔╝██████╔╝██║   ██║   ██║   ███████║",
"██║   ██║██╔══╝  ██╔══██╗██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══██║",
"███████╔╝███████╗██║  ██║██║  ██║██║  ██║╚██████╔╝   ██║   ██║  ██║",
"╚══════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝",
]

AHORCADO_0 ='''
     +----+
          |
          |
          |
          |
          |
    =========
    '''


AHORCADO = [
    '''
     +----+
     |    |
          |
          |
          |
          |
    =========
    ''',
    '''
     +----+
     |    |
     O    |
          |
          |
          |
    =========
    ''',
    '''
     +----+
     |    |
     O    |
     |    |
          |
          |
    =========
    ''',
    '''
     +----+
     |    |
     O    |
    /|\   |
          |
          |
    =========
    ''',
    '''
     +----+
     |    |
     O    |
    /|\   |
    / \   |
          |
    =========
    ''',
    '''
     +----+
     |    |
    [O]   |
    /|\   |
    / \   |
          |
    =========
    '''
]

PALABRAS_2000 = [
'casa','perro','gato','arbol','coche','camino','ventana','puerta','silla','mesa',
'libro','lapiz','papel','cielo','nube','lluvia','viento','fuego','tierra','agua',
'mar','rio','bosque','montana','ciudad','pueblo','campo','flor','hoja','rama',
'sol','luna','estrella','noche','dia','sombra','luz','fuerza','piedra','arena',
'playa','costa','barco','puerto','isla','oceano','laguna','charco','cascada','sendero',
'caminar','correr','saltar','nadar','volar','gritar','reir','llorar','pensar','soñar',
'vivir','morir','crecer','caer','abrir','cerrar','romper','crear','buscar','encontrar',
'seguir','parar','mirar','escuchar','hablar','callar','sentir','tocar','oler','gustar',
'comer','beber','cocinar','limpiar','ordenar','construir','pintar','escribir','leer','contar',
'jugar','ganar','perder','luchar','viajar','descansar','trabajar','estudiar','aprender','enseñar',
'amigo','enemigo','familia','madre','padre','hermano','hermana','hijo','hija','abuelo',
'abuela','tio','tia','primo','prima','vecino','vecina','jefe','jefa','compañero',
'persona','hombre','mujer','nino','nina','adulto','joven','anciano','gente','grupo',
'animal','planta','insecto','pez','ave','mamifero','reptil','serpiente','tigre','leon',
'elefante','jirafa','mono','oso','lobo','zorro','conejo','raton','caballo','vaca',
'oveja','cerdo','gallina','pato','ganso','aguila','halcon','paloma','cuervo','lagarto',
'cocodrilo','tortuga','delfin','ballena','tiburon','pulpo','calamar','cangrejo','langosta','medusa',
'rojo','azul','verde','amarillo','negro','blanco','gris','morado','rosa','naranja',
'marron','claro','oscuro','brillante','suave','duro','frio','caliente','templado','helado',
'feliz','triste','enojado','asustado','sorprendido','cansado','aburrido','emocionado','tranquilo','nervioso',
'rapido','lento','alto','bajo','grande','pequeno','ancho','estrecho','corto','largo',
'nuevo','viejo','bonito','feo','caro','barato','simple','complejo','famoso','desconocido',
'verdad','mentira','justicia','injusticia','paz','guerra','orden','caos','libertad','prision',
'amor','odio','alegria','miedo','esperanza','desesperacion','valor','honor','orgullo','verguenza',
'cuerpo','cabeza','brazo','pierna','mano','pie','ojo','oreja','nariz','boca',
'diente','espalda','pecho','corazon','cerebro','hueso','sangre','piel','pelo','uña',
'escuela','colegio','universidad','clase','examen','tarea','profesor','alumno','libreta','mochila',
'computadora','teclado','raton','pantalla','telefono','tablet','internet','pagina','correo','mensaje',
'musica','cancion','melodia','ritmo','instrumento','guitarra','piano','bateria','violin','trompeta',
'cine','pelicula','actor','actriz','escena','camara','teatro','obra','guion','director',
'deporte','futbol','baloncesto','tenis','ciclismo','natacion','boxeo','karate','yoga','gimnasia',
'tienda','mercado','supermercado','panaderia','fruteria','carniceria','farmacia','banco','hotel','restaurante',
'comida','pan','carne','pescado','fruta','verdura','arroz','pasta','huevo','leche',
'queso','mantequilla','aceite','sal','azucar','cafe','te','vino','cerveza','agua',
'ropa','camisa','pantalon','zapato','abrigo','chaqueta','falda','vestido','sombrero','bufanda',
'herramienta','martillo','destornillador','llave','sierra','taladro','clavo','tornillo','tuerca','cable',
'tiempo','segundo','minuto','hora','dia','semana','mes','ano','siglo','momento',
'historia','cultura','arte','ciencia','tecnologia','matematica','fisica','quimica','biologia','geografia',
'energia','materia','atomo','molecula','celula','organismo','ecosistema','planeta','estrella','galaxia',
'viaje','ruta','mapa','brujula','maleta','pasaporte','avion','tren','barco','autobus',
'emocion','sensacion','pensamiento','idea','concepto','teoria','practica','experimento','analisis','logica',
'jardin','parque','plaza','calle','avenida','carretera','puente','tunel','edificio','torre',
'herrero','carpintero','panadero','pescador','agricultor','doctor','enfermero','ingeniero','arquitecto','abogado',
'fabrica','oficina','empresa','negocio','mercancia','producto','servicio','cliente','proveedor','empleado',
'juego','carta','dado','tablero','ficha','puzzle','reto','nivel','puntuacion','victoria',
'invierno','primavera','verano','otonio','clima','tormenta','huracan','terremoto','sequía','inundacion',
'metal','madera','plastico','vidrio','piedra','cuero','tela','algodon','lana','acero',
'motor','rueda','freno','volante','asiento','ventilador','bateria','cable','tubo','valvula',
'poesia','cuento','novela','autor','lector','pagina','capitulo','titulo','editor','biblioteca',
'religion','mito','leyenda','ritual','templo','iglesia','dios','espiritu','creencia','moral',
'politica','gobierno','ley','derecho','voto','partido','ministro','presidente','senado','parlamento',
'economia','dinero','precio','mercado','impuesto','salario','ahorro','gasto','credito','deuda',
'industria','mineria','agricultura','ganaderia','comercio','transporte','energia','turismo','educacion','salud',
'robot','programa','codigo','algoritmo','sistema','red','servidor','base','dato','archivo',
'virus','bacteria','vacuna','sintoma','diagnostico','tratamiento','hospital','clinica','medico','paciente',
'pintura','escultura','dibujo','color','forma','textura','perspectiva','cuadro','galeria','museo',
'fiesta','baile','musico','cantante','grupo','escenario','luces','sonido','publico','evento',
'montana','valle','colina','desierto','sabana','jungla','selva','glaciar','volcan','crater',
'carrera','competicion','equipo','jugador','entrenador','arbitro','regla','campo','marcador','gol',
'cocina','horno','sarten','olla','cuchillo','tenedor','cuchara','plato','vaso','taza',
'emocion','caracter','personalidad','memoria','atencion','creatividad','inteligencia','motivacion','habito','costumbre',
'fabrica','industria','produccion','cadena','logistica','almacen','transporte','envio','paquete','contenedor',
'marco','foto','imagen','icono','simbolo','señal','codigo','clave','mensaje','texto',
'piedra','roca','minerales','cristal','diamante','oro','plata','cobre','hierro','carbon',
'universo','espacio','orbita','satellite','cohete','astronauta','nave','exploracion','sonda','telescopio',
'energia','fuerza','movimiento','velocidad','masa','peso','densidad','presion','temperatura','calor',
'cultura','tradicion','costumbre','idioma','lengua','dialecto','historia','memoria','patrimonio','identidad',
'emocion','risa','llanto','ira','calma','ansiedad','placer','dolor','confusion','claridad',
'pintor','escultor','artista','autor','director','productor','editor','critico','actor','actriz',
'mar','ola','marea','corriente','fondo','arena','coral','alga','pez','tiburon',
'bosque','arbol','tronco','hoja','raiz','semilla','fruto','flor','seta','musgo',
'ciudad','edificio','calle','avenida','plaza','parque','metro','autobus','trafico','peaton',
'jardin','flor','aroma','tierra','maceta','riego','poda','semilla','hoja','tallo',
'futuro','pasado','presente','recuerdo','plan','meta','objetivo','sueño','vision','proyecto',
'energia','solar','eolica','hidrica','nuclear','quimica','termica','mecanica','electrica','cinética',
'computadora','programa','archivo','carpeta','sistema','usuario','contraseña','seguridad','red','internet',
'juego','aventura','mision','enemigo','arma','nivel','poder','habilidad','tesoro','mapa',
'barco','vela','timón','ancla','cabo','proa','popa','casco','marinero','capitan',
'tren','vagon','locomotora','via','andén','billete','estacion','horario','ruta','destino',
'avion','ala','motor','cabina','piloto','vuelo','pista','torre','aeropuerto','equipaje',
'emocion','sensacion','intuicion','razon','logica','creencia','duda','certeza','opinion','decision',
'matematicas','suma','resta','multiplicacion','division','fraccion','ecuacion','variable','funcion','grafica',
'fisica','fuerza','energia','movimiento','velocidad','aceleracion','masa','densidad','presion','temperatura',
'quimica','atomo','molecula','reaccion','compuesto','elemento','mezcla','solucion','acido','base',
'biologia','celula','tejido','organo','sistema','organismo','especie','ecosistema','habitat','poblacion',
'geografia','mapa','region','clima','relieve','rio','montana','valle','costa','isla',
'historia','epoca','civilizacion','imperio','revolucion','batalla','rey','reina','gobierno','pueblo',
'arte','pintura','escultura','arquitectura','musica','danza','teatro','cine','literatura','poesia',
'economia','mercado','precio','oferta','demanda','produccion','consumo','ahorro','inversion','credito',
'politica','estado','ley','derecho','ciudadano','voto','partido','gobierno','parlamento','constitucion',
'salud','cuerpo','mente','nutricion','ejercicio','descanso','enfermedad','tratamiento','prevencion','bienestar',
'tecnologia','robot','inteligencia','algoritmo','software','hardware','red','servidor','base','dato',
'naturaleza','bosque','selva','desierto','oceano','montana','valle','pradera','glaciar','volcan',
'emocion','alegria','tristeza','miedo','ira','asco','sorpresa','calma','ansiedad','esperanza',
'trabajo','empleo','oficio','profesion','empresa','negocio','salario','contrato','jornada','equipo',
'viaje','ruta','destino','aventura','turismo','hotel','guia','mapa','maleta','pasaporte',
'hogar','casa','habitacion','cocina','bano','salon','jardin','terraza','garaje','pasillo',
'tienda','producto','precio','cliente','vendedor','carrito','compra','oferta','descuento','factura',
'musica','ritmo','melodia','armonía','instrumento','guitarra','piano','bateria','violin','voz',
'cine','pelicula','escena','actor','actriz','director','guion','camara','rodaje','estreno',
'deporte','equipo','jugador','entrenador','partido','gol','punto','marcador','victoria','derrota',
'cocina','receta','ingrediente','sabor','olor','textura','plato','horno','sarten','olla',
'emocion','sensacion','pensamiento','idea','concepto','creatividad','logica','razon','intuicion','decision',
'juego','tablero','carta','dado','ficha','puzzle','reto','nivel','puntuacion','victoria'
]