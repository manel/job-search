# Reto de práctica Factorial A — Gestión de ausencias

Ejemplo resuelto. La estructura refleja las cuatro páginas de Figma del guion de la hora 1 de la ronda 3: Encuadre del problema, Flujo central, Diseño, Lo que no construí. Léelo como referencia de cómo se ve un razonamiento a nivel staff de principio a fin, no como un guion que memorizar. El encargo real será distinto; el orden de las jugadas no debería serlo.

> **Leyenda de marcas**
> 🚩 **JUGADA** — una acción táctica ensayable. Transferible a cualquier encargo. Interioriza esto, no el diseño concreto.
> ⭐ **DECISIÓN CLAVE** — la columna vertebral. Una decisión de la que cuelga toda la solución, defendible por tres vías (dolor del usuario, riesgo de negocio, qué enseña).

---

## El encargo (tal como te lo dan)

> El spinoff de Factorial está construyendo gestión de ausencias desde cero. Diseña la experiencia central para solicitar y aprobar tiempo libre. Tienes 60 minutos. Empieza a trabajar.

La parquedad es la prueba. No empieces a trabajar.

---

## 0–8 min — Preguntas de aclaración (pregunta antes de abrir Figma)

> 🚩 **JUGADA** — Preguntas antes de Figma. Aunque el encargo diga "empieza a trabajar". Los candidatos senior resuelven el encargo; los staff lo reformulan primero.

Elige de 3 a 4. Cada una debe reconfigurar el diseño según la respuesta, si no es relleno.

1. "¿Quién es el usuario principal para la v1: el empleado que solicita, el manager que aprueba, o el admin de RRHH dueño de la política?" Les obliga a comprometerse, y les dice que sabes que son tres productos distintos.
2. "¿La autoridad de aprobación está centralizada en RRHH, o delegada en los managers de equipo?" Esta es la rama de mayor palanca. Centralizada es una cola y un aprobador. Delegada implica enrutado, escalado y lógica de cobertura.
3. "¿Optimizamos para velocidad de solicitud, para cumplimiento de política, o para confianza en el saldo? Puedo diseñar para una con limpieza, no para las tres."
4. "Spinoff greenfield, así que asumo que no hay motor de acumulación de saldos. ¿El cálculo de saldo está en alcance, o trato el saldo como un dato de entrada?"

Rama oculta que nombrar en voz alta aunque te digan que sigas:
"Antes de cerrar nada aclararía qué pasa cuando dos personas del mismo equipo solicitan la misma semana. El conflicto de cobertura es donde vive la fricción real, y si está en alcance cambia el flujo del manager de forma significativa."

> 🚩 **JUGADA** — Nombra la rama oculta en voz alta. Los flujos de RRHH y finanzas se expanden hacia permisos, delegación, excepciones, auditoría. Sacar una sin que te la pidan señala que ves el problema que el encargo esconde.

Para este ejemplo resuelto, asume: **el usuario principal es el manager de equipo, la autoridad es delegada, optimiza para velocidad de aprobación y confianza en el saldo, la acumulación es un dato de entrada fuera de alcance.**

---

## 8–18 min — Encuadre del problema (página 1 de Figma, déjala visible)

**¿Quién es el usuario principal?**
El manager de equipo. No el empleado. El empleado solicita una vez por trimestre; el manager procesa solicitudes cada semana y es el cuello de botella. Diseñar para el usuario de alta frecuencia es la elección de mayor palanca.

**¿El único trabajo que genera más fricción o coste?**
Decidir sobre una solicitud de ausencia con suficiente contexto para decir sí o no sin una conversación aparte. Hoy, en empresas de hoja de cálculo y email, el manager tiene que dejar la solicitud para ir a comprobar: ¿tiene esta persona saldo, quién más está fuera esa semana, es periodo de mucha carga? La decisión es barata; reunir el contexto es caro.

**Éxito frente a fracaso.**
Éxito: el manager aprueba o rechaza en una sola pantalla, en segundos, con plena confianza. Fracaso: el manager sella sin ver un choque de cobertura, y luego tiene que dar marcha atrás, lo que cuesta confianza con dos empleados.

**El bucle central (semanal, no casos límite):**
El manager abre una cola de solicitudes pendientes, ve cada una con saldo y cobertura del equipo en línea, decide, sigue. Ese es el bucle. Todo lo demás es soporte alrededor.

**Frontera del MVP.**
Dentro: la superficie de decisión del manager, con saldo y cobertura en línea. El formulario de solicitud del empleado, mínimo. Fuera de la v1: reglas de acumulación, configuración de política, cadenas de aprobación multinivel, integraciones de calendario, reporting.

**El problema real frente al del encargo.**
El encargo dice "solicitar y aprobar tiempo libre", lo que suena a un flujo de formulario y botón de dos caras. El problema real es el contexto de decisión. La aprobación no es un paso de flujo que necesite un botón; es un juicio que necesita información co-localizada. Resuelve el contexto y el botón es trivial. Construye el botón sin contexto y has lanzado la hoja de cálculo con mejor estilo.

---

## 18–30 min — Estructura antes que pantallas (página 2 de Figma, cajas y flechas)

**Punto de entrada:** el manager recibe una notificación, o abre un elemento "Aprobaciones pendientes" en su navegación. Llega con intención: vaciar la cola.

**Las 3 a 5 decisiones que toma el manager por solicitud:**
1. ¿Tiene esta persona saldo de verdad? (sí / no / al límite)
2. ¿Está cubierto el equipo esa semana? (choque / despejado)
3. ¿Es un periodo protegido o de mucha carga? (bloqueo / bien)
4. Aprobar, rechazar o preguntar.

**Estados a diseñar:**
- Vacío: ninguna solicitud pendiente. El estado bueno. Tranquiliza, no lo dejes en blanco.
- Cola con elementos: el estado de trabajo.
- Solicitud individual expandida: el momento de decisión.
- Conflicto en pantalla: dos personas, misma semana.
- Post-decisión: confirmación, ventana de deshacer, empleado notificado.

**Lo que el usuario tiene al final que no tenía al principio:**
Una cola vaciada y una decisión defendible, tomada sin salir de la pantalla a reunir contexto.

Decisión a registrar en esta página: cola-con-contexto-en-línea, no un asistente de una-solicitud-cada-vez. Un asistente es más limpio por solicitud pero oculta la señal entre solicitudes (dos personas, misma semana), que es justo la información que evita el error caro. Compromiso nombrado: cambio una pantalla algo más cargada por visibilidad entre solicitudes, porque el fracaso caro es un choque no visto, no una decisión individual lenta.

---

## 30–50 min — Diseña el flujo central (página 3 de Figma)

Construye una pantalla bien: **la cola de aprobación del manager con una solicitud expandida.**

Maquetación, de arriba abajo:
- Cabecera: "Aprobaciones pendientes (4)". El recuento ancla el trabajo: vaciar esto.
- Lista de filas de solicitud. Cada fila, colapsada, lleva en línea los datos críticos para decidir, para que el manager a menudo decida sin expandir:
  - Nombre del empleado y equipo
  - Fechas y total de días
  - Saldo tras esta solicitud (p. ej. "quedan 9 días después de esto"), con peso de color si queda en negativo o cerca de cero
  - Señal de cobertura: un pequeño indicador que dice "2 más fuera esta semana" o "equipo despejado", clicable
- Fila expandida: añade una mini tira de calendario del equipo para la semana solicitada mostrando quién más está fuera, el motivo si se aportó, y tres acciones: Aprobar, Rechazar, Preguntar.
- Rechazar exige un motivo de una línea. Aprobar es un clic con una ventana corta de deshacer.

Anotaciones puestas directamente en la pantalla:
- "El saldo mostrado se lee del motor de acumulación, tratado como dato de entrada. La lógica de acumulación fuera de alcance para la v1."
- "La tira de cobertura es la apuesta central. Es la diferencia entre esto y una aprobación por email."
- "Camino feliz mostrado. Rechazar-con-motivo y el hilo de preguntar están esbozados, no diseñados."
- "El formulario de solicitud del empleado es una superficie secundaria. Diseñado al mínimo, enlazado, no es el foco."

**Restricción dura cumplida: una pantalla real abierta en el minuto 35.** Si aquí sigues en diagramas de flujo, para y abre esta pantalla en bruto.

> ⭐ **DECISIÓN CLAVE** — **Contexto de cobertura en línea, no una vista de calendario aparte.** Un manager que tiene que abrir un calendario aparte para comprobar la cobertura dejará de comprobarlo. Co-localizar el choque con la decisión es el producto entero. Defiéndela por tres vías: dolor del usuario (el desvío semanal a reunir contexto), riesgo de negocio (los choques sellados a la ligera cuestan confianza), aprendizaje (valida si el contexto en línea cambia el comportamiento del manager).

---

## 50–60 min — Lo que no construí (página 4 de Figma)

Cinco cosas dejadas fuera de alcance, una línea cada una:

1. **Acumulación y cálculo de saldos.** Tratado como dato de entrada. Es un motor de reglas profundo y un problema distinto; diseñarlo en 60 minutos sería superficial en ambos.
2. **Configuración de política.** La superficie del admin de RRHH para definir tipos de ausencia y derechos. Usuario real, distinto, sesión aparte.
3. **Cadenas de aprobación multinivel.** Asumido un único aprobador delegado para la v1. Las cadenas son un problema de enrutado que diseñaría una vez validada la superficie de decisión de aprobador único.
4. **Integraciones de calendario y nómina.** Importantes para la adopción, no para demostrar que el bucle de decisión central funciona.
5. **Móvil.** Los managers sí aprueban desde el móvil. Diseñaría la cola mobile-first en la v2 una vez asentado el modelo de información, porque la tira de cobertura es el problema responsive difícil.

> 🚩 **JUGADA** — "Si tuviera dos horas más." Nombra el siguiente problema real y admite el límite actual. Es la señal de staff que la mayoría se salta.

"Si tuviera dos horas más, diseñaría el flujo de resolución de conflictos: qué hace el manager cuando hay un choque, ya que aprobar igualmente, rechazar o proponer fechas alternativas es la decisión difícil de verdad y ahora mismo solo he sacado el choque a la superficie, no he ayudado a resolverlo."

Guarda una o dos de estas para las preguntas en lugar de anticiparlo todo. Sobreanotar se lee como defensivo.

---

## Hora 2 — orden de narración (no presentes el resultado)

1. **"Así leí el problema."** Para Jonathan: el manager es el cuello de botella, cada decisión de ausencia hoy cuesta un desvío a reunir contexto, y un choque de cobertura no visto cuesta confianza con dos empleados. Encuadra el coste que el negocio paga ahora.
2. **"Esto es lo que elegí resolver."** El problema real es el contexto de decisión, no el botón de aprobar. Nombra que despioricé el formulario de solicitud del empleado y el motor de acumulación a propósito.
3. **"Esta es la estructura antes de la UI."** Cola-con-contexto-en-línea frente a un asistente, y por qué: la visibilidad entre solicitudes evita el error caro.
4. **"Esto es lo que diseñé y por qué."** La tira de cobertura es la apuesta. Declara el compromiso: pantalla más cargada a cambio de visibilidad del choque.
5. **"Esto es lo que falta."** La resolución de conflictos es lo siguiente y el hueco más arriesgado. Validaría que los managers confían en la señal de cobertura antes de construir nada más.

**Preguntas probables del panel y la línea que clavar:**
- Marta, "¿Por qué esto como MVP?" Tres ejes: dolor del usuario (el desvío semanal a por contexto), riesgo de negocio (los choques sellados cuestan confianza y retrabajo), potencial de aprendizaje (valida si el contexto en línea cambia el comportamiento del manager, lo que informa cualquier otra superficie de aprobación del producto).
- Alberto, "¿Cómo escala esto al crecer la complejidad?" La fila es un componente con estado: estado de saldo, estado de cobertura, estado de decisión. Las cadenas de aprobación, los periodos de bloqueo y los tipos de ausencia extienden el mismo modelo sin una pantalla nueva. La tira de cobertura es un patrón reutilizable que cualquier superficie de aprobación del HRIS puede adoptar.
- Jonathan, "¿Cómo mejora esto los resultados de negocio?" Elimina el ida y vuelta entre manager y empleado que retrasa las aprobaciones, y caza los choques de cobertura antes de que se conviertan en dos personas descontentas y una reprogramación. Aprobaciones más rápidas, menos marchas atrás.
- Compensación, si surge: "Eso depende de dónde encaje esto en vuestro marco. ¿Senior o Staff?" Luego 80K€ o 93K€. No ofrezcas primero.
