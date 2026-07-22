# Factorial — Ronda 3: Reto de diseño en directo

**Fecha:** Miércoles 2026-07-01, 10:00–12:00 CET
**Formato:** 2 horas. Hora 1: te dan el encargo, trabajo en solitario. Hora 2: se incorpora el panel, presentas el proceso, preguntas y respuestas.

---

## El panel

| Nombre | Rol | Mirada |
|---|---|---|
| Marta Serrano | Product Design Director | Criterio, calidad de las decisiones, razonamiento de producto |
| Alberto Martínez | Design Director (dominio Finanzas) | Pensamiento de sistemas, decisiones de diseño, madurez de DS. Viene del mundo DS en Prezi, habla tu idioma, no le expliques lo básico del oficio |
| Jonathan Centeno Mayado | Director of Growth (segundo empleado) | Resultados de producto, impacto de negocio, encuadre del usuario. No es diseñador. Encuádralo en resultados de usuario y de negocio |

**El encuadre de Marta en la Ronda 2:** buscan personas que construyen producto, no solo diseñadores, no solo ingenieros, no solo PMs. Alguien que disuelve las fronteras del rol y piensa en todo el producto. Esto debe aparecer en cómo narras el trabajo en la hora 2, no solo en lo que diseñas.

**Implicación:** esto no es una crítica de diseño. Es un panel multidisciplinar. Abre con problema e impacto de negocio, le funciona a todos, no solo a Jonathan. Luego pasa a estructura y decisiones. Si abres con vocabulario de diseño, te arriesgas a perder a media sala antes de haber defendido tu caso.

---

## Qué evalúa realmente esta ronda

No si eres capaz de producir un diseño pulido en 60 minutos. Evalúan:

1. ¿Haces preguntas de aclaración antes de tocar Figma, o te pones a diseñar sin más?
2. ¿Acotas el alcance con agresividad, o intentas diseñar el producto entero?
3. ¿Identificas el problema real que hay debajo del problema superficial del encargo?
4. ¿Nombras los compromisos de forma explícita, no "elegí esto" sino "elegí esto en lugar de X porque Y"?
5. ¿Muestras estructura a nivel de sistema antes de ir a la UI?
6. ¿Anotas lo que no construiste y por qué?

**El instrumento de nivelación:** usan esto para decidir Senior o Staff. Lo que produces en la hora 1 es la evidencia. La narración en la hora 2 es la prueba.

---

## Pool de dominios conocido

El reto saldrá de uno de los verticales del HRIS de Factorial. Formato confirmado por Marta: construir desde cero, definir el problema y diseñar la experiencia central. No es un encargo de "arregla este flujo roto".

- Tiempo y asistencia (fichaje, horarios, horas extra)
- Gestión de ausencias (solicitudes, aprobaciones, visibilidad de saldo)
- Nómina (cálculo, nóminas, correcciones)
- Reclutamiento / ATS (publicación de ofertas, pipeline, candidato)
- Onboarding (tareas, firma de documentos, progreso)
- Desempeño (evaluaciones, objetivos, 1:1s)
- Gastos (envío, aprobación, reporting)
- Estructura organizativa / jerarquía de empresa

El spinoff es de fase temprana. El dominio puede estar menos maduro, puede que estén probando si sabes definir qué cubre el MVP, no solo diseñar dentro de un producto ya establecido.

**La trampa:** intentar diseñar el producto entero. No lo hagas. Elige un usuario, un trabajo central, un flujo central. Nombra explícitamente lo que no estás construyendo.

---

## Guion de la hora 1

Usa este orden. No te saltes pasos.

### 0–8 min — Haz preguntas de aclaración antes de abrir Figma

Antes de tocar ninguna herramienta, haz de 3 a 5 preguntas afiladas. Aunque el encargo diga "empieza a trabajar".

Buenas preguntas:
- "¿Quién es la persona usuaria principal: responsable de RRHH, empleado o manager de equipo?"
- "¿Es greenfield o una extensión del producto actual de Factorial?"
- "¿Primero escritorio, o multiplataforma?"
- "¿Optimizamos para velocidad, cumplimiento normativo o reducción de errores?"
- "¿Alguna restricción sobre aprobaciones o permisos que deba conocer?"

Por qué importa: los candidatos senior resuelven el encargo. Los candidatos staff lo reformulan. Hacer preguntas afiladas antes de diseñar señala que la definición del problema es parte del trabajo, no algo dado.

Además: el encargo puede contener ambigüedad deliberada. Los flujos de RRHH y finanzas se expanden de forma natural hacia permisos, aprobaciones delegadas, excepciones, histórico de auditoría. El panel puede sondear esto a propósito. Cuando topes con una de esas ramas ocultas, nómbrala en voz alta: "Antes de cerrar este diseño, aclararía si la autoridad de aprobación es centralizada o delegada, eso cambia el flujo de forma significativa". Esa es la jugada.

### 8–18 min — Definir antes de diseñar

Abre una página de Figma titulada **"Encuadre del problema"**. Escribe las respuestas a esto antes de tocar ningún componente:

1. ¿Quién es el usuario principal? (responsable de RRHH, empleado, manager de equipo: elige uno, no te escabullas)
2. ¿Cuál es el único trabajo que necesita hacer en este dominio y que genera más fricción o coste?
3. ¿Cómo es el éxito para esa persona? ¿Cómo es el fracaso?
4. ¿Cuál es el bucle central? (Lo que hace cada día o cada semana, no los casos límite)
5. ¿Cuál es la frontera del MVP? ¿Qué incluye la v1 y qué deja fuera de forma explícita?
6. ¿Cuál es el problema real aquí frente al que nombra el encargo?

Los directores van a leer esta página. Déjala visible y legible.

### 18–30 min — Estructura antes que pantallas

Mapea el recorrido principal del usuario a nivel conceptual. Todavía sin UI.

- Punto de entrada: ¿cómo llega el usuario a este problema?
- Pasos: ¿cuáles son las 3 a 5 decisiones que toma?
- Estados: vacío, en curso, completado, error, casos límite
- Resultados: ¿qué tiene el usuario al final que no tenía al principio?

Cajas y flechas, bocetos low-fi. Las señales de staff viven aquí, no en los componentes.

### 30–50 min — Diseña el flujo central

Elige la 1 o 2 pantallas donde se resuelve el problema central. Ni onboarding, ni ajustes. La pantalla que carga más peso.

Acota de forma explícita: "Me centro en X porque ahí vive el problema central. Y y Z son reales, las nombraré como aplazadas".

Las anotaciones en el diseño son mejores que intentar cubrir todos los estados. Etiqueta con claridad: "solo el camino feliz, estados de error aplazados" o "móvil fuera de alcance".

**Restricción dura: en el minuto 35 debes tener al menos una pantalla real abierta, aunque esté en bruto.** El pensamiento de sistemas es tu ventaja comparativa y tu riesgo, bajo presión de tiempo puede convertirse en demasiado encuadre y poco artefacto. El panel necesita algo tangible al que reaccionar. Si en el minuto 35 sigues en diagramas de flujo, para y abre una pantalla.

### 50–60 min — Para y anota

Añade una página de Figma titulada **"Lo que no construí"**.

- Lista de 3 a 5 cosas que dejaste fuera de alcance de forma explícita
- Una línea de motivo para cada una
- Añade: "Si tuviera 2 horas más, haría X a continuación, porque..."

Esta es la señal de staff que la mayoría se salta. Anticípate a las objeciones de alcance evidentes, pero deja espacio para el debate. Las preguntas y respuestas son donde el razonamiento a nivel staff suele hacerse más visible, sobreanotarlo todo vuelve la presentación defensiva.

Si vas corto de tiempo, las notas de alcance en línea junto al flujo funcionan igual de bien. La prioridad es que el razonamiento sea visible, no que viva en una página aparte.

---

## Guion de la hora 2 — narrar al panel

**No presentes el resultado. Presenta el razonamiento.**

Recórrelo en este orden:

1. "Así leí el problema": tu encuadre, no el del encargo. Este es el momento Jonathan: usuario, objetivo, qué le cuesta el fracaso.
2. "Esto es lo que elegí resolver": el problema real que identificaste y por qué. Nombra lo que despriorizaste.
3. "Esta es la estructura a la que llegué antes de ir a la UI": flujos, puntos de decisión. Esto es para Alberto y Marta.
4. "Esto es lo que diseñé y por qué": decisiones y, de forma explícita, qué elegiste no construir.
5. "Esto es lo que falta": qué haría con más tiempo, qué sigue siendo arriesgado, qué validaría antes de lanzar.

**Sobre los compromisos:** nómbralos en voz alta aunque parezcan obvios. "El compromiso era X frente a Y. Fui con X porque Z". Cada compromiso explícito es una señal de staff.

**Sobre los supuestos:** si tomaste una decisión de la que no estás seguro, dilo. "Asumí que el usuario estaría en este contexto. Si eso es falso, la solución cambia de esta forma". Eso no es debilidad, es razonamiento de diseño.

---

## Checklist de señales de staff — clávalas de forma explícita

- [ ] Aclaración de alcance antes del output: "el encargo pedía X, lo interpreté como Y, porque..."
- [ ] Encuadre en resultado de producto: "esto importa porque el problema real del usuario es..."
- [ ] Qué elegiste no construir, con motivo declarado
- [ ] Qué validarías antes de seguir construyendo
- [ ] La metapregunta: ¿qué cambiaría si tuvieras 2 semanas en lugar de 1 hora?

---

## Ajustes específicos por panelista

**Marta (Design Director):** te ha visto dos veces. Ya sabe que sabes diseñar. En la hora 2 busca si el razonamiento aguanta bajo repregunta. Cuando cuestione una decisión, no la defiendas, dialoga con el cuestionamiento. "Es un empujón justo. Si hubiera ido por ahí, el compromiso habría sido..."

Pregunta probable: "¿Por qué elegiste esto como MVP?" Responde con tres ejes: dolor del usuario (qué fricción elimina), riesgo de negocio (qué se rompe si no lo resuelves) y potencial de aprendizaje (qué revela para la v2). No respondas con "me pareció el alcance correcto".

**Alberto (Design Director, background de DS):** habla de igual a igual. No expliques lo básico del diseño. Sondeará si pensaste en extensibilidad, estados e implicaciones de sistema más allá del camino feliz.

Pregunta probable: "¿Cómo escala esto cuando crece la complejidad?" Habla del modelo de estados, los patrones reutilizables, cómo la estructura maneja excepciones y permisos sin romperse. Aquí tu background de DS es un activo, piensa en términos de qué compone bien.

**Jonathan (Growth, no diseñador):** encuádralo en resultados de usuario y términos de negocio todo el tiempo. "Este paso elimina el ida y vuelta entre empleado y manager que retrasa la aprobación" aterriza. "Usé un patrón de acción única" no.

Pregunta probable: "¿Cómo mejora esto los resultados de negocio?" Evita el lenguaje de diseño por completo. Habla de menos retrasos, menos errores, eficiencia operativa, activación o retención. Conecta la decisión de diseño con un coste que el negocio está pagando ahora mismo.

---

## Preparación previa al reto (esta noche)

Prepara tu espacio de trabajo en Figma antes de las 10:00 de mañana:

- Archivo en blanco con las páginas ya creadas y etiquetadas:
  - `Encuadre del problema`
  - `Flujo central`
  - `Diseño`
  - `Lo que no construí`
- Un bloque de texto con las 5 preguntas de aclaración ya escritas, léelas, elige las relevantes, pregunta antes de tocar Figma
- Un bloque de texto con las 6 preguntas de definición ya escritas, pégalas y rellénalas cuando llegue el encargo
- Un pequeño kit de componentes listo: campos de formulario, botones, filas de tabla, shell de navegación, indicadores de estado. No gastes tiempo buscando primitivos bajo presión.
- Cierra el resto de pestañas y apps. Una sola ventana: Figma. Notificaciones apagadas.

---

## Posición salarial

El nivel se decide en esta ronda.

- **Si Senior:** 80K€. No bajes de ahí. Ese es el techo Senior.
- **Si Staff:** 93K€ de apertura. No bajes a precio Senior si te nivelan como Staff.

Si preguntan por compensación durante la hora 2: "Eso depende de dónde encaje este rol en vuestro marco, ¿me podéis decir si pensáis en Senior o Staff?" Luego das el número para lo que respondan. No ofrezcas una cifra antes de aclarar el nivel.

---

## Si la hora 1 se tuerce

Dos modos de fallo. Identifica en cuál estás.

**Si en el minuto 35 sigues encuadrando:** para. Abre una pantalla. Una definición clara del problema con una pantalla en bruto vence a una definición perfecta del problema sin artefacto. Necesitan algo tangible que discutir en la hora 2.

**Si estás metido en la UI y pierdes el hilo:** para. Vuelve a la página de encuadre del problema y escribe una frase sobre qué estás resolviendo en realidad y por qué. Pantallas pulidas que resuelven el problema equivocado son peores que pantallas en bruto que resuelven el correcto.

---

*Después del reto: ejecuta `/debrief-interview Factorial challenge` mientras esté fresco.*
