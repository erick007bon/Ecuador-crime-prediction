# Soluciones de IA (AI Solutions) 🤖

Esta carpeta contiene prototipos de herramientas que integran Inteligencia Artificial para resolver problemas específicos en empresas o automatizar procesos.

## MVP Destacado: Chatbot RAG Empresarial (`chatbot_rag.py`)

Un asistente virtual de atención al cliente construido usando el paradigma **RAG (Retrieval-Augmented Generation)**. A diferencia de ChatGPT, este bot no "alucina" (inventa respuestas). Está programado para buscar información *exclusivamente* en la base de datos de tu empresa (PDFs de preguntas frecuentes, horarios, precios, manuales).

### Características Clave:
*   **Búsqueda Semántica:** Extrae contexto de documentos específicos de la empresa.
*   **Generación Contextual:** Usa la información extraída para redactar respuestas amigables.
*   **Seguridad:** Si no encuentra la respuesta en sus documentos, rechaza cortésmente la pregunta en lugar de inventar.

### Cómo ejecutar el MVP
```bash
python chatbot_rag.py
```

### Tecnologías para Producción (Roadmap):
*   **LLMs:** OpenAI GPT-4o-mini, Anthropic Claude 3.5 Sonnet, Llama 3 (Open Source).
*   **Frameworks:** LangChain o LlamaIndex.
*   **Bases de Datos Vectoriales:** Pinecone, ChromaDB, Qdrant.
*   **Canales:** Integración vía webhook con WhatsApp Business API, Telegram o Widgets Web.
