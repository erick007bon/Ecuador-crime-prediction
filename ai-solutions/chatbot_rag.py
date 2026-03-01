import os

class SimpleChatbotRAG:
    """
    MVP de un Asistente IA (Chatbot) que usa RAG (Retrieval-Augmented Generation).

    Este es un script demostrativo de cómo un agente de IA puede "leer" los documentos
    de una empresa y responder preguntas basadas SOLAMENTE en esa información,
    evitando que invente respuestas (alucinaciones).
    """

    def __init__(self, company_name):
        self.company_name = company_name
        # Base de conocimiento "falsa" para el MVP.
        # En la vida real, esto sería una base de datos vectorial (ChromaDB, Pinecone)
        # llena de miles de PDFs, FAQs y sitios web de la empresa.
        self.knowledge_base = {
            "precios": f"En {company_name} tenemos tres planes: Básico ($50/mes), Pro ($150/mes) y Enterprise (Personalizado).",
            "horario": "Nuestro horario de atención es de Lunes a Viernes de 9:00 AM a 6:00 PM EST.",
            "servicios": "Ofrecemos: 1. Automatización con IA, 2. Bots de Trading, 3. Desarrollo Web y 4. Análisis de Datos.",
            "contacto": "Puedes escribirnos a hola@agencia.com o llamarnos al +1 800 555 1234."
        }

    def _retrieve_context(self, query):
        """
        Simula el paso de 'Retrieval' (Búsqueda) en RAG.
        Busca en la base de datos la información relevante a la pregunta.
        """
        query = query.lower()
        context = []
        if "precio" in query or "cuanto cuesta" in query or "plan" in query:
            context.append(self.knowledge_base["precios"])
        if "horario" in query or "a que hora" in query or "abierto" in query:
            context.append(self.knowledge_base["horario"])
        if "servicio" in query or "que hacen" in query or "ofrecen" in query:
            context.append(self.knowledge_base["servicios"])
        if "contacto" in query or "correo" in query or "telefono" in query:
            context.append(self.knowledge_base["contacto"])

        return " ".join(context) if context else None

    def ask(self, query):
        """
        Simula el paso de 'Generation' (Generación) usando el contexto.
        En la vida real, aquí enviaríamos el 'context' y el 'query' a la API de OpenAI (GPT-4)
        o a un modelo local (Llama 3).
        """
        print(f"\n👤 Usuario: {query}")

        # 1. Recuperar información relevante (RAG)
        context = self._retrieve_context(query)

        # 2. Generar respuesta
        print("🤖 Buscando en la base de conocimiento interna...")
        if context:
            # Simulamos que el LLM genera una respuesta basada en el contexto
            response = f"Basado en nuestros documentos: {context} ¿Hay algo más en lo que te pueda ayudar?"
        else:
            response = "Lo siento, no tengo información sobre eso en mi base de conocimiento. ¿Podrías reformular tu pregunta o preguntar sobre nuestros servicios, precios, horarios o contacto?"

        print(f"🤖 Asistente IA ({self.company_name}): {response}")
        return response

if __name__ == "__main__":
    print("=== Iniciando Demo de Chatbot RAG Empresarial ===")
    print("Cargando modelo y conectando a la base de datos vectorial... (Simulado)")

    agencia_bot = SimpleChatbotRAG(company_name="TechData AI Solutions")

    # Pruebas del Chatbot
    agencia_bot.ask("¿Qué servicios ofrecen?")
    agencia_bot.ask("Me interesa saber los precios de sus planes.")
    agencia_bot.ask("¿A qué hora abren el fin de semana?")
    agencia_bot.ask("¿Quién ganó el mundial de 2022?") # Pregunta fuera de contexto para probar límites

    print("\n================================================")
    print("💡 Nota para el desarrollador:")
    print("Para llevar esto a producción:")
    print("1. Usa LangChain o LlamaIndex.")
    print("2. Integra la API de OpenAI (gpt-4o-mini).")
    print("3. Usa una DB Vectorial como ChromaDB para buscar en miles de documentos.")
    print("4. Conéctalo a la API de WhatsApp Business (Meta).")
