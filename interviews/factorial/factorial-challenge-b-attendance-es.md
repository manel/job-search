# Reto de práctica Factorial B — Tiempo y asistencia

Ejemplo resuelto. La estructura refleja las cuatro páginas de Figma del guion de la hora 1 de la ronda 3: Encuadre del problema, Flujo central, Diseño, Lo que no construí. Úsalo para ver el listón del razonamiento, no como guion. Este encargo tiene una trampa de alcance plantada en el enunciado; la solución muestra cómo nombrar la costura en lugar de diseñar las dos mitades.

> **Leyenda de marcas**
> 🚩 **JUGADA** — una acción táctica ensayable. Transferible a cualquier encargo. Interioriza esto, no el diseño concreto.
> ⭐ **DECISIÓN CLAVE** — la columna vertebral. Una decisión de la que cuelga toda la solución, defendible por tres vías (dolor del usuario, riesgo de negocio, qué enseña).

---

## El encargo (tal como te lo dan)

> El spinoff necesita fichaje de entrada y salida para trabajadores por horas y por turnos. Diseña la v1 de cómo un empleado registra su tiempo y cómo ese tiempo llega a nómina. 60 minutos.

> 🚩 **JUGADA** — Detecta la trampa de alcance en el enunciado. "Y cómo ese tiempo llega a nómina" dobla en silencio el alcance en dos superficies con dos usuarios distintos. Diseñar las dos es la jugada Senior. Nombra la costura y elige una.

La trampa es "y cómo ese tiempo llega a nómina". Eso dobla en silencio el alcance en dos superficies con dos usuarios distintos. Diseñar las dos es la jugada Senior. Nombra la costura y elige una.

---

## 0–8 min — Preguntas de aclaración (pregunta antes de abrir Figma)

> 🚩 **JUGADA** — Preguntas antes de Figma. Aunque el encargo diga "empieza a trabajar". Los candidatos senior resuelven el encargo; los staff lo reformulan primero.

1. "Plataforma: ¿estos trabajadores van en su móvil personal, en un kiosco o tablet compartido en el centro, o en escritorio? Un kiosco de almacén y un móvil en remoto son diseños distintos." La pregunta de mayor palanca. Falla aquí y el flujo entero está mal.
2. "El encargo menciona llevar el tiempo a nómina. Lo leo como una superficie aparte con un usuario distinto, el admin de nómina. ¿Para la v1 me centro en la experiencia de registro del empleado y defino la entrega, o la parte de nómina es la prioridad?" Aquí nombras la costura, sobre la mesa.
3. "¿Optimizamos para velocidad, para cumplimiento o para corregir errores? Un trabajador ficha cientos de veces al mes, así que la fricción se acumula; pero el registro legal tiene que aguantar."
4. "¿Puede un empleado editar su propia hoja de horas, o un manager aprueba las correcciones?" La rama de autoridad delegada, vestida de asistencia.

> 🚩 **JUGADA** — Nombra la rama oculta en voz alta. Sacar el peor fallo del mundo real sin que te lo pidan señala que ves más allá del camino feliz.

Rama oculta que nombrar en voz alta:
"El evento real de mayor fricción en este dominio es el olvido de fichar la salida. Lo diseñaré de forma explícita en lugar de tratarlo como caso límite, porque es el que genera disputas de nómina."

Para este ejemplo resuelto, asume: **tablet kiosco compartido en el centro de trabajo, foco en la experiencia de registro del empleado con una entrega a nómina definida, optimiza para velocidad más corrección de errores, el manager aprueba las correcciones.**

---

## 8–18 min — Encuadre del problema (página 1 de Figma, déjala visible)

**¿Quién es el usuario principal?**
El trabajador por turnos por horas en un kiosco compartido. Poca paciencia, posibles guantes o manos mojadas, a menudo con cola detrás en el cambio de turno. No un trabajador del conocimiento ante un portátil.

**¿El único trabajo que genera más fricción o coste?**
Registrar con precisión un inicio y un fin de turno en menos de unos segundos, y recuperarse con limpieza cuando se olvida. Aquí la precisión es dinero: cada registro erróneo es una corrección de nómina o una disputa más adelante.

**Éxito frente a fracaso.**
Éxito: el trabajador ficha entrada o salida con un toque, ve una confirmación instantánea e inequívoca, y el olvido de salida tiene un arreglo autoservicio rápido. Fracaso: estado ambiguo, el trabajador no está seguro de si quedó registrado, ficha doble o se lo salta, y nómina hereda el lío semanas después.

**El bucle central (diario):**
Llegar, identificarse, fichar entrada, recibir confirmación. Al revés al final del turno. Descansos si están en alcance. Eso es, cientos de veces al mes. Cada gramo de fricción se multiplica.

**Frontera del MVP.**
Dentro: la experiencia de fichaje de entrada y salida en el kiosco, confirmación instantánea, y la corrección del olvido de salida. Fuera de la v1: cálculo de nómina, planificación y asignación de turnos, reglas de horas extra, geolocalización, identidad biométrica.

**El problema real frente al del encargo.**
El encargo encuadra una tubería de captura de datos: registra el tiempo, envíalo a nómina. El problema real es la confianza y la velocidad en el momento de la captura. Un trabajador que no está seguro de que el toque quedó registrado es la causa raíz de cada disputa de nómina aguas abajo. Resuelve la certeza-en-un-toque y los datos de nómina están limpios por construcción. La entrega a nómina pasa entonces a ser una exportación aburrida y fiable, no un problema de diseño.

---

## 18–30 min — Estructura antes que pantallas (página 2 de Figma, cajas y flechas)

**Punto de entrada:** el trabajador se acerca al kiosco. La pantalla ya muestra el reloj, en reposo, lista. Sin muro de login como primera barrera.

**Los 3 a 5 pasos / decisiones:**
1. Identificarse (PIN o toque de tarjeta, rápido, no contraseña).
2. El sistema muestra el estado actual: estás FUERA, listo para fichar ENTRADA. O al revés.
3. Una acción primaria, dimensionada al estado actual.
4. Confirmación instantánea: grande, inequívoca, "Entrada a las 08:02, Maria."
5. Camino de excepción: "¿Olvidaste fichar la salida ayer?" sacado a la superficie cuando el sistema detecta un turno abierto.

**Estados a diseñar:**
- Reposo / listo (por defecto).
- Identificado, fuera, ofreciendo Fichar entrada.
- Identificado, dentro, ofreciendo Fichar salida.
- Confirmación (el estado más importante, debe ser imposible de malinterpretar).
- Turno abierto detectado: recuperación del olvido de salida.
- Sin conexión: el kiosco pierde la red. Encola el fichaje en local, confirma, sincroniza luego. Nómbralo aunque no esté dibujado del todo, porque un kiosco que falla en silencio cuando se cae el wifi es un desastre de nómina.

**Lo que el usuario tiene al final:**
Un fichaje registrado, confirmado y en el que confía, y un registro limpio que fluye a nómina sin limpieza humana.

Decisión a registrar: **estado-primero, acción primaria única.** El kiosco siempre muestra tu estado actual y ofrece exactamente una siguiente acción obvia, nunca entrada y salida como botones iguales. Compromiso nombrado: un paso de identificación cuesta un toque, pero permite al sistema mostrar la acción única correcta y elimina el error más común, fichar en la dirección equivocada.

---

## 30–50 min — Diseña el flujo central (página 3 de Figma)

> 🚩 **JUGADA** — Una pantalla real abierta en el minuto 35. Este es el vertical donde más riesgo tienes de sobreencuadrar, porque el trabajo de problema es tan rico. Pon un alto duro y abre la pantalla aunque el encuadre se sienta sin terminar.

Construye una pantalla bien: **el momento de confirmación del kiosco, con el estado identificado-dentro y la recuperación del olvido de salida como segundo frame.**

Kiosco, identificado, estado dentro:
- Saludo grande y estado actual: "Maria, estás dentro desde las 08:02."
- Un botón primario grande: Fichar salida. Dimensionado para el pulgar, alcanzable, alto contraste.
- Horas de hoy hasta ahora, pequeño, para tranquilizar.
- Tras el toque: confirmación a pantalla completa, "Salida a las 16:31. 8h 29m hoy." Vuelve a reposo a los pocos segundos para que el siguiente trabajador tenga una pantalla limpia.

Frame de recuperación del olvido de salida:
- Al identificarse, si se detecta un turno abierto de un día anterior: "No fichaste salida ayer. ¿A qué hora terminó tu turno?" con presets rápidos (hora de fin programada, o introducir a mano).
- La corrección se marca para aprobación del manager, no se acepta en silencio. Anotación: "Arreglo autoservicio, aprobado por manager. Equilibra velocidad y un registro auditable."

Anotaciones en la pantalla:
- "Kiosco, dispositivo compartido. La identidad es PIN o tarjeta, no contraseña. Biometría fuera de alcance para la v1."
- "La confirmación es la apuesta central: el trabajador nunca debe dudar si quedó registrado."
- "Los fichajes sin conexión se encolan en local y sincronizan. Lógica anotada, diseño completo aplazado."
- "Entrega a nómina: estos datos se exportan a la superficie de nómina. Esa superficie y su usuario están fuera de alcance, nombrados no diseñados."

**Restricción dura cumplida: una pantalla real abierta en el minuto 35.** Si sigues dibujando flujos, abre la pantalla de confirmación en bruto y refínala.

> ⭐ **DECISIÓN CLAVE** — **Estado-primero con acción única en lugar de un par simétrico de entrada y salida.** Cuesta un toque de identificación y elimina el error cotidiano más caro, fichar en la dirección equivocada en el cambio de turno cuando hay cola y nada de paciencia. Defiéndela por tres vías: dolor del usuario (velocidad y certeza bajo presión de cola), riesgo de negocio (cada fichaje ambiguo es una futura disputa de nómina), aprendizaje (valida si la certeza-en-un-toque reduce el volumen de correcciones).

---

## 50–60 min — Lo que no construí (página 4 de Figma)

1. **Cálculo de nómina y la superficie del admin.** La costura que nombré en el minuto 5. Usuario distinto, problema distinto. La v1 produce datos limpios y los exporta; diseñar el motor de nómina en 60 minutos sería superficial.
2. **Planificación y asignación de turnos.** Quién trabaja cuándo está aguas arriba del registro. Real, aparte, aplazado.
3. **Horas extra y reglas de descanso.** Lógica de cumplimiento que varía por país y contrato. Una capa de reglas, no una pantalla de v1.
4. **Geolocalización e identidad biométrica.** Funciones de adopción y anti-fraude. Importan una vez que el bucle de captura central tiene confianza, no antes.
5. **Panel de aprobación del manager.** Las correcciones se enrutan a un manager, pero su superficie de revisión es una pantalla aparte que diseñaría tras validar el lado del trabajador.

> 🚩 **JUGADA** — "Si tuviera dos horas más." Nombra el siguiente problema real y admite el límite actual. La señal de staff que la mayoría se salta.

"Si tuviera dos horas más, diseñaría bien el modelo de sin-conexión-y-sincronización. Un kiosco que pierde la conexión a mitad de turno y pierde fichajes en silencio es el fallo que destruye la confianza en todo el sistema, y ahora mismo solo lo he anotado, no lo he resuelto."

Guarda una o dos para las preguntas. No lo anticipes todo.

---

## Hora 2 — orden de narración (no presentes el resultado)

1. **"Así leí el problema."** Para Jonathan: el trabajador ficha cientos de veces al mes, cada toque ambiguo se convierte en una disputa de nómina semanas después, y las disputas cuestan tiempo de administración y confianza del trabajador. Encuadra el coste que el negocio paga ahora.
2. **"Esto es lo que elegí resolver."** El encargo decía registra-el-tiempo-y-envíalo-a-nómina. Partí esa costura y elegí el momento de captura, porque una captura limpia hace trivial la entrega a nómina y una captura sucia la hace imposible. Despioricé la superficie de nómina a propósito.
3. **"Esta es la estructura antes de la UI."** Estado-primero con acción única frente a un par simétrico, y por qué: elimina el fichaje en dirección equivocada, el error más común en el cambio de turno.
4. **"Esto es lo que diseñé y por qué."** La confirmación es la apuesta. La recuperación del olvido de salida está diseñada dentro, no tratada como caso límite, porque es el principal generador de disputas.
5. **"Esto es lo que falta."** El modelo de sin-conexión-y-sincronización es el hueco más arriesgado. Validaría que los fichajes sobreviven a una caída de conexión antes de lanzar nada.

**Preguntas probables del panel y la línea que clavar:**
- Marta, "¿Por qué esto como MVP?" Tres ejes: dolor del usuario (velocidad y certeza en el kiosco bajo presión de cola), riesgo de negocio (cada fichaje ambiguo es una futura disputa de nómina y un coste de administración), potencial de aprendizaje (valida si la certeza-en-un-toque reduce el volumen de correcciones, que es la métrica de la que vive o muere todo el producto).
- Alberto, "¿Cómo escala esto al crecer la complejidad?" El kiosco se renderiza desde un único modelo de estado de asistencia: dentro, fuera, turno-abierto, encolado-sin-conexión. Los descansos, las marcas de horas extra y la multi-ubicación extienden ese modelo de estado en lugar de añadir pantallas. La confirmación y el patrón estado-primero son reutilizables en cualquier superficie de fichaje, móvil o kiosco.
- Jonathan, "¿Cómo mejora esto los resultados de negocio?" Menos disputas de nómina, menos tiempo de administración reconciliando hojas de horas, y trabajadores que confían en que sus horas se registran bien. Convierte un coste recurrente de limpieza mensual en un no-evento.
- Compensación, si surge: "Eso depende de dónde encaje esto en vuestro marco. ¿Senior o Staff?" Luego 80K€ o 93K€. No ofrezcas primero.
