# Reto de práctica Factorial C — Evaluaciones de desempeño

Ejemplo resuelto. La estructura refleja las cuatro páginas de Figma del guion de la hora 1 de la ronda 3: Encuadre del problema, Flujo central, Diseño, Lo que no construí. Este es el más turbio de los tres verticales. No hay un "bucle central" obvio como sí lo tienen el fichaje o la aprobación de ausencias, así que el trabajo de encuadre carga con casi todo el peso. Si clavas la definición del problema aquí, la pantalla es fácil. Si te la saltas, diseñarás un formulario precioso que nadie rellena con honestidad.

> **Leyenda de marcas**
> 🚩 **JUGADA** — una acción táctica ensayable. Transferible a cualquier encargo. Interioriza esto, no el diseño concreto.
> ⭐ **DECISIÓN CLAVE** — la columna vertebral. Una decisión de la que cuelga toda la solución, defendible por tres vías (dolor del usuario, riesgo de negocio, qué enseña).

---

## El encargo (tal como te lo dan)

> El spinoff quiere ayudar a las empresas a hacer evaluaciones de desempeño. Diseña la experiencia central. 60 minutos.

Este es el encargo más vago del conjunto, a propósito. "Evaluaciones de desempeño" es un problema de cultura disfrazado de problema de software. El candidato que empieza a dibujar un formulario de evaluación ya ha perdido. Todo el juego está en decidir qué significa siquiera "evaluaciones de desempeño" para la v1 antes de tocar un componente.

---

## 0–8 min — Preguntas de aclaración (pregunta antes de abrir Figma)

> 🚩 **JUGADA** — Preguntas antes de Figma. Aunque el encargo diga "empieza a trabajar". Con un encargo tan vago, las preguntas no son cortesía opcional; son la única forma de hacer el problema diseñable.

Elige de 3 a 4. Cada una debe colapsar la ambigüedad en una dirección distinta.

1. "Evaluaciones de desempeño puede significar una evaluación anual, feedback continuo o seguimiento de objetivos. ¿Qué problema resolvemos para la v1? Implican productos muy distintos." Les fuerza la decisión de alcance, y muestra que sabes que no son lo mismo.
2. "¿Para quién es la v1: el empleado evaluado, el manager que escribe las evaluaciones, o el admin de RRHH que opera el ciclo?" Tres usuarios, tres productos otra vez.
3. "¿El trabajo doloroso es escribir la evaluación, u operar el ciclo para que las evaluaciones se hagan de verdad, a tiempo y con justicia?" Separa el problema de documento del problema de operaciones.
4. "¿Optimizamos para calidad de la evaluación, para tasa de finalización, o para reducir sesgos? Puedo diseñar para uno con limpieza."

> 🚩 **JUGADA** — Nombra la rama oculta en voz alta. Desempeño está cargado de ramas de delegación, calibración, visibilidad y justicia. Sacar una muestra que ves la realidad política, no solo el formulario.

Rama oculta que nombrar en voz alta:
"Antes de diseñar nada aclararía quién puede ver una evaluación. Uno mismo, el manager, el manager del manager, RRHH. Las reglas de visibilidad no son un ajuste atornillado después; moldean lo que la gente está dispuesta a escribir, así que son parte del diseño central."

Para este ejemplo resuelto, asume: **la v1 es el manager escribiendo una evaluación durante un ciclo de toda la empresa, el trabajo doloroso es completar evaluaciones justas a tiempo, optimiza para tasa de finalización y calidad de la evaluación a la vez, la visibilidad por defecto es empleado más cadena de mando más RRHH.**

---

## 8–18 min — Encuadre del problema (página 1 de Figma, déjala visible)

**¿Quién es el usuario principal?**
El manager, a mitad de ciclo, con seis evaluaciones que entregar el viernes y una semana llena de trabajo real. No el admin de RRHH que configura el ciclo, no el empleado que lee el resultado. El manager es donde las evaluaciones triunfan o fracasan, porque una evaluación sin escribir o hecha a toda prisa es el modo de fallo que vuelve inútil todo el producto.

**¿El único trabajo que genera más fricción o coste?**
Escribir una evaluación específica y justa cuando el manager no recuerda qué pasó en febrero. La fricción no es el formulario. Es la página en blanco más la mala memoria más la presión de tiempo, que juntas producen evaluaciones vagas, sesgadas por lo reciente, que no ayudan a nadie y que el empleado resiente.

**Éxito frente a fracaso.**
Éxito: el manager escribe una evaluación específica, anclada en evidencias, en una sola sesión concentrada, y la entrega a tiempo. Fracaso: el manager mira en blanco una escala de puntuación, escribe "gran compañero de equipo, sigue así" desde el recuerdo de la última semana, y la evaluación erosiona la confianza de forma activa.

**El bucle central.**
> 🚩 **JUGADA** — Cuando el bucle no es obvio, dilo y defínelo. Los dominios turbios premian al candidato que impone un bucle en lugar de fingir que se lo dieron.

Aquí no hay bucle diario; esto es un ciclo periódico, no un hábito. El bucle es por evaluación: abrir una evaluación, recordar la evidencia, valorar contra unas pocas dimensiones, escribir lo específico, entregar. El problema de diseño es hacer que esa única sesión produzca una buena evaluación pese a la memoria imperfecta.

**Frontera del MVP.**
Dentro: la superficie de escritura del manager, con evidencia en pantalla para combatir la página en blanco y el sesgo de lo reciente. Fuera de la v1: autoevaluaciones, feedback de pares / 360, calibración, definición de objetivos, el admin de configuración del ciclo, analítica.

**El problema real frente al del encargo.**
> 🚩 **JUGADA** — Separa el problema real del problema superficial del encargo. En este vertical es el reto entero. Los directores leen este párrafo con más atención porque el encargo casi no les dio nada.

El encargo dice "ayudar a las empresas a hacer evaluaciones de desempeño", lo que suena a un motor de formularios y flujo: escalas de puntuación, enrutado, plazos. El problema real es que las evaluaciones son de baja calidad porque los managers las escriben de memoria bajo presión de tiempo, y un motor de flujo no hace nada al respecto. Solo enruta evaluaciones malas más rápido. La palanca real es reducir la carga de recuerdo en el momento de escribir, para que la evaluación se ancle en lo que pasó en lugar de en lo que el manager recuerda de la última semana. Resuelve el recuerdo y la calidad llega sola. Construye el flujo y habrás automatizado la producción de resentimiento.

---

## 18–30 min — Estructura antes que pantallas (página 2 de Figma, cajas y flechas)

**Punto de entrada:** el manager recibe una notificación del ciclo, "6 evaluaciones para el 12 de julio", y aterriza en una lista de sus reportes directos a evaluar. Llega bajo presión de plazo.

**Los 3 a 5 pasos por evaluación:**
1. Abrir la evaluación de una persona.
2. Recordar: la pantalla saca a la superficie evidencia del periodo (objetivos cumplidos, notas de 1:1 pasados, feedback previo, menciones de pares si las hay) para que el manager no empiece en blanco.
3. Valorar contra un conjunto pequeño de dimensiones, pocas a propósito.
4. Escribir lo específico, con la evidencia justo ahí para referenciarla.
5. Entregar, con una comprobación ligera que avisa de una sección vacía o sospechosamente pobre antes de que salga.

**Estados a diseñar:**
- Vista general del ciclo: quién ha terminado, quién está pendiente, plazo.
- Evaluación en blanco (el estado enemigo): nunca debe sentirse como una página en blanco.
- En curso, guardada: los managers escriben evaluaciones en varias sesiones, así que el estado borrador es central, no un lujo.
- Aviso de evaluación pobre: un empujón suave cuando una sección está vacía o tiene una línea.
- Entregada, bloqueada.

**Lo que el manager tiene al final:**
Evaluaciones específicas, ancladas en evidencias, entregadas a tiempo, que estaría cómodo leyendo en voz alta al empleado.

Decisión a registrar en esta página: **evidencia-junto-a-la-escritura, no un formulario en blanco con un plazo.** Un formulario en blanco más una fecha límite es el statu quo de hoja de cálculo y documento de Word con una barra de progreso añadida. La apuesta estructural es que la evaluación se escribe junto a la evidencia, no de memoria.

---

## 30–50 min — Diseña el flujo central (página 3 de Figma)

> 🚩 **JUGADA** — Una pantalla real abierta en el minuto 35. Este es el vertical donde más riesgo tienes de sobreencuadrar, porque el trabajo de problema es muy rico. Pon un alto duro y abre la pantalla aunque el encuadre se sienta sin terminar.

Construye una pantalla bien: **la superficie de escritura de una sola evaluación del manager, evidencia a un lado, escritura al otro.**

Maquetación, dos paneles:
- Panel izquierdo, evidencia (el diferenciador): los objetivos del empleado para el periodo y su estado, momentos destacados con fecha sacados de notas de 1:1, feedback previo dado durante el ciclo, menciones de pares si están en alcance. Escaneable, con marca de tiempo, para que el manager vea febrero además de la última semana.
- Panel derecho, la evaluación: un número pequeño de dimensiones, no una rúbrica larga. Cada una es un prompt corto más un campo de texto, no una mera puntuación de 1 a 5. Los prompts piden lo específico: "¿Qué entregó este periodo? Apunta a algo concreto."
- Cada elemento de evidencia se puede referenciar dentro de la evaluación con una acción, de modo que escribir queda anclado por defecto.
- Pie: Guardar borrador (siempre visible, los borradores son esperados), y Entregar con la comprobación de evaluación pobre.

Anotaciones en la pantalla:
- "El panel de evidencia es la apuesta central. Combate la página en blanco y el sesgo de lo reciente, que son las causas reales de las malas evaluaciones."
- "Dimensiones pocas a propósito. Más dimensiones bajan la finalización y la calidad, no las suben."
- "Los prompts piden lo específico por encima de las puntuaciones. Las puntuaciones sin evidencia son donde se esconde el sesgo."
- "El modelo de puntuación se muestra ligero. Si la empresa usa una escala numérica siquiera es una decisión de configuración del ciclo, fuera de alcance aquí."
- "La visibilidad es empleado más cadena de mando más RRHH. La visibilidad configurable está nombrada, no diseñada."

> ⭐ **DECISIÓN CLAVE** — **Evidencia junto a la escritura, no un formulario en blanco con un plazo.** El manager escribe cada sección junto a evidencia con fecha de todo el periodo, así la evaluación queda anclada por construcción en lugar de sacada del recuerdo de la última semana. Defiéndela por tres vías: dolor del usuario (la página en blanco bajo plazo es lo que los managers temen y hacen mal), riesgo de negocio (evaluaciones vagas sesgadas por lo reciente erosionan la confianza y vuelven inútil todo el producto), aprendizaje (valida si anclar el momento de escritura sube la calidad, la métrica de la que depende cualquier otra función de desempeño).

---

## 50–60 min — Lo que no construí (página 4 de Figma)

1. **Autoevaluaciones y feedback de pares / 360.** Reales y discutiblemente esenciales para la justicia, pero cada una es una superficie de entrada aparte. La v1 demuestra primero el problema de escritura del manager; las otras se enchufan al mismo modelo de evidencia luego.
2. **Calibración.** La conversación de justicia entre managers. Un problema genuinamente difícil y un contexto de usuario distinto. Aplazado a propósito, no olvidado.
3. **Definición de objetivos.** Los objetivos aparecen aquí como evidencia, solo lectura. Crearlos es una superficie continua aparte, no parte del momento de evaluación.
4. **Configuración del ciclo.** El producto del admin de RRHH: dimensiones, plazos, reglas de visibilidad, recordatorios. Usuario distinto, sesión aparte.
5. **Analítica y reporting.** Lo que RRHH hace con las evaluaciones completadas. Aguas abajo, fuera de alcance para demostrar la experiencia de escritura central.

> 🚩 **JUGADA** — "Si tuviera dos horas más." Nombra el siguiente problema real y admite el límite actual. La señal de staff que la mayoría se salta.

"Si tuviera dos horas más, diseñaría el camino de captura de evidencia que corre a lo largo del año, el registro ligero de notas de 1:1 y feedback que alimenta este panel. Ahora mismo asumo que esa evidencia existe; el riesgo honesto es que sin un hábito de captura durante todo el año el panel está vacío, y entonces la v1 vuelve a ser un formulario en blanco. Esa dependencia es lo primero que validaría."

Guarda una o dos para las preguntas. No lo anticipes todo.

---

## Hora 2 — orden de narración (no presentes el resultado)

1. **"Así leí el problema."** Para Jonathan: las malas evaluaciones se escriben de memoria bajo plazo, no ayudan a nadie y dañan en silencio la confianza entre manager y empleado, y una empresa que hace evaluaciones mal está peor que una que no las hace. Encuadra el coste.
2. **"Esto es lo que elegí resolver."** "Evaluaciones de desempeño" podría significar cinco productos. Lo acoté al manager escribiendo evaluaciones durante un ciclo, y el problema real debajo es el recuerdo, no el flujo. Despioricé autoevaluaciones, calibración y el producto de admin a propósito.
3. **"Esta es la estructura antes de la UI."** Evidencia-junto-a-la-escritura frente a un formulario en blanco con un plazo, y por qué: un motor de flujo solo enruta evaluaciones malas más rápido.
4. **"Esto es lo que diseñé y por qué."** El panel de evidencia es la apuesta. Compromiso: mantuve las dimensiones deliberadamente pocas, cambiando completitud de rúbrica por finalización y honestidad.
5. **"Esto es lo que falta."** Todo esto depende de que exista evidencia durante todo el año. Es el supuesto más arriesgado y lo primero que validaría antes de seguir construyendo.

**Preguntas probables del panel y la línea que clavar:**
- Marta, "¿Por qué esto como MVP?" Tres ejes: dolor del usuario (la temida página en blanco bajo plazo), riesgo de negocio (evaluaciones vagas erosionan la confianza y desperdician el ciclo entero), potencial de aprendizaje (valida si anclar el momento de escritura sube la calidad, de la que depende cualquier otra función de desempeño). No "me pareció el alcance correcto".
- Alberto, "¿Cómo escala esto al crecer la complejidad?" La evaluación se compone de componentes de dimensión alimentados por un modelo de evidencia. Autoevaluaciones, feedback de pares y objetivos son entradas adicionales al mismo modelo, no pantallas nuevas. La visibilidad es una propiedad de cada sección, así que añadir visibilidad configurable o calibración extiende la estructura en lugar de romperla. Aquí es donde mantener pocas dimensiones y el modelo limpio compone.
- Jonathan, "¿Cómo mejora esto los resultados de negocio?" Las evaluaciones se completan de verdad a tiempo y son lo bastante específicas para ser útiles, así que la empresa obtiene señal real sobre su gente en lugar de relleno tipo "gran compañero de equipo", y los empleados confían en el proceso en lugar de resentirlo. Eso es retención y credibilidad del manager, no papeleo.
- Compensación, si surge: "Eso depende de dónde encaje esto en vuestro marco. ¿Senior o Staff?" Luego 80K€ o 93K€. No ofrezcas primero.
