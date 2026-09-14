# CTE vigente para Vivienda Abelar

## Objeto del corpus

Este paquete reúne la documentación oficial del Código Técnico de la Edificación (CTE) necesaria para consultar una vivienda unifamiliar de nueva construcción en España. La selección fue verificada el 14 de septiembre de 2026 y procede exclusivamente de la web oficial del CTE —gestionada para el Ministerio de Vivienda y Agenda Urbana— y del Boletín Oficial del Estado (BOE).

El corpus separa deliberadamente tres niveles:

1. **Normativa vigente:** Parte I y Documentos Básicos (DB). Son la referencia técnica principal para justificar las exigencias básicas.
2. **Documentos de apoyo:** explican métodos, conceptos o criterios concretos. Facilitan la aplicación del CTE, pero no deben presentarse como articulado reglamentario.
3. **Control BOE:** texto consolidado del Real Decreto 314/2006. Es útil para comprobar el marco general y las modificaciones, aunque el propio BOE advierte que la consolidación tiene carácter informativo y no valor jurídico.

La página oficial indica que el CTE se ordena en una Parte I y seis familias de Documentos Básicos: SE, SI, SUA, HE, HR y HS.^1 El BOE identifica el Real Decreto 314/2006 como norma de aprobación del CTE y muestra la sucesión de modificaciones incorporadas al texto consolidado.^2

## Regla de uso para el asistente

Al responder una consulta técnica:

- Identificar primero el requisito y el documento aplicable.
- Citar siempre **documento, sección/apartado y tabla o anejo**, cuando exista.
- Distinguir entre una obligación reglamentaria, un criterio de un documento de apoyo y una recomendación propia.
- No extrapolar automáticamente requisitos de otros usos —industrial, pública concurrencia, residencial público— a una vivienda unifamiliar de uso residencial vivienda.
- Comprobar el ámbito de aplicación, las excepciones y las notas de cada sección antes de afirmar que una exigencia es obligatoria.
- Si la conclusión depende de la fecha del proyecto, solicitud de licencia, concesión de licencia o comienzo de obra, analizar expresamente las disposiciones transitorias de la modificación correspondiente.
- No sustituir el criterio ni la responsabilidad del arquitecto, arquitecto técnico, ingeniero o dirección facultativa.
- Ante contradicción entre un documento de apoyo y un Documento Básico, prevalece el texto reglamentario. Ante duda jurídica, debe acudirse a la disposición publicada en el BOE.

## Documentos reglamentarios incluidos

| Archivo | Materia | Relevancia para Vivienda Abelar |
|---|---|---|
| `00_CTE_Parte_I.pdf` | Ámbito, agentes, proyecto, ejecución, mantenimiento y exigencias básicas | Muy alta: fija cómo se acredita y documenta el cumplimiento |
| `01_DB_SE_Seguridad_Estructural.pdf` | Bases generales de seguridad estructural | Muy alta |
| `02_DB_SE_AE_Acciones_Edificacion.pdf` | Peso propio, uso, viento, nieve, temperatura y acciones accidentales | Muy alta |
| `03_DB_SE_C_Cimientos.pdf` | Terreno, estudio geotécnico, cimentaciones y contenciones | Muy alta |
| `04_DB_SE_A_Acero.pdf` | Elementos y uniones de acero | Alta si existen pilares, vigas o uniones metálicas |
| `05_DB_SE_F_Fabrica.pdf` | Muros y elementos resistentes de fábrica | Según solución estructural |
| `06_DB_SE_M_Madera.pdf` | Estructuras de madera | Según solución estructural |
| `07_DB_SI_Incendio.pdf` | Propagación, evacuación, intervención y resistencia al fuego | Alta; incorpora la modificación del RD 164/2025 |
| `08_DB_SUA_Utilizacion_Accesibilidad.pdf` | Caídas, impactos, atrapamiento, iluminación, vehículos, rayo y accesibilidad | Muy alta para pavimentos, desniveles, huecos, vidrio y garaje |
| `09_DB_HE_Ahorro_Energia.pdf` | Consumo, demanda, envolvente, renovables, iluminación y recarga | Muy alta para aislamiento, ventanas, puentes térmicos, ACS y sistemas |
| `10_DB_HR_Proteccion_Ruido.pdf` | Aislamiento acústico, ruido de instalaciones y reverberación | Alta, especialmente frente al exterior y las instalaciones |
| `11_DB_HS_Salubridad.pdf` | Humedad, residuos, ventilación, agua, saneamiento y radón | Muy alta para fachada, cubierta, VMC, fontanería, saneamiento y terreno |

El DB-SI descargado figura fechado el 4 de marzo de 2025 y la página oficial lo identifica como el documento que incorpora las modificaciones del Real Decreto 164/2025.^3 Los documentos Parte I, SUA, HE y HS recogen las modificaciones del Real Decreto 450/2022; la versión oficial de HE incluye además la corrección de errores publicada el 2 de febrero de 2023.^4

## Documentos oficiales de apoyo incluidos

| Archivo | Utilidad práctica |
|---|---|
| `DA_SI_1_Productos_comportamiento_fuego.pdf` | Justificación documental de prestaciones frente al fuego |
| `DA_SI_2_Puertas_resistentes_fuego.pdf` | Clasificación y normas de puertas resistentes al fuego |
| `DA_SI_3_Mantenimiento_puertas.pdf` | Conservación de puertas con función de protección contra incendios |
| `DA_SI_4_Salida_espacio_exterior_seguro.pdf` | Interpretación de salida de edificio y espacio exterior seguro |
| `DA_SUA_1_Vidrios_impacto.pdf` | Clasificación del vidrio frente a impacto y forma de rotura |
| `DA_SUA_2_Accesibilidad_edificios_existentes.pdf` | Flexibilidad para edificios existentes; normalmente no es la referencia principal en obra nueva |
| `DA_SUA_3_Resbaladicidad_suelos.pdf` | Criterios para determinar la resbaladicidad de pavimentos |
| `DA_HE_1_Parametros_envolvente.pdf` | Cálculo de transmitancias y parámetros de la envolvente |
| `DA_HE_2_Condensaciones.pdf` | Comprobación de condensaciones superficiales e intersticiales |
| `DA_HE_3_Puentes_termicos.pdf` | Criterios y valores para puentes térmicos |
| `DA_HE_Climas_referencia.pdf` | Descripción de los climas de referencia usados por DB-HE |
| `DA_HR_1_Magnitudes_aislamiento_acustico.pdf` | Interpretación de magnitudes acústicas |
| `DA_HR_2_Transmisiones_indirectas.pdf` | Procedimiento para transmisiones acústicas indirectas |

La web oficial clasifica expresamente estos archivos como documentos de apoyo y publica por separado los Documentos Básicos con comentarios del Ministerio.^5 Para mantener un corpus compacto y evitar duplicidades, no se han incorporado versiones históricas ni versiones comentadas completas: las consultas normativas deben comenzar siempre por el DB consolidado vigente.

## Consultas prioritarias para la vivienda

### Envolvente, aislamiento y ventanas

Consultar DB-HE, en especial HE 0 y HE 1, junto con DA HE/1, DA HE/2 y DA HE/3. Para la fachada, cubierta y contacto con el terreno, cruzar además con HS 1. En huecos acristalados, añadir SUA 2 y DA SUA/1 cuando exista riesgo de impacto o caída.

### Ventilación y extracción de cocina

La referencia central es HS 3, pero cualquier solución debe coordinarse con el diseño real de la VMC, las instrucciones del fabricante, el RITE cuando proceda y el proyecto de instalaciones. El asistente no debe asumir que una boca de extracción general de VMC equivale automáticamente a una campana de cocina ni validar caudales sin revisar el proyecto y el equipo concreto.

### Cimentación, estructura y pilares

Usar conjuntamente DB-SE, DB-SE-AE y DB-SE-C. Añadir DB-SE-A, DB-SE-F o DB-SE-M según el material del elemento. Para hormigón estructural, el corpus del CTE no basta: debe consultarse también el **Código Estructural vigente**, aprobado por el Real Decreto 470/2021, y las modificaciones que procedan.^6

### Humedades, cubierta, fachada y saneamiento

Usar HS 1 para protección frente a la humedad; HS 4 para suministro de agua; HS 5 para evacuación; y HS 6 para radón. No confundir los criterios nacionales del CTE con las exigencias urbanísticas, de habitabilidad o sectoriales propias de Galicia y del ayuntamiento.

### Garaje abierto, recorridos y pavimentos

Revisar SI para condiciones de incendio y SUA 1, SUA 2 y SUA 7 para caídas, impactos y circulación de vehículos. Para pavimentos exteriores y zonas mojadas, consultar también DA SUA/3. La caracterización del garaje como abierto, cubierto, zona de ocupación nula o uso aparcamiento debe basarse en la definición normativa y en el proyecto, no solo en su apariencia.

## Vigencia y límites

La web oficial del CTE informa de una revisión vinculada a la Directiva (UE) 2024/1275 y muestra que el proyecto de modificación fue sometido a audiencia pública en noviembre de 2025.^7 En la fecha de verificación de este paquete, la propia portada oficial seguía presentándolo como una modificación en tramitación, no como un nuevo texto reglamentario que sustituya a los PDF descargados.^8 Por tanto, no se ha incorporado el borrador al corpus normativo.

Esta colección representa el estado documental oficial comprobado el **14 de septiembre de 2026**. El CTE cambia con el tiempo: antes de usarla para una decisión contractual, certificación, modificación de obra o consulta jurídica, debe revisarse la web oficial y el BOE.

Para Vivienda Abelar debe distinguirse entre:

- la normativa vigente de forma general en la fecha de la consulta;
- la normativa aplicable al proyecto por sus fechas administrativas y disposiciones transitorias;
- las prestaciones declaradas en el proyecto básico y de ejecución;
- y las modificaciones de obra que requieran nueva justificación o autorización.

## Exclusiones deliberadas

No se incluyen en este paquete:

- versiones anteriores de los DB;
- borradores de futuras modificaciones;
- versiones comentadas completas;
- normas UNE de pago;
- normativa autonómica o municipal;
- Código Estructural, RITE, REBT, ICT y reglamentación de productos o instalaciones;
- herramientas de cálculo como HULC y archivos climáticos `.MET`.

Estas fuentes pueden formar un segundo corpus complementario de normativa integral para Vivienda Abelar.

## Fuentes

1. Ministerio de Vivienda y Agenda Urbana / IETcc-CSIC. [Documentos CTE](https://www.codigotecnico.org/DocumentosCTE/DocumentosCTE.html). Consultado el 14 de septiembre de 2026.
2. Agencia Estatal Boletín Oficial del Estado. [Real Decreto 314/2006, texto consolidado](https://www.boe.es/buscar/act.php?id=BOE-A-2006-5515). Consultado el 14 de septiembre de 2026.
3. Ministerio de Vivienda y Agenda Urbana / IETcc-CSIC. [Seguridad en caso de incendio](https://www.codigotecnico.org/DocumentosCTE/SeguridadEnCasoDeIncendio.html); BOE. [Real Decreto 164/2025](https://www.boe.es/buscar/doc.php?id=BOE-A-2025-7190).
4. Ministerio de Vivienda y Agenda Urbana / IETcc-CSIC. [Parte I](https://www.codigotecnico.org/DocumentosCTE/parte1.html), [SUA](https://www.codigotecnico.org/DocumentosCTE/SeguridadUtilizacionAccesibilidad.html), [HE](https://www.codigotecnico.org/DocumentosCTE/AhorroEnergia.html) y [HS](https://www.codigotecnico.org/DocumentosCTE/Salubridad.html).
5. Ministerio de Vivienda y Agenda Urbana / IETcc-CSIC. Páginas oficiales de [SI](https://www.codigotecnico.org/DocumentosCTE/SeguridadEnCasoDeIncendio.html), [SUA](https://www.codigotecnico.org/DocumentosCTE/SeguridadUtilizacionAccesibilidad.html), [HE](https://www.codigotecnico.org/DocumentosCTE/AhorroEnergia.html) y [HR](https://www.codigotecnico.org/DocumentosCTE/ProteccionRuido.html).
6. Agencia Estatal Boletín Oficial del Estado. [Real Decreto 470/2021, Código Estructural](https://www.boe.es/buscar/act.php?id=BOE-A-2021-13681).
7. Ministerio de Vivienda y Agenda Urbana. [Trámite de audiencia de la modificación del CTE](https://www.mivau.gob.es/el-ministerio/sala-de-prensa/noticias/vie-07112025-1203), 7 de noviembre de 2025.
8. Ministerio de Vivienda y Agenda Urbana / IETcc-CSIC. [Portal oficial del CTE](https://www.codigotecnico.org/). Consultado el 14 de septiembre de 2026.
